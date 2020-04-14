from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.views import generic
from datetime import datetime

# Create your views here.

# i = 0
# total_list = []

today_day = datetime.today().strftime("%m-%d")


url1 = "http://www.wedarak.net"
image_link = ""

with urlopen('http://www.wedarak.net/shop/rtjournal.asp') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.select("p.journaltit a"):
        url1004 = anchor.get('href')[26:64]
        url10 = url1+url1004

        # total_list.append([])
        # total_list[i].append(anchor.text)
        # total_list[i].append(url10)
        #
        # i+=1

        if (url10[-5:] == today_day):


            with urlopen(url10) as response:
                soup = BeautifulSoup(response, 'html.parser')
                for anchor1 in soup.select('table p img'):
                    url2 = str(anchor1)[17:]


            indexNo = url2.find("jpg")
            image_link = url1 + url2[:indexNo + 3]


def index(req):
    context = {
        # "total_list" : total_list,
        "image_link" : image_link,
    }
    return render(req, "index.html", context=context)

def single(req):
    context = {

    }
    return render(req, "single.html", context=context)