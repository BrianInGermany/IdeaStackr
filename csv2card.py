import imgkit
import sys, os
import csv

# WIP! Does not work yet!
csvPath = input("Please enter path of CSV file:\n")
imgModulePath = input("Please enter path to 'wkhtmltoimg' executable:\n")
csvFile = open(csvPath, "r", encoding="utf-8")
csvReader = csv.reader(csvFile, delimiter=";")
def validate_csv(csvReader):
    rowIndex = 0
    for row in csvReader:
        rowIndex += 1
        if rowIndex > 1:
            pass
def save_img_cards(csvReader):
    rowIndex = 0
    for row in csvReader:
        rowIndex += 1
        if rowIndex > 1:

            # config = imgkit.config(wkhtmltoimage='/examplePath/bin/wkhtmltoimage')
            config = imgkit.config(wkhtmltoimage=imgModulePath)
