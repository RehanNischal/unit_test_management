from sqlalchemy.orm import Session
from app.models import TestCase, TestSuite, TestRun
from datetime import datetime

# CRUD operations for Test Suite
def create_test_suite(db: Session, name: str, description: str):
    db_test_suite = TestSuite(name=name, description=description)
    db.add(db_test_suite)
    db.commit()
    db.refresh(db_test_suite)
    return db_test_suite

def get_test_suites(db: Session):
    return db.query(TestSuite).all()

def get_test_suite(db: Session, test_suite_id: int):
    return db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()

def update_test_suite(db: Session, test_suite_id: int, name: str, status: str, description: str):
    db_test_suite = db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()
    db_test_suite.status = status
    db_test_suite.name = name
    db_test_suite.description = description
    db.commit()
    db.refresh(db_test_suite)
    return db_test_suite

# CRUD operations for Test Case
def create_test_case(db: Session, name: str, description: str, test_suite_id: int, priority: str, expected_outcome: str):
    db_test_case = TestCase(name=name, description=description, test_suite_id=test_suite_id, priority=priority, expected_outcome=expected_outcome)
    db.add(db_test_case)
    db.commit()
    db.refresh(db_test_case)
    return db_test_case

def get_test_cases(db: Session, test_suite_id: int):
    return db.query(TestCase).filter(TestCase.test_suite_id == test_suite_id).all()

def get_test_case(db: Session, test_case_id: int):
    return db.query(TestCase).filter(TestCase.id == test_case_id).first()

def update_test_case(db: Session, test_case_id: int, name: str, description: str, priority: str, expected_outcome: str):
    db_test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    db_test_case.name = name
    db_test_case.description = description
    db_test_case.priority = priority
    db_test_case.expected_outcome = expected_outcome
    db.commit()
    db.refresh(db_test_case)
    return db_test_case

# CRUD operations for Test Run
def create_test_run(db: Session, test_suite_id: int, run_status: str):
    db_test_run = TestRun(test_suite_id=test_suite_id, run_status=run_status, start_time=datetime.utcnow())
    db.add(db_test_run)
    db.commit()
    db.refresh(db_test_run)
    return db_test_run

def get_test_runs(db: Session):
    return db.query(TestRun).all()

def get_test_run(db: Session, test_run_id: int):
    return db.query(TestRun).filter(TestRun.id == test_run_id).first()

def update_test_run(db: Session, test_run_id: int, result: str, end_time: datetime, test_results: list):
    db_test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    db_test_run.result = result
    db_test_run.end_time = end_time
    db_test_run.test_results = test_results
    db.commit()
    db.refresh(db_test_run)
    return db_test_run

def delete_test_run(db: Session, test_run_id: int):
    test_run = db.query(TestRun).filter(TestRun.id == test_run_id).first()
    if test_run:
        db.delete(test_run)
        db.commit()
        return {"message": "Test run deleted successfully", "id": test_run.id}
    else:
        return {"message": "Test run not found", "id": test_run_id}