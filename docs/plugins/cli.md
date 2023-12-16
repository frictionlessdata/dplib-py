# CLI

Command-line interface for the Data Package Library

!!! warning

    This plugin is experimental

## Installation

Extra dependency needs to be installed:

```bash
pip install dplib-py[cli]
```

## Usage

```bash
dp --help
```

```
 Usage: dp [OPTIONS] COMMAND [ARGS]...

 Python implementation of the Data Package standard and various tools for working with data

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --debug               -d        Show debug information                                                                            │
│ --install-completion            Install completion for the current shell.                                                         │
│ --show-completion               Show completion for the current shell, to copy it or customize the installation.                  │
│ --help                          Show this message and exit.                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ dialect                     Table Dialect related commands.                                                                       │
│ package                     Data Package related commands.                                                                        │
│ resource                    Data Resource related commands.                                                                       │
│ schema                      Table Schema related commands.                                                                        │
│ version                     Print the version of the program.                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```
