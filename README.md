## Task

Convert `report.json` to human-readable table format (e.g. xlsx or csv).

## Info

`report.json` is an output of some reporting tool for jira instance. 

- each `fix_version` may have multiple `issue_key`
- each `issue_key` may have multiple `sub_issue_key`
- `sub_issue_key` may be duplicated

desired way to represent such data by table columns:

```
fix_version -> each.issue_key -> each.sub_issue_key -> each.[commit_id, commit_date, commit_message, repository]
```
 
## Conditions

1. deadline:
    - 2020-05-27 16:00:00
2. tools:
    - any scripting language and libs you are convenient with
