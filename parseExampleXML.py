import xml.etree.ElementTree as ET

def exampleXML():
    tree = ET.parse('export.xml')
    root = tree.getroot()

    array = []
    i = 0

    for move in root.findall('ref'):
        array.append([])
        array[i].append(int(move[1].text)) # pop
        array[i].append([float(move[2].text[move[2].text.find('[')+1:move[2].text.find(',')]),float(move[2].text[move[2].text.find(',')+1:move[2].text.find(']')])])  # orig_loc
        array[i].append([float(move[3].text[move[3].text.find('[')+1:move[3].text.find(',')]),float(move[3].text[move[3].text.find(',')+1:move[3].text.find(']')])])  # dest_loc
        i+=1
    return array
