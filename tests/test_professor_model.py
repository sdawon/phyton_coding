from pathlib import Path

from sqlalchemy import inspect, select

from database.connection import create_session_factory, create_sqlite_engine
from database.migrations import run_migrations
from models.professor import Professor


def test_professor_can_be_saved(tmp_path: Path) -> None:
    engine = create_sqlite_engine(tmp_path / "test.db")
    run_migrations(engine)
    session_factory = create_session_factory(engine)

    with session_factory.begin() as session:
        session.add(Professor(name="테스트 교수", department="테스트 학과"))

    with session_factory() as session:
        professor = session.scalar(
            select(Professor).where(Professor.name == "테스트 교수")
        )

    assert professor is not None
    assert professor.department == "테스트 학과"
    assert professor.is_active is True
    engine.dispose()


def test_professor_table_is_created(tmp_path: Path) -> None:
    engine = create_sqlite_engine(tmp_path / "test.db")
    run_migrations(engine)

    assert "professors" in inspect(engine).get_table_names()
    engine.dispose()
