import argparse
import sys

import pytest
import dogecoinrpc
from dogecoinrpc.exceptions import DogecoinException, InsufficientFunds

from decimal import Decimal


@pytest.mark.integration
def test_testnet():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Specify configuration file")
    parser.add_argument(
        "--nolocal", help="Don't use connect_to_local", action="store_true"
    )
    parser.add_argument(
        "--noremote", help="Don't use connect_to_remote", action="store_true"
    )
    args = parser.parse_args()

    if args.config:
        from dogecoinrpc.config import read_config_file

        cfg = read_config_file(args.config)
    else:
        from dogecoinrpc.config import read_default_config

        cfg = read_default_config(None)
    # port = int(cfg.get('rpcport', '22555'))
    port = 44556  # for testnet
    rpcuser = cfg.get("rpcuser", "")

    connections = []
    if not args.nolocal:
        local_conn = (
            dogecoinrpc.connect_to_local()
        )  # will use read_default_config
        connections.append(local_conn)
    if not args.noremote:
        remote_conn = dogecoinrpc.connect_to_remote(
            user=rpcuser,
            password=cfg["rpcpassword"],
            host="localhost",
            port=port,
            use_https=False,
        )
        connections.append(remote_conn)

    for conn in connections:
        assert conn.getinfo().testnet  # don't test on prodnet

        assert type(conn.getblockcount()) is int
        assert type(conn.getconnectioncount()) is int
        assert type(conn.getdifficulty()) is Decimal
        assert type(conn.getgenerate()) is bool
        conn.setgenerate(True)
        conn.setgenerate(True, 2)
        conn.setgenerate(False)
        assert type(conn.gethashespersec()) is int
        account = "testaccount"
        account2 = "testaccount2"
        dogecoinaddress = conn.getnewaddress(account)
        conn.setaccount(dogecoinaddress, account)
        address = conn.getaccountaddress(account)
        address2 = conn.getaccountaddress(account2)
        assert conn.getaccount(address) == account
        addresses = conn.getaddressesbyaccount(account)
        assert address in addresses
        # conn.sendtoaddress(dogecoinaddress, amount, comment=None, comment_to=None)
        conn.getreceivedbyaddress(dogecoinaddress)
        conn.getreceivedbyaccount(account)
        conn.listreceivedbyaddress()
        conn.listreceivedbyaccount()
        # conn.backupwallet(destination)
        x = conn.validateaddress(address)
        assert x.isvalid == True
        x = conn.validateaddress("invalid")
        assert x.isvalid == False
        messages = ("Hello, world!", "かたな")
        for message in messages:
            signature = conn.signmessage(dogecoinaddress, message)
            assert (
                conn.verifymessage(dogecoinaddress, signature, message) is True
            )

        for accid in conn.listaccounts(as_dict=True).iterkeys():
            tx = conn.listtransactions(accid)
            if len(tx) > 0:
                txid = tx[0].txid
                txdata = conn.gettransaction(txid)
                assert txdata.txid == tx[0].txid

        assert type(conn.listunspent()) is list  # needs better testing

        try:
            conn.sendtoaddress(dogecoinaddress, 10000000)
            assert 0  # Should raise InsufficientFunds
        except InsufficientFunds:
            pass

    info = conn.getinfo()
    print("Blocks: %i" % info.blocks)
    print("Connections: %i" % info.connections)
    print("Difficulty: %f" % info.difficulty)

    m_info = conn.getmininginfo()
    print(
        "Pooled Transactions: {pooledtx}\n"
        "Testnet: {testnet}\n"
        "Hash Rate: {hashes} H/s".format(
            pooledtx=m_info.pooledtx,
            testnet=m_info.testnet,
            hashes=m_info.hashespersec,
        )
    )
