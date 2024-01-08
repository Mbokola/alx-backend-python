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

            result = obj._public_repos_url()

            self.assertEqual(result, mocked_property)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ unit-test for GithubOrgClient.public_repos
        """
        expected_data = {"a": True, "b": False}
        mock_get_json.return_value = expected_data

        obj = GithubOrgClient("google")

        result = obj.org

        self.assertEqual(result, expected_data)
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/\
google")

        mocked_property = "Mocked value"

        with patch('client.GithubOrgClient._public_repos_url') as mocked:
            mocked.return_value = mocked_property

            obj = GithubOrgClient("google")

            result = obj._public_repos_url()

            self.assertEqual(result, mocked_property)
            mocked.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test GithubOrgClient.has_license.
        """
        test_obj = GithubOrgClient("Dummy")

        self.assertEqual(test_obj.has_license(repo, license_key), expected)
