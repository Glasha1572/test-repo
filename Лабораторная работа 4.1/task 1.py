#TODO решите

import json
import math

# src = input("Введите путь до файла JSON: ")
#
# def summa_proizvedenii(src):
#      python_obj = json.loads(src)
#      summa = 0
#
#      for i in python_obj:
#
#           for _ in i:
#                val = i.values()
#                result = math.prod(val)
#           summa = summa + result
#
#      print(round(summa, 3))

import json
import math

src = input("Введите путь до файла JSON: ")

def summa_proizvedenii(src):
     python_obj = json.load(src)
     summa = 0

     for i in python_obj:
          val = [i.values for _ in i]
          result = math.prod(val)
     summa += result

     print(round(summa, 3))
print(src)
