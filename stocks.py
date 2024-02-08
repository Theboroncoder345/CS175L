# Arnav Vasa
#CS175L
#stocks
commission_rate = float(input('Commission Rate Percentage on stock purchase: '))
commission_rate = float(input('Commission Rate Percentage on stock sale: '))

num_shares = int(input('Shares purchased: '))
num_shares = int(input('Shares sold: '))

purchase_price = int(input('Purchase price per share: '))
sell_price = float(input('Sell price per share: '))

amountPaidForStock = num_shares*purchase_price
purchaseCommission = commission_rate*amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = num_shares*sell_price
sellingCommission = commission_rate*stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print(f'Amount paid for stock: ${amountPaidForStock:.2f}')
print(f'Commission paid on the purchase: ${purchaseCommission:.2f}')
print(f'Amount the stock sold for: ${stockSoldFor:.2f}')
print(f'Commission paid on the sale: ${sellingCommission:.2f}')
print(f'Profit (or loss if negative): ${profitOrLoss:.2f}')
