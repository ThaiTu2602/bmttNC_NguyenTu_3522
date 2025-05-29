from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.transposition import TranspositionCipher
from cipher.playfair.playfair_cipher import PlayfairCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)
playfair_cipher = PlayfairCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()

# Router routes for home page


@app.route("/")
def home():
    return render_template('index.html')

# Router routes for Caesar cipher


@app.route("/caesar")
def caesar():
    return render_template('caesar.html')


@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"


@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


@app.route("/playfair")
def playfair():
    return render_template("playfair.html")


@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted = playfair_cipher.playfair_encrypt(text, matrix)
    return f"Encrypted Text: <b>{encrypted}</b>"


@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    cipher = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted = playfair_cipher.playfair_decrypt(cipher, matrix)
    return f"Decrypted Text: <b>{decrypted}</b>"


@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")


@app.route("/railfence")
def railfence():
    return render_template("railfence.html")


@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

# Vigenere Cipher


@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = vigenere_cipher.encrypt(text, key)
    return f"Encrypted Text: <b>{encrypted_text}</b>"


@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = vigenere_cipher.decrypt(text, key)
    return f"Decrypted Text: <b>{decrypted_text}</b>"
# RailFence Cipher


@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
    return f"Encrypted Text: <b>{encrypted_text}</b>"


@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
    return f"Decrypted Text: <b>{decrypted_text}</b>"
# Transposition Cipher


@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = transposition_cipher.encrypt(text, key)
    return f"Encrypted Text: <b>{encrypted_text}</b>"


@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = transposition_cipher.decrypt(text, key)
    return f"Decrypted Text: <b>{decrypted_text}</b>"


# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
