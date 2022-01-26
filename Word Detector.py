import os

def findWord(txtFile:str,word:str):
    with open(txtFile,'r') as f:content = f.read()
    if word.lower() in content.lower():
        return True
    else:
        return False
dir_contents = os.listdir()
noWord = 0
word = input('Enter Word For Find In ".txt" File : ')
for item in dir_contents:
    if item.lower().endswith('.txt'):
        flag = findWord(item,word)
        if flag:
            noWord+=1
            print(f'"{word}" Found In {item} And "{word}" Found {noWord} Time(s)')
        else:
            print(f'"{word}" Not Found In {item} ;_;')