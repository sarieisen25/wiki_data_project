import xml.etree.ElementTree as ET
import pandas as pd

with open('/Users/sarieisen/Downloads/Research/1-june1.xml', 'rt') as f:
    tree = ET.parse(f)
    root = tree.getroot()


df = pd.read_csv('/Users/sarieisen/Downloads/Research/wiki_data2.csv')
page_titles = []
page_ids = []
rev_timestamp = []
rev_cont = []
rev_size = []

for child in root:
    for i in range(len(child)):
        t = child[i].tag.replace('{http://www.mediawiki.org/xml/export-0.10/}', '')
        if t == 'title':
            page_titles.append(child[i].text)
        elif t == 'id':
            page_ids.append(child[i].text)
            #df.loc[i, 'id'] = child[i].text
        elif t == 'revision':
            for j in range(len(child[i])):
                p = child[i][j].tag.replace('{http://www.mediawiki.org/xml/export-0.10/}', '')
                if p == 'timestamp':
                    rev_timestamp.append(child[i][j].text)
                elif p == 'contributor':
                    rev_cont.append(child[i][j][0].text)
                elif p == 'text':
                    rev_size.append(child[i][j].attrib.get('bytes'))
# # print(page_titles[5:20])
df[len(df.index), 'title'] = page_titles
df[len(df.index), 'id'] = page_ids
df[len(df.index), 'timestamp'] = rev_timestamp
# df.assign(timestamp = rev_timestamp)
df[len(df.index), 'contributor'] = rev_cont
# df.assign(contributor = rev_cont)
df[len(df.index), 'rev_bytes'] = rev_size
# df.assign(rev_bytes = rev_size)
df.to_csv('/Users/sarieisen/Downloads/Research/wiki_data2.csv', index = False)
#info put into csv for one xml file
print(df[0:5])