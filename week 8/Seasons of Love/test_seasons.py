from seasons import cacu

def test_1():
    assert cacu("1999-01-01") == "Thirteen million, ninety-nine thousand, six hundred eighty minutes"
    assert cacu("1999-12-31") == "Twelve million, five hundred seventy-five thousand, five hundred twenty minutes"
    assert cacu("1970-01-01") == "Twenty-eight million, three hundred fifty-two thousand, one hundred sixty minutes"
    assert cacu("2002-07-15") == "Eleven million, two hundred forty thousand, six hundred forty minutes"
    assert cacu("ali Ensafdoust") == "Invalid date"
    assert cacu("January 1, 1999") == "Invalid date"
