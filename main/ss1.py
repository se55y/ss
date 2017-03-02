import numpy as np
import matplotlib.pyplot as plt

with open('../data/ss.csv') as f:
    text = f.readlines()
t_prev, v_prev = None	
for line in text[1:]:
	t, v = line.split(',')
	t, v = float(t), int(v)
	print(t,v)
	if t_prev is None:
		t_prev, v_prev = t, v
		continue
	diff = t-t_prev
	if diff<0.00005:
		t_prev, v_prev = t, v
		continue
		
	stop	
		
	t_prev = t

