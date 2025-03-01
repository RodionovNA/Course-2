"""
Номер 1 - ввести слова, вывести самое встречающееся слово, 
если их несколько то вывести по алфавиту которое первое
"""


words = list(input().split())
cnt_words = {}
for d in words:
    if d in cnt_words:
        cnt_words[d] += 1
    else:
        cnt_words[d] = 1

answ = dict(sorted(cnt_words.items()))
CNT = -1
RES = None
for key, value in answ.items():
    if value > CNT:
        RES = key
        cnt = value

print(RES)
