from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app

from database.session import get_db
from database.db import Base
import pytest


TEST_DATABASE_URL = (
    "postgresql://postgres:Priyansh123"
    "@localhost:5432/payflow_test"
)

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db():

    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()


@pytest.fixture(scope="function")
def db_session():

    Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield db

    db.close()