from typing import TypedDict

class Person(TypedDict):
    name: str = 'Harris'
    age: int
    
new_person: Person = {
    'name': "Harris",
    'age': 21
}

print(new_person)