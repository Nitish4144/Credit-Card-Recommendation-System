from fastapi import APIRouter, UploadFile, File


from app.schemas.transaction import (
    TransactionRequest,
    TransactionResponse
)

router = APIRouter() 


@router.get("/health")
def health_check():
    return {
        "status": "healthy...."
    }


@router.post("/transactions" , response_model = TransactionResponse)
def create_transaction(transaction: TransactionRequest):
    return TransactionResponse(
        message=f"Received transaction from {transaction.merchant}"
    )


@router.post("/upload")
async def upload_file(file: UploadFile=File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "size": len(contents)
    }