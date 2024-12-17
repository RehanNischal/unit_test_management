from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, JSON
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

class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    test_suite_id = Column(Integer, ForeignKey("test_suites.id"))
    status = Column(String, default="active")
    priority = Column(String)
    expected_outcome = Column(String)

    # Relationship with TestSuite
    # Each TestCase belongs to one TestSuite
    test_suite = relationship("TestSuite", back_populates="test_cases")

class TestRun(Base):
    __tablename__ = "test_runs"

    id = Column(Integer, primary_key=True, index=True)
    test_suite_id = Column(Integer, ForeignKey("test_suites.id"))
    run_status = Column(String, default="in_progress")
    result = Column(String, default="pending")
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    test_results = Column(JSON, default=[])

    # Relationship with TestSuite
    # Each TestRun belongs to one TestSuite
    test_suite = relationship("TestSuite", back_populates="test_runs")
