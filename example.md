# YAML

```yaml
dict:
  subdict:
    key1: val1
    key2: val2
  list:
  - val1
  - val2
  primitive:
    string

list:
- - val1
  - val2
- key1: val1
  key2: val2
- primitive
```

# Python
_Displayed as JSON_

```json
{
    "dict": {
        "subdict": {"key1": "val1", "key2": "val2"},
        "list": ["val1", "val2"],
        "primitive": "string"
    },
    "list": [
        ["val1", "val2"],
        {"key1": "val1", "key2": "val2"},
        "primitive"
    ]
}
```

# Expected Tree

```
├ dict
| ├ subdict
| | ├ key1
| | | └ val1
| | └ key2
| |   └ val2
| ├ list
| | ├ val1
| | └ val2
| └ primitive
|   └ string
└ list
  ├─┬ val1
  | └ val2
  ├─┬ key1
  | | └ val1
  | └ key2
  |   └ val2
  └ primitive
```
