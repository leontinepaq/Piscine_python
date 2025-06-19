import sys

def whatis():
	args = sys.argv[1:]
	if len(args) == 0:
		return 

	try: 
		assert len(args) == 1, "more than one argument is provided"

		try:
			num = int(args[0])
		except ValueError:
			raise AssertionError("argument is not an integer")

		print("I'm Even." if num % 2 == 0 else "I'm Odd.")

	except AssertionError as error:
		print(f"AssertionError: {error}", file=sys.stderr)


if __name__ == "__main__":
	whatis()


# def test_whatis():
# 	import sys
# 	from io import StringIO

# 	test_cases = [
# 		(["whatis.py", "14"],      "I'm Even.\n"),
# 		(["whatis.py", "-5"],      "I'm Odd.\n"),
# 		(["whatis.py"],            ""),  # no output
# 		(["whatis.py", "Hi!"],     "AssertionError: argument is not an integer\n"),
# 		(["whatis.py", "13", "5"], "AssertionError: more than one argument is provided\n"),
# 		(["whatis.py", "--5"],     "AssertionError: argument is not an integer\n"),
# 	]

# 	for argv, expected_output in test_cases:
# 		original_stdout = sys.stdout
# 		original_stderr = sys.stderr

# 		sys.argv = argv

# 		sys.stdout = StringIO()
# 		sys.stderr = sys.stdout

# 		whatis()

# 		output = sys.stdout.getvalue()

# 		sys.stdout = original_stdout
# 		sys.stderr = original_stderr

# 		assert output == expected_output, (
# 			f"❌ Failed for argv: {argv}\n"
# 			f"Expected: {expected_output!r}\nGot: {output!r}"
# 		)

# 	print("✅ All inline tests passed!")

# if __name__ == "__main__":
# 	test_whatis()

