import json
with open('lab_info.json', 'r') as f:
  data = json.load(f)

CONFIGURATION = data["CONFIGURATION"]
