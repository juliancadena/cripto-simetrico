from fastapi import APIRouter, HTTPException
from app.schemas import AESRequest, AESResponse
from app.crypto.aes_service import encrypt_ecb, decrypt_ecb

router = APIRouter()

@router.post("", response_model = AESResponse)
async def aes_operation(request: AESRequest):
    if request.mode not in ['ECB', 'CBC', 'CFB', 'OFB', 'CTR', 'GCM']:
        raise HTTPException(status_code=400, detail="Unsupported mode")
    if request.action not in ['encrypt', 'decrypt']:
        raise HTTPException(status_code=400, detail="Unsupported action")
    if request.mode == "ECB":
        if request.action == "encrypt":
            ct_b64, key_b64 = encrypt_ecb(request.plaintext, request.key_b64, request.key_size_bits)
            return AESResponse(
                mode=request.mode,
                action=request.action,
                ciphertext=ct_b64,
                key_b64=key_b64
            )
        else:
            if not request.key_b64:
                raise HTTPException(status_code=400, detail="Key is required for decryption")
            pt_b64 = decrypt_ecb(request.ciphertext, request.key_b64, request.key_size_bits)
            return AESResponse(
                mode=request.mode,
                action=request.action,
                plaintext=pt_b64
            )
    elif request.mode == "CBC":
        if request.action == "encrypt":
            pass
        else:
            pass
    elif request.mode == "CFB":
        if request.action == "encrypt":
            pass
        else:
            pass 
    elif request.mode == "OFB":
        if request.action == "encrypt":
            pass
        else:
            pass 
    elif request.mode == "CTR":
        if request.action == "encrypt":
            pass
        else:
            pass 
    elif request.mode == "GCM":
        if request.action == "encrypt":
            pass
        else:
            pass 
    else:
        return AESResponse(
            mode=request.mode,
            action=request.action,
            ciphertext="dummy_ciphertext" if request.action == "encrypt" else None,
            plaintext="dummy_plaintext" if request.action == "decrypt" else None,
        )