#!/usr/bin/env python

"""Tests for `rich_tools.text`"""

from rich_tools import strip_markup_tags
from rich_tools.text import _strip_tags


def test_strip_markup_tags():
    marked_up_text = "[bold]Bold[/bold]"
    assert strip_markup_tags(marked_up_text) == "Bold"


def test__strip_tags_do_false():
    marked_up_text = "[bold]Bold[/bold]"
    assert _strip_tags(marked_up_text, do=False) == marked_up_text


def test__strip_tags_do_true():
    marked_up_text = "[bold]Bold[/bold]"
    assert _strip_tags(marked_up_text, do=True) == "Bold"
