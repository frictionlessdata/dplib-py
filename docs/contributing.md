# Development

Contributin code the `dplib-py` is simple as it is a pure Python library. Please read the following instructions:

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
.python/dplib-py/bin/python
```

## Documentation

Documentation is written with Mkdocs (defined in `mkdocs.yaml`). The source articles are in the `docs` directory. To start a live-reload server:

```bash
hatch run docs
```

Building the docs:

```bash
hatch run docs-build
```

## Testing

To run all the checks on the codebase:

```bash
hatch run test
```

## Releasing

> You need to have a `main` branch push permissions

Update the version and initiate the release script:

```bash
# Ensure you're on the up-to-date `main` branch
hatch version <major|minor|micro>
hatch run release
```
