## Python Dogecoin

[![PyPI](https://img.shields.io/pypi/v/python-dogecoin)](https://pypi.org/project/python-dogecoin)
[![Downloads](https://pepy.tech/badge/python-dogecoin)](https://pepy.tech/project/python-dogecoin)
[![Documentation Status](https://readthedocs.org/projects/python-dogecoin/badge/?version=latest)](https://python-dogecoin.readthedocs.io/en/latest/?badge=latest)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![EditorConfig](https://img.shields.io/badge/-EditorConfig-grey?logo=editorconfig)](https://editorconfig.org/)
![Tests](https://github.com/bmwant/python-dogecoin/actions/workflows/tests.yml/badge.svg)


[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://vshymanskyy.github.io/StandWithUkraine/)


This is a fork of a [dogecoin-python](https://github.com/jcsaaddupuy/dogecoin-python) library focused on a Python 3 support only. Note that you are looking for `python-dogecoin` version [on PyPI](https://pypi.org/project/python-dogecoin/) instead of original `dogecoin-python`.

This package allows performing commands such as listing the current balance and sending coins to the Satoshi (original) client from Python. The communication with the client happens over JSON-RPC.

📖 Documentation for the library can be found [here](https://python-dogecoin.readthedocs.io/en/latest/).

🍋 This project uses [podmena](https://github.com/bmwant/podmena) library to add fancy icons to commit messages.

### Installation

```bash
pip install python-dogecoin
```

### Usage

Connect to the blockchain daemon locally and make a simple request

```python
"""
Checks whether address provided is a valid Dogecoin wallet
"""
import dogecoinrpc

client = dogecoinrpc.connect_to_local()
address = 'D6cobCBMtRoJNw8kxAWJ8GtRbbaxSAB37u'
result = conn.validateaddress(address)
print(result)
```

For other examples and code snippets [check documentation](https://python-dogecoin.readthedocs.io/en/latest/).

### Development

[Poetry](https://python-poetry.org/docs/#installation) is used to manage virtual environment and project's dependencies as well as building the final package.

```bash
poetry install --all-extras
```

Formatting your code after adding changes

```bash
make format
```

### Testing

To launch basic set of unittests

```bash
make tests
# or the same underlying command
poetry run pytest -sv tests/
```

To launch integration tests you need [Dogecoin server](https://github.com/dogecoin/dogecoin) to be up and running and configured to use `testnet`.

```bash
poetry run pytest -sv tests/ --run-integration
```

### Much donations

If you love [Dogecoin](https://dogecoin.com/) and want to support the project you can send coins to this [MyDoge](https://www.mydoge.com/) wallet

`D7DA74qzZUyh9cctCxWovPTEovUSjGzL2S`

🐕 🚀 🌕
