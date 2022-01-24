import os
import json

basepath = '/Users/Nakkie/Downloads/'

loblist = os.listdir(basepath)

for file in loblist:
    print(file)


# checkdir = basepath+'/'+LOB
# schedule = basepath+'/'+LOB+'/'+LOB+'.json'
#
# itemlist = []
# itemlist = os.listdir(checkdir)
#
# pylist = []
# jsonlist = []
#
# remove = ['__init__.py',
#           'base.py',
#           'exporter_manager.py',
#           'qa_to_prod.py',
#           'mail_to_blob.py',
#           # '__pycache__',
#           # '.DS_Store',
#           LOB+'.json']
#
# for item in remove:
#     itemlist.pop(itemlist.index(item))
#
# for item in itemlist:
#     pylist.append(item.replace('.py',''))
#     print(item.replace('.py',''))