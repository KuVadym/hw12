from collections import UserDict
from datetime import datetime, timedelta
from fileinput import close
import re
import pickle

class Field():
    pass

class AddressBook(UserDict):
    def add_record (self,key, val):
        self.data.__setitem__(key, val)
    
    def iterator (self):
        records = self.data.items()
        it = []
        for i in records:
            it.append(i)
        index = 0
        while index < len (it):
            yield print (it[index])
            index += 1

    def search (self, arg = None):
        if arg == None:
            arg = input ("Enter a request ")
        if arg != None:
            userlist = []
            for rec in self.data.items():
                #rec = list (rec)
                for el in rec:
                    if el != list:
                        el = str (el)
                        if arg in el:
                            userlist.append (rec[0])
                    elif el == list:
                        for num in el:
                            if arg in num:
                                userlist.append (rec[0])
            print (userlist)


class Name(Field):
    def __init__(self, n, s=None):
        self.name = n
        self.surname = s

    def __repr__(self):
        return f"{self.name}"

class Phone():

    def __init__(self, phone = None):
        self.__phone = phone

    @property
    def phone (self):
        return self.__phone

    @phone.setter
    def phone(self, p):
        if p != None:
            regex_phone = re.compile(r"(\(\d{3}\))-(\d{3}-\d{4})")
            
            if bool(regex_phone.search(p)) == True:
                self.__phone = p
            else:
                print('Only numbers phones like (415)-555-4242 is appropriate')
                self.__phone = None


    def __repr__(self):
        return f"{self.phone}"
        
class Record():
    
    def __init__ (self, name, phone = None, birthday = None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        if phone:
            self.phones.append(phone)

    def add_phone (self, phone):
        self.phones.append(phone)
        print (f"for {self.name} add new phone {phone}." )
        
    def del_phone (self, phone):
        for p in self.phones:
            if p == phone:
                self.phones.remove(p)
                print (f"Phone {p} successfully deleted")

    def change_phone (self, phone_one, phone_two):
        i = 0                                                          # Лічильник для проходження і заміни елемента в списку
        for p in self.phones:
            
            if p == phone_one:
                self.phones[i] = phone_two
                print ("Phone successfully updated")
            i += 1
        else:
            print (f"Phone {phone_one} is not found!")

    def print_all_phones(self):
        for p in self.phones:
            print (f"{p}")

    def add_birthday (self, bd):
        self.birthday = bd

    def days_to_birthday (self):
        if self.birthday != None:
            current_datetime = datetime.now()             # Знаходимо нинішню дату
            if current_datetime > self.birthday.birthday:               
                difference = (current_datetime  - self.birthday.birthday).days
                i= 0
                old = ((current_datetime  - self.birthday.birthday).days)//365
                years = []
                z = self.birthday.birthday.year
                for el in range (old):
                    years.append(z)
                    z +=1
                for y in years:
                    if (y % 4) == 0:
                        i+=1
                day_to_bd = timedelta(days = 365).days - difference % 365 + i
                print (f"Days to the next birthday: {day_to_bd}")
        else:
            print("Haven't information")           
        
class Birthday ():
    def __init__ (self, birthday_y = None, birthday_m = None, birthday_d = None,):
        self.birthday = datetime (birthday_y, birthday_m, birthday_d)

    @property
    def bd (self):
        return self.__birthday

    @bd.setter
    def bd(self, b):
        if b != None:
            if isinstance (b, datetime):
                print ("Hello!")
            else:
                print ("You made mistake!")
    def __repr__(self):
        return f"Birthday: {self.birthday}"

class CustomIterator:
    def __iter__(self):
        return AddressBook()

file_name = 'adressbook.bin'

def saver(obj):
    with open(file_name, "wb") as file:
        pickle.dump(obj, file)

def loader():
    with open(file_name, "rb") as file:
       l = pickle.load(file)

sarch = loader()
