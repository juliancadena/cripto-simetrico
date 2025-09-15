from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from util.base64Helper import b64_decode, b64_encode
from util.keyHelper import get_or_make_key
from util.padderHelper import pad, unpad

def encrypt_ecb(plaintext_b64: str, key_b64: str | None = None, key_size_bits: int = 256) -> tuple[str, str]:
    pt = b64_decode(plaintext_b64)
    key = get_or_make_key(key_b64, key_size_bits)
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    enc = cipher.encryptor()
    ct = enc.update(pad(pt)) + enc.finalize()
    return b64_encode(ct), b64_encode(key)
    
def decrypt_ecb(ciphertext_b64: str, key_b64: str, key_size_bits: int = 256) -> str:
    ct = b64_decode(ciphertext_b64)
    key = get_or_make_key(key_b64, key_size_bits)
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    dec = cipher.decryptor()
    pt_padded = dec.update(ct) + dec.finalize()
    return b64_encode(unpad(pt_padded))