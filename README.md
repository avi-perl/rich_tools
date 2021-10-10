# 🔧 Rich Tools
[![Tests](https://github.com/avi-perl/rich_tools/actions/workflows/python-app.yml/badge.svg)](https://github.com/avi-perl/rich_tools/actions/workflows/python-app.yml)

A python package with helpful tools when working with the [rich](https://github.com/willmcgugan/rich) python library.

The current features are:

- Convert a [Pandas](https://pandas.pydata.org/) DataFrame into a [rich](https://github.com/willmcgugan/rich) Table.

  By making this conversion, we can now pretty print a DataFrame in the terminal with rich. Bridging the gap between 
  pandas and rich also provides a path for loading external data into a rich Table using Pandas functions such as `.from_csv()`!
- Convert a [rich](https://github.com/willmcgugan/rich) Table into a [Pandas](https://pandas.pydata.org/) DataFrame.

  By bridging the gap between a rich Table and a DataFrame, we can now take additional actions on our data such as   
  saving the data to a csv using the Pandas function `.to_csv()`!

### Installation
```bash
$ pip install rich-tools
```

### Example
Additional examples can be found in the `examples` dir.
```python
from datetime import datetime

import pandas as pd
from rich import box
from rich.console import Console
from rich.table import Table

from rich_tools.table import df_to_table

console = Console()


if __name__ == "__main__":
    sample_data = {
        "Date": [
            datetime(year=2019, month=12, day=20),
            datetime(year=2018, month=5, day=25),
            datetime(year=2017, month=12, day=15),
        ],
        "Title": [
            "Star Wars: The Rise of Skywalker",
            "[red]Solo[/red]: A Star Wars Story",
            "Star Wars Ep. VIII: The Last Jedi",
        ],
        "Production Budget": ["$275,000,000", "$275,000,000", "$262,000,000"],
        "Box Office": ["$375,126,118", "$393,151,347", "$1,332,539,889"],
    }
    df = pd.DataFrame(sample_data)

    # Initiate a Table instance to be modified
    table = Table(show_header=True, header_style="bold magenta")

    # Modify the table instance to have the data from the DataFrame
    table = df_to_table(df, table)

    # Update the style of the table
    table.row_styles = ["none", "dim"]
    table.box = box.SIMPLE_HEAD

    console.print(table)

```