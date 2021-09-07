amount_stock = 2000
cost_stock = 40.00
total_byu = amount_stock * cost_stock
broker_buy = total_byu * 0.03
total_money = total_byu + broker_buy
cost_sell_stock = 42.75
total_sell = amount_stock * cost_sell_stock
broker_sell = total_sell * 0.03
total_money_sell = total_sell - broker_sell
all_comission_broker = broker_buy + broker_sell
end_money = total_sell - all_comission_broker
profit = end_money - total_byu
per_profit = format(profit / total_byu * 100, '.2f')
print('Сумма денег уплаченная за акции', total_byu)
print('Сумма комисии уплаченная брокеру', broker_buy)
print('Сумма денег уплаченная за акции вместе с комиссией брокера', total_money)
print('Сумма денег выручення за акции', total_sell)
print('Сумма комиссии выплаченная брокеру за продажу акций', broker_sell)
print('Прибыль после всех манипуляций с акциями составила', profit)
print('Прибыль в процентах после всех манипуляций с акциями составила', per_profit)



