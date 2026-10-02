import numpy as np
import matplotlib.pyplot as plt

# constante
mu = 4.5
def f(x): 
    return mu * x * (1 - x)

# Dados
x = np.linspace(0, 1, 500)
y = f(x)

# Criando a figura com 2 subplots lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
plt.tight_layout(pad=4.0)

#  Intervalo A0 (escapam na 1ª iteração)

ax1.plot(x, y, 'b-', label=r'$F_\mu(x)$ ($\mu=4.5$)')
ax1.axhline(y=1, color='r', linestyle='--', label='y = 1')

# achando pontos para A0 onde f(x) > 1 (mu*x^2 - mu*x + 1 = 0)
d0 = np.sqrt(mu**2 - 4*mu*1)
x0_min = (mu - d0) / (2*mu)
x0_max = (mu + d0) / (2*mu)

# sombreamento laranja de A0
ax1.axvspan(x0_min, x0_max, color='orange', alpha=0.4, label='A0: Escapam 1ª Iteração')

# Configurações de ax1
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1.3)
ax1.legend(loc='upper right', framealpha=0.9, fontsize=9)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.set_xlabel('x')
ax1.set_ylabel('F(x)')

# Intervalos A1 (escapam na 2ª iteração)

ax2.plot(x, y, 'b-', label=r'$F_\mu(x)$')

# Área central cinza 
ax2.axvspan(x0_min, x0_max, color='grey', alpha=0.3, label='A0 (já escaparam)')

# achando as pré-imagens de A0 para encontrar A1
y1_min = x0_min
y1_max = x0_max

def acha_x(val_y):
    d = np.sqrt(mu**2 - 4*mu*val_y)
    return (mu - d) / (2*mu), (mu + d) / (2*mu)

x1_min_I0, x1_max_I1 = acha_x(y1_min) 
x1_max_I0, x1_min_I1 = acha_x(y1_max) 

# sombreamento roxo de A1 
ax2.axvspan(x1_min_I0, x1_max_I0, color='purple', alpha=0.5, label='A1: Escapam 2ª Iteração')
ax2.axvspan(x1_min_I1, x1_max_I1, color='purple', alpha=0.5)

# linhas verdes horizontais (limitam a altura de onde as pré-imagens são calculadas)
ax2.axhline(y=y1_min, color='g', linestyle=':')
ax2.axhline(y=y1_max, color='g', linestyle=':', label='Limites de A0 no eixo-y')

# Configurações de ax2
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1.3)
ax2.legend(loc='upper right', framealpha=0.9, fontsize=9)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.set_xlabel('x')
ax2.set_ylabel('F(x)')

plt.show()