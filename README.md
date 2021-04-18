## Python Dogecoin

[![PyPI](https://img.shields.io/pypi/v/python-dogecoin)](https://pypi.org/project/python-dogecoin)
[![Downloads](https://pepy.tech/badge/python-dogecoin)](https://pepy.tech/project/python-dogecoin)

This is a fork of a [dogecoin-python](https://github.com/jcsaaddupuy/dogecoin-python) library focused on a Python 3 support only. Note that you are looking for `python-dogecoin` version [on PyPI](https://pypi.org/project/python-dogecoin/) instead of original `dogecoin-python`.

This package allows performing commands such as listing the current balance and sending coins to the Satoshi (original) client from Python. The communication with the client happens over JSON-RPC.

### Installation

```bash
$ pip install python-dogecoin
```

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
$ pip install -e .[dev]
$ make format
```

### Tests

You need [Dogecoin server](https://github.com/dogecoin/dogecoin) to be up and running and configured to use `testnet`.

```bash
$ pyenv activate python-dogecoin
$ pip install -e .[test]
$ python tests/test.py
$ pytest -sv tests/
```


### Running Dogecoin server

```bash
$ ./src/dogecoind -daemon -testnet
$ ./src/dogecoin-cli stop  # stop after end of testing
```
