# Coinbase Profit Estimating Calculator

This calculator is a fun CLI tool that I built to estimate profit/loss when exchanging bitcoin on Coinbase.  All calculations are determined using US-based fees referenced on 01/14/2021.

## Installation

Create and activate *venv* file.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage

Example:
```bash
python -m app.py -i 1000 -b 38000 -s 40000 -f 0.0149

# Returns:
+----------------------+------------+
| Net Profit:          | 22.28      |
+----------------------+------------+
| Investment:          | 1000.00    |
| Purchase Price:      | 38000.00   |
| Shares Purchased:    | 0.02592368 |
| Sell Price:          | 40000.00   |
| Purchase Fees:       | 14.90      |
| Sell Fees:           | 15.45      |
| Total Fees at 1.49%: | 30.35      |
+----------------------+------------+
```
The returned table should be green in color if the Net Profit is positive, and red in color if the Net Profit is negative.

Investment value *-i* is set to **1000** as default, and the fee *-f* is set to **0.0149** as default, so both could be omitted to use a command such as the following for the same result as above:
```bash
python -m app.py -b 38000 -s 40000

# Returns:
+----------------------+------------+
| Net Profit:          | 22.28      |
+----------------------+------------+
| Investment:          | 1000.00    |
| Purchase Price:      | 38000.00   |
| Shares Purchased:    | 0.02592368 |
| Sell Price:          | 40000.00   |
| Purchase Fees:       | 14.90      |
| Sell Fees:           | 15.45      |
| Total Fees at 1.49%: | 30.35      |
+----------------------+------------+
```

## Fee Calculations
The fees are determined using US-based fees referenced on 01/14/2021.

Coinbase states that they charge a flat fee or a variable percentage fee, and they will charge whichever is the highest.
The flat fees schedule is shown below:

>If the total transaction amount is less than or equal to $10, the fee is $0.99.  
If the total transaction amount is more than $10 but less than or equal to $25, the fee is $1.49.  
If the total transaction amount is more than $25 but less than or equal to $50, the fee is $1.99.  
If the total transaction amount is more than $50 but less than or equal to $200, the fee is $2.99

For example, for a purchase in the US of $100 of bitcoin using a US bank account or USD Coinbase Wallet, the flat fee would be calculated as $2.99. The variable percentage fee would be 1.49% of the total transaction, or $1.49. Because the flat fee is greater than the 1.49%, the calculation would use the fee of $2.99

If you wanted to purchase bitcoin with a debit card, the user would need to input *-i 0.0399*. 
 3.99% of the above example would be higher than the flat fee, so 3.99% would be used in the calculation.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Disclaimer
This tool is designed as a proof of concept project and to serve as practice creating CLI tools.  While calculations could create accurate predictions, this project is not updated on a regular basis and the creator(s) should not be held responsible for any incorrect calculations or predictions.  The creator(s) do not claim to give any financial or legal advice in relation to this product.