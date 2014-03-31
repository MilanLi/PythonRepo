import urllib
from bs4 import BeautifulSoup


def printList(List):
    print("\n".join(List))


url = raw_input("Please input a url:")
choice = raw_input("you want links, images, or both?")

htmltext = urllib.urlopen(url).read()
soup = BeautifulSoup(htmltext)



if choice.startswith('l') or choice.startswith('b'):
    linkList = []
    for link in soup.find_all('a'):
        linkList.append(link["href"])

    print("links: ")
    printList(linkList)

if choice.startswith('i') or choice.startswith('b'):
    imageList = []
    for image in soup.find_all('img'):
        imageList.append(image["src"])

    print("images: ")
    printList(imageList)
