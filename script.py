import sys, json
import pandas as pd

fileInput = sys.argv[1]
fileOutput = sys.argv[2]

with open(fileInput) as f:
    data = json.load(f)

dataNorm = pd.json_normalize(data)                                      # read and normalize data

dataNormExp = pd.json_normalize(data=data, record_path='sub_issues', 
                            meta=['issue_key', 'fix_version'])          # expand 'sub_issues'

columns_titles = ["fix_version", "issue_key", "sub_issue_key", "commit_id", "commit_date",
                    "commit_message", "repository"]
dataReindex = dataNormExp.reindex(columns=columns_titles)               # sorting columns

dataReindex.to_csv(fileOutput, index=False)                             # write csv