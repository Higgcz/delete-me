# delete-me

[![Python](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python Project Template](https://img.shields.io/badge/template-2.2.0-orange)
](https://codebase.nnaisense.com/templates/cookiecutter-python/tree/2.2.0)

> Use other shields suitable for your project, visit https://img.shields.io for
> inspiration.

Template with a complete set of files for starting a new Python Project.

## Table of Contents

* [TL;DR](#tldr)
* [Installation](#installation)
* [Usage](#usage)
* [Development setup](#development-setup)
* [Authors](#authors)

## TL;DR

Summary of steps for quickly installing using/running the project.

## Installation

> **EDIT:** Everything users need to do in order to use/run the project.

```bash
pip install git+ssh://git@codebase.nnaisense.com/vojtech/delete-me.git
```

## Usage

> **EDIT:** How to use/run the project.

```python
import delete_me
```

## Development setup

1. Clone the repo

```bash
git clone git+ssh://git@codebase.nnaisense.com/vojtech/delete-me.git
cd delete-me
```

2. Create a local conda environment

```bash
conda env create -f env.yml

conda activate PROJECT_NAME
```

> This will install all dependencies defined in `setup.cfg` including your
> project in editable mode. That means you don't need to install the project
> every time you change something.

3. Install pre-commit hooks:

```bash
pre-commit install
```
> Check the `.pre-commit-config.yaml` file to see which pre-commit hooks you are
> using. If you update this file, you need to install the hooks again.

4. Run pre-commit hooks:

To check the code before committing, run all the pre-commit hooks manually:

```bash
pre-commit run --all-files
```
> Option `--all-files` would run the hooks on all files
> Run `pre-commit autoupdate` to update all your hooks to the latest version

5. Run tests
```bash
pytest -v
```
> Use option `-v` to get more verbose output

**Note:** See [PyTest website](https://docs.pytest.org/en/stable/) for more information on how to use PyTest and how to write
tests.

6. Update the dependencies

When you update dependencies of the project (in `setup.cfg`), you need to re-install the project:

```bash
pip install -e .[dev]
```

**Note:** If you have some problems running the above command, try quoting `pip install -e ".[dev]"`

## Authors

- [**Vojtech Micka**](mailto:vojtech@nnaisense.com)

> Add other project members, only maintainer should be **bold**
