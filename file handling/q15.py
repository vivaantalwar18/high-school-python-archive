import pickle
strings = ["radar", "hello", "level", "python"]
with open("words.dat", "wb") as f:
	pickle.dump(strings, f)
with open("words.dat", "rb") as f:
	data = pickle.load(f)
for s in data:
	if s == s[::-1]:
		print("Palindrome:", s)