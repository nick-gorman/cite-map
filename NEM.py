import network_map
import pandas as pd
from random import shuffle
from fuzzywuzzy import fuzz
import itertools

paper_data = pd.read_csv('nem_papers.csv', dtype=str)

paper_data['First Author'] = paper_data['Author'].apply(lambda x: x.split(';')[0])

paper_data['Author and Year'] = paper_data['First Author'] + ', ' + paper_data['Publication Year']

paper_data['Publication Year'] = pd.to_numeric(paper_data['Publication Year'])

nodes = list(paper_data['Author and Year'])

years = dict(zip(paper_data['Author and Year'], paper_data['Publication Year']))

authors_and_nodes = dict(zip(paper_data['Author and Year'], paper_data['Author']))

authors = list(paper_data['Author'])

def cal_goodness(order):
    adjacent_match_count = 0
    for element in order:
        index = order.index(element)
        if index == len(order) - 1:
            break
        next_element = order[index + 1]
        match_count = 0
        for name1, name2 in itertools.product(element.split(';'), next_element.split(';')):
            temp_distance = fuzz.ratio(name1, name2)
            if temp_distance > 80:
                match_count += 1
        adjacent_match_count += match_count

    return adjacent_match_count

potential_orders = []
order_goodness = []
temp_count =0
for i in range(1, 1000):
    shuffle(authors)
    try_order = authors.copy()
    potential_orders.append(try_order)
    order_goodness.append(cal_goodness(try_order))
    if temp_count == 10000:
        print(i)
        temp_count = 0
    temp_count += 1

max_distance = max(order_goodness)
best_order = potential_orders[order_goodness.index(max_distance)]

for names in best_order:
    print(names)

edges = [('Chand, Pramesh, 2006', 'Thatcher, Marcus J., 2007'),
         ('Vytelingum, Perukrishnen, 2009', 'Chand, Pramesh, 2006'),
         ('Thatcher, Marcus J., 2007', 'GROZEV, George, 2005'),
         ('Wagner, Liam, 2010', '(Graham et al., 2008)'),
         ('Wagner, Liam, 2010', 'Exemplar, Energy, 2000'),
         ('Hindsberger, Magnus, 2011', 'Exemplar, Energy, 2000')]

network_map.create_cit_map(nodes, edges, years, authors_and_nodes, best_order)


