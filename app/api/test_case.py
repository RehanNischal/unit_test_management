from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import create_test_case, get_test_cases, get_test_case, update_test_case, delete_test_case
from app.schemas import TestCaseCreate, TestCaseResponse, TestCaseUpdate
from app.database import get_db

router = APIRouter(
    prefix="/test_cases",
    tags=["Test Cases"]
)

@router.post("/", response_model=TestCaseResponse)
def create_test_case_route(test_case: TestCaseCreate, db: Session = Depends(get_db)):
    return create_test_case(
        db=db,
        name=test_case.name,
        description=test_case.description,
        test_suite_id=test_case.test_suite_id,
        priority=test_case.priority,
        expected_outcome=test_case.expected_outcome
    )

@router.get("/", response_model=list[TestCaseResponse])
def read_test_cases(test_suite_id: int, db: Session = Depends(get_db)):
    return get_test_cases(db=db, test_suite_id=test_suite_id)

@router.get("/{test_case_id}", response_model=TestCaseResponse)
def read_test_case(test_case_id: int, db: Session = Depends(get_db)):
    return get_test_case(db=db, test_case_id=test_case_id)

@router.put("/{test_case_id}", response_model=TestCaseResponse)
def update_case(test_case_id: int, test_case_update: TestCaseUpdate, db: Session = Depends(get_db)):
    response = update_test_case(
        db = db,
        test_case_id = test_case_id,
        name = test_case_update.name,
        priority = test_case_update.priority,
        description = test_case_update.description,
        expected_outcome = test_case_update.expected_outcome)
    if response:
        return response
    elif response == {}:
        raise Exception("Test Case not found with id: {}".format(test_case_id))

@router.delete("/{test_case_id}")
def delete_suite(test_case_id: int, db: Session = Depends(get_db)):
    return delete_test_case(
        db=db,
        test_case_id= test_case_id
    )