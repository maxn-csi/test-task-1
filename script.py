# fix_version -> each.issue_key -> each.sub_issue_key -> 
# each.[commit_id, commit_date, commit_message, repository]

import csv, json, sys
from pandas import json_normalize

fileInput = sys.argv[1]
fileOutput = sys.argv[2]
inputFile = open(fileInput)
outputFile = open(fileOutput, 'w')

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

data = json.load(inputFile)

print(data)
print(json_normalize(data))
print(json_normalize(flatten_json(data)))

inputFile.close()

output = csv.writer(outputFile)

output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values()) #values row
# for row in (data["sub_issues"]):
#     output.writerow(row.values()) #values row