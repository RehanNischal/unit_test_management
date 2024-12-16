from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import create_test_suite, get_test_suites, get_test_suite
from app.schemas import TestSuiteCreate, TestSuiteResponse
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
    return get_test_suite(db=db, test_suite_id=test_suite_id)
