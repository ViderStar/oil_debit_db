from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from repositories import WellRepository

class WellService:
    def __init__(self, repository: WellRepository):
        self.repository = repository

    def add_val(self, id_well: int, id_tag: int, tag_val: str, date_time: datetime):
        try:
            new_record = self.repository.create_well_record(
                id_well, id_tag, tag_val, date_time
            )
            return new_record
        except SQLAlchemyError as e:
            print(f"Ошибка при добавлении записи: {e}")
            return None

    def get_all_val(self):
        try:
            return self.repository.get_all_records()
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении записей: {e}")
            return []

    def get_val_by_well(self, id_well: int):
        try:
            records = self.repository.get_records_by_well_id(id_well)
            if not records:
                return None
            return records
        except SQLAlchemyError as e:
            print(f"Ошибка при чтении записей: {e}")
            return None

    def delete_well(self, id_well: int):
        try:
            return self.repository.delete_well_by_id(id_well)
        except SQLAlchemyError as e:
            print(f"Ошибка при удалении записи: {e}")
            return None