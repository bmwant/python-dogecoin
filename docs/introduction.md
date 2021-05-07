### Introduction

``dogecoin-python`` attempts to create an even more friendly interface by wrapping the JSON-RPC API. The major advantages
compared to a raw ``jsonrpc`` based approach are:

- Better exception handling. Exceptions are converted to subclasses of :class:`~dogecoinrpc.exceptions.DogecoinException`.

- Automatic dogecoin configuration loading. In case the ``dogecoin -server`` or ``dogecoind`` program runs on the same
  machine as the client script, and as the same user, the configuration file can automatically be parsed. This
  makes it unneccesary to explicitly specify a *username* and *password*. Of course, this is still possible.

- The functions
  :func:`~dogecoinrpc.connection.DogecoinConnection.getinfo`, :func:`~dogecoinrpc.connection.DogecoinConnection.listreceivedbyaccount`,
  :func:`~dogecoinrpc.connection.DogecoinConnection.listreceivedbyaddress`,
  :func:`~dogecoinrpc.connection.DogecoinConnection.listtransactions` and more return actual Python objects, instead of simply
  dictionaries. This makes for cleaner code, as the fields can simply be addressed with ``x.foo`` instead of
  ``x['foo']``.
