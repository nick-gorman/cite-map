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

authors = list(paper_data['Author'] + ';' + paper_data['Key'])

authors_and_nodes = dict(zip(paper_data['Author and Year'], authors))

author_groups = author_space.group_author_lists(authors)

best_order = author_space.order_all_spaces(author_groups)

best_order.sort(key=len)


edges = [('Chand, Pramesh, 2006', 'Thatcher, Marcus J., 2007'),
         ('Vytelingum, Perukrishnen, 2009', 'Chand, Pramesh, 2006'),
         ('Thatcher, Marcus J., 2007', 'GROZEV, George, 2005'),
         ('Wagner, Liam, 2010', 'Graham, P., 2008'),
         ('Wagner, Liam, 2010', 'Exemplar, Energy, 2000'),
         ('Wagner, Liam, 2010', 'Wagner, Liam, 2014'),
         ('Hindsberger, Magnus, 2011', 'Exemplar, Energy, 2000'),
         ('Wagner, Liam, 2014', 'Exemplar, Energy, 2000'),
         ('GROZEV, George, 2008', 'Thatcher, Marcus J., 2007'),
         ('GROZEV, George, 2008', 'GROZEV, George, 2005'),
         ('Reedman, Luke J, 2012', 'Elliston, Ben, 2012'),
         ('Samocha, Shira, 2017', 'Reedman, Luke J, 2012'),
         ('Samocha, Shira, 2017', 'Riesz, Jennifer J, 2016'),
         ('Samocha, Shira, 2017', 'Elliston, Ben, 2013'),
         ('Elliston, Ben, 2013', 'Elliston, Ben, 2012'),
         ('Elliston, Ben, 2013', 'MacGill, Iain, 2010')]

network_map.create_cit_map(nodes, edges, years, authors_and_nodes, best_order)


