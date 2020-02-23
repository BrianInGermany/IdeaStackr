import imgkit
import sys, os
import csv

# WIP! Does not work yet!
print("I need three paths from you:")
csvPath = input("Please enter path of CSV file:\n")
imgModulePath = input("Please enter path to 'wkhtmltoimg' executable:\n")
outputPath = input("Please enter the name of an existing directory where cards can be saved:\n")
options = {
    'width':666,
        'encoding': 'UTF-8'
}
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
