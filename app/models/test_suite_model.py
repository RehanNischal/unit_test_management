from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class TestSuite(Base):
    __tablename__ = "test_suites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(String, default="active")

    ## All the Test Runs and Test Cases will be deleted automatically if the corresponding suite gets deleted
    # A TestSuite can have many TestCases (One to Many)
    test_cases = relationship("TestCase", back_populates="test_suite", cascade="all, delete")
    # A TestSuite can have many TestRuns (One to Many)
    test_runs = relationship("TestRun", back_populates="test_suite", cascade="all, delete")