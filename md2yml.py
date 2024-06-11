import yaml

markdown_table = """
| year | name | publisher | rank | core | scope | short | full | format | cfp | country |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2099 | [ABC'99](https://conf.researchr.org/series/abc) | IEEE | C | <https://portal.core.edu.au/conf-ranks/2099> | SE | 2 | 10 | 1C | 2099-12-31 | Antarctica |
"""

lines = markdown_table.strip().split('\n')
header = [item.strip() for item in lines[0].split('|')][1:-1]
print(header)
data_rows = [[item.strip() for item in row.split('|')][1:-1] for row in lines[2:]]

data = [dict(zip(header, row)) for row in data_rows]
print(data)

yaml_output = yaml.dump(data, default_flow_style=False)

with open('res.yml', 'w') as f:
    f.write(yaml_output)
print(yaml_output)
