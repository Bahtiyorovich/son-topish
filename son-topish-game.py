# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:42:01 2024

@author: Sherzodbek
"""

import random as r

def sontop(x = 10):
    tasodifiy_son = r.randint(1, x)
    print(f"Men 1 dan {x} gacha oraliqdagi bir sonni o'yladim, topaolasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))
        if taxmin < tasodifiy_son:
            print("Xato. Men o'ylagan son sal kattaroq. Yana harakat qiling:")
        elif taxmin > tasodifiy_son:
            print("Xato. Men o'ylagan son sal kichikroq. Yana urinib ko'ring:")
        else: 
            break
    print(f"Tabriklayman, siz {taxminlar} urinishda topdingiz")
    return taxminlar
    
def sontop_pc(y = 10):
    print(f"1 dan {y} gacha oraliqda son o'ylang men topaman!")
    quyi = 1
    yuqori = y
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin_pc = r.randint(quyi, yuqori)
        else:
            taxmin_pc = quyi
        javob = input(f"Siz {taxmin_pc} sonini o'yladingiz: to'g'ri (t), "
                      f"men o'ylagan son bundan kattaroq (+), yoki (-)".lower())
        if javob == "-":
            yuqori = taxmin_pc - 1
        elif javob == "+":
            quyi = taxmin_pc + 1
        else:
            break
    print(f"Men {taxminlar} ta urinishda topdim")
        
    return taxminlar
            
def gamer(x = 10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1), Yo'q(0): "))
        
gamer()          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            