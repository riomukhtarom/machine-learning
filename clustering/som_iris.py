data_som = data.values
data_som

import SimpSOM as sps

som = sps.somNet(8,8, data_som, PBC=True)

som.train(0.05, 10)

som.diff_graph(show=True, printout=True)

som.cluster(data_som, type='qthresh', show=True)