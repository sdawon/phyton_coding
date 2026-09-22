from pathlib import Path

from database.connection import create_session_factory, create_sqlite_engine
from database.migrations import run_migrations
from models.professor import Professor
from models.project import Project
from repositories.professor_repository import ProfessorRepository
from repositories.project_repository import ProjectRepository


def make_session_factory(tmp_path: Path):
    engine = create_sqlite_engine(tmp_path / "test.db")
    run_migrations(engine)
    return engine, create_session_factory(engine)


def test_project_crud(tmp_path: Path) -> None:
    engine, session_factory = make_session_factory(tmp_path)

    # 1. 데이터 준비 (교수님 생성)
    with session_factory.begin() as session:
        prof_repo = ProfessorRepository(session)
        project_repo = ProjectRepository(session)
        
        professor = prof_repo.create("김교수", "컴퓨터공학부")
        professor_id = professor.id

        # 2. 과제 생성
        project = project_repo.create(
            name="AI 연구 과제", 
            professor_id=professor_id, 
            organization="한국연구재단",
            project_type="정부과제"
        )
        project_id = project.id

    # 3. 조회 및 수정 테스트
    with session_factory() as session:
        project_repo = ProjectRepository(session)
        
        retrieved = project_repo.get_by_id(project_id)
        assert retrieved is not None
        assert retrieved.name == "AI 연구 과제"

        project_repo.update(retrieved, name="업데이트된 과제")
        
        updated = project_repo.get_by_id(project_id)
        assert updated.name == "업데이트된 과제"

    # 4. 교수님별 과제 목록 조회 테스트
    with session_factory() as session:
        project_repo = ProjectRepository(session)
        prof_repo = ProfessorRepository(session)
        
        # 두 번째 과제 추가
        professor = prof_repo.get_by_id(professor_id)
        project_repo.create("두번째 과제", professor.id)

        projects = project_repo.list_all_by_professor(professor_id)
        assert len(projects) == 2

    engine.dispose()
