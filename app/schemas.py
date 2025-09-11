from typing import Optional, Literal
from pydantic import BaseModel, Field

AESMode = Literal['ECB', 'CBC', 'CFB', 'OFB', 'CTR', 'GCM']
Action = Literal['encrypt', 'decrypt']

class AESRequest(BaseModel):
    action: Action = Field(description="Action to perform: encrypt or decrypt")
    mode: AESMode
    plaintext: Optional[str] = Field(None, description="Plaintext to be encrypted (required for encryption)")
    ciphertext: Optional[str] = Field(None, description="Ciphertext to be decrypted (required for decryption)")
    key_b64: Optional[str] = Field(None, description="Base64-encoded encryption key (16, 24, or 32 bytes)")
    key_size_bits: Optional[int] = Field(256, description="Key size in bits: 128, 192, or 256")
    iv_b64: Optional[str] = Field(None, description="Base64-encoded initialization vector (16 bytes), required for some modes")
    nonce_b64: Optional[str] = Field(None, description="Base64-encoded nonce (16 bytes), required for CTR and GCM modes")
    tag_b64: Optional[str] = Field(None, description="Base64-encoded authentication tag (16 bytes), required for GCM decryption")

class AESResponse(BaseModel):
    mode: AESMode
    action: Action
    ciphertext: Optional[str] = None
    plaintext: Optional[str] = None
    key_b64: Optional[str] = None
    iv_b64: Optional[str] = None
    nonce_b64: Optional[str] = None
    tag_b64: Optional[str] = None