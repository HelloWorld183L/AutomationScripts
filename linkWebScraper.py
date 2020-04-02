from bs4 import BeautifulSoup
import requests

url = input("Please enter a URL to search for links: ")

response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, 'html.parser')

txtFile = open("links.txt", "a")

links = []

for link in content.find_all('a'):
    print(link.get('href'))
    txtFile.write("%s\n" % link.get('href'))

txtFile.writelines(links)

print("Links have been written to the links.txt text file in the root directory of this script.")
txtFile.close()