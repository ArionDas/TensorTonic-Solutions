import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """

    w = np.array(w, dtype=float)
    g = np.array(g, dtype=float)
    G = np.array(G, dtype=float)
    
    G_next = G + g**2
    w_next = w - (lr/(np.sqrt(G_next + eps)))*g

    return (w_next, G_next)