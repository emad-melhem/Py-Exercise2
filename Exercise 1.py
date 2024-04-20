_name=input("Enter your name :").strip()
_age= input("Enter your age :").strip()
_hobbies=input("Enter your hobbies :").strip()
_place=input("Enter your living place :").strip()
_old_work=input("Enter your old work :").strip()
_new_work=input("Enter your new work :").strip()

if not _name:
    _name="Wes"
if not _age:
    _age="21"
if not _hobbies:
    _hobbies="programming and playing volleyball"
if not _place:
    _place="a town called Erica in the Netherlands"
if not _old_work:
    _old_work="a baker"
if not _new_work:
    _new_work="a mentor for Clarusway"

print(f"I am {_name},I am {_age} years old.\nI enjoy {_hobbies}.",
      f"\nI am originally from {_place},\nI used to work as {_old_work} and am now working as {_new_work}.")