from collections import UserDict
from datetime import datetime, timedelta
from fileinput import close
import re
import pickle

def save (obj):
    save = pickle.dump (obj)

def load ():
    load = pickle.load()

class Field():
    pass

class AddressBook(UserDict):
    def add_record (self,key, val):
        self.data.__setitem__(key, val)

    def iterator(self, page_num=2):
        self.obj = []
        for i in self.data.items():
            self.obj.append(i)
        end = len(self.obj)
        i = 0
        limit = page_num
        while True:
            yield "\n".join([str(item) for item in self.obj[i:limit]])
            print("next page")
            i, limit = i + page_num, limit + page_num
            if i > end:
                break
    
    

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

    def open(self):
        self.fh = open(file_name, "wb")     
    
    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    def __getstate__(self):
        attributes = {**self.__dict__}
        attributes['fh'] = None
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])
    
    


class Name(Field):
    def __init__(self, n, s=None):
        self.name = n
        self.surname = s

    def __repr__(self):
        return f"{self.name}"

class Phone():

    def __init__(self, phone = None):
        self.__phone = None

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



file_name = 'adressbook.bin'




user = Phone ("06655")
user_name = Name ("Vadym")
v = Birthday (1994, 1, 2)
vadym_r = Record (user_name, user, v)
phone = Phone ("(063)-710-61-94")
vadym_r.add_phone (phone)
actual_phone = Phone ("(050)-352-352-3")
vadym_r.change_phone (user, actual_phone)
new_phone = Phone ("0-(800)-000-0000")
vadym_r.change_phone (new_phone, actual_phone)
vadym_r.print_all_phones()
vadym_r.add_phone (user)
vadym_r.print_all_phones()
vadym_r.del_phone (user)
vadym_r.print_all_phones()
vadym_page = AddressBook ()
vadym_page.add_record (vadym_r.name, (vadym_r.phones, v))
print (vadym_page)
print (v.birthday)
vadym_r.days_to_birthday ()
zzz = Birthday (1994, 1, 3)
vadym_r.add_birthday (zzz)
vadym_r.days_to_birthday ()
print (vadym_r.birthday.birthday)
kira_name = Name ("Kira")
kira_phone = Phone ("(063)-000-00-00")
artem_name = Name ("Artem")
artem_phone = Phone ("(050)-000-00-00")
artem_bd = Birthday (1994, 1, 2)
vadym_page.add_record (kira_name, kira_phone)
vadym_page.add_record (artem_name, (artem_phone, artem_bd))

vadym_page.search ()

for i in vadym_page.iterator(2):
    print(i)



