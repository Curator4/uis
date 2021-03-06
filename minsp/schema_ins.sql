
DELETE FROM Patients;
DELETE FROM HbA1c_results;

-- patient data
INSERT INTO public.Patients(cpr_number, name, password, address) VALUES (5000, 'patient1', 'UIS', 'address1');
INSERT INTO public.Patients(cpr_number, name, password, address) VALUES (5001, 'patient2', 'UIS', 'address2');
INSERT INTO public.Patients(cpr_number, name, password, address) VALUES (5002, 'patient3', 'UIS', 'address3');
INSERT INTO public.Patients(cpr_number, name, password, address) VALUES (5003, 'patient4', 'UIS', 'address4');

-- patient 1 test data
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (10.1, '2019-06-02', 5000);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (8.3, '2019-09-13', 5000);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (7.6, '2019-12-28', 5000);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (6.5, '2020-03-08', 5000);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (7.9, '2020-06-18', 5000);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (8.4, '2020-10-10', 5000);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (10.9, '2021-01-24', 5000);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (11.3, '2021-04-15', 5000);

-- patient 2 test data
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (8.9, '2019-01-09', 5001);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (7.5, '2019-03-12', 5001);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (10.1, '2019-08-18', 5001);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (11.3, '2020-01-31', 5001);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (8.9, '2020-03-01', 5001);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (7.4, '2020-04-01', 5001);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (8.3, '2021-01-01', 5001);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (9.2, '2021-03-01', 5001);

-- patient 3 test data
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (9.6, '2017-06-01', 5002);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (10.2, '2017-06-01', 5002);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (11.7, '2018-06-01', 5002);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (13.1, '2018-03-01', 5002);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (12.5, '2019-12-01', 5002);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (10.2, '2019-08-01', 5002);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (9.3, '2020-02-01', 5002);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (9.1, '2020-01-01', 5002);

-- patient 4 test data
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (5.6, '2019-09-03', 5003);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (6.3, '2019-12-27', 5003);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (6.8, '2020-03-15', 5003);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (6.9, '2020-06-23', 5003);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (7.3, '2020-09-09', 5003);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (8.2, '2020-12-11', 5003);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (10.1, '2021-03-13', 5003);
INSERT INTO public.HbA1c_results(result, date_of_test, CPR_number) VALUES (7.1, '2021-06-08', 5003);
