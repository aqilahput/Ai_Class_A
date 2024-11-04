#Perkalian
import numpy as np

# Set seed untuk memastikan hasil random yang sama setiap kali program dijalankan
np.random.seed(5)

# Inisialisasi matriks random ukuran 3x3 untuk contoh sederhana
matriks_a = np.random.randint(1, 10, size=(2, 3))
matriks_b = np.random.randint(1, 10, size=(3, 4))

# Fungsi perkalian matriks manual tanpa menggunakan np.dot atau np.matmul
def kali_matriks_manual(a, b):
    hasil = np.zeros((len(a), len(b[0])), dtype=int)  # Matriks hasil dengan ukuran yang sesuai
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                hasil[i][j] += a[i][k] * b[k][j]
    return hasil

# Perkalian matriks menggunakan np.matmul
def kali_matriks_matmul(a, b):
    return np.matmul(a, b)

# Menampilkan matriks A dan B
print("Matriks A:")
print(matriks_a)
print("\nMatriks B:")
print(matriks_b)

# Hasil perkalian matriks secara manual
hasil_manual = kali_matriks_manual(matriks_a, matriks_b)
print("\nHasil Perkalian Matriks A * B (manual):")
print(hasil_manual)

# Hasil perkalian matriks menggunakan numpy
hasil_matmul = kali_matriks_matmul(matriks_a, matriks_b)
print("\nHasil Perkalian Matriks A * B (NumPy menggunakan matmul):")
print(hasil_matmul)

#Pertambahan
import numpy as np

np.random.seed(0) 
A = np.random.randint(1, 10, (2, 3))
B = np.random.randint(1, 10, (2, 3))

addition_numpy = A + B

print("Matriks A (NumPy):")
print(A)
print("\nMatriks B (NumPy):")
print(B)
print("\nHasil Penambahan Matriks (NumPy):")
print(addition_numpy)

def matrix_add_manual(A, B):
    
    result_rows = len(A)
    result_columns = len(A[0])
    
    result = [[0 for _ in range(result_columns)] for _ in range(result_rows)]
    
    for i in range(result_rows):
        for j in range(result_columns):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

A_list = [[6, 1, 4], [4, 8, 4]]
B_list = [[5, 9, 2], [3, 7, 6]]

addition_manual = matrix_add_manual(A_list, B_list)

print("\nMatriks A (Manual):")
print(A_list)
print("\nMatriks B (Manual):")
print(B_list)
print("\nHasil Penambahan Matriks (Manual):")
print(addition_manual)