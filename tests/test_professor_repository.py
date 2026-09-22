from pathlib import Path

from database.connection import create_session_factory, create_sqlite_engine
from database.migrations import run_migrations
from repositories.professor_repository import ProfessorRepository


def make_session_factory(tmp_path: Path):
    engine = create_sqlite_engine(tmp_path / "test.db")
    run_migrations(engine)
    return engine, create_session_factory(engine)


def test_professor_crud(tmp_path: Path) -> None:
    engine, session_factory = make_session_factory(tmp_path)

    with session_factory.begin() as session:
        repository = ProfessorRepository(session)
        professor = repository.create("테스트 교수", "테스트 학과")
        professor_id = professor.id

    with session_factory.begin() as session:
        repository = ProfessorRepository(session)
        professor = repository.get_by_id(professor_id)

        assert professor is not None
        repository.update(professor, "수정 교수", "수정 학과")

    with session_factory() as session:
        repository = ProfessorRepository(session)
        professor = repository.get_by_name("수정 교수")

        assert professor is not None
        assert professor.department == "수정 학과"

    engine.dispose()


def test_inactive_professor_is_excluded_by_default(tmp_path: Path) -> None:
    engine, session_factory = make_session_factory(tmp_path)

    with session_factory.begin() as session:
        repository = ProfessorRepository(session)
        active = repository.create("활성 교수")
        inactive = repository.create("비활성 교수")
        repository.set_active(inactive, False)

    with session_factory() as session:
        repository = ProfessorRepository(session)

        assert [item.name for item in repository.list_all()] == ["활성 교수"]
        assert len(repository.list_all(active_only=False)) == 2

    engine.dispose()
