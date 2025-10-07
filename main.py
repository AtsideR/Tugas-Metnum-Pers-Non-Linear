from jacobi import jacobi
from seidel import seidel
from newton import newton
from secant_broyden import broyden

x0, y0 = 1.5, 3.0
tol = 1e-6

methods = {
    "Jacobi": jacobi,
    "Gauss-Seidel": seidel,
    "Newton-Raphson": newton,
    "Broyden (Secant)": broyden
}
print("Nama : Redista Rakha Izza")
print("NIM : 21120123130085")
print("=== Sistem Iteratif ===")
for name, func in methods.items():
    print(f"\n>>> Metode {name}")
    sol, hist, conv, iters = func(x0, y0, tol=tol)
    print(f"Konvergen: {conv}")
    print(f"Iterasi: {iters}")
    print(f"Solusi akhir: {sol}")
    if conv:
        print(f"Error terakhir: {max(abs(hist[-1][0]-hist[-2][0]), abs(hist[-1][1]-hist[-2][1]))}")
