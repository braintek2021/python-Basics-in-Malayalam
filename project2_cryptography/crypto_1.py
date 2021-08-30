# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:07:27 2020

@author: hp
"""

ciphertext = "REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER"
#List Creation
cipherlist = list(ciphertext.split())
#print(cipherlist)
COLS = 4
ROWS = 5
start=0
stop=5
translation_matrix = [None]*COLS
plaintext = ''
old_words=['VILLAGE','ROANOKE','GODWIN','SNOW']
new_words=['ENEMY','CAVALRY','TENNESSEE','REBELS']
#Translation Matrix
for i in range(COLS):
    row_items = cipherlist[start:stop]
    #print('First= ',row_items)
    start=start+ROWS
    stop=stop+ROWS
    #print('Second= ',row_items)
    translation_matrix[i] = row_items
#print('First= ',translation_matrix)
#Replace Words
for lst in translation_matrix: 
    for i, v in enumerate(lst):
        for k in range(len(old_words)):
            if old_words[k]== lst[i]:
                lst[i] = v.replace(old_words[k], new_words[k])

#print('Second= ',translation_matrix)

for i in range(ROWS):
    for matrix_col in translation_matrix:         
        word = str(matrix_col.pop())
        #print(matrix_col.pop())
        plaintext += word + ' '
print("translated = {}".format(plaintext))