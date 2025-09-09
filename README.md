Proyecto base con FastAPI para implementar cifrado/descifrado AES en modos
ECB, CBC, CFB, OFB, CTR y GCM. Este commit incluye solo la **estructura**
(routers, schemas, config). La lógica criptográfica se añadirá en `app/crypto/aes_service.py`.

## Requisitos

- Python 3.11+

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar

```bash
uvicorn app.main:app --reload
# Swagger UI: http://127.0.0.1:8000/docs
```
