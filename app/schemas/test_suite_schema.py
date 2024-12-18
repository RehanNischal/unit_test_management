from pydantic import BaseModel
from datetime import datetime

# Test Suite Schema
class TestSuiteCreate(BaseModel):
    name: str
    description: str

class TestSuiteResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    status: str

    class Config:
        orm_mode = True

class TestSuiteUpdate(BaseModel):
    status: str
    name: str
    description: str