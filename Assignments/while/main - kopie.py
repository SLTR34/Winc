from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

def unique_koala_facts(num_requested):
    loops, max_loops = 0, 1000
    facts = []
    while len(facts) < num_requested:
        fact = random_koala_fact()
        if fact not in facts:
            facts.append(facts)
        if loops > max_loops:
            break
        loops += 1
    return facts


def num_joey_facts():
    first_fact_count = 10
    list = []
    joey_list = []
    while first_fact_count < 20:
        first_fact = random_koala_fact()
        if "joey" in first_fact:
            first_fact_count += 1
            list.append(first_fact)
    for element in list:
        if "joey" in element and element not in joey_list:
            joey_list.append(element)
    return joey_list


def koala_weight():
    fact = random_koala_fact()
    while "kg" not in fact.lower():
        fact = random_koala_fact()
    return int(fact.split("kg")[0].split(" ")[-1])
    

if __name__ == "__main__":
    #print(random_koala_fact())
    #print(len(unique_koala_facts(50)))
    print(num_joey_facts())
    #print(koala_weight())