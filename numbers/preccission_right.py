from decimal import Decimal
unit_price = Decimal('2.32')
number_sold = 3
money_received = Decimal('6.96')
if unit_price * number_sold == money_received:
    print('Accounts balanced')
else:
    raise ValueError('Accounts not balanced')
