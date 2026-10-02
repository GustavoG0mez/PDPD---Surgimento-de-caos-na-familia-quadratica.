import numpy as np
import matplotlib.pyplot as plt

# Dados iniciais
n_pontos = 10000
mu = np.linspace(0, 4, n_pontos)
total_iteracoes = 1000
iteracoes_finais = 100

# Condição inicial de x
x = 1e-5 * np.ones(n_pontos)

# Configuração da figura
plt.figure(figsize=(10, 6))

# Aplicação iterativa da função
for i in range(total_iteracoes):
    x = mu * x * (1 - x)
    
    # Plota apenas os últimos resultados
    if i >= (total_iteracoes - iteracoes_finais):
        plt.plot(mu, x, ',k', alpha=0.25)

# Configurações do gráfico
plt.xlim(0, 4)
plt.ylim(-0.05, 1.05)
plt.title(r'O diagrama de órbita de $F_\mu$ com $0 \leq \mu \leq 4$.')
plt.xlabel(r'$\mu$')
plt.ylabel('x')
plt.tight_layout()
plt.show()