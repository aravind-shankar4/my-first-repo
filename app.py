from assistant import generate_response, index_documents, retrieve
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Zepto Support Assistant")


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: float


@app.on_event("startup")
def startup_event():
    index_documents()


@app.post("/chat", response_model=QueryResponse)
def chat_endpoint(req: QueryRequest):
    state = {
        "query": req.query,
        "documents": [],
        "answer": "",
        "confidence": 0.0,
        "sources": [],
    }
    state = retrieve(state)
    state = generate_response(state)
    return QueryResponse(
        answer=state["answer"],
        sources=state["sources"],
        confidence=state["confidence"],
    )
