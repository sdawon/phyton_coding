from sqlalchemy import select
from sqlalchemy.orm import Session

from models.project import Project


class ProjectRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(
        self, 
        name: str, 
        professor_id: int, 
        organization: str | None = None, 
        project_type: str | None = None
    ) -> Project:
        project = Project(
            name=name.strip(),
            professor_id=professor_id,
            organization=organization.strip() if organization else None,
            project_type=project_type.strip() if project_type else None,
        )
        self.session.add(project)
        self.session.flush()
        return project

    def get_by_id(self, project_id: int) -> Project | None:
        return self.session.get(Project, project_id)

    def list_all_by_professor(self, professor_id: int) -> list[Project]:
        """특정 교수님의 모든 과제 목록을 조회합니다."""
        statement = select(Project).where(Project.professor_id == professor_id).order_by(Project.created_at.desc())
        return list(self.session.scalars(statement))

    def update(
        self,
        project: Project,
        name: str | None = None,
        organization: str | None = None,
        project_type: str | None = None,
    ) -> Project:
        if name:
            project.name = name.strip()
        if organization:
            project.organization = organization.strip()
        if project_type:
            project.project_type = project_type.strip()
        
        self.session.flush()
        return project

    def delete(self, project: Project) -> None:
        self.session.delete(project)
        self.session.flush()
