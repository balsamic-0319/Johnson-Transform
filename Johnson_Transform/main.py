import numpy as np

#Johnson変換3種
def Su_Johnson_Transform(x, gamma, delta, xi, lam):
    ans = gamma + delta * np.arcsinh((x - xi) / lam)
    return ans

def Sb_Johnson_Transform(x, gamma, delta, xi, lam):
    eps = 1e-8
    z = (x - xi) / lam
    z = np.clip(z, eps, 1 - eps)
    ans = gamma + delta * np.log(z / (1 - z))
    return ans

def Sl_Johnson_Transform(x, gamma, delta, xi, lam):
    eps = 1e-8
    z = (x - xi) / lam
    z = np.clip(z, eps, None)
    ans = gamma + delta * np.log(z)
    return ans

#逆行列3種
def Su_Inverse(z, gamma, delta, xi, lam):
    ans = xi - lam * np.sinh((gamma - z) / delta)
    return ans

def Sb_Inverse(z, gamma, delta, xi, lam):
    ans = xi + (lam / (1 + np.exp((gamma - z) / delta)))
    return ans

def Sl_Inverse(z, gamma, delta, xi, lam):
    ans = xi + lam * np.exp((z - gamma) / delta)
    return ans