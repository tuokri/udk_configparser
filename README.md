# udk_configparser

Like CPython standard configparser but adjusted for UDK config files.

## Installation

```shell
pip install udk_configparser
```

## Example usage

### Setting a single value

```python
from udk_configparser import UDKConfigParser

cg = UDKConfigParser()

cg.read("Engine.ini")
cg["Section"]["Key"] = "NewValue"
```

### Setting a multi-value field and writing the file

```python
# Multi-value example.
pkg_name = "MyPackage"
edit_packages = cg["UnrealEd.EditorEngine"].getlist("+EditPackages")
if pkg_name not in edit_packages:
    edit_packages.append(pkg_name)
    # Currently, setting multi-value data requires manually 
    # joining the data to ensure it is written correctly.
    cg["UnrealEd.EditorEngine"]["+EditPackages"] = "\n".join(edit_packages)

with open("Engine.ini", "w") as config_file:
    cg.write(config_file, space_around_delimiters=False)

# Engine.ini before writing:
#  [UnrealEd.EditorEngine]
#  +EditPackages=UTGame
#  +EditPackages=UTGameContent

# After:
#  [UnrealEd.EditorEngine]
#  +EditPackages=UTGame
#  +EditPackages=UTGameContent
#  +EditPackages=MyPackage
```

## Known issues

- Comments get removed during writes.
