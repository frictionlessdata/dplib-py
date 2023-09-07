# Development

Contributin code the `dpspecs-py` is simple as it is a pure Python library. Please read the following instructions:

## Prerequisites

To start working on the project:

- Python 3.8+

## Enviroment

!!! note

    For development orchestration we use [Hatch](https://github.com/pypa/hatch) for Python (defined in `pyproject.toml`)

```bash
pip3 install hatch
```

### Python

Before starting with the project we recommend configuring `hatch`. The following line will ensure that all the virtual environments will be stored in the `.python` directory in project root:

```bash
hatch config set 'dirs.env.virtual' '.python'
hatch shell # Enter the venv
```

Now you can setup you IDE to use a proper Python path:

```bash
.python/dpspecs/bin/python
```

## Installation

To start working on the project install the dependencies:

```bash
make install
```

## Documentation

Documentation is written with Mkdocs (defined in `mkdocs.yaml`). The source articles are in the `docs` directory. To start a live-reload server:

```bash
make write
```

Building the docs:

```bash
make docs
```

## Testing

To run all the checks on the codebase:

```bash
make test
```
