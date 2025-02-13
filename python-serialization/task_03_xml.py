#!/usr/bin/python3
"""
This module defines a class named Rectangle.

Usage:
    You can create instances of Rectangle.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(data, filename):
    try:
        root = ET.Element("data")
        for key, value in data.items():
            item = ET.SubElement(root, key)
            item.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename)
        return True
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False


        import xml.etree.ElementTree as ET

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}

    for child in root:

        value = child.text.strip()


        if value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
            value = float(value)

        data[child.tag] = value

    return data

