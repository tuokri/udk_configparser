# udk_configparser

Like CPython standard configparser but adjusted for UDK config files.

## Example usage

```python
from udk_configparser import UDKConfigParser

cg = UDKConfigParser()

cg.read("Engine.ini")
cg["Section"]["Key"] = "NewValue"

with open("Engine.ini", "w") as config_file:
    cg.write(config_file, space_around_delimiters=False)
```
