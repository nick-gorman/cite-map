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
        'wind power. Renewable Energy 34, 1040–1049.'
        }

nodes = list(defs.keys())

edges = [('(Chand and Grozev)', '(Thatcher, 2007)'),
         ('(Vytelingum et al.)', '(Chand and Grozev)'),
         ('(Thatcher, 2007)', '(GROZEV et al.)'),
         ('(Rose et al., 2005)', )]

network_map.create_cit_map(nodes, edges)