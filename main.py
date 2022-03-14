from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routes

app = FastAPI(title="Cooper-Backend-App")
app.include_router(routes.router, tags=["Backend App"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can be updated as per frontend requirements i.e (“http://localhost:3000.”)
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
