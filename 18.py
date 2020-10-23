import json
import yaml


#  Json to text

with open("sample_json.json","r") as js:
	text = json.load(js)
with open("json_to_text","a") as jfile:
	jfile.write(str(text))

print("Json to text done")


# Json to Yaml

with open("sample_json.json","r") as js:
	text = json.load(js)
with open("json to yaml","a") as jy:
	jy.write(yaml.dump(text))

print("Json to Yaml done")	


 # Yaml to Json

with open("yaml_file.yaml") as y:
	text = yaml.load(y)

with open("yaml to json", "r") as yj:
	yj.write(str(json.dump(text)))

print("yaml to json")	


# Yaml to text

with open("yaml_file.yaml","r") as f:
	a = yaml.load(f)
with open("yaml to text.txt","a") as f:
	f.write(a)




