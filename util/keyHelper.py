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