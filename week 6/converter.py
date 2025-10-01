print("=== Cups to Grams Converter ===")
# Conversion rates (cups per gram)
conversions = {
'flour': 120,
'sugar': 200,
'butter': 227,
'milk': 240,
'cocoa': 85,
}
print(f"\n 3 cup(s) of flour = {round(3 * conversions['flour'], 2)}g")
print(f"\n 2.5 cup(s) of sugar = {round(2.5 * conversions['sugar'], 2)}g")
print(f"\n 2 cup(s) of butter = {round(2 * conversions['butter'], 2)}g")
print(f"\n 1 cup(s) of milk = {round(1 * conversions['milk'], 2)}g")
print(f"\n 0.5 cup(s) of cocoa = {round(0.5 * conversions['cocoa'], 2)}g")