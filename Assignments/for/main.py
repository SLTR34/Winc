from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(countries: list) -> list:
  """
  Takes a list of countries and returns a list with the countries that have the shortest names."""
  shortest = min(countries, key=len)
  shortest_names = []
  for country in countries:
      if len(country) == len(shortest):
          shortest_names.append(country)
  return(shortest_names)


def most_vowels(countries: list):
  """
  Takes a list of countries and returns a list with the 3 countries that contain the most vowels.
  """
  vowels = "aeiou"

  # List of tuples of (country_name, vowel_count)
  # Can also be lists if unfamiliar with tuples
  leaderboard = [("", 0)]

  for country_name in countries:
      # Count vowels
      vowel_count = 0
      for char in country_name:
          if char.lower() in vowels:
              vowel_count += 1
      # Insert into leaderboard if deserving.
      for position in range(len(leaderboard)):
          if vowel_count >= leaderboard[position][1]:
              leaderboard.insert(position, (country_name, vowel_count))
              break
          if position > 2:
              break
  return [x[0] for x in leaderboard[:3]]


def alphabet_set(countries):
  """
  Takes a list of countries and returns a list of country names whose letters can be combined to form the         
  complete alphabet.
  """
  # Assembles alphabet
  countries = [country.lower() for country in countries]
  letters_needed = list("abcdefghijklmnopqrstuvwxyz")
  countries_used = []
  for country in countries:
      for char in country:
          if char in letters_needed:
              letters_needed.remove(char)
              if country not in countries_used:
                  countries_used.append(country)
      if len(letters_needed) == 0:
          return countries_used


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
  countries = get_countries()

  """ Write the calls to your functions here. """
  print(shortest_names(countries))
  print(most_vowels(countries))
  print(alphabet_set(countries))
  print(len(alphabet_set(countries)))


