from sqlalchemy.orm import Session
from models import Well


class WellRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_well_record(self, id_well: int, id_tag: int, tag_val: str, date_time):
        new_record = Well(
            id_well=id_well,
            id_tag=id_tag,
            tag_val=tag_val,
            date_time=date_time
        )
        self.db.add(new_record)
        self.db.commit()
        self.db.refresh(new_record)
        return new_record

    def get_all_records(self):
        return self.db.query(Well).all()

    def get_records_by_well_id(self, id_well: int):
        return self.db.query(Well).filter(Well.id_well == id_well).all()

    def delete_well_by_id(self, id_well: int):
        records_to_delete = self.db.query(Well).filter(Well.id_well == id_well).all()
        if not records_to_delete:
            return False
        for record in records_to_delete:
            self.db.delete(record)
        self.db.commit()
        return True