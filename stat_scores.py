import pdb
import pickle
import matplotlib.pyplot as plt

with open('f1_scores.pkl', 'rb') as f:
    scores = pickle.load(f)

freq_dict = {}

for k in scores:
    #if k[0] == '6' or k[0] == '5':
    if k[0] == '9':
        if scores[k] > 19.0 and scores[k] < 21.0:
            print('20')
            pdb.set_trace()
        if scores[k] > 59.0 and scores[k] < 61.0:
            print('60')
            pdb.set_trace()
        if scores[k] > 65.0 and scores[k] < 75.0:
            print('70')
            pdb.set_trace()
        if scores[k] > 79.0 and scores[k] < 81.0:
            print('80')
            pdb.set_trace()
        if scores[k] > 89.0 and scores[k] < 91.0:
            print('90')
            pdb.set_trace()
        #if scores[k] == 100.0 or scores[k] == 0.0:
        #    continue
        if scores[k] in freq_dict:
            freq_dict[scores[k]] += 1
        else:
            freq_dict[scores[k]] = 1
       
freqs = [freq_dict[k] for k in freq_dict]
s = [k for k in freq_dict]

pdb.set_trace()

plt.plot(s, freqs, '.')
plt.savefig('scores.png')
