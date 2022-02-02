def moo():
	"""
	Makes cow sound.
	"""
	for i in range(100):
		print('MOO!')

def make_cow():
	cow = ["          \\  ^__^","           \\ (oo)\\________","             (__)\\        )\\/\\","                  ||----W |","                  ||     ||"]
	for line in cow:
		print(line)

if __name__ == '__main__':
	moo()
	make_cow()
