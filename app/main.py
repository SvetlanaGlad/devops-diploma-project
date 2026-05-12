from fastapi import FastAPI
import psutil


app = FastAPI(title="DevOps Diploma Research App")


@app.get("/")
def read_root():
    return {"message": "Welcome to my Research Project", "status": "Ready"}


@app.get("/health")
def health_check():
    return {"status": "UP", "version": "1.0.0"}


@app.get("/system")
def system_metrics():
    return {
        "cpu_load": psutil.cpu_percent(),
        "memory_load": psutil.virtual_memory().percent
    }
