import numpy as np
import matplotlib.pyplot as plt

with open('../data/ss.csv') as f:
    text = f.readlines()
text = text[1:]
text = [s.strip() for s in text]
# text = text[:4]

events = []
for s in text:
    events.append(s.split(', '))

events = np.array(events, dtype=np.float)
diff = events[1:,0]-events[:-1,0]
events = events[diff>0.00005]

events = list(events)
new_events = []
for i, (t, v) in enumerate(events):
    # print(i)
    new_events.append((t,v))
    if i==len(events)-1:
        break
    new_events.append((events[i+1][0], v))

# print(new_events)
events = np.array(new_events, dtype=np.float)



plt.plot(events[:,0], events[:,1])

plt.show()