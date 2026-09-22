from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    organization: Mapped[str | None] = mapped_column(String(200), nullable=True)  # 지원기관 (예: 한국연구재단)
    project_type: Mapped[str | None] = mapped_column(String(100), nullable=True)  # 과제유형 (예: 정부과제)
    
    # 외래키: 어떤 교수님의 과제인지 연결
    professor_id: Mapped[int] = mapped_column(ForeignKey("professors.id"), nullable=False)
    
    # Relationship: 교수님 객체와 연결
    professor: Mapped["Professor"] = relationship("Professor", back_populates="projects")

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
