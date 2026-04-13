from fastapi import FastAPI
import os
import psutil

app = FastAPI(title="DevOps Diploma Research App")

@app.get("/")
def read_root():
    return { "message": "Welcome to my Research Project", "status": "Ready"}

@app.get("/health")
def health_check():
    return {"status": "UP", "version":"1.0.0"}

@app.get("/system")
def system_metrics():
    return{
        "cpu_load": psutil.cpu_percent(),
        "memory_load": psutil.virtual_memory().percent
    }

@app.get("/security-test")
def security_test():
    SECRET_KEY = "SUPER_SECRET_123_PROTECT_ME" 
    return {"info": "Testing security scanners...", "key_detected": True}

