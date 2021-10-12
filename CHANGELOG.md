# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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