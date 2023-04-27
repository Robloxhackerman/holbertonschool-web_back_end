#!/usr/bin/env python3
import unittest
from unittest import TestCase
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()

class TestMemoize(unittest.TestCase):
    def test_memoiz(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            final_return = test_class.a_property

            self.assertEqual(final_return, 42)
            patched.assert_called_once()