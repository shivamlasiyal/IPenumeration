import subprocess

hostname =input("enter the IP :") 

halfurl = ""# Website url from where you get the api
halfurl1 = "" # API key and output format

url = halfurl+hostname+halfurl1

command = ['curl', '-X', 'GET', url]
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result.returncode == 0:
    print('Command executed successfully')
    xml_output = result.stdout.decode('utf-8')
    with open('output.xml', 'w') as f:
        f.write(xml_output)
else:
    print('Command execution failed')
    print('Error:', result.stderr.decode('utf-8'))
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('') # Path for XML file
root = tree.getroot()

# Extract tag values
tag_values = []
for tag in root.iter('name'):
    tag_values.append(tag.text)

# Write output to file
with open('output.txt', 'w') as f:
    for value in tag_values:
        f.write(value + '\n')
