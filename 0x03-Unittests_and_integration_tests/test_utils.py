#!/usr/bin/env python3
"""test_utils module
"""

import unittest
import utils

from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test for access_nested_map method
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for access_nested_map method
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test class for utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, url, test_payload, mock_get):
        """ Test for utils.get_json
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        print(dir(mock_get))
        mock_get.return_value = mock_response

        result = utils.get_json(url)

        mock_get.assert_called_once_with(url)
        self.assertEqual(result, test_payload)
