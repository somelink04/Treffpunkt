from db_api import *
import unittest
from db_entities import *
from sqlalchemy import text
import datetime
class Test(unittest.TestCase):
    """
    Issues/Questions:
    Should the function get user return a region id and zip and gender id etc? 
    When adding a user the id was set to 5 then 8 then 12 then 16 etc why not 5 again?
    """
    
    
    def setUp(self):
            delete_user_by_id(5)
    def tearDown(self):
            delete_user_by_id(5)
            
    def test_getting_users(self):
        
       
        """
        Check if all users with passwords are picked up
         """
        self.assertEqual(len(get_all_user_auth()), 4, "Four Users in test data")
        """
        Check if all users without the passwords are picked up
        """
        self.assertEqual(len(get_all_users()), 4,"Four test entries are needed")
        self.assertEqual(len(get_all_users()[0]),8, "Recieving 8 different Attributes excluding the password")
        
    def test_getting_specific_user(self):
        """
        Check if a password of a specific user is chosen correctly
        """
        self.assertEqual("e8c8a7411cc909f99144119279aff1976ea26ef280865a6d0a5530b868e7ca2d",str(get_user_auth("heinz60")), "Test password of User heinz60")
        
        """
        Check for information of a specific User (no password)
        """
        self.assertEqual((1, 'Heinz', 'Müller', datetime.date(1960, 4, 22), 'heinz60', 'heinz.mueller@example.de', 1, 6838, 1, 'männlich', 6838, 'Hannover', '30159'),get_user(1), "User hein60")
    def test_adding_and_deleting_users(self):
        add_user("bob","burger",datetime.date(1960, 4, 22),"bobby46","bobero@example.de","hashingishard",1,1)  
        delete_user_by_id(5)
  
delete_user_by_id(16)
print(get_all_users())
print("checkpoint")      
unittest.main()
 
    