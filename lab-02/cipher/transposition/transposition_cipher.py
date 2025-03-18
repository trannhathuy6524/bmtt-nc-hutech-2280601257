class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += key
        return ''.join(encrypted_text)

    def decrypt(self, text, key):
        num_cols = (len(text) + key - 1) // key  # Số cột cần có (làm tròn lên)
        num_rows = key  # Số hàng bằng key
        num_shaded_cells = (num_cols * num_rows) - len(text)  # Số ô trống

        decrypted_text = [''] * num_cols
        col, row = 0, 0

        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            if col == num_cols or (col == num_cols - 1 and row >= num_rows - num_shaded_cells):
                col = 0
                row += 1

        return ''.join(decrypted_text)
