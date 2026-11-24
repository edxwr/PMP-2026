## Exercitiul 3

PyMC: 4 lanturi, 1000 tune, 2000 draws, target_accept=0.9.

a) si b)
HDI 95% pentru r (tau): [9.20, 22.76].
HDI 95% pentru k: [0.05, 1.89].
Parametrul r arata ziua de mijloc a schimbarii (in jurul zilelor 15-16), iar k arata cat de brusca este schimbarea (valorile mici arata o trecere lenta).

c) Probabilitatea ca rata finala sa fie mai mare decat cea initiala este 1.0 (100%). Rata estimata creste treptat de la aproximativ 3 la 9-10 solicitari pe zi.

d) 100% dintre datele observate cad in intervalul HDI 95% predictiv, iar eroarea medie absoluta este 0.76. Modelul reproduce foarte bine tranzitia graduala din date.