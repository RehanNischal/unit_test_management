from sqlalchemy.orm import Session
from app.models.test_suite_model import TestSuite
from app import constants

# CRUD operations for Test Suite

# method to create new test suit
def create_test_suite(db: Session, name: str, description: str):
    db_test_suite = TestSuite(name=name, description=description)
    db.add(db_test_suite)
    db.commit()
    db.refresh(db_test_suite)
    return db_test_suite

# method to get all suites
def get_test_suites(db: Session):
    return db.query(TestSuite).all()

# method to get a single suite
def get_test_suite(db: Session, test_suite_id: int):
    return db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()

# method to update a test suite
def update_test_suite(db: Session, test_suite_id: int, name: str, status: str, description: str):
    db_test_suite = db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()
    if db_test_suite:
        db_test_suite.status = status
        db_test_suite.name = name
        db_test_suite.description = description
        db.commit()
        db.refresh(db_test_suite)
        return db_test_suite
    else:
        return {}

# method to delete a test suite
def delete_test_suite(db: Session, test_suite_id: int):
    test_suite = db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()
    if test_suite:
        db.delete(test_suite)
        db.commit()
        return {"message": constants.TEST_SUIT_SUCCESSFUL_DELETION_MESSAGE, "id": test_suite.id}
    else:
        return {"message": constants.TEST_SUIT_NOT_FOUND, "id": test_suite_id}

# method to check if a test_suite_id is valid
def validate_test_suite_id(db: Session, test_suite_id: int):
    test_suite = db.query(TestSuite).filter(TestSuite.id == test_suite_id).first()
    if not test_suite:
        return False
    return True
