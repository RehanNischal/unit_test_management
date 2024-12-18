from app.crud import test_case_crud, test_run_crud, test_suite_crud
from app.database import SessionLocal
from datetime import datetime

def test_create_test_run():
    db = SessionLocal()
    test_run = test_run_crud.create_test_run(db=db, test_suite_id=1, run_status="in_progress")
    assert test_run.run_status == "in_progress"
    db.close()

def test_update_test_run():
    db = SessionLocal()
    test_run = test_run_crud.create_test_run(db=db, test_suite_id=1, run_status="in_progress")
    updated_test_run = test_run_crud.update_test_run(
        db=db, test_run_id=test_run.id, result="completed",
        end_time=datetime.utcnow(), test_results=[{"test_case_id": 1, "status": "pass"}]
    )
    assert updated_test_run.result == "completed"
    db.close()
