\i schema_drop.sql

CREATE TABLE IF NOT EXISTS Patients(
	CPR_number integer PRIMARY KEY,
    name varchar(200),
    password varchar(200),
    address text
);

CREATE TABLE IF NOT EXISTS HbA1c_results(
    test_id SERIAL PRIMARY KEY,
    result float,
    date_of_test date,
    CPR_number integer REFERENCES Patients(CPR_number)
);

