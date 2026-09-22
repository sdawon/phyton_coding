from pathlib import Path

from sqlalchemy import func, select

from database.connection import create_session_factory, create_sqlite_engine
from database.migrations import CURRENT_SCHEMA_VERSION, run_migrations
from models.schema_version import SchemaVersion


def test_initial_migration_records_version(tmp_path: Path) -> None:
    engine = create_sqlite_engine(tmp_path / "test.db")

    version = run_migrations(engine)

    assert version == CURRENT_SCHEMA_VERSION
    engine.dispose()


def test_migration_is_idempotent(tmp_path: Path) -> None:
    engine = create_sqlite_engine(tmp_path / "test.db")

    run_migrations(engine)
    run_migrations(engine)

    session_factory = create_session_factory(engine)
    with session_factory() as session:
        count = session.scalar(
            select(func.count()).select_from(SchemaVersion)
        )

    assert count == 1
    engine.dispose()
