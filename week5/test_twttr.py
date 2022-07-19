from twttr import shorten


def test_name():
	assert shorten("abaseen") == "bsn"
	assert shorten("cat") == "ct"
	assert shorten("  ") == "  "
