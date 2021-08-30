# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:07:27 2020

@author: hp
"""

ciphertext = "REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER"
cipherlist = list(ciphertext.split())
print(cipherlist)
COLS = 4
ROWS = 5
start=0
stop=5
translation_matrix = [None]*COLS
plaintext = ''
old_words=['VILLAGE','ROANOKE','GODWIN','SNOW']
new_words=['ENEMY','CAVALRY','TENNESSEE','REBELS']
key=[-1,2,-3,4]

for k in key:
    if k < 0: # reading bottom-to-top of column
        row_items = cipherlist[start:stop]
    elif k > 0: # reading top-to-bottom of columnn
        row_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = row_items
    start += ROWS
    stop += ROWS
print(translation_matrix)

for lst in translation_matrix: 
    for i, v in enumerate(lst):
        for k in range(len(old_words)):
            if old_words[k]== lst[i]:
                lst[i] = v.replace(old_words[k], new_words[k])

print(translation_matrix)

for i in range(ROWS):
    for matrix_col in translation_matrix:         
        word = str(matrix_col.pop())
        plaintext += word + ' '
print("translated = {}".format(plaintext))