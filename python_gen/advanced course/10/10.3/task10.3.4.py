'''
Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.
'''
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
s_list = sorted(s.split())
ch = 0
for i in sorted(set(s_list), reverse=True):
    if s_list.count(i) >= ch:
        ch = s_list.count(i)
        qwe += [i]
print(sorted(qwe[0]))


'''words_list = s.split()

words_dict = {}
for word in words_list:
    words_dict[word] = words_dict.get(word, 0) + 1

most_common = words_list[0]
for word in words_dict.keys():
    if words_dict[word] > words_dict[most_common]:
        most_common = word
    elif words_dict[word] == words_dict[most_common] and word < most_common:
        most_common = word

print(most_common)'''