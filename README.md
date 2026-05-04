# Projet Gibbs et ABC 
## Ina Campan, Gildas Montcel et Alistair Renaud

Ce projet de groupe a été réalisé dans le cadre du cours Simulation and Monte Carlo Methods (N. Chopin). Il s’appuie sur l’appendice de l’article de recherche "Component-wise Approximate Bayesian Computation via Gibbs-like steps" (publié par Grégoire Clarté, Christian P. Robert, Robin J. Ryder et Julien Stoehr).

Le code se décompose en trois parties principales : le Gibbs-ABC algorithm, un ABC sampler plus standard, et un random walk Metropolis sampler. Les différents algorithmes implémentés sont comparés en termes de temps de calcul, d’erreur d’inférence et d’erreur de Monte Carlo.

Conclusions principales : Le Gibbs-ABC estime mieux que le ABC-Reject nos paramètres theta (meilleur inferrential error et MC error). Cependant, dû à la dimension du modèle, le Gibbs-ABC met 2 fois plus de temps de calcul. Concernant le Metropolis Random Walk, puisque la vraisemblance est connue l'estimation est la meilleure : c'est le gold standard. 
