#! /usr/bin/env python
# http://www.amk.ca/talks/2006-02-07/
# http://docs.python.org/lib/elementtree-functions.html
# http://effbot.org/zone/element.htm#searching-for-subelements
import xml.etree.ElementTree as ET
tree = ET.parse("converter.config")
doc = tree.getroot()
thingy = doc.find('inputfile')

print thingy.text