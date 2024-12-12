def lire_matrice(T, N, M, nom):
    for i in range(N):
        for j in range(M):
            T[i][j] = float(input(f"{nom}[{i}][{j}]= "))

def afficher_matrice(T, b, N, M):
    for i in range(N):
        print("[", end="")
        for j in range(M):
            print(f"{T[i][j]:.2f}", end="  ")
        print("] [", b[i], "]")
    print()

def lire_vecteur(T, N, nom):
    for i in range(N):
        T[i] = float(input(f"{nom}[{i}]= "))

def afficher_vecteur(T, N, nom):
    for i in range(N):
        print(f"{nom}[{i}]= {T[i]:.2f}")
    print()

def decomposer_LU(A, N):
    """
    Décompose la matrice A en L et U où A = L * U
    L est une matrice triangulaire inférieure
    U est une matrice triangulaire supérieure
    """
    L = [[0] * N for _ in range(N)]
    U = [[0] * N for _ in range(N)]

    for i in range(N):
        # Calcul des éléments de U
        for k in range(i, N):
            somme = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - somme
        
        # Calcul des éléments de L
        for k in range(i, N):
            if i == k:
                L[i][i] = 1  # La diagonale de L est composée de 1
            else:
                somme = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - somme) / U[i][i]

    return L, U

def descente(L, b, N):
    """
    Résout Ly = b par substitution avant.
    """
    y = [0] * N

    for i in range(N):
        somme = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - somme) / L[i][i]

    return y

def remontee(U, y, N):
    """
    Résout Ux = y par substitution arrière.
    """
    x = [0] * N

    for i in range(N - 1, -1, -1):
        somme = sum(U[i][j] * x[j] for j in range(i + 1, N))
        x[i] = (y[i] - somme) / U[i][i]

    return x

def resoudre_systeme(A, b, N):
    """
    Résout Ax = b en utilisant la décomposition LU.
    """
    print("Lire la matrice A :")
    lire_matrice(A, N, N, 'A')

    print("Lire le vecteur b :")
    lire_vecteur(b, N, 'b')

    print("Matrice A initiale :")
    afficher_matrice(A, b, N, N)

    # Décomposition LU
    L, U = decomposer_LU(A, N)

    print("Matrice L :")
    afficher_matrice(L, [0] * N, N, N)

    print("Matrice U :")
    afficher_matrice(U, [0] * N, N, N)

    # Résolution de Ly = b (descente)
    y = descente(L, b, N)
    print("Solution de Ly = b (y) :")
    afficher_vecteur(y, N, 'y')

    # Résolution de Ux = y (remontée)
    x = remontee(U, y, N)
    print("Solution de Ux = y (x) :")
    afficher_vecteur(x, N, 'x')

    return x

# Exemple d'utilisation
N = int(input("Entrez la taille de la matrice carrée A : "))
A = [[0] * N for _ in range(N)]
b = [0] * N
resoudre_systeme(A, b, N)
