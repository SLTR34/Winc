# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

#def main():
        # Weather = ['rainy','sunny','windy','neutral']
        # Time_of_day = ['day','night']
        # cow_milking_status = [True, False]
        # location_of_the_cows =['pasture','cowshed']
        # season = ['winter' ,'spring' ,'summer','fall']
        # slurry_tank = [True, False]
        # grass_stats = [True, False]

        # farm_action('rainy' ,'night' ,False ,'cowshed' ,'winter' ,True ,False)
        # farm_action('rainy' ,'night' ,False ,'cowshed' ,'winter' ,False ,True)
        # farm_action('windy' ,'night' ,True ,'cowshed' ,'winter' ,True ,True)
        # farm_action('sunny' ,'day' ,True ,'pasture' ,'spring' ,False ,True)
        # farm_action('sunny' ,'day' ,True ,'cowshed' ,'spring' ,False ,True)


#Factors
def farm_action(Weather, Time_of_day, cow_milking_status, location_of_the_cows, season, slurry_tank, grass_status):
#Actions
    #take cows to cowshed
    if (Weather == "rainy") and (Time_of_day == 'night') and (cow_milking_status == False) and (location_of_the_cows == 'pasture'):
     return ('take cows to cowshed')

    elif (Weather == 'sunny') and (Time_of_day == 'day') and (cow_milking_status == True) and (location_of_the_cows == 'pasture') and (season == 'spring') and (slurry_tank == False) and (grass_status == True):
     return  """take cows to cowshed\nmilk cows\ntake cows back to pasture"""

    #milk cows
    elif (cow_milking_status is True) and (location_of_the_cows=='cowshed'):
     return ('milk cows')

    #fertilize pasture
    elif (slurry_tank is True) and (location_of_the_cows=='cowshed') and (Weather=='rainy' or 'neutral'):
     return ('fertilize pasture')
    
    #mow grass
    elif (location_of_the_cows=='cowshed') and (grass_status is True) and (season=='spring') or (Weather=='sunny'):
     return ('mow grass')
    
    #wait
    else:
        return ('wait')
         


# print(farm_action('rainy' ,'night' ,False ,'pasture' ,'winter' ,True ,False))
# print(farm_action('rainy' ,'night' ,False ,'cowshed' ,'winter' ,False ,True))
# print(farm_action('windy' ,'night' ,True ,'cowshed' ,'winter' ,True ,True))
# print(farm_action('sunny' ,'day' ,True ,'pasture' ,'spring' ,False ,True))
# print(farm_action('sunny' ,'day' ,True ,'cowshed' ,'spring' ,False ,True))

