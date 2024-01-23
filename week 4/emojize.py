import emoji
#getting input
emoji_in = input("Input: ").strip()
#printting emoji
print(f"Output: {emoji.emojize(emoji_in,language='alias')}")
