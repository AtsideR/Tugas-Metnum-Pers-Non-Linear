import numpy as np

def F(vec):
    x, y = vec
    return np.array([
        x * y + x**2 - 10,
        3 * x * y**2 + y - 57
    ], dtype=float)

def J(vec):
    x, y = vec
    return np.array([
        [y + 2*x, x],
        [3*y**2, 6*x*y + 1]
    ], dtype=float)

def newton(x0, y0, tol=1e-6, maxiter=100):
    x, y = x0, y0
    history = [(x, y)]
    for k in range(1, maxiter + 1):
        Fv = F((x, y))
        Jv = J((x, y))
        delta = np.linalg.solve(Jv, -Fv)
        x_new, y_new = x + delta[0], y + delta[1]
        history.append((x_new, y_new))
        if max(abs(delta[0]), abs(delta[1])) < tol:
            return (x_new, y_new), history, True, k
        x, y = x_new, y_new
    return (x, y), history, False, maxiter
