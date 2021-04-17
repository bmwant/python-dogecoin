
### Installation

```bash
$ pyenv virtualenv 3.8.1 dogecoin-python
$ pyenv activate dogecoin-python
$ pip install --upgrade pip
$ pip install -e .
```

### Tests

You need [Dogecoin server](https://github.com/dogecoin/dogecoin) to be up and running and configured to use `testnet`.

```bash
$ pyenv activate dogecoin-python
$ python tests/test.py
```


### Running Dogecoin server

```bash
$ ./src/dogecoind -daemon -testnet
$ ./src/dogecoin-cli stop  # stop after end of testing
```
