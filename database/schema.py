from sqlalchemy.engine import Engine

from database.base import Base
from models.schema_version import SchemaVersion  # noqa: F401
from models.professor import Professor  # noqa: F401


def create_all_tables(engine: Engine) -> None:
    Base.metadata.create_all(engine)
