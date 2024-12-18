from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# Test Run Schema
class TestRunCreate(BaseModel):
    test_suite_id: int
    run_status: str

# Test Run Response Schema
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

# Test Run Update Schema
class TestRunUpdate(BaseModel):
    result: str
    end_time: datetime
    run_status: str
