from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from schema import EmbeddingRequest, EmbeddingResponse, SimilarityResponse, CompareSentencesRequest, SimilarityRequest, CompareSentencesResponse, RerankRequest, RerankResponse
import service
app = FastAPI()


@app.get("/")
def index():
    return RedirectResponse(url="/docs")

@app.post("/embedding", response_model=EmbeddingResponse)
async def encode(request: EmbeddingRequest):
    """bge-m3"""
    return {
        "object": "list",
        "data": service.encode_m3(request.sentences)
    }

@app.post("/embedding2", response_model=EmbeddingResponse)
async def encode2(request: EmbeddingRequest):
    """bge-m3"""
    return {
        "object": "list",
        "data": service.encode_m3_v2(request.sentences)
    }



@app.post("/compare_sentences",response_model=CompareSentencesResponse)
async def compare_sentences(request: CompareSentencesRequest):
    """句子语义检索"""
    return {
        "object": "list",
        "data": service.compare_sentences(request.source_sentence, request.compare_to_sentences)
    }

uvicorn.run(app, host="0.0.0.0", port=8000)
