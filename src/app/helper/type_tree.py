import json
import xml.etree.ElementTree as ET
import Queue
from pprint import pprint


tree = ET.parse('type.xml')
root = tree.getroot()
root.depth = 0
type_id = 0
root.id = type_id
type_id += 1

types = []
queue = Queue.Queue()
queue.put(root)


while not queue.empty():
    parent = queue.get()
    for child in parent:
        child.id = type_id
        type_id += 1
        child.depth = parent.depth + 1
        child_type = {
            'id':         child.id,
            'name':     child.tag,
            'depth':    child.depth,
            'parent':     parent.id,
            'color':    child.attrib['color'] if 'color' in child.attrib else parent.attrib['color']
        }
        types.append(child_type)
        queue.put(child)

if __name__ == '__main__':
    print(json.dumps(types))

