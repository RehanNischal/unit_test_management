from sqlalchemy.orm import Session
from app.models.test_run_model import TestRun
from datetime import datetime
from app import constants

# CRUD operations for Test Run
def create_test_run(db: Session, test_suite_id: int, run_status: str):
    db_test_run = TestRun(test_suite_id=test_suite_id, run_status=run_status, start_time=datetime.utcnow())
    db.add(db_test_run)
    db.commit()
    db.refresh(db_test_run)
    return db_test_run

def get_test_runs(db: Session):
    return db.query(TestRun).filter(TestRun.test_suite_id.isnot(None)).all()


def get_test_run(db: Session, test_run_id: int):
    return db.query(TestRun).filter(TestRun.id == test_run_id).first()

def update_test_run(db: Session, test_run_id: int, result: str, end_time: datetime, test_results: list):
    db_test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    if db_test_run:
        db_test_run.result = result
        db_test_run.end_time = end_time
        db_test_run.test_results = test_results
        db.commit()
        db.refresh(db_test_run)
        return db_test_run
    else:
        return {}

def delete_test_run(db: Session, test_run_id: int):
    test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    if test_run:
        db.delete(test_run)
        db.commit()
        return {"message": constants.TEST_RUN_SUCCESSFUL_DELETION_MESSAGE, "id": test_run.id}
    else:
        return {"message": constants.TEST_RUN_NOT_FOUND, "id": test_run_id}