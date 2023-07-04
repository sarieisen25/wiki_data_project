import xml.etree.ElementTree as ET
import pandas as pd

# tree = ET.iterparse('/Users/sarieisen/Downloads/VSCode/wiki_example.xml', ('start', 'end'))
# for node in tree:
#     print(node[1])

with open('/Users/sarieisen/Downloads/Research/wiki_example.xml', 'rt') as f:
    tree = ET.parse(f)
    root = tree.getroot()

# from https://pymotw.com/3/xml.etree.ElementTree/parse.html
# csvfile = open('/Users/sarieisen/Downloads/VSCode/wiki_data.csv', newline = '')
# writer = csv.writer(csvfile, quoting = csv.QUOTE_NONNUMERIC)
# group_name = ''
# parsing = ET.iterparse('/Users/sarieisen/Downloads/VSCode/wiki_example.xml', events = ('start', 'end'))
# for (event, node) in parsing:
#     if node.tag != 'page':
#         continue
#     if not node.attrib.get('title'):
#         group_name = node.attrib('text')
#     else:
#         writer.writerow((group_name, node.attrib('title'), 
#                          node.attrib('id')))

#print(root.tag)
#print(len(root[100]))
# for elem in root[100]:
#     print('tag: '+ elem.tag)
#     print('text: '+elem.text)
# print(root[105][2])

# for child in root:
#     for i in range(len(child)):
#         if child[i].tag != None and child[i].text != None:
#             print(child[i].tag+': '+child[i].text)

# for child in root:
#     for i in range(len(child)):
#         if child[i].tag == 'title':
#             print('Title: '+child[i].text)

# for child in root:
#     print(child.tag, child.text)
#prints '{http://www.mediawiki.org/xml/export-0.10/}page' over and over


# path = []
# for event, elem in ET.iterparse('/Users/sarieisen/Downloads/VSCode/wiki_example.xml', events = ('start', 'end')):
#     if event == 'start':
#         path.append(elem.tag)
#     elif event == 'end':
#         if elem.tag == 'page':
#             if 'members' in path:
#                 print('member')
#             else:
#                 print('nonmember')
#         path.pop()
# print(path)

#lists the tags of each node
#make list of tuples (tag, text)
# data1 = []
# for node in tree.iter():
#     t = node.tag.replace('{http://www.mediawiki.org/xml/export-0.10/}', '')
#     if t == 'title' or t == 'id':
#         data1.append((t, node.text))

# for node in tree.iter():
#     print(node.tag.replace('{http://www.mediawiki.org/xml/export-0.10/}', ''))

#83545 pages

# #for parse not iterparse
# for node in tree.iter():
#     print(node.attrib.get('title'))

# with open('/Users/sarieisen/Downloads/VSCode/wiki_data.csv', mode = 'r') as file:
#     wiki_data = csv.reader(file)

# with open('/Users/sarieisen/Downloads/VSCode/wiki_data.csv', newline = '') as csvfile:
#     data = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
#     for row in data:
#         print(', '.join(row))








#WORKS
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
df['title'] = page_titles
df['id'] = page_ids
df['timestamp'] = rev_timestamp
# df.assign(timestamp = rev_timestamp)
df['contributor'] = rev_cont
# df.assign(contributor = rev_cont)
df['rev_bytes'] = rev_size
# df.assign(rev_bytes = rev_size)
df.to_csv('/Users/sarieisen/Downloads/Research/wiki_data2.csv', index = False)
#info put into csv for one xml file
print(df[0:5])

#to do:
#stop replacing csv every time
#add other data sheets













#intent: count the number of 'page' tags in the file
#result: always prints 0
# page_count = 0
# for node in tree.findall('page'):
#     page_count += 1
# print (str(page_count)+' pages')

# print(type(root))

#intent: print each page's title and id
#result: prints 'None: None' a bunch of times 
# for page in root:
#     t = page.attrib.get('title')
#     id = page.attrib.get('id')
#     if t != None:
#         print(str(t)+', id: '+str(id))

#intent: print each page's title
#result: prints 'None' a bunch of times and some titles, unsure how it chooses which
# for page in root:
#     for child in page:
#         if child.tag == 'title':
#             print('Title: '+child.attrib.get('title'))

#intent: print the list of page ids
#result: prints nothing
# for (event, node) in ET.iterparse('/Users/sarieisen/Downloads/VSCode/wiki_example.xml', ('start', 'end')):
#     if node.attrib.get('id') != None:
#         print(node.attrib.get('id'))

#intent: print the details of each page
#result: prints 'None' forever
# for page in root.iter():
#     print (page.attrib.get('title')+', ID: '+page.attrib.get('id'))

# cols = ['title', 'id']
# rows = []
# for node in tree.iter():
#     title = node.attrib.get('title')
#     id = node.attrib.get('id')
#     if title != None and id != None:
#         rows.append({'title': title, 'id': id})

# # print('rows: '+ str(len(rows)))
# table = pd.DataFrame(rows, cols)
# print(table)

#write loop that: goes through the pages then comments
#if comment contains 'revert' add the number page to an array
#add pages of those indicated numbers to a csv or array

# pages = []
# for child in root:
#     for node in child:
#         for i in range(len(node)):
#             t = node[i].tag.replace('{http://www.mediawiki.org/xml/export-0.10/}', '')
#             if t == 'revision':
#                 for line in node[i]:
#                     if line.tag == 'comment' and ('Revert' in line.text or 'Reversion' in line.text):
#                         pages.append(i)
# print(pages)
#prints []

#head (filename)
#title, id, ns

