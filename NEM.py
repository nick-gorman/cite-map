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

authors = list(paper_data['Author'])

lists_of_authors =[]
for author_list in authors:
    lists_of_authors.append(author_list.lower())


authors_and_nodes = dict(zip(paper_data['Author and Year'], lists_of_authors))

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
        if index < len(order) - 2:
            next_element = order[index + 2]
            for name1, name2 in itertools.product(element.split(';'), next_element.split(';')):
                temp_distance = fuzz.ratio(name1, name2)
                if temp_distance > 80:
                    match_count += 0.5
        adjacent_match_count += match_count

    return adjacent_match_count

def matches(list1, list2):
    match_count = 0
    for name1, name2 in itertools.product(list1.split(';'), list2.split(';')):
        temp_distance = fuzz.ratio(name1, name2)
        if temp_distance > 80:
            match_count += 1
    return match_count

comp_list = lists_of_authors.copy()
groups = []
current_group = 0
for element in comp_list:
    comp_list[comp_list.index(element)] = ''
    groups.append([element])
    sub_com_list = comp_list.copy()
    for comp_elment in sub_com_list:
        if matches(element, comp_elment) > 0:
            groups[current_group].append(comp_elment)
            comp_list.pop(comp_list.index(comp_elment))
    current_group += 1

potential_orders = []
order_goodness = []
temp_count =0
for i in range(1, 1000000):
    shuffle(lists_of_authors)
    try_order = lists_of_authors.copy()
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


