import math

def gauss_seidel(tol=1e-6, max_iter=100):
    x, y = 1.5, 3.5
    print("Iter |      x        |      y        |    Δx        |    Δy")
    print("-------------------------------------------------------------")

    for r in range(1, max_iter + 1):
        try:
            x_new = (10 - x**2) / y
            y_new = math.sqrt((57 - y) / (3 * x_new))
        except (ValueError, ZeroDivisionError):
            print(f"Iterasi ke-{r}: Error matematis (akar negatif / pembagian 0)")
            return

        dx = abs(x_new - x)
        dy = abs(y_new - y)
        print(f"{r:3d} | {x_new:11.6f} | {y_new:11.6f} | {dx:10.6f} | {dy:10.6f}")

        if max(dx, dy) < tol:
            print(f"\n Konvergen pada iterasi ke-{r}: x = {x_new:.6f}, y = {y_new:.6f}")
            return

        x, y = x_new, y_new

    print("\n Tidak konvergen sampai iterasi maksimum.")

if __name__ == "__main__":
    gauss_seidel()
