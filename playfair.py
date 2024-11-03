import numpy as np

def create_playfair_matrix(keyword):
    """Створює матрицю Плейфеєра 7x5 на основі ключового слова."""
    alphabet = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя'."
    seen = set()
    unique_keyword = []
    
    # Удаляємо дублікат символів у ключовому слові
    for char in keyword:
        if char not in seen:
            seen.add(char)
            unique_keyword.append(char)
    
    # Заповнюємо матрицю ключовим словом
    matrix = unique_keyword.copy()
    for char in alphabet:
        if char not in seen:
            matrix.append(char)
            seen.add(char)
    
    # Формуємо 7x5 матрицю
    matrix = np.array(matrix).reshape(7, 5)
    return matrix

def playfair_encrypt(plaintext, matrix):
    """Шифрує текст за методом Плейфеєра."""
    alphabet = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя'."
    plaintext = plaintext.replace(' ', "'")  # Заміна пробілів на заповнювач
    
    # Паруємо символи
    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
            if a == b:  # Якщо букви однакові
                pairs.append((a, "'"))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        else:
            pairs.append((a, "'"))  # Непарна кількість символів
            i += 1
    
    # Шифрування пар
    encrypted = ""
    for a, b in pairs:
        row_a, col_a = np.where(matrix == a)
        row_b, col_b = np.where(matrix == b)
        if row_a == row_b:  # Один рядок
            encrypted += matrix[row_a[0], (col_a[0] + 1) % 5]
            encrypted += matrix[row_b[0], (col_b[0] + 1) % 5]
        elif col_a == col_b:  # Один стовпець
            encrypted += matrix[(row_a[0] + 1) % 7, col_a[0]]
            encrypted += matrix[(row_b[0] + 1) % 7, col_b[0]]
        else:  # Прямокутник
            encrypted += matrix[row_a[0], col_b[0]]
            encrypted += matrix[row_b[0], col_a[0]]

    return encrypted

# Дані для користувачів
users = [
    {"id": 1, "surname": "волков", "password": "дєкиалмфєп"},
    {"id": 2, "surname": "корсун", "password": "гіаукїфп"},
    {"id": 3, "surname": "пащенко", "password": "спгдсщ"},
    {"id": 4, "surname": "коваленко", "password": "авко"},
    {"id": 5, "surname": "пєтухова", "password": "авілгм"},
    {"id": 6, "surname": "войтюк", "password": "їтлфо."},
    {"id": 7, "surname": "щербаков", "password": "фщбщцжй'"},
    {"id": 8, "surname": "шишкун", "password": "хепбтфдїй'"},
    {"id": 9, "surname": "демченко", "password": "йвткяфбї"},
    {"id": 10, "surname": "лисенко", "password": "обкртбхлїю"},
    {"id": 11, "surname": "смірнова", "password": "іпслчю"},
    {"id": 12, "surname": "таран", "password": "уфрічю"},
    {"id": 13, "surname": "волошин", "password": "йланвс"},
    {"id": 14, "surname": "киришко", "password": "икшкїд"},
    {"id": 15, "surname": "станько", "password": "тапєїь"},
]

def main():
    """Головна програма для шифрування паролів користувачів."""
    for user in users:
        matrix = create_playfair_matrix(user["surname"])
        encrypted_password = playfair_encrypt(user["password"], matrix)
        print(f"Користувач {user['id']} ({user['surname']}): зашифрований пароль - {encrypted_password}")

if __name__ == "__main__":
    main()