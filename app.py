import argparse
from terminaltables import AsciiTable
from k3color import green, red


parser = argparse.ArgumentParser(
    description="Estimate profit on stock, ETF, or cryptocurrency exchanges.",
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
buyFee = investment * feePercent
sharesPurchased = (investment - buyFee) / buyPrice
sellPrice = float(args.sellPrice)
sellFee = sharesPurchased * sellPrice * feePercent

# calculating the gross Profit, total cost of fees, and net profit
grossProfit = (investment * sellPrice / buyPrice) - investment

totalFees = buyFee + sellFee

netProfit = grossProfit - totalFees

# logic to determine color of table: red(-) or green(+)
colorFormat = green if netProfit > 0 else red

# create the outline for the data included in the table
table_data = [
    ['Net Profit:', format(netProfit, ".2f")],
    ['Investment:', format(investment, ".2f")],
    ['Purchase Price:', format(buyPrice, ".2f")],
    ['Shares Purchased:', format(sharesPurchased, ".8f")],
    ['Sell Price:', format(sellPrice, ".2f")],
    ['Purchase Fees:', format(buyFee, ".2f")],
    ['Sell Fees:', format(sellFee, ".2f")],
    [f'Total Fees at {feePercent * 100}%:', format(totalFees, ".2f")]
]

table = AsciiTable(table_data)

print(colorFormat(table.table))