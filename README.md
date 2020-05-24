# mempool_panda
Query the mempool with Python and Pandas

# Get mempool information from BTCD and save to file
```
USERNAME=
PASSWORD=
HOST=localhost
btcctl -s $HOST -u $USERNAME -P $PASSWORD getrawmempool true > mempool.json
```

# Install Python Dependancies
```
pip3 install pandas
```

# Get Python shell with sorted dataframes
```
python3 mempool/mempool_panda.py
```

# Example
Get the 10 heaviest transactions and the 10 most expensive transactions, and get their total weights
![example](https://raw.githubusercontent.com/sako0938/mempool_panda/master/panda-example.png)

# TODO
- [] Use websockets to query data from BTCD directly instead of as a file