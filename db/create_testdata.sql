USE TREFFPUNKT_DB;

INSERT INTO USER (USER_FIRSTNAME, USER_SURNAME, USER_BIRTHDATE, USER_USERNAME, USER_EMAIL, USER_PASSWORD, USER_GENDER, USER_REGION)
VALUES ('Heinz', 'Müller', '1960-04-22', 'heinz60', 'heinz.mueller@example.de', 'e8c8a7411cc909f99144119279aff1976ea26ef280865a6d0a5530b868e7ca2d', 1, 6838),
    ('Sabrina', 'Koch', '1985-11-05', 'sabrina85', 'sabrina.koch@example.de', 'a87d7121b63cf024edd392ec4e575098da9f6c1d037c7d75fa2db05b1ac3270d', 2, 6838),
    ('Lukas', 'Schmidt', '2001-09-14', 'lukas01', 'lukas.schmidt@example.de', 'cf39f19dc92440bede7cca24f81ceab3d2c7d416dee957a90fc1ad9a65c7f986', 1, 406),
    ('Emilia', 'Fischer', '2005-03-28', 'emilia05', 'emilia.fischer@example.de', 'c10df7304cc1b1bd913e7359dc21ec1c58dbf187a4716cd255dab73a724e114f', 2, 406);