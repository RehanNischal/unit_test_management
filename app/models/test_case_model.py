from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    test_suite_id = Column(Integer, ForeignKey("test_suites.id", ondelete="CASCADE"))
    status = Column(String, default="active")
    priority = Column(String)
    expected_outcome = Column(String)

    # Relationship with TestSuite
    # Each TestCase belongs to one TestSuite
    test_suite = relationship("TestSuite", back_populates="test_cases")