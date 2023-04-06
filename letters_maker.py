def check_word(word):
	with open('ru_RU.dic', 'r', encoding='utf-8') as file:
		lines = file.readlines()
		for i in range(0, len(lines)):
			if '/' in lines[i]:
				lines[i] = lines[i].split('/')[0]
			else:
				lines[i] = lines[i].rstrip()
			if word == lines[i]:
				return True
		return False


def counter(word, mass_letters):
	for i in range(0, len(mass_letters)):
		if word.count(mass_letters[i]) > mass_letters.count(mass_letters[i]):
			return False
	return True


def length_three(mass_letters):
	three_words = []
	for x1 in mass_letters:
		for x2 in mass_letters:
			for x3 in mass_letters:
				word = x1 + x2 + x3

				if counter(word, mass_letters):
					if check_word(word):
						if word not in three_words:
							three_words.append(word)
							print(f"\033[33m\033[2m {word}")


def length_four(mass_letters):
	four_words = []
	for x1 in mass_letters:
		for x2 in mass_letters:
			for x3 in mass_letters:
				for x4 in mass_letters:
					word = x1 + x2 + x3 + x4

					if counter(word, mass_letters):
						if check_word(word):
							if word not in four_words:
								four_words.append(word)
								print(f"\033[33m\033[2m {word}")


def length_five(mass_letters):
	five_words = []
	for x1 in mass_letters:
		for x2 in mass_letters:
			for x3 in mass_letters:
				for x4 in mass_letters:
					for x5 in mass_letters:
						word = x1 + x2 + x3 + x4 + x5

						if counter(word, mass_letters):
							if check_word(word):
								if word not in five_words:
									five_words.append(word)
									print(f"\033[33m\033[2m {word}")


def length_six(mass_letters):
	six_words = []
	for x1 in mass_letters:
		for x2 in mass_letters:
			for x3 in mass_letters:
				for x4 in mass_letters:
					for x5 in mass_letters:
						for x6 in mass_letters:
							word = x1 + x2 + x3 + x4 + x5 + x6

							if counter(word, mass_letters):
								if check_word(word):
									if word not in six_words:
										six_words.append(word)
										print(f"\033[33m\033[2m {word}")


while True:
	length = str(input('\033[37m\033[2m Введите все длины слов через пробел (0 - окончание) '))
	if '0' in length:
		quit()
	letters = str(input('\033[37m Введите все буквы из набора через пробел ')).lower()
	list_of_letters = letters.split(' ')
	list_of_lengths = length.split(' ')

	flag = True

	if '3' in list_of_lengths:
		print(f'\033[32m\033[1m --- Ищу слова из трёх букв ---')
		length_three(list_of_letters)
		flag = False
	if '4' in list_of_lengths:
		print(f'\033[32m\033[1m  --- Ищу слова из четырёх букв ---')
		length_four(list_of_letters)
		flag = False
	if '5' in list_of_lengths:
		print(f'\033[32m\033[1m  --- Ищу слова из пяти букв ---')
		length_five(list_of_letters)
		flag = False
	if '6' in list_of_lengths:
		print(f'\033[32m\033[1m  --- Ищу слова из шести букв ---')
		length_six(list_of_letters)
		flag = False

	if flag:
		print(f"\033[31m\033[2m Такой формат я не приму: {length}, {list_of_letters}")
