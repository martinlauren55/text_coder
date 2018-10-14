#!/usr/bin/python3
# -*- coding: utf-8 -*-
text_res = " "
with open('input_text.txt', "r") as f:
  while True:
    c = f.read(1)
    c= c.lower()
    print("Read:", c)
    if c in ["а", "б", "в", "г"]:
        print("2")
        text_res+=str(2)

    elif c in ["д", "е", "ё", "ж", "з"]:
        print("3")
        text_res += str(3)
        print(text_res)

    elif c in ["и", "й", "к", "л"]:
        print("4")
        text_res += str(4)
        print(text_res)

    elif c in ["м", "н", "о", "п"]:
        print("5")
        text_res += str(5)
        print(text_res)

    elif c in ["р", "с", "т", "у"]:
        print("6")
        text_res += str(6)
        print(text_res)


    elif c in ["ф", "ч", "ц", "ч"]:
        print("7")
        text_res += str(7)
        print(text_res)

    elif c in ["ш", "щ", "ъ", "ы"]:
        print("8")
        text_res += str(8)
        print(text_res)

    elif c in ["ь", "э", "ю", "я"]:
        print("9")
        text_res += str(9)
        print(text_res)

    elif c in [" ", "+"]:
        print("#")
        text_res += str(0)
        print(text_res)

    if not c:
        print ("End of file")
        print(text_res)
        break
