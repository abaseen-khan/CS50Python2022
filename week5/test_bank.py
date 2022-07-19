from bank import value


def test_hello():
	assert value("hello") == "$0"
	assert value("Hello") == "$0"


def test_letter_h():
	assert value("howdy") == "$20"
	assert value("Howdy") == "$20"
	assert value("hows it going") == "$20"
	assert value("How's it going") == "$20"


def test_normal():
	assert value("whats up") == "$100"
	assert value("What's up") == "$100"
	assert value("greetings") == "$100"
	assert value("Greetings") == "$100"


