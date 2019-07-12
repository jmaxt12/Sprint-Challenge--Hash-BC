#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    # source - starting airport
    # destination - next airport

'''
tickets = [
  Ticket{ source: "PIT", destination: "ORD" },
  Ticket{ source: "XNA", destination: "CID" },
  Ticket{ source: "SFO", destination: "BHM" },
  Ticket{ source: "FLG", destination: "XNA" },
  Ticket{ source: "NONE", destination: "LAX" },
  Ticket{ source: "LAX", destination: "SFO" },
  Ticket{ source: "CID", destination: "SLC" },
  Ticket{ source: "ORD", destination: "NONE" },
  Ticket{ source: "SLC", destination: "PIT" },
  Ticket{ source: "BHM", destination: "FLG" }
]

output should look like =>
["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
'''


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

# key => source
# value => destination

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    route[0] = hash_table_retrieve(hashtable, 'NONE')
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
        
    return route
