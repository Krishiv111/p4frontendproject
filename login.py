from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
import json

class User:    

    def __init__(self, name, uid, classof, password, dob):
        self._name = name    # variables with self prefix become part of the object, 
        self._uid = uid
        self._classof = classof
        self.set_password(password)
        self._dob = dob
    
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
    # a getter method, extracts email from object
    @property
    def uid(self):
        return self._uid
    
    # a setter function, allows name to be updated after initial object creation
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, uid):
        return self._uid == uid
    
    @property
    def classof(self):
        return self._classof
    
    @classof.setter
    def classof(self, classof):
        self.classof = classof
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def dob(self):
        dob_string = self._dob.strftime('%m-%d-%Y')
        return dob_string
    
    # dob should be have verification for type date
    @dob.setter
    def dob(self, dob):
        self._dob = dob
        
    # age is calculated and returned each time it is accessed
    @property
    def age(self):
        today = date.today()
        return today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
    
    # dictionary is customized, removing password for security purposes
    @property
    def dictionary(self):
        dict = {
            "name" : self.name,
            "uid" : self.uid,
            "classof" : self.classof,
            "dob" : self.dob,
            "age" : self.age
        }
        return dict
    
    # update password, this is conventional setter
    def set_password(self, password):
        """Create a hashed password."""
        self._password = generate_password_hash(password, method='sha256')

    # check password parameter versus stored/encrypted password
    def is_password(self, password):
        """Check against hashed password."""
        result = check_password_hash(self._password, password)
        return result
    
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.dictionary)
    
    # output command to recreate the object, uses attribute directly
    def __repr__(self):
        return f'User(name={self._name}, uid={self._uid}, classof={self._classof} password={self._password},dob={self._dob})'
    

if __name__ == "__main__":
    u1 = User(name='Thomas Edison', uid='toby', classof='1867', password='123toby', dob=date(1847, 2, 11))
    print("JSON ready string:\n", u1, "\n") 
    print("Raw Variables of object:\n", vars(u1), "\n") 
    print("Raw Attributes and Methods of object:\n", dir(u1), "\n")
    print("Representation to Re-Create the object:\n", repr(u1), "\n") 