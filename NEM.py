import network_map

defs = {'(Hesamzadeh et al., 2014)':
        'Hesamzadeh, M.R., Galland, O., and Biggar, D.R. (2014). Short-run economic dispatch with mathematical'
        ' modelling of the adjustment cost. International Journal of Electrical Power & Energy Systems 58, 9–18.',
        '(Vytelingum et al.)':
        'Vytelingum, P., Ramchurn, S.D., Voice, T.D., Rogers, A., and Jennings, N.R. Trading agents for the smart' 
        ' electricity grid. 8.',
        '(Chand and Grozev)':
        'Chand, P., and Grozev, G. Modelling Australia’s National Electricity Market Using. 6.',
        '(Thatcher, 2007)':
        'Thatcher, M.J. (2007). Modelling changes to electricity demand load duration curves as a consequence of '
        'predicted climate change for Australia. Energy 32, 1647–1659.',
        '(GROZEV et al.)':
        'GROZEV, G., BATTEN, D., ANDERSON, M., LEWIS, G., MO, J., and KATZFEY, J. NEMSIM: Agent-based Simulator for'
        'Australia’s National Electricity Market. 5.',
        '(Rose et al., 2005)':
        'Rose, I., Bones, D.R., and Pimentel, M. (2005). Monte Carlo simulation and its application in modelling '
        'electricity market behaviour. Australian Journal of Electrical and Electronics Engineering 2, 199–208.',
        '(Forrest and MacGill, 2013)':
        'Forrest, S., and MacGill, I. (2013). Assessing the impact of wind generation on wholesale prices and generator' 
        ' dispatch in the Australian National Electricity Market. Energy Policy 59, 120–132.',
        '(Göransson and Johnsson, 2009)':
        'Göransson, L., and Johnsson, F. (2009). Dispatch modeling of a regional power generation system – Integrating '
        'wind power. Renewable Energy 34, 1040–1049.',
        '(Riesz et al.)':
        'Riesz, J.J., Shiao, F.-S., Gilmore, J.B., Yeowart, D., Turley, A., and Rose, I.A. Frequency Control Ancillary '
        'Service Requirements with Wind Generation - Australian Projections. 6.',
        '(Maisano et al.)':
        'Maisano, J., Radchik, A., and Skryabin, I. A method of forecasting wholesale electricity market prices. 20.',
        '(Riesz et al.)':
        'Riesz, J.J., Gilmore, J.B., Buchanan, M., Vanderwaal, B., and Rose, I.A. Impacts of Electricity Markets on '
        'Solar Revenues – An Australian Case Study. 6.',
        '(Wagner et al., 2014)':
        'Wagner, L., Molyneaux, L., and Foster, J. (2014). The magnitude of the impact of a shift from coal to gas '
        'under a Carbon Price. Energy Policy 66, 280–291.',
        '(Memisevic et al.)':
        'Memisevic, R., Choudhury, S., Sanderson, P., and Wong, W. Integrated power scheme simulator for human-system '
        'integration studies. 6.',
        '(Hindsberger and Eastwood, 2011)':
        'Hindsberger, M., and Eastwood, M. (2011). Assessing the market benefits of large-scale interconnectors. 13.',
        '(Brown et al.)':
        'Brown, K., Bennett, J., Parkyn, R., and Ling, F. TRANSLATING CLIMATE PROJECTIONS INTO USABLE INFORMATION '
        'FOR BUSINESS – A CASE STUDY FROM TASMANIA. 10.',
        '(Wagner and Reedman, 2010)':
        'Wagner, L., and Reedman, L. (2010). Modeling the deployment of plug-in hybrid and electric vehicles and their '
        'effects on the Australian National Electricity Market. (IEEE), pp. 165–170.',
        '(Graham et al., 2008)':
        'Graham, P., Reedman, L., and Poldy, F. (2008). Fuel for Thought. The Future of Transport Fuels: Challenges '
        'and Opportunities (Canberra: Commonwealth of Australia).',
        '(Energy Exemplar)':
        'Energy Exemplar, Pty Ltd. P.O. Box 13, North Adelaide, SA 5006, Adelaide, Australia, ' 
        'http://www.energyexemplar.com'
        }

years = {'(Hesamzadeh et al., 2014)': 2014,
        '(Vytelingum et al.)': 2009,
        '(Chand and Grozev)': 2006,
        '(Thatcher, 2007)': 2007,
        '(GROZEV et al.)': 2005,
        '(Rose et al., 2005)': 2005,
        '(Forrest and MacGill, 2013)': 2013,
        '(Göransson and Johnsson, 2009)': 2009,
        '(Riesz et al.)': 2010,
        '(Maisano et al.)': 2014,
        '(Riesz et al.)': 2008,
        '(Wagner et al., 2014)': 2014,
        '(Memisevic et al.)': 2004,
        '(Hindsberger and Eastwood, 2011)': 2011,
        '(Brown et al.)': 2010,
        '(Wagner and Reedman, 2010)': 2010,
        '(Graham et al., 2008)': 2008,
        '(Energy Exemplar)': 2000}



nodes = list(defs.keys())

edges = [('(Chand and Grozev)', '(Thatcher, 2007)'),
         ('(Vytelingum et al.)', '(Chand and Grozev)'),
         ('(Thatcher, 2007)', '(GROZEV et al.)'),
         ('(Wagner and Reedman, 2010)', '(Graham et al., 2008)'),
         ('(Wagner and Reedman, 2010)', '(Energy Exemplar)'),
         ('(Hindsberger and Eastwood, 2011)', '(Energy Exemplar)')]

network_map.create_cit_map(nodes, edges, years)