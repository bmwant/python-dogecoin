## Python Dogecoin

[![PyPI](https://img.shields.io/pypi/v/python-dogecoin)](https://pypi.org/project/python-dogecoin)
[![Downloads](https://pepy.tech/badge/python-dogecoin)](https://pepy.tech/project/python-dogecoin)
[![Documentation Status](https://readthedocs.org/projects/python-dogecoin/badge/?version=latest)](https://python-dogecoin.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Tests](https://github.com/bmwant/python-dogecoin/actions/workflows/tests.yml/badge.svg)


This is a fork of a [dogecoin-python](https://github.com/jcsaaddupuy/dogecoin-python) library focused on a Python 3 support only. Note that you are looking for `python-dogecoin` version [on PyPI](https://pypi.org/project/python-dogecoin/) instead of original `dogecoin-python`.

This package allows performing commands such as listing the current balance and sending coins to the Satoshi (original) client from Python. The communication with the client happens over JSON-RPC.

:book: Documentation for the library can be found [here](https://python-dogecoin.readthedocs.io/en/latest/).

:lemon: This project uses [podmena](https://github.com/bmwant/podmena) library to add fancy icons to commit messages.

### Installation

```bash
$ pip install python-dogecoin
```

### Usage

Connect to blockchain daemon locally and make a simple request

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

[pyenv](https://github.com/pyenv/pyenv) is used to easily create virtual environment for the development. Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) to quickly setup it locally.

```bash
$ pyenv virtualenv 3.8.1 python-dogecoin
$ pyenv activate python-dogecoin
$ pip install --upgrade pip
$ pip install -e .
```

Formatting your code after adding changes

```bash
$ pyenv activate python-dogecoin
$ pip install -e ".[dev]"
$ make format
```

### Testing

To launch basic set of unittests

```bash
$ pyenv activate python-dogecoin
$ pip install -e ".[test]"
$ pytest -sv tests/
$ flake8 .  # lint code to spot any other errors
```

To launch integration tests you need [Dogecoin server](https://github.com/dogecoin/dogecoin) to be up and running and configured to use `testnet`.

```bash
$ pytest -sv tests/ --run-integration
```

### Much donations

If you love [Dogecoin](https://dogecoin.com/) and want to support the project you can send coins to this wallet

`D7DA74qzZUyh9cctCxWovPTEovUSjGzL2S`

:dog2: :rocket: :full_moon:
