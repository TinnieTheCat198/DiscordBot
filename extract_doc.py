import sqlite3
import re
import requests
from bs4 import BeautifulSoup
import time

regex = 'Mã lớp:\s([A-Z]+[0-9]+)\s?$'
GS_TRI_THUC_URL = "https://docs.google.com/document/d/e/2PACX-1vT1YqDoJ6oQo5fuZs-maN6MJ2i82zk_DeX6dW1_S7d5DLgVNHt66Y6QRr3o4qRQK-RsgbdcDqsASJAi/pub"
class_ids = set()

def check_patter_classid(phrase):
    return re.match(regex,phrase)

def extract_class_ids(phrase):
    return re.match(regex,phrase)[1]

def retrieve_class_ids():
    class_ids_t = set()
    response = requests.get(GS_TRI_THUC_URL)
    soup = BeautifulSoup(response.text,'lxml')
    tags = soup.find_all('p')
    for tag in tags:
        if check_patter_classid(tag.text):
            class_ids_t.add(extract_class_ids(tag.text))
    return class_ids_t

def printSet(setName):
    for item in setName:
        print(item)