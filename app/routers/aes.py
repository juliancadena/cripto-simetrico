from fastapi import APIRouter, HTTPException
from app.schemas import AESRequest, AESResponse

router = APIRouter()

@router.post("", response_model=AESResponse)
async def aes_operation(request: AESRequest):
    if request.action == "encrypt" and not request.plaintext:
        raise HTTPException(status_code=400, detail="Plaintext is required for encryption")
    if request.action == "decrypt" and not request.ciphertext:
        raise HTTPException(status_code=400, detail="Ciphertext is required for decryption")
    
    return AESResponse(
        mode=request.mode,
        action=request.action,
        ciphertext="dummy_ciphertext" if request.action == "encrypt" else None,
        plaintext="dummy_plaintext" if request.action == "decrypt" else None,
    )