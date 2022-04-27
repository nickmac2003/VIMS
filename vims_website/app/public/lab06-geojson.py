import re

match = re.compile(r'}}\n{')

f = open('lab06.out', 'r')
text = f.read()
conts = match.sub('}},\n{', text)
f.close()

f = open('lab06geojson.js', 'w')
f.write('var mydata = {"type": "FeatureCollection", "features": [\n')
f.write(conts)
f.write(']}')
f.close()
