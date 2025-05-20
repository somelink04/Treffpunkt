from db_entities import *
from sqlalchemy import text

#Create Session
engine = create_engine("mysql+pymysql://treffpunkt:b55tQKAc0z2K0hluWSo7Zxq2cMs9pTgx@localhost/TREFFPUNKT_DB")
Session = sessionmaker(bind=engine)


def add_user(firstname, surname, birthday, username, email, password, gender, region):
    """
    Add a new user to the database.
    :param firstname: First name of new user
    :param surname: Last name of new user
    :param birthday: Birthday of new user
    :param username: User name of new user
    :param email: email of new user
    :param password: password of new user (hashed)
    :param gender: ID of gender -> mapped table
    :param region: ID of region -> mapped table
    """
    with Session() as session:
        new_user = User()
        new_user.USER_FIRSTNAME = firstname
        new_user.USER_SURNAME = surname
        new_user.USER_BIRTHDATE = birthday
        new_user.USER_USERNAME = username
        new_user.USER_EMAIL = email
        new_user.USER_PASSWORD = password
        new_user.USER_GENDER = gender
        new_user.USER_REGION = region
        session.add(new_user)
        session.commit()

def delete_user_by_id(user_id):
    """
    Delete a user from the database.
    :param user_id: id of user to delete
    """
    with Session() as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            print(f"Deleted user with ID {user_id}")
        else:
            print(f"No user found with ID {user_id}")


def get_all_user_auth ():
    """
    Gets all users auth data from the database.
    :return: List of all users with username and passwords (User object --> access with User.USER_USERNAME and User.USER_PASSWORD)
    """
    with Session() as session:
        user_auth = session.query(User).with_entities(User.USER_USERNAME, User.USER_PASSWORD).all()

    return user_auth

#Alternativ: Einzelner User?
def get_user_auth(user_name):
    """
    Gets one user auth data from the database.
    :return: The Password of the User if existent, None otherwise
    """
    with Session() as session:
        user_auth_one_user = session.query(User).with_entities(User.USER_PASSWORD).filter_by(USER_USERNAME=user_name).first()
        if user_auth_one_user:
            return user_auth_one_user.USER_PASSWORD
        else:
            print ("No User with this Username in DB.")
            return None



#ohne passwort? Gleich hier raus oder handelt back?
def get_user (user_id):
    """
    :param user_id: ID of the searched User
    :return: The searched user (User object)
    """
    with Session() as session:
        user = session.query(User).filter_by(USER_ID=user_id).first()
        if user:
            return user
        else:
            print ("No User with this ID in DB.")
            return None

def get_all_users ():
    """
    :return: list of all users
    """
    with Session() as session:
        user = session.query(User).all()
        return user


#Get User_Settings
#--TODO
'''
#hä? lieber einzeln holen? ist sonst schon recht convoluted ;D 
def get_user_settings (user_id):
 #loopen
    with Session() as session:
        user_region = session.query(User).with_entities(User.USER_REGION).filter_by(USER_ID=user_id).first()
        user_hour = session.query(UserTime).with_entities (UserTime.HOUR_USER_TIME_ID).filter_by(USER_USER_TIME_ID=user_id).all()
        print (user_region)
        for entity in user_hour:
            print (entity)
        user_weekday_ids = session.query(UserTime).with_entities (UserTime.WEEKDAY_USER_TIME_ID).filter_by(USER_USER_TIME_ID=user_id).all()
        user_category_ids = session.query(UserCategory).with_entities(UserCategory.CATEGORY_USER_CATEGORY_ID).filter_by(USER_USER_CATEGORY_ID=user_id).all()
        for user_weekday_ids in user_weekday_ids:
            user_weekday = session.query(Hour).filter_by(USER_HOUR_USER_TIME_ID=user_weekday_ids).all()
        for user_category_ids in user_category_ids:
            user_category_ = session.query(Weekday).filter_by(USER_WEEDAY_USER_TIME_ID=user_weekday_ids).all()

'''
#Write User_Settings - evtl auch einzeln
#--TODO

#Write New_Event
#--TODO

#Get Events
#--TODO
