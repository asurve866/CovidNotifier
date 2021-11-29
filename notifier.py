from plyer import notification
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import json
import urllib




def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon = "C:\\Users\\VRUDDHI PARAG TOLIA\\PycharmProjects\\COVID NOTIFIER\\images\\index.ico",
        timeout=10
    )

def getData(url):
    req = requests.get(url)
    return req.text


if __name__ == "__main__":
    notifyMe("Hello ", "Vruddhi Utth jaa")
    myHtmlData = getData("https://www.covidsimpact.com/indiaInfo")
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.prettify())

    #for table in soup.find_all('tbody').find_all('tr'):
     #   print(table.get_text())



