<h1 align="center" style="font-size:50px;">🔧 Rich Tools</h1>
<p align="center">
    <em>A python package with helpful functions for use alongside with the <a href="https://github.com/willmcgugan/rich">rich</a> python library.</em>
</p>
<p align="center">
<a href="https://pypi.org/project/rich-tools/" target="_blank">
    <img src="https://badge.fury.io/py/rich-tools.svg" alt="PyPI version">
</a>
<a href="https://badge.fury.io/py/rich_tools"code>
    <img src="https://img.shields.io/pypi/pyversions/rich_tools" alt="Supported Python Versions">
</a>
<a href="https://github.com/avi-perl/rich_tools/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/avi-perl/rich_tools/actions/workflows/test.yml/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/avi-perl/rich_tools" target="_blank">
  <img src="https://codecov.io/gh/avi-perl/rich_tools/branch/master/graph/badge.svg?token=7A5RYLZ37B"/>
</a>
</p>

---

#### The current features are:

- **Convert a [Pandas](https://pandas.pydata.org/) DataFrame into a [rich](https://github.com/willmcgugan/rich) Table ➜ `df_to_table()`**

  By making this conversion, we can now pretty print a DataFrame in the terminal with rich. Bridging the gap between 
  pandas and rich also provides a path for loading external data into a rich Table using Pandas functions such as `.from_csv()`!
- **Convert a [rich](https://github.com/willmcgugan/rich) Table into a [Pandas](https://pandas.pydata.org/) DataFrame ➜ `table_to_df()`**

  By bridging the gap between a rich Table and a DataFrame, we can now take additional actions on our data such as   
  saving the data to a csv using the Pandas function `.to_csv()`!
- **Convert a [rich](https://github.com/willmcgugan/rich) Table into a list of dictionaries. ➜ `table_to_dicts()`**

  Get your tables rows as a list of dictionaries with column names as key, and row contents as values.
- **Strip [rich](https://github.com/willmcgugan/rich) markup tags from a string. ➜ `strip_markup_tags()`**

  Helper function to remove tags from text formatted with rich. `"[bold]Bold[/bold]"` becomes `"Bold"`

### Installation
```bash
$ pip install rich-tools
```

### Example
Additional examples can be found in the [examples](examples) dir.
```python
# Print csv data to the terminal as a pretty printed rich formatted table

import pandas as pd
from rich import print
from rich_tools import df_to_table

if __name__ == '__main__':
    df = pd.read_csv("sample_input.csv")
    table = df_to_table(df)
    print(table)

```

### Credits
- Like the [rich](https://github.com/willmcgugan/rich) package itself, its creator [Will McGugan](https://twitter.com/willmcgugan)
is awesome! Check out [Textual](https://github.com/willmcgugan/textual) "a TUI (Text User Interface) framework for 
Python inspired by modern web development". Thank you for the advice you've given on this project! 🙏
- I am grateful for folks who give some of their time to this project in any form. Check out the list of 
[contributors](https://github.com/avi-perl/rich_tools/graphs/contributors) and learn more about contributing [here](CONTRIBUTING.md).