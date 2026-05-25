from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Harris'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt = 0, lt = 10)
    
new_student = {
    'name': 'Harris Amin',
    "age" : '21',
    'email': 'harrisaminjutt@gmail.com',
    'cgpa': '3.8'
}

# Pydantic automatically fixes parsing issues

student = Student(**new_student)
print(student.age)

student_dict = dict(student)
student_json = student.model_dump_json()
print(student_json)

print(type(student))