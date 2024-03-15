from bs4 import BeautifulSoup
import codecs
import urllib.request

url="https://www.notion.so/owid/Data-analysis-exercise-Our-World-in-Data-Junior-Data-Scientist-application-ab287a3c07264b4d91aadc436021b8c0"
#url="https://www.who.int"
#url="https://www.linkedin.com/jobs/view/pharmaceutical-scientist-at-varda-space-industries-3631892846?trk=public_jobs_topcard-title"
#url="https://www.notion.so"
"""
req = urllib.request.Request(url, headers={'User-Agent': 'Slimjet/30.0.5.0'})
html = urllib.request.urlopen(req).read()

soup = BeautifulSoup(html,features="lxml")

tabulka = soup.find("table", {"class" : "detail-char"})

records = [] # store all of the records in this list
for row in tabulka.findAll('tr'):
    col = row.findAll('td')
    prvy = col[0].string.strip()
    druhy = col[1].string.strip()
    record = '%s;%s' % (prvy, druhy) # store the record with a ';' between prvy and druhy
    records.append(record)

fl = codecs.open('output.txt', 'wb', 'utf8')
line = ';'.join(records)
fl.write(line + u'\r\n')
fl.close()
"""
    
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

req = Request(url, headers={'User-Agent': 'Mozilla'})
html = urlopen(req).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
