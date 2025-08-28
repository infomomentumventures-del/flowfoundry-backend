from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WorkflowAnalysis(BaseModel):
    workflow_yaml: str

@app.get("/health")
async def health_check():
    return {"status": "ok", "product": "FlowFoundry API"}

@app.post("/analyze")
async def analyze_workflow(workflow: WorkflowAnalysis):
    # Stub implementation
    return {"plan": "Stub JSON plan for workflow analysis"}
