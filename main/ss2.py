import numpy as np
import matplotlib.pyplot as plt
import re

with open('../data/cw_ccw.csv') as f:
    text = f.readlines()
text = text[1:]
events = []
for s in text:
    events.append(s.split(', '))
events = np.array(events, dtype=np.float)

diff = events[1:,0]-events[:-1,0]
events = events[:-1][diff > 0.00005]
diff = events[1:,0]-events[:-1,0]
diff = (np.round(diff * 10000,0)).astype(np.int)

stream = ''
for i in range(events.shape[0]-1):
   stream += str(int(events[i,1])) * diff[i]

# ...0000-startbit-d5-d6-d7-d8-d9-d10-d11-d12-101111-d4-d3-d2-d1-d0-0000...
# ...0000-startbit-d5-d6-d7-d8-d9-d10-d11-d12-101010-d4-d3-d2-d1-d0-0000... (inverted d's)

m = re.findall('1([01]{8})101111([01]{5})0+1([01]{8})101010([01]{5})', stream)
f = open('../data/text.txt', 'w')
for v1, v2, v1_, v2_ in m:
    a = v1[::-1] + v2[::-1]                         # прямые данные d12~d5+d4~d0
    a_ = v1_[::-1] + v2_[::-1]                      # инверсные данные d12~d5+d4~d0
    b = v1[-2::-1] + v2[::-1]                       # d11~d0 data
    same = [a for a, a_ in zip(a, a_) if a == a_]   # побитно проверяю
    if not same:
        print(int(b, 2))                            # печать десятичного значения угла
        f.write(str(int(b, 2)) + '\n')
f.close()

		