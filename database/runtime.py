from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from config.settings import DATABASE_PATH
from database.connection import create_session_factory, create_sqlite_engine
from database.migrations import run_migrations

engine: Engine = create_sqlite_engine(DATABASE_PATH)
SessionFactory: sessionmaker[Session] = create_session_factory(engine)


def initialize_database() -> int:
    return run_migrations(engine)
