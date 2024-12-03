# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# deel 1
# doelpunten makers
scorer_van_Basten= "Marco van Basten"
scorer_Gullit = "Ruud Gullit"

# minuten doelpunten
goal_0 = 32
goal_1 = 54

# scoren verloop
when_they_scored = [goal_0, goal_1]

scorers = f"{scorer_Gullit } {str (goal_0)}, { scorer_van_Basten } {str (goal_1)}"

report = f"{scorer_Gullit} scored in the {goal_0}nd minute\n{scorer_van_Basten} scored in the {goal_1}th minute"

print (report)

# deel 2
#1
player = "Frank Rijkaard"
#2
first_name = player[:player.find(' ')]
print(first_name)
#3
last_name_len = len(player [:player.find(' ')+3:])
print (last_name_len)
#4
name_short = player[0] + '.' +  player[5:14]
print(name_short)
#5
chant = len(first_name) * (first_name + '! ')
#6
chant = chant.rstrip( )
print(chant)

good_chant = (chant [-1] != " ")
print(good_chant)
