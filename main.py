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


@app.get("/.well-known/agent-card.json")
def agent_card():
    return {
        "name": "Web3 Research Assistant",
        "description": "A friendly Web3 + finance agent for research, monitoring, and automation.",
        "version": "1.0.0",
        "endpoints": {
            "oasf": "/oasf",
            "chat": "/oasf/chat"
        },
        "skills": [
            "market_research",
            "web_search",
            "summarization",
            "data_extraction",
            "portfolio_monitoring",
            "onchain_analysis"
        ]
    }


@app.get("/.well-known/agent-card.json")
def agent_card_main():
    return {
        "name": "Web3 Multi-Agent Assistant",
        "description": "A friendly AI assistant for Web3, finance research, monitoring, and content support.",
        "version": "1.0.0",
        "skills": ["web3_research", "market_monitoring", "summarization", "content_support"],
        "endpoints": {
            "oasf": "/oasf",
            "chat": "/oasf/chat"
        }
    }


@app.get("/.well-known/agent-card-research.json")
def agent_card_research():
    return {
        "name": "Web3 Research Agent",
        "description": "Focused on Web3 and finance research, trend scanning, and turning news into clear insights.",
        "version": "1.0.0",
        "skills": ["web_search", "market_intel", "onchain_analysis", "summarization"],
        "endpoints": {
            "oasf": "/oasf",
            "chat": "/oasf/chat"
        }
    }


@app.get("/.well-known/agent-card-content.json")
def agent_card_content():
    return {
        "name": "Web3 Content Agent",
        "description": "Helps write clean, human content for Web3 topics, including posts, threads, summaries, and scripts.",
        "version": "1.0.0",
        "skills": ["copywriting", "thread_writing", "rewriting", "content_optimization"],
        "endpoints": {
            "oasf": "/oasf",
            "chat": "/oasf/chat"
        }
    }


@app.post("/oasf/chat/research")
def research_chat(req: AgentRequest):
    reply = (
        "Here’s a research-focused breakdown:\n"
        f"- key topic: {req.message}\n"
        "- next step: gather recent sources + confirm market signals\n"
        "- output: short summary + actionable takeaways"
    )
    return {"reply": reply, "agent": "research", "status": "success"}


@app.post("/oasf/chat/content")
def content_chat(req: AgentRequest):
    reply = (
        "Here’s a content-focused output:\n"
        f"tweet idea: {req.message}\n\n"
        "hook: most people are missing this.\n"
        "angle: explain it simply, then drop the bullish takeaway.\n"
        "ending: ask a question to drive engagement."
    )
    return {"reply": reply, "agent": "content", "status": "success"}

