from util.base64Helper import b64_decode
import os

def get_or_make_key(key_b64: str | None, key_size_bits: int) -> bytes:
    size = {128: 16, 192: 24, 256: 32}
    if key_b64 is not None:
        key = b64_decode(key_b64)
        if len(key) not in size.values():
            raise ValueError("Invalid key size")
        return key
    return os.urandom(size[key_size_bits])

def get_or_make_iv(iv_b64: str | None) -> bytes:
    if iv_b64 is not None:
        iv = b64_decode(iv_b64)
        if len(iv) != 16:
            raise ValueError("Invalid IV size")
        return iv
    return os.urandom(16)

def get_or_make_nonce(nonce_b64: str | None, size: int = 12) -> bytes:
    if nonce_b64 is not None:
        nonce = b64_decode(nonce_b64)
        if len(nonce) != size:
            raise ValueError("Invalid nonce size")
        return nonce
    return os.urandom(size)