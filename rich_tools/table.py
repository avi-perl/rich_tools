from typing import Optional, Iterator, Dict, Any

from rich.text import Text
from rich.table import Table

import pandas as pd


def df_to_table(
    pandas_dataframe: pd.DataFrame,
    rich_table: Table = Table(),
    show_index: bool = True,
    index_name: Optional[str] = None,
) -> Table:
    """Convert a pandas.DataFrame obj into a rich.Table obj.

    Args:
        pandas_dataframe (DataFrame): A Pandas DataFrame to be converted to a rich Table.
        rich_table (Table): A rich Table that should be populated by the DataFrame values.
        show_index (bool): Add a column with a row count to the table. Defaults to True.
        index_name (str, optional): The column name to give to the index column. Defaults to None, showing no value.

    Returns:
        Table: The rich Table instance passed, populated with the DataFrame values."""

    if show_index:
        index_name = str(index_name) if index_name else ""
        rich_table.add_column(index_name)

    for column in pandas_dataframe.columns:
        rich_table.add_column(str(column))

    for index, value_list in enumerate(pandas_dataframe.values.tolist()):
        row = [str(index)] if show_index else []
        row += [str(x) for x in value_list]
        rich_table.add_row(*row)

    return rich_table


def table_to_df(rich_table: Table) -> pd.DataFrame:
    """Convert a rich.Table obj into a pandas.DataFrame obj with any rich formatting removed from the values.

    Args:
        rich_table (Table): A rich Table that should be populated by the DataFrame values.

    Returns:
        DataFrame: A pandas DataFrame with the Table data as its values."""

    return pd.DataFrame(
        {
            x.header: [Text.from_markup(y).plain for y in x.cells]
            for x in rich_table.columns
        }
    )


def table_to_dicts(rich_table: Table, remove_markup: bool = True) -> Iterator[Dict[str, Any]]:
    """Convert a rich.Table obj into a list of dictionary's with keys set as column names.

    Args:
        rich_table (Table): A rich Table instance containing data to be converted into a list of dictionary's.
        remove_markup (bool): Removes rich markup from the keys and values in the table if True.

    Returns:
        Iterator: A list of the input Table's rows, each as a dictionary."""

    def strip_tags(value: str) -> str:
        if remove_markup:
            return Text.from_markup(value).plain
        else:
            return value

    column_keys = [strip_tags(c.header) for c in rich_table.columns]

    if "" in column_keys:
        raise ValueError("You cannot convert a Table instance that has blank header")

    if len(column_keys) != len(set(column_keys)):
        raise ValueError("You cannot convert a Table instance that has duplicate headers")

    column_values = [[strip_tags(v) for v in c._cells] for c in rich_table.columns]

    return (dict(zip(column_keys, row_values)) for row_values in zip(*column_values))