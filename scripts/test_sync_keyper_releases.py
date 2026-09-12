import io
import json
from datetime import datetime, timezone
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from sync_keyper_releases import Release, register_release


class Response(io.BytesIO):
    status = 201


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.release = Release('5.0.8', '62', datetime(2026, 9, 11, tzinfo=timezone.utc),
                               'https://example.com/v5.0.8/ExtraDock.dmg')
        self.payload = {'product': 'extradock', 'track': 'v5-stable', 'version': '5.0.8',
                        'download_url': self.release.download_url}

    def response(self, payload=None):
        return Response(json.dumps(self.payload if payload is None else payload).encode())

    def blocked(self, code=403):
        return HTTPError('https://keyper.example/api/releases', code, 'Blocked', {},
                         io.BytesIO(b'Imunify360 bot-protection'))

    @patch('sync_keyper_releases.time.sleep')
    @patch('sync_keyper_releases.urllib.request.urlopen')
    def test_transient_firewall_rejection_can_recover(self, urlopen, sleep):
        urlopen.side_effect = [self.blocked(), self.response()]
        self.assertEqual(register_release('https://keyper.example/api/releases', 'test-token', self.release), 201)
        self.assertEqual(urlopen.call_count, 2)

    @patch('sync_keyper_releases.time.sleep')
    @patch('sync_keyper_releases.urllib.request.urlopen')
    def test_persistent_firewall_rejection_fails_publication(self, urlopen, sleep):
        urlopen.side_effect = [self.blocked(), self.blocked(), self.blocked()]
        with self.assertRaisesRegex(RuntimeError, 'HTTP 403'):
            register_release('https://keyper.example/api/releases', 'test-token', self.release)
        self.assertEqual(urlopen.call_count, 3)

    @patch('sync_keyper_releases.urllib.request.urlopen')
    def test_registration_conflict_is_not_retried(self, urlopen):
        urlopen.side_effect = self.blocked(409)
        with self.assertRaisesRegex(RuntimeError, 'HTTP 409'):
            register_release('https://keyper.example/api/releases', 'test-token', self.release)
        self.assertEqual(urlopen.call_count, 1)

    @patch('sync_keyper_releases.urllib.request.urlopen')
    def test_html_challenge_is_not_a_success(self, urlopen):
        response = Response(b'<html>challenge</html>')
        response.status = 200
        urlopen.return_value = response
        with self.assertRaises(ValueError):
            register_release('https://keyper.example/api/releases', 'test-token', self.release)

    @patch('sync_keyper_releases.urllib.request.urlopen')
    def test_wrong_product_track_version_or_download_fails(self, urlopen):
        for field in self.payload:
            with self.subTest(field=field):
                urlopen.return_value = self.response(self.payload | {field: 'wrong'})
                with self.assertRaisesRegex(RuntimeError, 'did not confirm'):
                    register_release('https://keyper.example/api/releases', 'test-token', self.release)

    @patch('sync_keyper_releases.urllib.request.urlopen')
    def test_idempotent_registration_is_accepted(self, urlopen):
        response = self.response()
        response.status = 200
        urlopen.return_value = response
        self.assertEqual(register_release('https://keyper.example/api/releases', 'test-token', self.release), 200)


if __name__ == '__main__':
    unittest.main()
