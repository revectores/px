import json
import xml.etree.ElementTree as ET
from pprint import pprint



tree = ET.parse('backup.xml')
root = tree.getroot()

intervals = []
types = json.load(open('../db/init/type.json'))
type_name2id = {t['name']: t['id'] for t in types}

for group in root.find('categories').findall('group'):
    print(group.find('name').text)
    for category in group.iter('category'):
        name = category.find('name').text
        print('\t' + name)
        for log in category.find('logs').iter('log'):
            interval = log.find('intervals').find('interval')

            intervals.append({
                'type':     type_name2id[name],
                'start':     int(interval.find('from').text),
                'end':         int(interval.find('to').text),
                'reported':    False,
                'report':    ""
            })
            # print('\t\t' + interval.find('from').text, interval.find('to').text)

json.dump(intervals, open('log.json', 'w'))

