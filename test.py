#!/usr/bin/env python3
import os
import social_net_size as test_doc
import json
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)

class TestSmall(unittest.TestCase):
    """A collection of small test cases to check quickly if the implementation
    is correct.
    """
    def test_01_git_example(self):
        dictionary = ['HI', 'HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
        result = test_doc.social_net_size(dictionary, 'HI')
        self.assertEqual(7, result)

    def test_02_connected_graph(self):
        """Testing on a completely connected graph."""
        dictionary = ['AB', 'BB', 'BBC', 'ABD', 'AA', 'ABC', 'AAA']
        result = test_doc.social_net_size(dictionary, 'AB')
        self.assertEqual(len(dictionary), result)

    def test_03_non_connected_graph(self):
        """Testing on a not completely connected graph."""
        dictionary = ['AB', 'BB', 'BBC', 'ABZ', 'VV', 'VZ', 'RT', 'YT']
        result = test_doc.social_net_size(dictionary, 'AB')
        self.assertEqual(4, result)

    def test_04_single_value(self):
        dictionary = ['AB', 'BB', 'BBC', 'ABZ', 'VV', 'VZ', 'RT', 'YT', 'WW']
        result = test_doc.social_net_size(dictionary, 'WW')
        self.assertEqual(1, result)

    def test_05_cycle(self):
        """Test against a graph with a cycle."""
        dictionary = ['AB', 'CB', 'CD', 'ED', 'EA', 'AF']
        result = test_doc.social_net_size(dictionary, 'AB')
        self.assertEqual(6, result)


class TestFiles(unittest.TestCase):
    """Test cases derived from the dictionaries given at
    https://gist.github.com/NWKMF/6589960bc4d6a7a22cd81feff3e0f67b. I
    converted the txt files to json for easier manipulation and testing.
    The files can be found in the 'resources' directory.
    """
    def test_06_very_small_dict(self):
        filename = 'resources/very_small_test_dictionary.json'
        with open(filename, 'r') as f:
            dictionary = json.load(f)
            result = test_doc.social_net_size(dictionary, 'LISTY')
            self.assertEqual(5, result)

    def test_07_eigth_dict(self):
        filename = 'resources/eighth_dictionary.json'
        with open(filename, 'r') as f:
            dictionary = json.load(f)
            result = test_doc.social_net_size(dictionary, 'LISTY')
            self.assertEqual(5132, result)

    def test_08_quarter_dict(self):
        filename = 'resources/quarter_dictionary.json'
        with open(filename, 'r') as f:
            dictionary = json.load(f)
            result = test_doc.social_net_size(dictionary, 'LISTY')
            self.assertEqual(11008, result)

    def test_09_half_dict(self):
        filename = 'resources/half_dictionary.json'
        with open(filename, 'r') as f:
            dictionary = json.load(f)
            result = test_doc.social_net_size(dictionary, 'LISTY')
            self.assertEqual(22741, result)

    def test_10_dict(self):
        filename = 'resources/dictionary.json'
        with open(filename, 'r') as f:
            dictionary = json.load(f)
            result = test_doc.social_net_size(dictionary, 'LISTY')
            self.assertEqual(51710, result)


class TestEdgeCases(unittest.TestCase):
    """A collection of test cases to ensure code doesn't randomly break."""
    def test_11_no_dictionary(self):
        dictionary = []
        result = test_doc.social_net_size(dictionary, 'HI')
        self.assertEqual(0, result)

    def test_12_repeated_words(self):
        dictionary = ['HI', 'HERE', 'HERE', 'THERE', 'HER', 'HE', 'SHE', \
                      'HEAR', 'HALLOW', 'HI', 'THERE']
        result = test_doc.social_net_size(dictionary, 'HI')
        self.assertEqual(7, result)

    def test_13_word_not_in_dict(self):
        dictionary = ['HI', 'HERE', 'THERE', 'HER', 'HE', 'SHE', 'HEAR', 'HALLOW']
        result = test_doc.social_net_size(dictionary, 'A')
        self.assertEqual(0, result)

    def test_14_one_word_dict(self):
        dictionary = ['HI']
        result = test_doc.social_net_size(dictionary, 'HI')
        self.assertEqual(1, result)

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
