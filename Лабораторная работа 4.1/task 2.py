 # TODO импортировать необходимые молули

import csv
import json

src = input("Введите путь до файла CSV: ")
def konverter(src):
    lines = [line for line in csv.DictReader(src)]
    print(json.dumps([lines], 4))

import csv
import json


src = input("Введите путь до файла CSV: ")


def konverter(src):
    lines = [line for line in csv.DictReader(src)]
    print(json.dumps([lines], 4))
