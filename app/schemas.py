from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

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

    # Test Case Schema
class TestCaseCreate(BaseModel):
    name: str
    description: str
    priority: str
    expected_outcome: str
    test_suite_id: int

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

# Test Run Schema
class TestRunCreate(BaseModel):
    test_suite_id: int
    run_status: str

class TestRunResponse(BaseModel):
    id: int
    test_suite_id: int
    run_status: str
    result: str
    start_time: datetime
    end_time: Optional[datetime]
    test_results: List[dict]  # List of individual test case results

    class Config:
        orm_mode = True

class TestRunUpdate(BaseModel):
    result: str
    end_time: datetime
    test_results: List[dict]  # List of individual test case results

