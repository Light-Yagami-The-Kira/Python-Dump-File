import json
import re

with open(r'email extractor/data.json', 'r') as f:
    content = f.read()

x = str(json.loads(content)['persons'])

pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

matches = re.findall(pattern, x)
print(matches)