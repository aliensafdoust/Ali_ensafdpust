from um import count

def test_1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count(" ali ensafdoust") == 0


if __name__ == "__main__" :
    main()
