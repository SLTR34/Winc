from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

def unique_koala_facts(num_requested: int) -> list:
  """
  Takes an integer as an argument, representing the number of unique koala facts you want to retrieve.   Returns a list containing the requested number of unique facts.
  Loop stops at 1000 iterations if the requested number has not yet been retrieved.
  """
  loops, max_loops = 0, 1000
  facts = []
  while len(facts) < num_requested:
      fact = random_koala_fact()
      if fact not in facts:
          facts.append(fact)
      if loops > max_loops:
          break
      loops += 1
  return facts


def num_joey_facts() -> int:
  """
  Counts how many unique facts contain 'joey' by getting random facts until 1 specific fact is seen 10 times.
  """
    first_fact = random_koala_fact()
    times_seen_first_fact = 0
    num_joey_facts = 0
    # Using a set instead of a list for unique_facts would be better if you are
    # familiar with it.
    unique_facts = []

    while times_seen_first_fact < 10:
        fact = random_koala_fact()
        if fact == first_fact:
            times_seen_first_fact += 1
        if fact not in unique_facts:
            unique_facts.append(fact)
            if "joey" in fact.lower():
                num_joey_facts += 1
    return num_joey_facts


def koala_weight() -> int:
  """
  Returns the weight of a koala in kg which is mentioned in the dataset.
  """
    fact = random_koala_fact()
    while "kg" not in fact.lower():
        fact = random_koala_fact()
    return int(fact.split("kg")[0].split(" ")[-1])
  
# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(unique_koala_facts(20))
    print(len(unique_koala_facts(50)))
    print(num_joey_facts())
    print(koala_weight())
