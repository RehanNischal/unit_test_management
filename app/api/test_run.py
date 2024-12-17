from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import create_test_run, get_test_runs, get_test_run, update_test_run, delete_test_run
from app.schemas import TestRunCreate, TestRunResponse, TestRunUpdate
from app.database import get_db

router = APIRouter(
    prefix="/test_runs",
    tags=["Test Runs"]
)

@router.post("/", response_model=TestRunResponse)
def create_run(test_run: TestRunCreate, db: Session = Depends(get_db)):
    return create_test_run(db=db, test_suite_id=test_run.test_suite_id, run_status=test_run.run_status)

@router.get("/", response_model=list[TestRunResponse])
def read_runs(db: Session = Depends(get_db)):
    return get_test_runs(db=db)

@router.get("/{test_run_id}", response_model=TestRunResponse)
def read_run(test_run_id: int, db: Session = Depends(get_db)):
    return get_test_run(db=db, test_run_id=test_run_id)



@router.put("/{test_run_id}", response_model=TestRunResponse)
def update_run(test_run_id: int, test_run_update: TestRunUpdate, db: Session = Depends(get_db)):
    return update_test_run(
        db=db, test_run_id=test_run_id,
        result=test_run_update.result,
        end_time=test_run_update.end_time,
        test_results=test_run_update.test_results
    )

@router.delete("/{test_run_id}")
def delete_run(test_run_id: int, db: Session = Depends(get_db)):
    result = delete_test_run(db=db, test_run_id=test_run_id)
    if "Test run deleted successfully" in result["message"]:
        return result
    else:
        raise HTTPException(status_code=404, detail=result["message"])

