import numpy as np
import matplotlib.pyplot as plt

#constante
mu = 4.5

def f(x): 
    return mu * x * (1 - x) # função

# gerando os dados
x = np.linspace(0, 1, 500)
y = f(x)

plt.figure(figsize=(8, 6))

# plotando
plt.plot(x, y, 'b-', linewidth=1.5, label=r'$F_\mu(x) = \mu x(1-x)$')
plt.plot(x, x, color='silver', linestyle='--', label='y = x')

#intervalo J no eixo y
ymin = 0.2
ymax = 0.6

# linha vermelha lateral
plt.plot([-0.01, -0.01], [ymin, ymax], 'r-', lw=3, label='Intervalo J')
plt.text(-0.04, 0.38, 'J', color='r', fontsize=10, style='italic')

# achando as raizes
# mu*x^2 - mu*x + y = 0
def acha_x(val_y):
    d = np.sqrt(mu**2 - 4*mu*val_y)
    return (mu - d) / (2*mu), (mu + d) / (2*mu)

x1_min, x2_max = acha_x(ymin)
x1_max, x2_min = acha_x(ymax)

# linhas pontilhadas vermelhas (horizontais e verticais)
plt.plot([0, x1_min], [ymin, ymin], 'r:', lw=0.8)
plt.plot([0, x1_max], [ymax, ymax], 'r:', lw=0.8)
plt.plot([x1_min, x1_min], [0, ymin], 'r:', lw=0.8)
plt.plot([x1_max, x1_max], [0, ymax], 'r:', lw=0.8)

plt.plot([0, x2_min], [ymax, ymax], 'r:', lw=0.8)
plt.plot([0, x2_max], [ymin, ymin], 'r:', lw=0.8)
plt.plot([x2_min, x2_min], [0, ymax], 'r:', lw=0.8)
plt.plot([x2_max, x2_max], [0, ymin], 'r:', lw=0.8)

#I0 e I1
plt.plot([0, 0.35], [0, 0], 'g-', lw=3, label=r'$I_0, I_1$')
plt.plot([0.65, 1], [0, 0], 'g-', lw=3)

# pre-imagens 
plt.plot([x1_min, x1_max], [0, 0], color='purple', lw=3, label=r'$F_\mu^{-1}(J)$')
plt.plot([x2_min, x2_max], [0, 0], color='purple', lw=3)
plt.text((x1_min+x1_max)/2, -0.06, r'em $I_0$', color='purple', ha='center', fontsize=8, weight='bold')
plt.text((x2_min+x2_max)/2, -0.06, r'em $I_1$', color='purple', ha='center', fontsize=8, weight='bold')

# ajustes finais 
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.3)
plt.xticks([0, 0.5, 1], ['0', '1/2', '1'])
plt.yticks([0, ymin, ymax, 1], ['0', '%s'%ymin, '%s'%ymax, '1'])

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle=':', alpha=0.4)
plt.legend(loc='upper right', framealpha=0.9)

plt.show()