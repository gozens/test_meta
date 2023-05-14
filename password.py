
from repertoire import effter,__ecri_fic__
from string import ascii_letters
from random import randint,choices
from os import walk
effter()
ch = r'C:\Users\T_xOx_T\Desktop\git_test'
ch = walk(ch)

for chemin,rep,fic in ch:break

def password():return ''.join(choices(ascii_letters,k=randint(5,9)))

for i in fic:
    if 'txt' in i:
        for j in range(1,randint(10,15)):__ecri_fic__(i,password()+'\n','a')