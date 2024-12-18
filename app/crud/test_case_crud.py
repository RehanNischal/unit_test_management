from sqlalchemy.orm import Session
from app.models.test_case_model import TestCase
from app import constants
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
    if db_test_case:
        db_test_case.name = name
        db_test_case.description = description
        db_test_case.priority = priority
        db_test_case.expected_outcome = expected_outcome
        db.commit()
        db.refresh(db_test_case)
        return db_test_case
    else:
        return {}

def delete_test_case(db: Session, test_case_id: int):
    test_case = db.query(TestCase).filter(TestCase.id == test_case_id).first()
    if test_case:
        db.delete(test_case)
        db.commit()
        return {"message": constants.TEST_CASE_SUCCESSFUL_DELETION_MESSAGE, "id": test_case.id}
    else:
        return {"message": constants.TEST_CASE_NOT_FOUND, "id": test_case_id}

def search_test_cases(db: Session, keyword: str):
    print("keyword: "+keyword)
    keyword_filter = f"%{keyword}%"
    test_cases = db.query(TestCase).filter(
        ((TestCase.name.ilike(keyword_filter)) | (TestCase.description.ilike(keyword_filter))) &
        (TestCase.test_suite_id.isnot(None))
    ).all()

    if test_cases:
        return test_cases
    else:
        return []

