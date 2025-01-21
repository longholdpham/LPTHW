# Strings, Bytes, and Character Encodings
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
	line = language_file.readline() #Read one line 

	if line: #if statement here is used to simply tests for empty string, as long as readline above give us something, this will be true, thus the indented code below will run. This if statement also keep the main function from looping forever
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)

#unicode is the univiersal dictionary of characters, include emoji + other international languages. E.g, the letter 'A' has a unicode point of U+0041
#encoding translates unicode code points into bit format so that computer can understand and store it
#there's also different encoding schemes: UTF-8, UTF-16, and UTF-32
#decoding is the reverse of encoding, takes bits and converts back into unicode code points

def print_line(line, encoding, errors):
	next_lang = line.strip() #strip() method removes any white spaces in the string, also removing any trailing \n on the string
	raw_bytes = next_lang.encode(encoding, errors=errors) #utf-8 encode the string (turning string into byte), with 'errors' ouput for the error method
	cooked_string = raw_bytes.decode(encoding, errors=errors) #decode the the byte, allowing you to display the original string

	print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)