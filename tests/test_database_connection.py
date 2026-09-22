from pathlib import Path

from sqlalchemy import text

from database.connection import create_session_factory, create_sqlite_engine


def test_database_file_is_created(tmp_path: Path) -> None:
    db_path = tmp_path / "test.db"
    engine = create_sqlite_engine(db_path)

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    engine.dispose()
    assert db_path.exists()


def test_foreign_keys_are_enabled(tmp_path: Path) -> None:
    engine = create_sqlite_engine(tmp_path / "test.db")

    with engine.connect() as connection:
        result = connection.execute(text("PRAGMA foreign_keys")).scalar_one()

    engine.dispose()
    assert result == 1


def test_session_factory_creates_session(tmp_path: Path) -> None:
    engine = create_sqlite_engine(tmp_path / "test.db")
    session_factory = create_session_factory(engine)

    with session_factory() as session:
        result = session.execute(text("SELECT 1")).scalar_one()

    engine.dispose()
    assert result == 1
