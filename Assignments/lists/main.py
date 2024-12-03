# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# 1 alphabetical_order

movies = ['jaws', 'how to steal a million', 'away']

def alphabetical_order(movies):
   return sorted(movies)
   
#2 won_golden_globe

def won_golden_globe(movies):
    List_winning_movies = ['Jaws', 'Star Wars: Episode IV - A New Hope', 'E.T. the Extra-Terrestrail', 'Memoirs of a Geisha']
    if movies.lower() in [x.lower() for x in List_winning_movies]:
        return True
    else:
        return False


#3 remove_toto_albums  
toto_album_list = ["Fahrenheit", "Falling In Between", "The Seventh One", "Toto XX", "Toto XIV", "Old Is New"]

def remove_toto_albums(toto_album_list):
    for x in toto_album_list:
        if ("Fahrenheit" in toto_album_list):
            toto_album_list.remove("Fahrenheit")
        if ("Old Is New" in toto_album_list):
            toto_album_list.remove("Old Is New")
    return toto_album_list

remove_toto_albums(toto_album_list)