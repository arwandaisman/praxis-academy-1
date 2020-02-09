from xml.dom import minidom
mydoc = minidom.parse('file.xml')

items = mydoc.getElementsByTagName('item')

#for p in data['people']:
 #       print('Name: ' + p['name'])
  #      print('Website: ' + p['website'])
   #     print('From: ' + p['from'])
    #    print('')