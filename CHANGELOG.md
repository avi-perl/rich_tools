# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.1] - 2024-09-09

### Changed

- Library dependencies updated to latest versions of everything.
- Migrated from use of Black to Ruff for linting and formatting.
- My thanks to @johnlettman for his contributions and pushing me to upgrade.

## [0.5.0] - 2021-10-13

### Added

- Added a new function `rich_tools.strip_markup_tags()` that removes rich markup tags from a string. 
  It's a simple helper function to call the rich library's method: `Text.from_markup("[i]str[/i]").plain`

### Changed

- `rich_tools.table_to_df()` now supports a `remove_markup` argument that when False will leave rich markup in the
  values added to the `df`.


## [0.4.0] - 2021-10-13

### Added

- Added a new function `table_to_dicts()` that converts a `Table` instance's records into dictionaries and 
yields them back one at a time.


## [0.3.0] - 2021-10-12

### Changed

- Made the passing of a `Table` instance to `df_to_table` optional.


## [0.2.0] - 2021-10-11

### Changed

- Support (and encourage) importing functions directly from `rich_tools`.
  - Previously we would use `from rich_tools.table import df_to_table`
  - Now we support `from rich_tools import df_to_table`
  - The old import is still available if the extra namespace is your preference. 


## [0.1.2] - 2021-10-10

### Changed

- Changed the import of `pandas` in `rich_tools/table.py`.


## [0.1.0] - 2021-10-10

### Added

- Added base code, tests, and examples for the first release.