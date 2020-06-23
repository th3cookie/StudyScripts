#!/usr/bin/env python3.8

import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

'''
Setting up some things to parse the XML nicely
'''

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []

    def handle_data(self, data):
        self.data.append(data)

file_name = "ozfeed.xml"
# file_name = "products.xml"

try:
    tree = ET.parse(file_name)
except FileNotFoundError:
    print(f"File not found: {file_name}")
    sys.exit(1)

'''
First method to parsing XML is to iterate through the element in a for loop
'''

# Iterating through the element tree:
for item in tree.findall("channel/item"):
    # findtext grabs the text of the element straight away:
    title = item.findtext("title")
    link = item.findtext("link")
    description = item.findtext("description")
    parser = MyHTMLParser()
    parser.feed(description)

    print(f"TITLE = {title}")
    print(f"LINK = {link}")
    desc = ''.join(parser.data)
    print(f"DESCRIPTION: \n-------------------\n{desc}-------------------")

    # To grab the value of an attribute, first create the attribute element, then use the "get" method
    guid = item.find("guid")
    permalink = guid.get("isPermaLink")
    print(permalink)

    # To print the text of an element, specify the "text" method on the element:
    print(guid.text)

    # Returns the category element only if the attribute "Domain" = "https://www.ozbargain.com.au/tag/android"
    print(item.findall('category[@domain="https://www.ozbargain.com.au/tag/android"]'))

'''
Second method is to use the 'iter' method directly provided by the xml library
'''

# Element "Channel" is the root (even though everything is inside "rss" tag)
root = tree.getroot()
print(list(root))

# The iterator loops over the element and all subelements in document order, returning all elements with a matching tag.
print(list(root.iter("item")))

# Find all matching subelements by tag name or path.
print(list(root.iterfind("./channel/item/title")))
