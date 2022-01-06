from conversion.currency import Currency

currency_type = str(input("input currency type eg: USD, RUP"))
amount= str(input("input amount"))
product_amount= str(input("input product amount"))
currencyobj = Currency(currency_type)
currencyobj.get_money_after_purchase( amount, product_amount)
# c1.get_money_after_purchase( "$200", "$49.21")
