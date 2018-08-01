import network_map
import pandas as pd
from random import shuffle
from fuzzywuzzy import fuzz
import itertools
import author_space

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

author_groups = author_space.group_author_lists(authors)

edges = [('Chand, Pramesh, 2006', 'Thatcher, Marcus J., 2007'),
         ('Vytelingum, Perukrishnen, 2009', 'Chand, Pramesh, 2006'),
         ('Thatcher, Marcus J., 2007', 'GROZEV, George, 2005'),
         ('Wagner, Liam, 2010', '(Graham et al., 2008)'),
         ('Wagner, Liam, 2010', 'Exemplar, Energy, 2000'),
         ('Hindsberger, Magnus, 2011', 'Exemplar, Energy, 2000')]

network_map.create_cit_map(nodes, edges, years, authors_and_nodes, 1)


