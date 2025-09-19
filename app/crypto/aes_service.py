from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from util.base64Helper import b64_decode, b64_encode
from util.keyHelper import get_or_make_key, get_or_make_iv, get_or_make_nonce
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

def encrypt_cbc(plaintext_b64: str, key_b64: str | None = None, iv_b64: str | None = None, key_size_bits: int = 256) -> tuple[str, str, str]:
    pt = b64_decode(plaintext_b64)
    key = get_or_make_key(key_b64, key_size_bits)
    iv = get_or_make_iv(iv_b64)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    enc = cipher.encryptor()
    ct = enc.update(pad(pt)) + enc.finalize()
    return b64_encode(ct), b64_encode(key), b64_encode(iv)

def encrypt_cfb(plaintext_b64: str, key_b64: str | None = None, iv_b64: str | None = None, key_size_bits: int = 256) -> tuple[str, str, str]:
    pt = b64_decode(plaintext_b64)
    key = get_or_make_key(key_b64, key_size_bits)
    iv = get_or_make_iv(iv_b64)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    enc = cipher.encryptor()
    ct = enc.update(pt) + enc.finalize()
    return b64_encode(ct), b64_encode(key), b64_encode(iv)

def encrypt_ofb(plaintext_b64: str, key_b64: str | None = None, iv_b64: str | None = None, key_size_bits: int = 256) -> tuple[str, str, str]:
    pt = b64_decode(plaintext_b64)
    key = get_or_make_key(key_b64, key_size_bits)
    iv = get_or_make_iv(iv_b64)
    cipher = Cipher(algorithms.AES(key), modes.OFB(iv))
    enc = cipher.encryptor()
    ct = enc.update(pt) + enc.finalize()
    return b64_encode(ct), b64_encode(key), b64_encode(iv)

def encrypt_ctr(plaintext_b64: str, key_b64: str | None = None, nonce_b64: str | None = None, key_size_bits: int = 256) -> tuple[str, str, str]:
    pt = b64_decode(plaintext_b64)
    key = get_or_make_key(key_b64, key_size_bits)
    nonce = get_or_make_nonce(nonce_b64, size=16)
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    enc = cipher.encryptor()
    ct = enc.update(pt) + enc.finalize()
    return b64_encode(ct), b64_encode(key), b64_encode(nonce)

def encrypt_gcm(plaintext_b64: str, key_b64: str | None = None, nonce_b64: str | None = None,  key_size_bits: int = 256) -> tuple[str, str, str, str]:
    pt = b64_decode(plaintext_b64)
    key = get_or_make_key(key_b64, key_size_bits)
    nonce = get_or_make_nonce(nonce_b64)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    enc = cipher.encryptor()
    ct = enc.update(pt) + enc.finalize()
    tag = enc.tag
    return b64_encode(ct), b64_encode(key), b64_encode(nonce), b64_encode(tag)