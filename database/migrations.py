from sqlalchemy import func, select
from sqlalchemy.engine import Engine

from database.connection import create_session_factory
from database.schema import create_all_tables
from models.schema_version import SchemaVersion

CURRENT_SCHEMA_VERSION = 1


def run_migrations(engine: Engine) -> int:
    create_all_tables(engine)
    session_factory = create_session_factory(engine)

    with session_factory.begin() as session:
        latest_version = session.scalar(
            select(func.max(SchemaVersion.version))
        )

        if latest_version is None:
            session.add(SchemaVersion(version=CURRENT_SCHEMA_VERSION))
            return CURRENT_SCHEMA_VERSION

        if latest_version > CURRENT_SCHEMA_VERSION:
            raise RuntimeError(
                "데이터베이스 버전이 프로그램보다 높습니다."
            )

        return latest_version
