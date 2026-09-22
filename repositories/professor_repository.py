from sqlalchemy import select
from sqlalchemy.orm import Session

from models.professor import Professor


class ProfessorRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, name: str, department: str | None = None) -> Professor:
        professor = Professor(
            name=name.strip(),
            department=department.strip() if department else None,
        )
        self.session.add(professor)
        self.session.flush()
        return professor

    def get_by_id(self, professor_id: int) -> Professor | None:
        return self.session.get(Professor, professor_id)

    def get_by_name(self, name: str) -> Professor | None:
        return self.session.scalar(
            select(Professor).where(Professor.name == name.strip())
        )

    def list_all(self, active_only: bool = True) -> list[Professor]:
        statement = select(Professor).order_by(Professor.name)

        if active_only:
            statement = statement.where(Professor.is_active.is_(True))

        return list(self.session.scalars(statement))

    def update(
        self,
        professor: Professor,
        name: str,
        department: str | None = None,
    ) -> Professor:
        professor.name = name.strip()
        professor.department = department.strip() if department else None
        self.session.flush()
        return professor

    def set_active(
        self,
        professor: Professor,
        is_active: bool,
    ) -> Professor:
        professor.is_active = is_active
        self.session.flush()
        return professor
