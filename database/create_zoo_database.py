import sqlite3


def create_species_table(cursor):
    create_query = '''create table if not exists
        species(
            species_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            life_expectancy INTEGER,
            food_type TEXT,
            gestation INTEGER,
            newborn_weight REAL,
            average_weight INTEGER,
            weight_age_ratio REAL,
            food_weight_ratio REAL
        )'''

    cursor.execute(create_query)


def create_zoos_table(cursor):
    create_query = '''create table if not exists
        zoos(
            zoo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            capacity INTEGER,
            budget REAL
        )'''

    cursor.execute(create_query)


def create_animals_table(cursor):
    create_query = '''create table if not exists
        animals(
            animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            weight REAL,
            is_alive INTEGER,
            time_after_last_birth INTEGER,
            species_id,
            zoo_id,
            FOREIGN KEY(species_id) REFERENCES species(species_id),
            FOREIGN KEY(zoo_id) REFERENCES zoos(zoo_id)
        )'''

    cursor.execute(create_query)


def insert_species_into_table(
    cursor, name, life_expectancy, food_type, gestation, newborn_weight,
    average_weight, weight_age_ratio, food_weight_ratio
):
    insert_query = '''insert into
        species(
            name, life_expectancy, food_type, gestation, newborn_weight,
            average_weight, weight_age_ratio, food_weight_ratio
        ) values(?, ?, ?, ?, ?, ?, ?, ?)
    '''

    cursor.execute(insert_query, (
        name, life_expectancy, food_type, gestation, newborn_weight,
        average_weight, weight_age_ratio, food_weight_ratio
    ))


def main():
    conn = sqlite3.connect("zoos.db")
    cursor = conn.cursor()

    create_species_table(cursor)
    create_zoos_table(cursor)
    create_animals_table(cursor)

    animals = [
        ("lion", 15, "carnivore", 3, 2, 200, 7.5, 0.035),
        ("tiger", 20, "carnivore", 4, 1, 250, 12, 0.06),
        ("red panda", 9, "herbivore", 4, 0.15, 5, 0.25, 1),
        ("kangaroo", 12, "herbivore", 9, 8, 50, 1.75, 0.1),
        ("koala", 15, "herbivore", 7, 1, 12, 0.5, 0.05),
        ("raccoon", 3, "herbivore", 2, 0.5, 7, 0.3, 0.35),
        ("baboon", 45, "herbivore", 6, 1, 41, 1, 0.074),
        ("impala", 15, "herbivore", 6, 1, 60, 0.33, 0.1),
        ("hippo", 45, "herbivore", 8, 30, 1500, 2.72, 25),
        ("cougar", 13, "carnivore", 3, 14, 80, 0.42, 0.075),
        ("goat", 18, "herbivore", 5, 5, 52, 0.217, 0.38)
    ]

    for animal in animals:
        insert_species_into_table(cursor, *animal)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
