import unittest
from ahocorasick import AhoCorasick

class TestAhoCorasick(unittest.TestCase):
    def test_paper_example(self):
        corpus = 'ushers'
        keywords = ['he', 'she', 'his', 'hers']
        expected = {
            'he'  : 1,
            'hers': 1,
            'she' : 1,
        }

        ac = AhoCorasick(keywords)
        ac.build()
        actual = ac.search(corpus)

        self.assertEqual(actual, expected)

    def test_wikipedia_example(self):
        corpus = 'abccab'
        keywords = ['a', 'ab', 'bab', 'bc', 'bca', 'c', 'caa']
        expected = {
            'a' : 2,
            'ab': 2,
            'bc': 1,
            'c' : 2,
        }

        ac = AhoCorasick(keywords)
        ac.build()
        actual = ac.search(corpus)

        self.assertEqual(actual, expected)

    def test_simple_all_substrings(self):
        corpus = 'abc'
        keywords = ['a', 'b', 'c', 'ab', 'bc', 'abc']
        expected = {
            'a'  : 1,
            'b'  : 1,
            'c'  : 1,
            'ab' : 1,
            'bc' : 1,
            'abc': 1,
        }

        ac = AhoCorasick(keywords)
        ac.build()
        actual = ac.search(corpus)

        self.assertEqual(actual, expected)

    def test_nonalpha_chars(self):
        corpus = 'I think she said, "the quick brown dog jumps over the lazy dog", maybe!'
        keywords = ['the', 'dog', 'he']
        expected = {
            'the': 2,
            'dog': 2,
            'he' : 3,
        }

        ac = AhoCorasick(keywords)
        ac.build()
        actual = ac.search(corpus)

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
