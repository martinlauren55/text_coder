#!/usr/bin/python3
# -*- coding: utf-8 -*-

with open('text.txt', "r") as f:
  while True:
    c = f.read(1)
    c= c.lower()
    print("Read:", c)
    if c in ["а", "б", "в", "г"]:
        print("2")

    elif c in ["д", "е", "ё", "ж", "з"]:
        print("3")

    elif c in ["и", "й", "к", "л"]:
        print("4")

    elif c in ["м", "н", "о", "п"]:
        print("5")

    elif c in ["р", "с", "т", "у"]:
        print("6")

    elif c in ["ф", "ч", "ц", "ч"]:
        print("7")

    elif c in ["ш", "щ", "ъ", "ы"]:
        print("8")

    elif c in ["ь", "э", "ю", "я"]:
        print("9")

    elif c in [" ", "+"]:
        print("#")

    if not c:
        print ("End of file")
        break
