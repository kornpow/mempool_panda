# mempool_panda
Query the mempool with Python and Pandas

# Get mempool information from BTCD and save to file
```
USERNAME=
PASSWORD=
HOST=localhost
btcctl -s $HOST -u $USERNAME -P $PASSWORD getrawmempool true > mempool.json
```

# Get Python shell with sorted dataframes
```
python3 mempool/mempool_panda.py
```

# Example
![example](https://raw.githubusercontent.com/sako0938/mempool_panda/master/panda-example.png)

# TODO
- [] Use websockets to query data from BTCD directly instead of as a file