from fastapi import FastAPI
from app.api import test_suite, test_case, test_run
from app.database import engine
from app.models import Base

# Initializing FastAPI app
app = FastAPI()

# Creating all database tables
Base.metadata.create_all(bind=engine)

# Including the API routes
app.include_router(test_suite.router)
app.include_router(test_case.router)
app.include_router(test_run.router)
