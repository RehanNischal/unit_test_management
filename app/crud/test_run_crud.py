from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.test_run_model import TestRun
from datetime import datetime
from app import constants
from app.crud.test_suite_crud import validate_test_suite_id

# CRUD operations for Test Run

# method to create new test run
# If the test_suite_id does not exist then it will raise exception
def create_test_run(db: Session, test_suite_id: int, run_status: str):
    if not validate_test_suite_id(db, test_suite_id):
        raise HTTPException(
            status_code=400,
            detail=f"Test Suite with id {test_suite_id} does not exist"
        )
    db_test_run = TestRun(test_suite_id=test_suite_id, run_status=run_status, start_time=datetime.utcnow())
    db.add(db_test_run)
    db.commit()
    db.refresh(db_test_run)
    return db_test_run

# method to create new test run
def get_test_runs(db: Session):
    return db.query(TestRun).filter(TestRun.test_suite_id.isnot(None)).all()

# method to get all test runs
def get_test_run(db: Session, test_run_id: int):
    return db.query(TestRun).filter(TestRun.id == test_run_id).first()

# method to update a test run
def update_test_run(db: Session, test_run_id: int, result: str, end_time: datetime, status: str):
    db_test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    if db_test_run:
        db_test_run.result = result
        db_test_run.end_time = end_time
        db_test_run.run_status = status
        db.commit()
        db.refresh(db_test_run)
        return db_test_run
    else:
        return {}

# method to delete a test run
def delete_test_run(db: Session, test_run_id: int):
    test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    if test_run:
        db.delete(test_run)
        db.commit()
        return {"message": constants.TEST_RUN_SUCCESSFUL_DELETION_MESSAGE, "id": test_run.id}
    else:
        return {"message": constants.TEST_RUN_NOT_FOUND, "id": test_run_id}