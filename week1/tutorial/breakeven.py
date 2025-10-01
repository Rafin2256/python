#define know values
cost_per_item = 20.00
sale_price_per_item = 40.0
fixed_costs = 50000.0
#calculate profit per item
profit_per_item = sale_price_per_item -cost_per_item
# Calculate the breakeven point (number of items to sell to cover fixed costs)
breakeven_point = fixed_costs / profit_per_item

#output the information with meaningful labels 

print("cost to produce each item :" , cost_per_item)
print("Sale price per item: ", sale_price_per_item)
print("Fixed cost: ", fixed_costs)
print("profit per item: " , profit_per_item)
print("Number os items needed to breakeven: " , breakeven_point)