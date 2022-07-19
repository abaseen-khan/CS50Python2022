from fuel import convert


def test_ints():
	assert convert("1/2") == 50
	assert convert("3/4") == 75
	assert convert("1/5") == 20
	assert convert("3/6") == 50
	assert convert("36/100") == 36
	assert convert("99/100") == 99
	assert convert("1/100") == 1


def test_floats():
	assert convert("1.0/2.0") == 50
	assert convert("3.0/4.0") == 75
	assert convert("1.0/5.0") == 20
	assert convert("3.0/6.0") == 50
	assert convert("36.0/100.0") == 36
	assert convert("99.0/100.0") == 99
	assert convert("1.0/100.0") == 1


def test_zero():
	assert convert("1/0") is None
	assert convert("50/0") is None
	assert convert("100/0") is None


def test_non_int():
	assert convert("cat/dog") is None
	assert convert("me/you") is None
