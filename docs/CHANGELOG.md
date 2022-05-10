# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### PR [#3](https://github.com/nilomr/xeno-canto-py/pull/3#issue-1230096023)

#### Added 

- Minimal docstrings
- Type hints. Requires python >= 3.7
- Optional `out_directory` kwarg in functions that write to disk.
- Progress bar for downloads.

#### Changed

- `str.format()`-like patterns to f-strings.
- Code now 80 cols wide

<br>

## [2.0.2] - Oct 26, 2021 
Added console messages.
- Added confirmation message when running delete. 
- Fixed recordings not being completely downloaded if the download was canceled and executed with the same query. 
- Fixed SSL certificate error.
- Fixed using double quote operator in arguments. 
## [2.0.1] - March 15, 2020 
- Installed command-line tool from pull request.
## [2.0] - October 21, 2019
- Added purge, delete, and execution via command line arguments.
## [1.1] - March 30, 2019 
- Added metadata generation.
## [1.0.2] - March 18, 2019 
- Update package name in README.
## [1.0.1] - March 13, 2019 
- Refactor to PEP8 standards, add comments.
## [1.0] - March 12, 2019 
- Initial release.