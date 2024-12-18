
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.test_suite_crud import create_test_suite, get_test_suites, get_test_suite, update_test_suite, delete_test_suite
from app.schemas.test_suite_schema import TestSuiteCreate, TestSuiteResponse, TestSuiteUpdate
from app.database import get_db

router = APIRouter(
    prefix="/test_suites",
    tags=["Test Suites"]
)

@router.post("/", response_model=TestSuiteResponse)
def create_test_suite_route(test_suite: TestSuiteCreate, db: Session = Depends(get_db)):
    return create_test_suite(
        db=db,
        name=test_suite.name,
        description=test_suite.description
    )

@router.get("/", response_model=list[TestSuiteResponse])
def read_test_suites(db: Session = Depends(get_db)):
    return get_test_suites(db=db)

@router.get("/{test_suite_id}", response_model=TestSuiteResponse)
def read_test_suite(test_suite_id: int, db: Session = Depends(get_db)):
    response = get_test_suite(db=db, test_suite_id=test_suite_id)
    return response


@router.put("/{test_suite_id}", response_model=TestSuiteResponse)
def update_suite(test_suite_id: int, test_suite_update: TestSuiteUpdate, db: Session = Depends(get_db)):
    response = update_test_suite(
        db=db,
        test_suite_id= test_suite_id,
        name = test_suite_update.name,
        status=test_suite_update.status,
        description=test_suite_update.description
    )
    if response:
        return response
    elif response == {}:
        raise Exception("Test Suit not found with id: {}".format(test_suite_id))

@router.delete("/{test_suite_id}")
def delete_suite(test_suite_id: int, db: Session = Depends(get_db)):
    return delete_test_suite(
        db=db,
        test_suite_id= test_suite_id
    )
