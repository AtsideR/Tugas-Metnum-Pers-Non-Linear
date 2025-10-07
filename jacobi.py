import math

def fx(x, y):
    return (10 - x ** 2) / y

def fy(x, y):
    arg = (57 - y) / (3 * x) if x != 0 else -1
    return math.sqrt(arg) if arg >= 0 else float('nan')

def jacobi(x0, y0, tol=1e-6, maxiter=200):
    x, y = x0, y0
    history = [(x, y)]
    for k in range(1, maxiter + 1):
        x_new = fx(x, y)
        y_new = fy(x, y)
        history.append((x_new, y_new))

        if not (math.isfinite(x_new) and math.isfinite(y_new)):
            return None, history, False, k
        if max(abs(x_new - x), abs(y_new - y)) < tol:
            return (x_new, y_new), history, True, k
        x, y = x_new, y_new
    return (x, y), history, False, maxiter
