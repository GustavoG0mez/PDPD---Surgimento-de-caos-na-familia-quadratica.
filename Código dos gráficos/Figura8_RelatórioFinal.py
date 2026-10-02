import numpy as np
import matplotlib.pyplot as plt

#Dados Iniciais
n_pontos = 3000
mu = np.linspace(3.825, 3.86, n_pontos)
total_iteracoes = 2000
iteracoes_finais = 300

# Condição inicial de x
x = 1e-5 * np.ones(n_pontos)

# Configuração da figura
plt.figure(figsize=(10, 6))

# Cálculo iterativo da função
for i in range(total_iteracoes):
    x = mu * x * (1 - x)
    
    # Plota apenas os últimos valores
    if i >= (total_iteracoes - iteracoes_finais):
        plt.plot(mu, x, ',k', alpha=0.1)

# Configurações do gráfico
plt.xlim(3.825, 3.86)
plt.title(r"O diagrama de órbita de $F_\mu$ com $3.825 \leq \mu \leq 3.86$.")
plt.xlabel(r"$\mu$")
plt.ylabel("x")
plt.tight_layout()

# Exibição
plt.show()