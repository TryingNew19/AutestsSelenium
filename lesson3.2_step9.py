def test_substring(fulltext, substring):
   assert substring in fulltext, ('expected {} to be substring of {}').format(substring, fulltext)

test_substring("fulltext1", "fulltext")