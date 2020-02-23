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
            # check all fields are of correct type. ANd that each row has right length
            pass

def save_img_cards(csvReader):
    rowIndex = 0
    newCards = 0
    
    # config = imgkit.config(wkhtmltoimage='/examplePath/bin/wkhtmltoimage')
    config = imgkit.config(wkhtmltoimage=imgModulePath)
    for row in csvReader:
        rowIndex += 1
        if rowIndex > 1:
            if (str(idNum)+".jpg") not in os.listdir(outputDir):
                htmlTemplate = f"""
<!DOCTYPE html>
<head>
    <style>
    table, th, td {{
    border: 1px solid black;
    }}
    </style>
    </head>
<html>
    <table width="666" height="53" border="1">
        
        <tr>
        <th><font size="5">ID: {idNum}</font></th>
        <th><font size="5">{infoType}</font></th>
        <th><font size="5">Source: {source}</font></th>
        <th><font size="5">Page: {page}</font></th>
        </tr>
        
    </table>
    <table width="666" height="375" border="1">
        <tr>
        <th width="25%" height="38"><font size="5">Topic</font></th>
        <th width="75%" height="38"><font size="5">Statement</font></th>
        </tr>
        <tr>
            
        <td height="338"><font size="5">{topic}</font></td>
        <td height="338"><font size="5">{statement}</font></td>
    </tr>
        
    </table>
</html>
"""
                imgkit.from_string(htmlTemplate, outputDir + str(idNum) + ".jpg", options=options)
                newCards += 1
    print(str(newCards) + " new cards saved to jpg.")

