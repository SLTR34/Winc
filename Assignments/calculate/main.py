# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

#1 groenten.
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

#2 totale som van alle groenten.
sum_one_each = broccoli+leek+potato+brussel_sprout

#3 gemiddelde prijs.
avg_price = sum_one_each /4

#4 de boodschappenlijst.
num_broccolis = 5
num_potatoes = 7
num_leeks = 2
num_brussel_sprouts = 10

#5 kosten boodschappenlijst.
sum_total = num_broccolis * 2 + num_brussel_sprouts * 7 + num_leeks * 2 + num_potatoes * 3

#6 korting.
discount_percentage = 30

#7 Korting bereken.
discount_amount = discount_percentage/100 * sum_total
discounted_sum_total = sum_total - discount_amount

#8 total kosten.
print(discounted_sum_total)



