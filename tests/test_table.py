#!/usr/bin/env python

"""Tests for `rich_tools` package."""

from datetime import datetime

import pytest

import pandas as pd
from rich.table import Table

from rich_tools import table_to_df, df_to_table, table_to_dicts


@pytest.fixture
def df():
    return pd.DataFrame.from_dict(
        {
            "field_1": [datetime.now(), print, "string", str, 1],
            "field_2": [datetime.now(), print, "string", str, 1],
        }
    )


@pytest.fixture
def table():
    table = Table()
    table.add_column("Date", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Production Budget", justify="right")
    table.add_column("Box Office", justify="right")
    table.add_row(
        "Dec 20, 2019",
        "Star Wars: The Rise of Skywalker",
        "$275,000,000",
        "$375,126,118",
    )
    table.add_row(
        "May 25, 2018",
        "[red]Solo[/red]: A Star Wars Story",
        "$275,000,000",
        "$393,151,347",
    )
    table.add_row(
        "Dec 15, 2017",
        "Star Wars Ep. VIII: The Last Jedi",
        "$262,000,000",
        "[bold]$1,332,539,889[/bold]",
    )
    return table


def test_df_to_table(df):
    new_table = df_to_table(df, Table())

    assert isinstance(new_table, Table)
    assert new_table.row_count == len(df.index)
    # Index was added to the table, so the number of columns will be +1
    assert len(new_table.columns) == df.shape[1] + 1


def test_df_to_table_default_table(df):
    new_table = df_to_table(df)

    assert isinstance(new_table, Table)
    assert new_table.row_count == len(df.index)
    # Index was added to the table, so the number of columns will be +1
    assert len(new_table.columns) == df.shape[1] + 1


def test_df_to_table_alt_table_used(df):
    table = Table(show_header=True, header_style="bold magenta")
    new_table = df_to_table(df, table)

    assert new_table.header_style == "bold magenta"
    assert df_to_table(df).header_style != "bold magenta"


def test_df_to_table_show_index_true(df):
    new_table = df_to_table(df, Table(), show_index=True)
    assert len(new_table.columns) == df.shape[1] + 1


def test_df_to_table_show_index_false(df):
    new_table = df_to_table(df, Table(), show_index=False)
    assert len(new_table.columns) == df.shape[1]


def test_df_to_table_index_name(df):
    new_table = df_to_table(df, Table(), index_name="test")
    assert len(new_table.columns) == df.shape[1] + 1
    assert new_table.columns[0].header == "test"

    new_table = df_to_table(df, Table(), index_name=1)
    assert new_table.columns[0].header == "1"


def test_table_to_df(table):
    df = table_to_df(table)

    assert isinstance(df, pd.DataFrame)
    assert len(df.index) == table.row_count
    assert df.shape[1] == len(table.columns)


def test_table_to_dicts(table):
    dicts = table_to_dicts(table)
    assert table.row_count == len(list(dicts))


def test_table_to_dicts_blank_header():
    table = Table()
    table.add_column("")
    table.add_column("Title")
    table.add_row(
        "0",
        "Title",
    )

    with pytest.raises(ValueError):
        table_to_dicts(table)


def test_table_to_dicts_dupe_header():
    table = Table()
    table.add_column("Title")
    table.add_column("Title")
    table.add_row(
        "Title",
        "Title",
    )

    with pytest.raises(ValueError):
        table_to_dicts(table)


def test_table_to_dicts_remove_markup_true():
    table = Table()
    table.add_column("[bold]Bold[/bold]")
    table.add_row(
        "[bold]Bold value[/bold]",
    )

    dicts = table_to_dicts(table, remove_markup=True)
    dicts = list(dicts)

    assert list(dicts[0].keys())[0] == "Bold"
    assert list(dicts[0].values())[0] == "Bold value"


def test_table_to_dicts_remove_markup_false():
    table = Table()
    table.add_column("[bold]Bold[/bold]")
    table.add_row(
        "[bold]Bold value[/bold]",
    )

    dicts = table_to_dicts(table, remove_markup=False)
    dicts = list(dicts)

    assert list(dicts[0].keys())[0] == "[bold]Bold[/bold]"
    assert list(dicts[0].values())[0] == "[bold]Bold value[/bold]"
