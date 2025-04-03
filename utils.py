from json import loads,dumps,dump
import csv
import uuid

def pr(data):
    print(dumps(data,indent=2))

def file(data,int=''):
    with open('data'+str(int)+'.json', 'w') as document:
        dump(data, document,indent=2)

def sheet(name,headers,content):
    with open(str(name)+'.csv','w',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(content)

def UUID():
    return uuid.uuid4()

def clear():
    print("\033[H\033[2J")