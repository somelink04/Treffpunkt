USE TREFFPUNKT_DB;

INSERT INTO USER(USER_FIRSTNAME, USER_SURNAME, USER_BIRTHDATE, USER_USERNAME, USER_EMAIL, USER_PASSWORD, USER_GENDER, USER_REGION)
VALUES ('Heinz', 'Müller', '1960-04-22', 'heinz60', 'heinz.mueller@example.de', 'e8c8a7411cc909f99144119279aff1976ea26ef280865a6d0a5530b868e7ca2d', 1, 6838),
    ('Sabrina', 'Koch', '1985-11-05', 'sabrina85', 'sabrina.koch@example.de', 'a87d7121b63cf024edd392ec4e575098da9f6c1d037c7d75fa2db05b1ac3270d', 2, 6838),
    ('Lukas', 'Schmidt', '2001-09-14', 'lukas01', 'lukas.schmidt@example.de', 'cf39f19dc92440bede7cca24f81ceab3d2c7d416dee957a90fc1ad9a65c7f986', 1, 406),
    ('Emilia', 'Fischer', '2005-03-28', 'emilia05', 'emilia.fischer@example.de', 'c10df7304cc1b1bd913e7359dc21ec1c58dbf187a4716cd255dab73a724e114f', 2, 406),
	('Voyager', 'I', '1977-09-05', 'voyageri', 'voyager@outer.space', '9d9078a2ca94a536bd0279f6192bbf5f8718fb18df4c0eeec506273bcce955f4', 3, 406),
	('Voyager', 'II', '1977-08-20', 'voyagerii', 'voyager@solar.sys', '0a62ab1d8d4c2ce4094d29df516cd24b84038ec15eae9bbb168f2e3731bcfc38', 3, 406),
	('Saturn', 'V', '1969-07-20', 'saturnv', 'saturnv@the.moon', '4bfcb47557d126921fa05360316f12ac29ac9bbaee002d70d2deed4235a232e7', 3, 406),
	('Hubble Space', 'Telescope', '1990-04-24', 'hubble', 'hubble@space.tele', '18d9486f99df32c58605e574ffae3773efe42294e95a1577c52a6f5d987ad44f', 3, 406);

INSERT INTO EVENT(EVENT_TIME, EVENT_REGION, EVENT_CATEGORY)
VALUES  ('2025-06-16 14:30:00', 1, 2),
        ('2025-06-17 10:00:00', 2, 3),
        ('2025-06-18 08:15:00', 3, 1);
INSERT INTO USER_EVENT(USER_USER_EVENT_ID, EVENT_USER_EVENT_ID, USER_EVENT_ZUSAGE)
VALUES
	/*Alle sagen ab beim ersten event*/
	(1, 1, FALSE),
	(2, 1, FALSE),
	(3, 1, FALSE),
	(4, 1, FALSE),
	(5, 1, FALSE),
	(6, 1, FALSE),
	(7, 1, FALSE),
	/*Alle stimmen zweitem event zu */
	(1, 2, TRUE),
	(2, 2, TRUE),
	(3, 2, TRUE),
	(4, 2, TRUE),
	(5, 2, TRUE),
	(6, 2, TRUE),
	(7, 2, TRUE),
	/*Gemischt und enthaltungen*/
    (1, 3, FALSE),
    (3, 3, FALSE),
    (5, 3, FALSE),
    (6, 3, TRUE),
    (7, 3, FALSE);

