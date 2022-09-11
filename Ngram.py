import random
import math
text = open("451.txt").read() #программа будет тестироваться на книге "451 градус по Фаренгейту"
for c in '''!@#№?/%.,"'[]:;-''': #обработка файла
    text = text.replace(c,"")
text = text.lower()
corpus = text.split()
print("Введите размер n-грамма")
n = int(input())
print("Введите стартовое слово на английском")
word = input()
word = word.lower()
while corpus.count(word) <=5:
    print("Введите другое слово")
    word = input()
print("Введите длину предложения ")
l = int(input())

'''функция ниже создаёт n-gram модель при помощи словаря, в котором key это n подряд идущих слов,
а значение словаря это число таких комбинаций в тексте.'''
def create_ngram(n):
    gram = dict()
    for i in range(len(corpus)-(n-1)):
        key = tuple(corpus[i:i+n])
        if key in gram:
            gram[key] +=1
        else:
            gram[key] = 1
    gram = sorted(gram.items(),key = lambda items : items[1],reverse = True) #сортируем словарь по убыванию частоты комбинации
    return gram
gram = create_ngram(n)
'''Данная функция выбирает следующее слово случайным образом,учитывая частоту, с которой комбинация предыддущего
и следующего слова встречается в тексте'''
def weighted_choice(choices):
    cumm_sum = sum(element[1] for element in choices)
    r = random.uniform(0,cumm_sum)
    start = 0
    for element in choices:
        if start + element[1] > r:
            return element[0][1]
        start += element[1]

#составляем предложение
sentence = ""
def get_gram_sentence(gram,word,l):
    for i in range(l):
        global sentence
        sentence = sentence + " " + word
        choices =[element for element in gram if element[0][0] == word]
        word = weighted_choice(choices)
get_gram_sentence(gram,word,l)
print(sentence)




