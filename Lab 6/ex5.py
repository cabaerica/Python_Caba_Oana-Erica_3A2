import xml.etree.ElementTree as ET

def get_elements(path, attrs):
    tree = ET.parse(path)
    root = tree.getroot()
    elements = []
    for element in root.iter():
        for key, value in attrs.items():
            if element.attrib.get(key) == value:
                elements.append(element)
    return elements

def main():
    path = input('Enter path: ')
    attrs = input('Enter attrs: ')
    elements = get_elements(path, attrs)
    print(elements)


main()