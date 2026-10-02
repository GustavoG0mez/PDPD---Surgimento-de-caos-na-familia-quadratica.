import numpy as np
import matplotlib.pyplot as plt

def f(x,mu): return mu*x*(1-x)
def f2(x,mu): return f(f(x,mu), mu)

# gerando os dados
x = np.linspace(0.4, 0.9, 1000)

# Parâmetros antes, durante e após a primeira bifurcação
lista_mu = [2.8, 3.0, 3.3]

fig, axs = plt.subplots(1, 3, figsize=(15,5))

for i, mu in enumerate(lista_mu):
    p = (mu-1)/mu # ponto fixo 
    
    # Plotando das curvas principais e da reta y=x
    axs[i].plot(x,x, 'k--', alpha=0.6, label="y = x")
    axs[i].plot(x, f(x,mu), 'b-', lw=1.5, label=r'$F_\mu(x)$')
    axs[i].plot(x, f2(x,mu), 'r-', lw=1.5, label=r'$F_\mu^2(x)$')
    
    # Marcação do ponto fixo
    axs[i].plot(p,p, 'ko', markersize=5)
    
    # Cálculo da órbita de período 2 para mu > 3
    if mu > 3:
        # Raízes da equação quadrática para F^2(x) = x
        q1 = (mu+1 + np.sqrt((mu-3)*(mu+1)))/(2*mu)
        q2 = (mu+1 - np.sqrt((mu-3)*(mu+1)))/(2*mu)
        axs[i].plot(q1,q1, 'ro', markersize=5)
        axs[i].plot(q2,q2, "ro", markersize=5)

    # Formatação dos eixos
    axs[i].set_title(r'$\mu = %s$' % mu)
    axs[i].set_xlabel('x')
    axs[i].set_ylabel("y")
    axs[i].set_xlim(0.4, 0.9)
    axs[i].set_ylim(0.4, 0.9)
    axs[i].grid(True, linestyle=':', alpha=0.7)
    axs[i].legend(loc="upper left")

plt.tight_layout()
plt.subplots_adjust(top=0.88) 

plt.show()