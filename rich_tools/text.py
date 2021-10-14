from rich.text import Text


def strip_markup_tags(value: str) -> str:
    """Remove rich markup tags from a string.

    Example: "[bold]Bold[/bold]" becomes "Bold"

    Args:
        value (string): A string containing rich markup

    Returns:
        str: A plain string no longer containing rich markup."""

    return Text.from_markup(value).plain


def _strip_tags(value: str, do: bool) -> str:
    """Internal helper function to run `strip_markup_tags` conditionally.

    The purpose of this function is concise code when conditionally calling `strip_markup_tags`.

    For example:
    {
        _strip_tags(x.header, remove_markup): [_strip_tags(y, remove_markup) for y in x.cells]
        for x in rich_table.columns
    }
    This would be much more verbose without this helper function.

    Args:
        value (string): A string containing rich markup
        do (bool): A bool specifying if `_strip_tags` should do anything at all

    Returns:
        str: A string either containing rich markup, or not, depending on the value of `do`."""

    if do:
        return strip_markup_tags(value)
    else:
        return value
