# addons_xml_generator.py
import os

addons_dir = './addons'
addons_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n'

for addon in os.listdir(addons_dir):
    addon_path = os.path.join(addons_dir, addon, 'addon.xml')
    if os.path.isfile(addon_path):
        with open(addon_path, 'r', encoding='utf-8') as f:
            content = f.read()
            addons_xml += content + '\n'

addons_xml += '</addons>\n'

with open('addons.xml', 'w', encoding='utf-8') as f:
    f.write(addons_xml)