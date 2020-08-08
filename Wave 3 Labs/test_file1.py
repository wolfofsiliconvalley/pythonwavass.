state = 'CA'
purchase_amount = 15
if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount * (1 + tax_amount)
    result = f"Since you are from {state}, your total cost is ${total_cost}"
elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount * (1 + tax_amount)
    result = f"Since you are from {state}, your total cost is ${total_cost}"
elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount * (1 + tax_amount)
    result = f"Since you are from {state}, your total cost is ${total_cost}"

print(result)