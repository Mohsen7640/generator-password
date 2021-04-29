import string
from random import choices
import argparse


def create_valid_password(length, lower=False, upper=False,
						  digits=False, punctuation=False):

	pool = ''

	if lower:
		pool += string.ascii_lowercase

	if upper:
		pool += string.ascii_uppercase

	if digits:
		pool += string.digits

	if punctuation:
		pool += string.punctuation

	if pool == '':
		pool += string.ascii_letters

	password = choices(pool, k=length)
	return ''.join(password)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description='Password Creator'
	)

	parser.add_argument(
		'--length',
		help='Length of password(default=8)[Int]',
		type=int,
		default=8
	)

	parser.add_argument(
		'-l', '--lower',
		help='Password include lowercase characters',
		action='store_true'
	)

	parser.add_argument(
		'-u', '--upper',
		help='Password include uppercase characters',
		action='store_true'
	)

	parser.add_argument(
		'-d', '--digits',
		help='Password include digits characters',
		action='store_true'
	)

	parser.add_argument(
		'-p', '--punctuation',
		help='Password include punctuations characters',
		action='store_true'
	)

	args = parser.parse_args()
	print(create_valid_password(
		length=args.length,
		lower=args.lower,
		upper=args.upper,
		digits=args.digits,
		punctuation=args.punctuation
	))
