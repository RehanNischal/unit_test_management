from pydantic import BaseModel
from datetime import datetime

# Test Case Schema
class TestCaseCreate(BaseModel):
    name: str
    description: str
    priority: str
    expected_outcome: str
    test_suite_id: int

# Test Case Response Schema
class TestCaseResponse(BaseModel):
    id: int
    name: str
    description: str
    priority: str
    expected_outcome: str
    created_at: datetime
    updated_at: datetime
    status: str
    test_suite_id: int

    class Config:
        orm_mode = True

# Test Case Update Schema
class TestCaseUpdate(BaseModel):
    name: str
    description: str
    priority: str
    expected_outcome: str

