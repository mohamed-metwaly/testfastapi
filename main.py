from fastapi import FastAPI, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List


class Student(BaseModel):

    id: int
    name: str
    grade: int


students = [
    Student(id=1, name="Ahmed", grade=5),
    Student(id=2, name="Mohamed", grade=3),
    Student(id=33, name="Metwaly", grade=10),
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/students/")
def show_students():

    return students


@app.post("/student/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student


@app.put("/students/{student_id}")
def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student
    return {"error": "Student not found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message": "student deletedG "}
    return {"error": "Student not found"}
