from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class TestRun(Base):
    __tablename__ = "test_runs"

    id = Column(Integer, primary_key=True, index=True)
    test_suite_id = Column(Integer, ForeignKey("test_suites.id", ondelete="CASCADE"))
    run_status = Column(String, default="in_progress")
    result = Column(String, default="pending")
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    test_results = Column(JSON, default=[])

    # Relationship with TestSuite
    # Each TestRun belongs to one TestSuite
    test_suite = relationship("TestSuite", back_populates="test_runs")