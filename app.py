import argparse
from terminaltables import AsciiTable
from k3color import green, red


parser = argparse.ArgumentParser(
    description="Estimate profit cryptocurrency transactions using Coinbase fee method.",
    epilog="Sample script to run in terminal: 'python app.py -i 10000 -b 1134.66 -s 1200'")
parser.add_argument('-i', '--investment', type=float, metavar='', default=1000, help='Total initial investment (defaults to 1000)')
parser.add_argument('-b', '--buyPrice', type=float, required=True, metavar='', help='Purchase price')
parser.add_argument('-s', '--sellPrice', type=float, required=True, metavar='', help='Anticipated sale price')
parser.add_argument('-f', '--feePercent', type=float, metavar='', default=0.0149, help='Fee charge expressed in as decimal percent(defaults to 0.0149)')
args = parser.parse_args()

# define the values provided
investment = float(args.investment)
buyPrice = float(args.buyPrice)
feePercent = float(args.feePercent)
buyFee = 0

# calculates flat rate fee
if investment <= 10:
    buyFee = 0.99
elif investment > 10 and investment <= 25:
    buyFee = 1.49
elif investment > 25 and investment <= 50:
    buyFee = 1.99
elif investment > 50 and investment <= 200:
    buyFee = 2.99

# if flat rate fee is < variable % fee, variable % fee is appliedif (investment * feePercent) > buyFee:
if (investment * feePercent) > buyFee:
    buyFee = investment * feePercent
    

sharesPurchased = (investment - buyFee) / buyPrice
sellPrice = float(args.sellPrice)

sellFee = 0
grossSale = sharesPurchased * sellPrice

# calculates flat rate fee
if grossSale <= 10:
    sellFee = 0.99
elif grossSale > 10 and grossSale <= 25:
    sellFee = 1.49
elif grossSale > 25 and grossSale <= 50:
    sellFee = 1.99
elif grossSale > 50 and grossSale <= 200:
    sellFee = 2.99

# if flat rate fee is < variable % fee, variable % fee is appliedif (investment * feePercent) > buyFee:
    buyFee = investment * feePercent
if (grossSale * feePercent) > sellFee:
    sellFee = grossSale * feePercent

# calculating the gross Profit, total cost of fees, and net profit
grossProfit = (investment * sellPrice / buyPrice) - investment

totalFees = buyFee + sellFee

netProfit = grossProfit - totalFees

# logic to determine color of table: red(-) or green(+)
colorFormat = green if netProfit > 0 else red

# create the outline for the data included in the table
table_data = [
    ['Net Profit:', format(netProfit, ".2f")],
    ['Initial Investment:', format(investment, ".2f")],
    ['Purchase Price:', format(buyPrice, ".2f")],
    ['Purchase Fees:', format(buyFee, ".2f")],
    ['Shares Purchased:', format(sharesPurchased, ".8f")],
    ['Sell Price:', format(sellPrice, ".2f")],
    ['Sell Fees:', format(sellFee, ".2f")],
    [f'Total Fees at {feePercent * 100}%:', format(totalFees, ".2f")]
]

table = AsciiTable(table_data)

print(colorFormat(table.table))