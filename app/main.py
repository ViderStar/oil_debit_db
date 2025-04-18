import datetime
from database import Base, engine, get_db
from services import WellService
from repositories import WellRepository

def main():
    Base.metadata.create_all(bind=engine)

    with next(get_db()) as db:
        well_repository = WellRepository(db)
        well_service = WellService(well_repository)

        well_service.add_val(id_well=101, id_tag=10, tag_val="Value1", date_time=datetime.datetime.now())
        well_service.add_val(id_well=101, id_tag=11, tag_val="Value2", date_time=datetime.datetime.now())
        well_service.add_val(id_well=102, id_tag=10, tag_val="Value3", date_time=datetime.datetime.now())

        all_vals = well_service.get_all_val()
        print("Все замеры:")
        for v in all_vals:
            print(v.id, v.id_well, v.id_tag, v.tag_val, v.date_time)

        well_101_vals = well_service.get_val_by_well(101)
        print("\nЗамеры по скважине 101:")
        if well_101_vals is None:
            print("Скважина не найдена!")
        else:
            for w in well_101_vals:
                print(w.id, w.id_well, w.id_tag, w.tag_val, w.date_time)

        delete_result = well_service.delete_well(101)
        print("\nРезультат удаления:", delete_result)

        well_101_vals_after_delete = well_service.get_val_by_well(101)
        print("Состояние после удаления:", well_101_vals_after_delete)


if __name__ == "__main__":
    main()