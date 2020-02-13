# FETCHING INTERNET DATA ########################

import urllib.request

def main():
  webUrl = urllib.request.urlopen("http://www.google.com")
  print("Result code: " + str(webUrl.getcode()))    # just gives you the code for the website, e.g. 404 if it's not working correctly
  data = webUrl.read()                              # gives you the HTML for the webpage
  print(data)

# WORKING WITH JSON #################################################
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)  #json.load() takes JSON data and makes it useable in python
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
  count = theJSON["metadata"]["count"]
  print(str(count) + "events recorded")

  # for each event, print the place where it occurred
  for i in theJSON["features"]:
    print(i["properties"]["place"]
  print("--------------------------\n")    # just to separate the data to make it look cleaner

  # print the events that only have a magnitude greater than 4
  for i in theJSON["features"]:
    if i["properties"]["mag"] >= 4.0
    print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])   # %2.1f is just a format for decimals
  print("--------------------------\n")
      
  # print only the events where at least 1 person reported feeling something
  print("Events that were felt: ")
  for i in theJSON["features"]:
    feltReports = i["properties"]["felt"]
    if feltReports != None:
      if feltReports > 0:
        print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
        " reported " + str(feltReports) + " times")
        
        
    
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
  else:
    print("Received error, cannot parse results")


if __name__ == "__main__":
  main()

# PARSING AND PROCESESSING HTML ########################
from html.parser import HTMLParser

metacount = 0;

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print("Encountered comment: ", data)
    pos = self.getpos()
    print("\tAt line: ", pos[0], "position ", pos[1])
    
  def handle_starttag(self, tag, attrs):
    global metacount
    if tag == 'meta':
      metacount += 1
    print("Encountered tag: ", tag)
    pos = self.getpos()
    print("\tAt line: ", pos[0], "position ", pos[1])
    
    if attrs.__len__() > 0:
      print("\Attributes:")
      for a in attrs:
        print("\t", a[0], "=", a[1])
  
  def handle_endtag(self, tag):
    print("Encountered tag: ", tag)
    pos = self.getpos()
    print("\tAt line: ", pos[0], "position ", pos[1])
    
  def handle_data(self, data):
  print("Encountered data: ", data)
    if data.isspace:
      return
    pos = self.getpos()
    print("\tAt line: ", pos[0], "position ", pos[1])

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = open("sample.html")
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)


# MANIPULATING XML ###################################################
import xml.dom.minidom

# use the parse() function to load and parse an XML file
doc = xml.dom.minidom.parse("samplexml.xml")

# print out the document node and the name of the first child tage
print(doc.nodeName)
print(doc.firstChild.tagName)

# get a list of XML tags from the document and print each one 
skills = doc.getElementsByTagName("skill")
print("%d skills: " : % skills.length)
for skills in skills:
  print(skill.getAttribute("name"))
  
# create a new XML tag and add it into the document
newSkill = doc.createElement("skill")
newSkill.setAttribute("name", jQuery")
doc.firstChild.appendChild(newSkill)




