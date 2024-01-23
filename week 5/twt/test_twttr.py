from twttr import shorten

def test_program():
        assert shorten("ali") == "l"
        assert shorten("Aeu") == ""
        assert shorten("uiOe") == ""
        assert shorten("1a2x3E") == "12x3"

