#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #   weights - a list of integers
    #   length - the length of the list
    #   limit - the integer to solve for 

#   2 nested loops

    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    
    for i in range(length):
        weight = hash_table_retrieve(ht, limit-weights[i])
        if weight != None:
            return (i, weight) if i > weight else (weight, i)
            
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([1,2,3], 3, 4))
