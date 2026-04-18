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

# generation d'un modèle MA2 hierarchique en étapes simples


def sample_mu(alpha, rng):
    """
    Niveau 1 : génère un coefficient MA(2) mu depuis la loi Dirichlet(alpha)
    """
    beta = rng.dirichlet(alpha)
    b1, b2 = beta[0], beta[1]
    mu = np.array([b1 - b2, 2*(b1 + b2) - 1])
    return mu


def sample_sigma2(zeta, rng):
    """
    Niveau 2 : génère une variance sigma depuis la loi Inverse-Gamma(zeta)
    """
    sigma2 = invgamma.rvs(zeta[0], scale=zeta[1], random_state=rng)
    return sigma2


def simulate_ma2(mu, sigma2, T, rng):
    """
    Niveau 3 : simule une série MA(2) de longueur T avec coefficients mu et variance sigma2
    Les hyperparamètres sont calculés par les fonction précédentes
    """
    sig = np.sqrt(sigma2)
    y = rng.normal(0, sig, T + 2)
    x = np.array([y[t+2] + mu[0]*y[t+1] + mu[1]*y[t] for t in range(T)])
    return x


def generate_data(n, T, alpha, zeta, rng=None):
    """
    Génère n séries MA(2) hiérarchiques de longueur T
    """
    if rng is None:
        rng = np.random.default_rng(42)

    x_star, mu_list, sigma2_list = [], [], []

    # pour n séries simulées de taille T
    for j in range(n):
        mu = sample_mu(alpha, rng)         # niveau 1
        sigma2 = sample_sigma2(zeta, rng)      # niveau 2
        x = simulate_ma2(mu, sigma2, T, rng)  # niveau 3

        x_star.append(x)
        mu_list.append(mu)
        sigma2_list.append(sigma2)

    # retourner le résultat final
    return x_star, mu_list, sigma2_list
