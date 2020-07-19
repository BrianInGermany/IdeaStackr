import imgkit
import sys
import os
import csv
from pathlib import Path


print("I need two paths from you:")
csvPath = input("Please enter path of CSV file:\n")
outputDir = input("Please enter the path of an existing directory where cards can be saved:\n")
options = {
    'width':666,
        'encoding': 'UTF-8'
}
csvPath = Path(csvPath)
outputDir = Path(outputDir)
csvFile = open(csvPath, "r", encoding="utf-8")
csvReader = csv.reader(csvFile, delimiter=";")



def validate_csv(csvReader):
    idNumList = []
    success = True
    failureDict = {}
    rowIndex = 0
    fieldDict = {
        0:"ID number is not an int",
        1:"Info Type is not 'q', 'o' or 'p'",
        2:"Source is not a string",
        3:"Page number is not a string",
        4:"Topic is not a string",
        5:"Statement is not a string",
        6:"Wrong number of columns in row: check for extra semicolons or missing fields"
    }
    for row in csvReader:
        rowIndex += 1
        if rowIndex > 1:
           
            # One boolean for each column, plus one more for a length check:
            failureDict[rowIndex] = [True, True, True, True, True, True, True]
            try:
                int(row[0])
                # save idNums to list to make sure not repetitions.
                idNumList.append(row[0])
            except:
                failureDict[rowIndex][0] = False
            if row[1].lower() not in ["q", "p", "o"]:
                failureDict[rowIndex][1] = False
            # if not (isinstance(row[2], str)):
            #     failureDict[rowIndex][2] = False
            # if not (isinstance(row[3], str)):
            #     failureDict[rowIndex][3] = False
            # if not (isinstance(row[4], str)):
            #     failureDict[rowIndex][4] = False
            # if not (isinstance(row[5], str)):
            #     failureDict[rowIndex][5] = False
            if len(row) != 6:
                failureDict[rowIndex][6] = False
    for rowNum, statusList in failureDict.items():
        fieldIndex = 0
        for field in statusList:
            
            if field == False:
                success = False
                print("\n")
                print(f"ERROR! Row number {rowNum} of CSV:")
                print(f"Field: {fieldDict[fieldIndex]}\n")
    
            fieldIndex += 1
    idCountDict = {}
    for idVal in idNumList:
        idCountDict[idVal] = 0
    for idVal in idNumList:
        idCountDict[idVal] += 1
        if idCountDict[idVal] > 1:
            print(f"ERROR! ID number {idVal} is not unique! Make it unique...\n")

    return success


            

def save_img_cards(csvReader):
    csvFile.seek(0)
    rowIndex = 0
    newCards = 0
    # if wkhtemltopdf in installed but not found, run the below command with the path to the executable, 
    # or add the containing directory to the system path.
    # config = imgkit.config(wkhtmltoimage='/examplePath/bin/wkhtmltoimage')
    for row in csvReader:
        rowIndex += 1
        if rowIndex > 1:
            idNum = row[0]
            infoType = row[1]
            if infoType.lower() == "o":
                infoType = "My Opinion"
            if infoType.lower() == "p":
                infoType = "Paraphrase"
            if infoType.lower() == "q":
                infoType = "Quote"
            source = row[2]
            page = row[3]
            topic = row[4]
            statement = row[5]
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
                cardPath = Path.joinpath(outputDir, str(idNum) + ".jpg")
                imgkit.from_string(htmlTemplate, cardPath, options=options)
                newCards += 1
    print(str(newCards) + " new cards saved to jpg.")

if validate_csv(csvReader) == True:
    print("Validation passed, writing to JPG for rows not yet generated to card.")
    save_img_cards(csvReader)
else:
    print("CSV validation failed, see above output for errors.\nNo cards saved.")

csvFile.close()

