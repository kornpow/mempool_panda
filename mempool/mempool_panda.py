import pandas
import code

pandas.set_option('display.max_colwidth', None)
pandas.set_option('display.max_rows', None)
pandas.options.display.float_format = '{:,.8f}'.format

def calcSatPerByte(row):
	sats = row.fee * 100000000
	return sats/row.vsize

# Output mempool in json format to file on command line
# btcctl getrawmempool true > mempool.json
# bitcoin-cli getrawmempool true > test2.json
# a = pandas.read_json('mempool.json')
a = pandas.read_json('../mempool_dumps/test2.json')
b = a.T

# Lists to filter columns
d = ['size', 'vsize', 'weight', 'fee', 'height', 'depends']
d1 = ['sats_byte', 'vsize', 'weight', 'fee', 'height']

# Calculate sat/byte for each transaction
b['sats_byte'] = b.apply(lambda x: calcSatPerByte(x), axis=1)

# Use these sorted dataframes to do analysis
# Sort mempool by weight and by feerate
weight_sort = b.sort_values(['weight'],ascending=False)[d1]
fee_sort = b.sort_values(['sats_byte'],ascending=False)[d1]

### END SETUP
### BEGIN Calculation

# Block Parameters
# weight unit per block
wu_block = 4000000

# total mempool size blocks
weight_sort.weight.sum()/wu_block

# Average fee for the heaviest 3000 txns
weight_sort.head(3000).sats_byte.sum()/3000
# Number of blocks for the heaviest 3000 txns
weight_sort.head(3000).weight.sum()/wu_block
# Number of blocks for the most expensive 10000 txns
fee_sort.head(10000).weight.sum()/wu_block
# Average fee for most expensive 30000 txns
fee_sort.head(30000).sats_byte.sum()/30000
# Number of blocks for most expensive 30000 txns
fee_sort.head(30000).weight.sum()/wu_block
# Number of blocks for cheapest 20000 txns
fee_sort.tail(20000).weight.sum()/4000000
# Average fee rate for cheapest 20000 txns
fee_sort.tail(20000).sats_byte.sum()/20000

# First Full Block
fbi = pandas.Index(fee_sort.weight.cumsum()).get_loc(4000000, 'bfill', tolerance=100000)
# Second Full Block
sbi = pandas.Index(fee_sort.weight.cumsum()).get_loc(8000000, 'bfill', tolerance=100000)

# Fees in first block
print(f"First block fees: {fee_sort[0:fbi].fee.sum()}")
# Fees in second block
print(f"First block fees: {fee_sort[fbi:sbi].fee.sum()}")

code.interact(local=locals())