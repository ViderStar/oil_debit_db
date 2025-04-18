import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.repositories import WellRepository
from app.services import WellService

TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="module")
def test_db():
    engine = create_engine(TEST_DATABASE_URL, echo=False)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    yield db
    db.close()

@pytest.fixture
def well_service(test_db):
    repository = WellRepository(test_db)
    service = WellService(repository)
    return service

def test_add_val(well_service):
    record = well_service.add_val(1, 10, "TestVal", datetime.now())
    assert record is not None
    assert record.id_well == 1
    assert record.id_tag == 10
    assert record.tag_val == "TestVal"

def test_get_all_val(well_service):
    all_vals = well_service.get_all_val()
    assert len(all_vals) > 0

def test_get_val_by_well_existing(well_service):
    records = well_service.get_val_by_well(1)
    assert records is not None
    assert len(records) > 0

def test_get_val_by_well_non_existing(well_service):
    records = well_service.get_val_by_well(9999)
    assert records is None

def test_delete_well(well_service):
    result = well_service.delete_well(1)
    assert result is True
    result_again = well_service.delete_well(1)
    assert result_again is False