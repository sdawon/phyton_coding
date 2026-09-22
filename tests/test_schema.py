from pathlib import Path

from sqlalchemy import inspect, select

from database.connection import create_session_factory, create_sqlite_engine
from database.schema import create_all_tables
from models.schema_version import SchemaVersion


def test_schema_version_table_is_created(tmp_path: Path) -> None:
    engine = create_sqlite_engine(tmp_path / "test.db")
    create_all_tables(engine)

    assert "schema_versions" in inspect(engine).get_table_names()
    engine.dispose()


def test_schema_version_can_be_saved(tmp_path: Path) -> None:
    engine = create_sqlite_engine(tmp_path / "test.db")
    create_all_tables(engine)
    session_factory = create_session_factory(engine)

    with session_factory.begin() as session:
        session.add(SchemaVersion(version=1))

    with session_factory() as session:
        saved = session.scalar(
            select(SchemaVersion).where(SchemaVersion.version == 1)
        )

    assert saved is not None
    assert saved.version == 1
    engine.dispose()
