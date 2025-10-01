import math

# Total bill and number of friends
total_bill = 84.87
friends = 3

# Calculate each friend's share before rounding
amount_per_friend = total_bill / friends

# Round up to the nearest pound
rounded_amount = math.ceil(amount_per_friend)

# Calculate the tip each friend adds
extra_tip = rounded_amount - amount_per_friend

# Calculate total paid and total tip
total_paid = rounded_amount * friends
total_tip = total_paid - total_bill

# Display results
print(f"Each friend owes before rounding: £{amount_per_friend:.2f}")
print(f"Extra each friend adds as tip: £{extra_tip:.2f}")
print(f"Each friend pays: £{rounded_amount}")
print(f"Total paid: £{total_paid:.2f}")
print(f"Total tip paid: £{total_tip:.2f}")
