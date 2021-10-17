#!/usr/bin/env ipython


import pickle

class Teste:
    def predict(x: int):
        return x + 1

# Store data (serialize)
with open('model.pkl', 'wb') as handle:
    pickle.dump(Teste, handle, protocol=pickle.HIGHEST_PROTOCOL)
