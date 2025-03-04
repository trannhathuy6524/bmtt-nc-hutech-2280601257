from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    encrypted_text = data["encrypted_text"]
    key = int(data['key'])
    plain_text = caesar_cipher.decrypt_text(encrypted_text, key)
    return jsonify({'plain_text': plain_text})


vigenere_cipher = VigenereCipher()
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = data['key']
    plain_text = vigenere_cipher.vigenere_decrypt(encrypted_text, key)
    return jsonify({'plain_text': plain_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)