from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="OASF Agent Endpoint", version="0.8")


class AgentRequest(BaseModel):
    message: str
    context: Dict[str, Any] = {}


@app.get("/oasf")
def oasf_info():
    return {
        "name": "Web3 Research Assistant",
        "description": "A friendly Web3 + finance agent for research, monitoring, and automation.",
        "version": "0.8",
        "endpoints": {
            "chat": "/oasf/chat"
        }
    }


@app.post("/oasf/chat")
def chat(req: AgentRequest):
    # placeholder response (later you can connect OpenAI / other model)
    reply = f"Got it. You said: {req.message}"

    return {
        "reply": reply,
        "status": "success"
    }


@app.get("/")
def root():
    return {"status": "running", "endpoint": "/oasf"}

