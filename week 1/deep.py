Enter = (
    str(
        input(
            "What is the Answer to the Great Question of Life, the Universe, and Everything? "
        )
    )
    .strip()
    .lower()
)
if Enter == "42" or Enter == "forty-two" or Enter == "forty two":
    print("Yes")
else:
    print("No")
