#!/usr/bin/env python3
""" test_client module
"""

import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test class for test_client
    """
    @parameterized.expand([
        ('google',),
        ('abc',),
        ])
    @patch('client.get_json')
    def test_org(self, name, mock_get_json):
        """ test that GithubOrgClient.org returns the correct value.
        """
        expected_data = {"a": True, "b": False}
        mock_get_json.return_value = expected_data

        obj = GithubOrgClient(name)

        result = obj.org

        self.assertEqual(result, expected_data)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/\
{name}")

    def test_public_repos_url(self):
        """ test for GithubOrgClient._public_repos_url
        """
        mocked_property = "Mocked value"

        with patch('client.GithubOrgClient._public_repos_url') as mocked:
            mocked.return_value = mocked_property

            obj = GithubOrgClient("google")

            result = obj._public_repos_url.return_value

            self.assertEqual(result, mocked_property)
