# Data Package Library

[![Build](https://img.shields.io/github/actions/workflow/status/frictionlessdata/dplib-py/general.yaml?branch=main)](https://github.com/frictionlessdata/dplib-py/actions)
[![Coverage](https://img.shields.io/codecov/c/github/frictionlessdata/dplib-py/main)](https://codecov.io/gh/frictionlessdata/dplib-py)
[![Codebase](https://img.shields.io/badge/codebase-github-brightgreen)](https://github.com/frictionlessdata/dplib-py)
[![Release](https://img.shields.io/pypi/v/dplib-py.svg)](https://pypi.python.org/pypi/dplib-py)

Python implementation of the Data Package standard and various tools for working with data

!!! note

    It's highly recommended to get acquainted with [Data Package Standard](https://datapackage.org) before reading this documentation

## Purpose

The Data Package Library is a lightweight Data Package Standard implementation in Python providing Pydantic data models and various metadata converters. At the moment, the main purpose of this library is to be used as an underlying component of Data Package based integrations.

!!! tip

    If you are not an integrator consider using [frictionless-py](https://framework.frictionlessdata.io/), full-featured end-user framework, instead of this library

## Features

- Open Source (MIT)
- Few dependencies
- Strictly typed
- High test coverage
- Fully pluggable architecture
- Works perfectly with `pyright` and `mypy`
- Experimental command-line interface

## Models

The library supports all the Data Package Standard metadata classes.

## Converters

Here is a list of currently supported metadata converters:

- CKAN
- DataCite
- DCAT
- GitHub
- Pandas
- Polars
- SQL
- Zenodo
