# Bibliothèques

from scipy.stats import invgamma
import numpy as np

# Déclaration de variables globales (récupérées dans la section 10 du papier)

T = 100
n = 5
alpha = [1., 2., 3.]
zeta = [1., 1.]
N_miu = 1000
N_alpha = 100
N_sigma = 100
N_zeta = 100

# generation d'un modèle MA2 hierarchique


def generate_data(n, T, alpha, zeta, rng=None):
    """
    Fonction de génération de données d'un modèle MA(2) hierarchique
    n : séries temporelles observées en parallèle
    T : la longeur d'une série
    alpha : hyperparamétre
    zeta : hyperparamétre
    """

    if rng is None:
        rng = np.random.default_rng(42)

    x_star, mu_list, sigma2_list = [], [], []

    # nous construissons n séries de longuer T
    for j in range(n):
        # etape 1 : génération de hyper paramètres / données selon une loi de Dirichlet
        beta = rng.dirichlet(alpha)
        b1, b2 = beta[0], beta[1]
        mu = np.array([b1 - b2, 2*(b1 + b2) - 1])

        # etape 2 : génération de hyper paramètres selon une loi inverse de Gamma
        # choix .rvs -> pour retourner la valeur d'une variable aléatoire
        sigma2 = invgamma.rvs(zeta[0], scale=zeta[1], random_state=rng)

        # étape 3 : simuler la marche aléatoire (2)
        sig = np.sqrt(sigma2)
        y = rng.normal(0, sig, T + 2)   # bruit blanc : pour T observation => T + 2 bruits
        x = np.array([y[t+2] + mu[0]*y[t+1] + mu[1]*y[t] for t in range(T)])

        x_star.append(x)
        mu_list.append(mu)
        sigma2_list.append(sigma2)

    return x_star, mu_list, sigma2_list
