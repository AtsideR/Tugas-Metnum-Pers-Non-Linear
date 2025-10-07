import numpy as np

def F(x, y):
    return np.array([
        x**2 + x*y - 10,
        3*x*y**2 + y - 57
    ])

def J(x, y):
    return np.array([
        [2*x + y, x],
        [3*y**2, 6*x*y + 1]
    ])

def newton_raphson(tol=1e-6, max_iter=100):
    x, y = 1.5, 3.5
    print("Iter |        x        |        y        |      Δx        |      Δy")
    print("-------------------------------------------------------------------")

    for r in range(1, max_iter + 1):
        try:
            Fx = F(x, y)
            Jx = J(x, y)
            delta = np.linalg.solve(Jx, -Fx)
        except np.linalg.LinAlgError:
            print(f"Iterasi ke-{r}: Matriks singular (tidak dapat diselesaikan)")
            return

        dx, dy = delta
        x_new, y_new = x + dx, y + dy
        print(f"{r:3d} | {x_new:13.8f} | {y_new:13.8f} | {dx:12.8f} | {dy:12.8f}")

        if max(abs(dx), abs(dy)) < tol:
            print(f"\n✅ Konvergen pada iterasi ke-{r}: x = {x_new:.6f}, y = {y_new:.6f}")
            return

        x, y = x_new, y_new

    print("\n❌ Tidak konvergen sampai iterasi maksimum.")

if __name__ == "__main__":
    newton_raphson()
