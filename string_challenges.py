# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(sum([word.lower().count(x) for x in 'аеиоуюя']))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(*[n[0] for n in sentence.split()], sep='\n')


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(sum([len(n) for n in sentence.split()])/len(sentence.split()))