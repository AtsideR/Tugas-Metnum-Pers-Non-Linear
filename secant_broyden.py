import numpy as np

def F(x, y):
    return np.array([
        x**2 + x*y - 10,
        3*x*y**2 + y - 57
    ])

def secant_method(tol=1e-6, max_iter=100):
    x0, y0 = 1.5, 3.5
    x1, y1 = 2.0, 4.0

    print("Iter |        x        |        y        |      Δx        |      Δy")
    print("-------------------------------------------------------------------")

    for r in range(1, max_iter + 1):
        try:
            F0 = F(x0, y0)
            F1 = F(x1, y1)

            dx = (x1 - x0) / (F1[0] - F0[0]) * (-F1[0])
            dy = (y1 - y0) / (F1[1] - F0[1]) * (-F1[1])
        except (ZeroDivisionError, FloatingPointError):
            print(f"Iterasi ke-{r}: Error pembagian dengan nol.")
            return

        x2, y2 = x1 + dx, y1 + dy
        print(f"{r:3d} | {x2:13.8f} | {y2:13.8f} | {dx:12.8f} | {dy:12.8f}")

        if max(abs(dx), abs(dy)) < tol:
            print(f"\n✅ Konvergen pada iterasi ke-{r}: x = {x2:.6f}, y = {y2:.6f}")
            return

        x0, y0 = x1, y1
        x1, y1 = x2, y2

    print("\n❌ Tidak konvergen sampai iterasi maksimum.")

if __name__ == "__main__":
    secant_method()
