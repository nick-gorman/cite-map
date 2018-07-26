import network_map

defs = {'Elliston, B. 2014':
            'Comparing least cost scenarios for 100% renewable electricity with low emission fossil fuel scenarios in the Australian National Electricity Market',
        'Connolly, D. 2010':
            'A review of computer tools for analysing the integration of renewable energy into various energy systems',
        'Stringer, N. 2017':
            'Open Source Model for Operational and Commercial Assessment of Local Electricity Sharing Schemes in the Australian National Electricity Market',
        'Haghdadi, N. 2017':
            'Tariff Design and Assessment Tool User Guide'
        }

nodes = list(defs.keys())

edges = [('Elliston, B. 2014', 'Connolly, D. 2010')]

network_map.create_cit_map(nodes, edges)
