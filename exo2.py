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

def jacobi(A, b, N, max_iter):
    x = [0] * N
    x_new = [0] * N
    for k in range(max_iter):
        for i in range(N):
            somme = 0
            for j in range(N):
                if i != j:
                    somme += A[i][j] * x[j]
            x_new[i] = (b[i] - somme) / A[i][i]
        for i in range(N):
            x[i] = x_new[i]
    return x

def gauss_seidel(A, b, N, max_iter):
    x = [0] * N
    for k in range(max_iter):
        for i in range(N):
            somme1 = 0
            somme2 = 0
            for j in range(i):
                somme1 += A[i][j] * x[j]
            for j in range(i + 1, N):
                somme2 += A[i][j] * x[j]
            x[i] = (b[i] - somme1 - somme2) / A[i][i]
    return x

def menu():
    print("\nMenu:")
    print("1 methode de Jacobi")
    print("2 methode de Gauss-Seidel")
    print("3 quiter")

def resoudre_systeme():
    N = int(input("Entrez la taille de la matrice carre A : "))
    A = [[0] * N for _ in range(N)]
    b = [0] * N

    print("Lire la matrice A :")
    lire_matrice(A, N, N, 'A')

    print("Lire le vecteur b :")
    lire_vecteur(b, N, 'b')

    while True:
        menu()
        choix = input("Choisissez une methode : ")

        if choix == "1":
            max_iter = int(input("Nombre maximum d'iterations : "))
            x = jacobi(A, b, N, max_iter)
            print("Solution approchee (x) avec Jacobi :")
            afficher_vecteur(x, N, 'x')

        elif choix == "2":
            max_iter = int(input("Nombre maximum d'iterations : "))
            x = gauss_seidel(A, b, N, max_iter)
            print("Solution approchee (x) avec Gauss-Seidel :")
            afficher_vecteur(x, N, 'x')

        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez ressayer.")


resoudre_systeme()
