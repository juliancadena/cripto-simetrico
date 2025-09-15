from base64 import b64decode, b64encode

def b64_encode(data: bytes) -> str:
    return b64encode(data).decode('utf-8')

def b64_decode(data: str) -> bytes:
    try:
        return b64decode(data, validate=True)
    except Exception:
        raise ValueError("Invalid base64 string")