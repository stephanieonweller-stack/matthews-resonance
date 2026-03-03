
import numpy as np
from dataclasses import dataclass
from scipy.integrate import solve_ivp

@dataclass
class Params:
    p: int = 2
    q: int = 3
    w0: float = 1.0
    w1: float = 2.0
    w2: float = 3.0
    eps: float = 1.0
    kappa: float = 1.0

def wrap(x):
    return (x + np.pi) % (2*np.pi) - np.pi

def residuals(Y, p, q):
    phi0 = Y[:,0]
    phi1 = Y[:,1]
    phi2 = Y[:,2]
    Delta = q*phi2 - p*phi1
    Psi = 3*phi0 - phi1 - phi2
    return Delta, Psi

def rhs_full(t, y, par):
    phi0, phi1, phi2 = y
    Delta = par.q*phi2 - par.p*phi1
    Psi = 3*phi0 - phi1 - phi2

    dphi0 = par.w0 + 3*par.kappa*np.sin(Psi)
    dphi1 = par.w1 + par.eps*par.q*np.sin(Delta) - par.kappa*np.sin(Psi)
    dphi2 = par.w2 - par.eps*par.p*np.sin(Delta) - par.kappa*np.sin(Psi)

    return np.array([dphi0, dphi1, dphi2])

def integrate(par, t_span=(0,50), y0=(0,0.1,0.2), n=5000):
    t_eval = np.linspace(t_span[0], t_span[1], n)
    sol = solve_ivp(lambda t,y: rhs_full(t,y,par),
                    t_span, y0, t_eval=t_eval, rtol=1e-9, atol=1e-12)
    return sol.t, sol.y.T
