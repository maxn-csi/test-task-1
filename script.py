# fix_version -> each.issue_key -> each.sub_issue_key -> 
# each.[commit_id, commit_date, commit_message, repository]

import csv, json, sys

fileInput = sys.argv[1]
fileOutput = sys.argv[2]
inputFile = open(fileInput)
outputFile = open(fileOutput, 'w')

data = json.load(inputFile)
# print(data)
inputFile.close()

output = csv.writer(outputFile)

output.writerow(data[0].keys())  # header row
for row in data:
    output.writerow(row.values()) #values row
# for row in (data["sub_issues"]):
#     output.writerow(row.values()) #values row