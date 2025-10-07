import numpy as np

def F(vec):
    x, y = vec
    return np.array([
        x * y + x**2 - 10,
        3 * x * y**2 + y - 57
    ], dtype=float)

def broyden(x0, y0, tol=1e-6, maxiter=100):
    x = np.array([x0, y0], dtype=float)
    B = np.eye(2)
    Fx = F(x)
    history = [tuple(x)]
    for k in range(1, maxiter + 1):
        delta = np.linalg.solve(B, -Fx)
        x_new = x + delta
        Fx_new = F(x_new)
        s = (x_new - x).reshape(2,1)
        yv = (Fx_new - Fx).reshape(2,1)
        denom = (s.T @ s)[0,0]
        if denom == 0:
            break
        B = B + ((yv - B.dot(s)).dot(s.T)) / denom
        history.append(tuple(x_new))
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return tuple(x_new), history, True, k
        x, Fx = x_new, Fx_new
    return tuple(x), history, False, maxiter
