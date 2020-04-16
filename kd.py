from re import findall

print('''

█▄▀ █▀█ ▀█▀ ▄█ █▄▀   █░█ █▄░█ █▄▀ █▄░█ █▀█ █░█░█ █▄░█
█░█ █▄█ ░█░ ░█ █░█   █▄█ █░▀█ █░█ █░▀█ █▄█ ▀▄▀▄▀ █░▀█


===========================
vk: https://vk.com/kot1kunknown
github: https://github.com/Kot1kUnknown
===========================


	''')

keysen = {
	'A':"AAA", 'B':"AAА", 'C':"AAΑ",
	'D':"AАA", 'E':"AАА", 'F':"AАΑ",
	'G':"AΑA", 'H':"AΑА", 'I':"AΑΑ",
	'J':"АAA", 'K':"АAА", 'L':"АAΑ",
	'M':"ААA", 'N':"ААА", 'O':"ААΑ",
	'P':"АΑA", 'Q':"АΑА", 'R':"АΑΑ",
	'S':"ΑAA", 'T':"ΑAА", 'U':"ΑAΑ",
	'V':"ΑАA", 'W':"ΑАА", 'X':"ΑАΑ",
	'Y':"ΑΑA", 'Z':"ΑΑА", ' ':"ΑΑΑ",
}

cryptmode = input("[E]ncrypt|[D]ecrypt: ").upper()

if cryptmode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit

startMessage = input("Напиши своё сообщение: ").upper()

def regular(text):
	template = r"\w{3}"
	return findall(template, text)

def encryptDecrypt(mode, message, final = ""):
	if mode == 'E':
		for symbol in message:
			if symbol in keysen:
				final += keysen[symbol]
	else:
		for threeSymbols in regular(message):
			for key in keysen:
				if threeSymbols == keysen[key]:
					final += key

	return final
print("Твоё сообщение:", encryptDecrypt(cryptmode, startMessage))
