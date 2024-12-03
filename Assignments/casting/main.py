# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# 1
Leek_price = 2
print("Leek is",+ Leek_price,"euro per kilo.")

# 2
order = 'leek 4'
result = order.find(' ')
aantal = int(order[order.find(' ')+1:])

sum_total = (Leek_price * aantal)
print(sum_total)

# 3
broccoli_order = 1.6
broccoli_price = 2.34
sum_broccoli = ((broccoli_price) * (broccoli_order))

print(f'{broccoli_order}kg broccoli costs {round(sum_broccoli,  2)}e')