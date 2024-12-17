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

    # Relationship with TestCase
    # A TestSuite can have many TestCases
    test_cases = relationship("TestCase", back_populates="test_suite")
    # A TestSuite can have many TestRuns
    test_runs = relationship("TestRun", back_populates="test_suite")