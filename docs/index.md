# Welcome to python-dogecoin

**python-dogecoin** - Easy-to-use Dogecoin API client.

`python-dogecoin` is a Python library that allows easy access to the [Dogecoin](https://dogecoin.com/) peer-to-peer cryptocurrency client API.

The goal of this library is to make it easier for:

* Payment gateways to support dogecoin
* Merchant sites to integrate dogecoin payments directly
* Other services that require (micro-)payments to use dogecoin

### Installation

```bash
$ pip install python-dogecoin
```

### Usage

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

See [Usage](usage.md) for more examples.
