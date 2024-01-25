commission_rate = float(input('Commission Rate Percentage on stock purchase: '))
print('Commission Rate Percentage on stock sale:', commission_rate)

num_shares = int(input('Shares purchased: '))
print('Shares sold:', num_shares)

purchase_price = int(input('Purchase price per share: '))
sell_price = float(input('Sell price per share: '))

amountPaidForStock = num_shares*purchase_price
purchaseCommission = commission_rate*amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = num_shares*sell_price
sellingCommission = commission_rate*stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print('Amount paid for stock: $', f'{amountPaidForStock:.2f}')
print('Commission paid on the purchase: $', f'{purchaseCommission:.2f}')
print('Amount the stock sold for: $', f'{stockSoldFor:.2f}')
print('Commission paid on the sale: $', f'{sellingCommission:.2f}')
print('Profit (or loss if negative): $', f'{profitOrLoss:.2f}')
