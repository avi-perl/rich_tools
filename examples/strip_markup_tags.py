from rich.console import Console

from rich_tools import strip_markup_tags

console = Console()


if __name__ == "__main__":
    string_example = (
        "Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i]."
    )

    print(f"Raw string: {string_example}")
    console.print(f"What is looks like: {string_example}")
    print(f"After calling strip_markup_tags(): {strip_markup_tags(string_example)}")
