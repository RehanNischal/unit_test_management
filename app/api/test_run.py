
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.test_run_crud import create_test_run, get_test_runs, get_test_run, update_test_run, delete_test_run
from app.schemas.test_run_schema import TestRunCreate, TestRunResponse, TestRunUpdate
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
    response = update_test_run(
        db=db, test_run_id=test_run_id,
        result=test_run_update.result,
        end_time=test_run_update.end_time,
        status=test_run_update.run_status
    )
    if response:
        return response
    elif response == {}:
        raise Exception("Test Run not found with id: {}".format(test_run_id))


@router.delete("/{test_run_id}")
def delete_run(test_run_id: int, db: Session = Depends(get_db)):
    return delete_test_run(db=db, test_run_id=test_run_id)


