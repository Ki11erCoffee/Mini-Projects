"""
Created on Wed Dec  8 11:09:25 2021

@author: Paul
"""

# import regex and assets
import re
import numpy as np
import csv
from pandas import *

'''
while(True):

    print("To quit enter q or quit \n\n")
    val = input("Enter your value: \n")
    if (val == "q" or val == 'quit'):
        print("\n\n")
        break
    else:
        print(val)
'''

def xltoDict(exelFile):
    '''

    Parameters
    ----------
    exelFile : TYPE
        DESCRIPTION.

    Returns
    -------
    Returns Dictionary with {'TextColor': Value}
    
    myDict : TYPE
        DESCRIPTION.

    '''
    color_df = pandas.read_excel(exelFile)
    values = color_df.to_dict('records')

    

    myDict = {}

    

    for i in range(len(values)):
        myDict[values[i]['TextColor']] = values[i]['Value']
        
    return myDict


# Creates Dictionary Mapping
myDict = xltoDict("./TextColor-Map.xlsx")

# Used to reference Dict. Index
name = list(myDict)


def clean(str):
    '''

    Parameters
    ----------
    str : TYPE
        DESCRIPTION.

    Returns
    -------
    Formulates Text to all undercase and replace - with space
    no_wspace_string : TYPE
        DESCRIPTION.

    '''
    # input string
    string = str

    # convert to lower case
    lower_string = string.lower()

    # remove numbers
    no_number_string = re.sub(r'\d+', '', lower_string)

    # remove all punctuation except words and space
    no_punc_string = no_number_string.replace("-", " ")
    no_punc_string = no_punc_string.replace("_", " ")
    # remove white spaces
    no_wspace_string = no_punc_string.strip()

    return no_wspace_string


# Read File
file_read = ""
with open("./Book1.csv") as file_name:
    file_read = csv.reader(file_name)
    
    handArrayOG = list(file_read)
    

del handArrayOG[0]

handArray = []

# Cleans up data to have an array of text
for x in handArrayOG:
    temp = ' '
    handArray.append(clean(temp.join(x)))
    
#print(handArray)

colorSort = []


# Assign Handle a value to be used to sort
for index in range(0,len(handArray)):
    temp = ' '
    temp = temp.join(handArrayOG[index])
    for color in myDict:
        if color in handArray[index]:
            
            # check flag to see if color is first word
            check = handArray[index].index(color)
            
            # Logic to check if text is in word
            if check == 0:
                colorSort.append([temp, myDict[color]])
                break
            elif " " + color + " " in handArray[index]:
                colorSort.append([temp, myDict[color]])
                break
            else:
                if color == name[-1]:
                    colorSort.append([temp, 404])
        
        
        else:
            # Assign value 404 if color isn't found
            if color == name[-1]:
                colorSort.append([temp, 404])
            

#print(colorSort)

# Sort based off of the value we assigned it
colorSort = sorted(colorSort, key=lambda x: x[1])
sortedColor = []

# Letters we are going to assign the handle (3 letters = 26^3 Combinations )
order = ['a', 'a', 'a']

# Assign letter and increment to the next letter
for i in colorSort:
    sortedColor.append(order[0]+order[1]+order[2] + '_' + i[0])
    
    order[2] = chr(ord(order[2]) + 1)

    
    if (order[1] == 'z' and order[2] == 'z'):
        order[0] = chr(ord(order[0]) + 1)
        order[2] = 'a'
        order[1] = 'a'
    elif (order[2] == 'z'):
        order[1] = chr(ord(order[1]) + 1)
        order[2] = 'a'


print(sortedColor)

# Output CSV file with sorted handles 
np.savetxt('./b.csv', sortedColor, delimiter=',', fmt='%s')


    

    
