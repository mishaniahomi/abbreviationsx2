from bs4 import BeautifulSoup
import re
import requests
arr_abbreviations=[]
URL = "http://klmn.price-review.ru/sokrashcheniya.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
full_page = requests.get(URL, headers=headers)
soups = BeautifulSoup(full_page.content, "html.parser")
print("____________________________________________________________________________")
counter = 0
for li in soups.findAll("a"):
    try:
        str1 = li["href"]

        str1 = str1.replace('http://klmn.price-review.ru/search.html?ask=','')
        upper = 0
        for letter in str1:
            if(letter.isupper()):
                upper+=1
        if upper>=2:
            full_page = requests.get(li["href"], headers=headers)
            soups2 = BeautifulSoup(full_page.content, "html.parser")
            p1 = ""

            p1 = soups2.find("p", {"class": "value"})
            print(str1 + " - "+p1)
            if p1=="":
                p1="пусто"



            counter+=1

    except:
        URL = "http://klmn.price-review.ru/sokrashcheniya.html"

print(counter)