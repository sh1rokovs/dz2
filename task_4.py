import re
single_line = 'Олег Оля Вася'

# single_line = input('Введите предложение:')

words_in_lines = '\n'.join(single_line.split())
words_in_lines = single_line.replace(' ', '\n')
words_in_lines = re.sub(r'\s+', '\n', single_line)

print(words_in_lines)
