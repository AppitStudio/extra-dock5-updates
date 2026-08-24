#!/usr/bin/env python3
"""Validate an ExtraDock 5 appcast and idempotently register its releases."""

from __future__ import annotations

import argparse
import email.utils
import json
import os
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

SPARKLE = "http://www.andymatuschak.org/xml-namespaces/sparkle"
KEYPER_ENDPOINT = "https://keyper.appitstudio.com/api/releases"


def parse_items(path: Path) -> list[dict[str, str]]:
    root = ET.parse(path).getroot()
    releases: list[dict[str, str]] = []
    seen_builds: set[str] = set()
    seen_versions: set[str] = set()
    previous_released_at = None

    for item in root.findall("./channel/item"):
        build = (item.findtext(f"{{{SPARKLE}}}version") or "").strip()
        version = (item.findtext(f"{{{SPARKLE}}}shortVersionString") or "").strip()
        pub_date = (item.findtext("pubDate") or "").strip()
        enclosure = item.find("enclosure")
        if not build or not version or not pub_date or enclosure is None:
            raise ValueError("every appcast item needs version, shortVersionString, pubDate, and enclosure")
        if build in seen_builds:
            raise ValueError(f"duplicate Sparkle build number: {build}")
        seen_builds.add(build)
        if version in seen_versions:
            raise ValueError(f"duplicate release-registry version: {version}")
        seen_versions.add(version)

        released_at = email.utils.parsedate_to_datetime(pub_date)
        if released_at is None or released_at.tzinfo is None:
            raise ValueError(f"pubDate must be RFC 2822 with a timezone: {pub_date}")
        if previous_released_at is not None and released_at > previous_released_at:
            raise ValueError("appcast items must remain in newest-to-oldest release order")
        previous_released_at = released_at
        releases.append(
            {
                "version": version,
                "released_at": released_at.isoformat(),
            }
        )

    if not releases:
        raise ValueError("appcast contains no release items")
    return releases


def register(release: dict[str, str]) -> None:
    secret_name = "KEYPER_RELEASE_TOKEN"
    token = os.environ.get(secret_name, "").strip()
    if not token:
        raise RuntimeError(f"{secret_name} is required")

    request = urllib.request.Request(
        KEYPER_ENDPOINT,
        data=json.dumps(
            {"version": release["version"], "released_at": release["released_at"]}
        ).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status not in (200, 201):
                raise RuntimeError(f"Keyper returned HTTP {response.status}")
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"Keyper returned HTTP {error.code}") from error


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("appcast", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    try:
        releases = parse_items(args.appcast)
        if not args.validate_only:
            for release in releases:
                register(release)
    except (ET.ParseError, OSError, RuntimeError, ValueError) as error:
        print(f"release registration failed: {error}", file=sys.stderr)
        return 1

    print(f"validated {len(releases)} appcast release(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
