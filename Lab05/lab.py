import numpy as np
from hmmlearn import hmm

stari = ["Dificil", "Mediu", "Usor"]
n_stari = len(stari)

observatii_posibile = ["FB", "B", "S", "NS"]
mapare_obs = {nota: idx for idx, nota in enumerate(observatii_posibile)}

start_prob = np.array([1/3, 1/3, 1/3])

trans_mat = np.array([
    [0.0,  0.5,  0.5],
    [0.5, 0.25, 0.25],
    [0.5, 0.25, 0.25]
])

emission_prob = np.array([
    [0.10, 0.20, 0.40, 0.30],
    [0.15, 0.25, 0.50, 0.10],
    [0.20, 0.30, 0.40, 0.10]
])

model = hmm.CategoricalHMM(n_components=n_stari)
model.startprob_ = start_prob
model.transmat_ = trans_mat
model.emissionprob_ = emission_prob

secventa_note = ["FB", "FB", "S", "B", "B", "S", "B", "B", "NS", "B", "B", "S"]

X = np.array([[mapare_obs[nota]] for nota in secventa_note])

log_prob, secventa_stari_idx = model.decode(X, algorithm="viterbi")
probabilitate = np.exp(log_prob)

secventa_dificultati = [stari[i] for i in secventa_stari_idx]

print("Secventa de note observata:")
print(secventa_note)
print("Cea mai probabila secventa de dificultati:")
print(secventa_dificultati)
print(f"Probabilitatea secventei: {probabilitate:.12f}")