import os
import urllib.request
import json
import xml.etree.cElementTree as ET
import sys
from bs4 import BeautifulSoup
first_name=None
last_name=None
image=None
email=None

def main():
    url="https://reqres.in/api/users/"
    for i in range(1, 12):
        pageurl=url + str(i)
        resp = urllib.request.urlopen(pageurl)
        if resp.status_code == 200:
            json_resp = resp.json()
            id[i]=json_resp['data']['id']
            first_name[i] = json_resp['data']['first_name']
            last_name[i] = json_resp['data']['last_name']
            image[i]=json_resp['data']['avatar']
            email[i]=json_resp['data']['email']
            root = ET.Element("report")
            doc = ET.SubElement(root, "project")
            ET.SubElement(doc, "id").text = str(id_no)
            ET.SubElement(doc, "first_name").text = str(first_name)
            ET.SubElement(doc, "last_name").text = str(last_name)
            ET.SubElement(doc, "avatar").text = str(image)
            ET.SubElement(doc, "email").text = str(email)
            tree = ET.ElementTree(root)
            tree.write("report.xml", encoding="UTF-8", xml_declaration=True)

        else:
            print("Error while connecting...!")


if __name__ == '__main__':
    main()
