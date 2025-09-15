from cryptography.hazmat.primitives import padding

_BLOCK_SIZE = 128

def pad(data: bytes) -> bytes:
    padder = padding.PKCS7(_BLOCK_SIZE).padder()
    return padder.update(data) + padder.finalize()

def unpad(data: bytes) -> bytes:
    unpadder = padding.PKCS7(_BLOCK_SIZE).unpadder()
    return unpadder.update(data) + unpadder.finalize()