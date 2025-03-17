#Hello, this should be where we contribute our work as a team
#Our team are: Mariam, Malak, Karim, Salma, and, finally, me, Kahrawi.
class User:
    User_counter = 0

    def __init__(self, name: str, age: int, address: str, id: int, phone_number: str, per_email: str, bus_email:str, begin_date: str, password: str, end_date = None):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__id = id
        self.__phone_number = phone_number
        self.__per_email = per_email
        self.__bus_email = bus_email
        self.__begin_date = begin_date
        self.__end_date = end_date
        self.__password = password
        User.User_counter += 1

    def login(self, id, password):
        if self.id == id and self.password == password:
            print(f'Welcome {self.name} back!')
        else:
            print("Invalid Credentials. Try again.")
    def logout(self):
        out = int(input("Are you sure you want to log out? Press 1 to log out:"))
        if out == 1:
            print("You're logged out.")


    def display_userinfo(self):
        print(f'(General Info)User Name: {self.__name}, User Age: {self.__age}, User ID: {self.__id}, User Phone Number: {self.__phone_number}, User Personal Email: {self.__per_email}, User Business Email: {self.__bus_email}. Number of users: {User.User_counter}')
        print(f'They started with us in {self.__begin_date}')
        if self.__end_date:
            print(f'Unfortunately, they left us in {self.__end_date}')

class Student(User):
    def __init__(self, name: str, age: int, address: str, id: int, phone_number: str, per_email: str, bus_email:str, faculty: str, enrollment_date: str, begin_date: str, password: str, end_date = None , gpa = None, program = None):
        super().__init__(name, age, address, id, phone_number, per_email, bus_email, begin_date, end_date, password)
        self.__faculty = faculty
        self.__program = program
        self.__enrollment_date = enrollment_date
        self.__gpa = gpa
    def display_studentinfo(self):
        self.display_userinfo()
        print(f'Student Faculty: {self.__faculty}, Their Program: {self.__program}, Their Enrollment Date: {self.__enrollment_date}')

class Professor(User):
    students = []
    def __init__(self, name: str, age: int, address: str, id: int, phone_number: str, per_email: str, bus_email:str, faculty: str, begin_date: str, password: str, end_date = None):
        super().__init__(name, age, address, id, phone_number, per_email, bus_email, begin_date, end_date, password)
        self.__faculty = faculty
        self.__enrollment_date = enrollment_date

class Course:
    def __init__ (self, course_name: str, course_code: int, reg_students: list):
        self.course_name = course_name
        self.course_code = course_code
        self.reg_students = reg_students
    def display_courseinfo(self):
        print(f'Course Name: {self.course_name}, Course Code: {self.course_code}, Registered Students: {self.reg_students}')

class Administrator(User):
    def __init__(self, name: str, age: int, address: str, id: int, phone_number: str, per_email: str, bus_email:str,)

class Fee :
    def __init__ (self ,fee_id: int, student_id: int, amount: float, due_date: str, payment_status: str, payment_date: str = None):
        self.fee_id = fee_id
        self.student_id = student_id
        self.amount = amount
        self.due_date = due_date
        self.payment_status = payment_status
        self.payment_date = payment_date
    def generate_fee(self) -> None:
        print(f"Fee of {self.amount} created for student {self.student_id} with due date {self.due_date}.")
    def record_payment(self, payment_date) -> None:
        self.payment_status = "Paid"
        self.payment_date = payment_date
        print(f"Payment recorded for fee {self.fee_id} on {payment_date}.")
    def check_payment_status(self) -> str:
        return self.payment_status
    def view_fee_history(self) -> None:
        print(f"Fee history {self.fee_id}: Student {self.student_id}, Amount {self.amount}, Due Date {self.due_date}, Payment Status {self.payment_status}, Payment Date {self.payment_date}.")

class FinancialAid:
    def __init__(self, aid_id: int, student_id: int, amount: float, type: str, application_date: str, approval_status: str):
        self.aid_id = aid_id
        self.student_id = student_id
        self.amount = amount
        self.type = type
        self.application_date = application_date
        self.approval_status = approval_status
    def apply_for_aid(self) -> None:
        print(f"Application submitted for financial aid {self.aid_id} for student {self.student_id}.")
    def approve_aid(self) -> None:
        self.approval_status: str = "Approved"
        print(f"Financial aid {self.aid_id} approved.")
    def view_aid_status(self) -> str:
        return self.approval_status

class ResearchProject:
    def __init__(self, project_id: int, title: str, researchers: list, funding: float, start_date: str, end_date: str, publications: list = None):
        self.project_id = project_id
        self.title = title
        self.researchers = researchers
        self.funding = funding
        self.start_date = start_date
        self.end_date = end_date
        self.publications = publications or []
    def create_project(self) -> None:
        print(f"Research project '{self.title}' created with ID {self.project_id}.")
    def add_researcher(self, researcher: str) -> None:
        self.researchers.append(researcher)
        print(f"Researcher {researcher} added to project {self.project_id}.")
    def view_project_details(self) -> None:
        print(f"Project details {self.project_id}: Title '{self.title}', Researchers {self.researchers}, Funding {self.funding}, Start Date {self.start_date}, End Date {self.end_date}.")

class Publication:
    def __init__(self, publication_id: int, title: str, authors: list, journal: str, date: str, abstract: str):
        self.publication_id = publication_id
        self.title = title
        self.authors = authors
        self.journal = journal
        self.date = date
        self.abstract = abstract
    def add_publication(self) -> None:
        print(f"Publication '{self.title}' added with ID {self.publication_id}.")
    def view_publication_details(self) -> None:
        print(f"Publication details {self.publication_id}: Title '{self.title}', Authors {self.authors}, Journal {self.journal}, Date {self.date}.")
  
class Housing:
    def __init__(self, housing_id: int, building_id: int, room_number: str, student_id: int, capacity: int):
        self.housing_id = housing_id
        self.building_id= building_id
        self.room_number = room_number
        self.student_id  = student_id
        self.capacity = capacity
    def allocate_room(self) -> None:
        print(f"Room {self.room_number} allocated to student {self.student_id} in housing {self.housing_id}.")
    def check_room_availability(self) -> bool:
        if self.student_id is None:
            print(f"Room {self.room_number} in housing {self.housing_id} is available.")
            return True
        else:
            print(f"Room {self.room_number} in housing {self.housing_id} is not available.")
            return False
    def view_housing_details(self) -> None:
        print(f"Housing details {self.housing_id}: Room {self.room_number}, Student {self.student_id}, Capacity {self.capacity}.")

class building :
    def __init__ (self , building_id : int ,name : str ,address: str, number_of_floors: int, classrooms: list = None):
        self.building_id = building_id
        self.name = name
        self.address = address
        self.number_of_floors = number_of_floors
        self.classrooms = classrooms
    def add_classroom(self, classroom: str) -> None:
        self.classrooms.append(classroom)
        print(f"Classroom {classroom} added to building {self.building_id}.")
    def view_building_details(self) -> None:
        print(f"Building details {self.building_id}: Name '{self.name}', Address '{self.address}', Floors {self.number_of_floors}, Classrooms {self.classrooms}.")

class MedicalRecord:
    def __init__(self, record_id: int, student_id: int, date: str, diagnosis: str, treatment: str, doctor_name: str):
        self.record_id = record_id
        self.student_id = student_id
        self.date = date
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.doctor_name = doctor_name
    def add_record(self) -> None:
        print(f"Medical record {self.record_id} added for student {self.student_id}.")
    def view_record(self) -> None:
        print(f"Medical record {self.record_id}: Date {self.date}, Diagnosis '{self.diagnosis}', Treatment '{self.treatment}', Doctor '{self.doctor_name}'.")
    def update_record(self) -> None:
        print(f"Medical record {self.record_id} updated.")

class Parking:
    def __init__(self, parking_id: int, location: str, capacity: int, availability: int, user_id: int = None):
        self.parking_id = parking_id
        self.availability = availability
        self.user_id = user_id
    def allocate_parking_spot(self) -> bool:
        if self.availability > 0:
            self.availability -= 1
            print(f"Parking spot allocated at {self.location}.")
            return True
        else:
            print(f"No parking spots available at {self.location}.")
            return False
    def check_availability(self) -> int:
        return self.availability
    def view_parking_details(self) -> None:
        print(f"Parking details {self.parking_id}: Location {self.location}, Capacity {self.capacity}, Availability {self.availability}.")

class Inventory:
    def __init__(self, item_id: int, name: str, quantity: int, location: str, description: str):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.location = location
        self.description = description
    def add_item(self) -> None:
        self.quantity += 1
        print(f"Item {self.name} added to inventory.")
    def remove_item(self) -> None:
        if self.quantity > 0:
            self.quantity -= 1
            print(f"Item {self.name} removed from inventory.")
        else:
            print(f"Cannot remove item {self.name}. Quantity is zero.")
    def check_inventory(self) -> int:
        return self.quantity

class Club:
    def __init__(self, club_id: int, name: str, president_id: int, members: list = None, activities: list = None):
        self.club_id = club_id
        self.name = name
        self.president_id = president_id
        self.members = members or []
        self.activities = activities or []
    def add_member(self, member: str) -> None:
        self.members.append(member)
        print(f"Member {member} added to club {self.name}.")
    def schedule_activity(self, activity: str) -> None:
        self.activities.append(activity)
        print(f"Activity '{activity}' scheduled for club {self.name}.")
    def view_club_details(self) -> None:
        print(f"Club details {self.club_id}: Name '{self.name}', President ID {self.president_id}, Members {self.members}, Activities {self.activities}.")

class Department:
    def __init__(self, department_id: int, name: str, head_of_department: str, courses_offered: list, faculty_members: list):
        self.department_id = department_id
        self.name = name
        self.head_of_department = head_of_department
        self.courses_offered = courses_offered
        self.faculty_members = faculty_members
    def get_department_info(self) -> None:
        print(f"Department ID: {self.department_id}")
        print(f"Name: {self.name}")
        print(f"Head of Department: {self.head_of_department}")
        print(f"Courses Offered: {self.courses_offered}")
        print(f"Faculty Members: {self.faculty_members}")
    def list_courses(self) -> None:
        print("Courses Offered:")
        for course in self.courses_offered:
            print(f"- {course}")
    def list_professors(self) -> None:
        print("Faculty Members:")
        for professor in self.faculty_members:
            print(f"- {professor}")

class Classroom:
    def __init__(self, classroom_id: int, location: str, capacity: int, schedule: dict):
        self.classroom_id = classroom_id
        self.location = location
        self.capacity = capacity
        self.schedule = schedule
    def allocate_class(self, time_slot: str, course: str) -> None:
        if time_slot not in self.schedule:
            self.schedule[time_slot] = course
            print(f"Classroom {self.classroom_id} allocated for {course} at {time_slot}.")
        else:
            print(f"Time slot {time_slot} is already occupied.")
    def check_availability(self, time_slot: str) -> bool:
        return time_slot not in self.schedule
    def get_classroom_info(self) -> None:
        print(f"Classroom ID: {self.classroom_id}")
        print(f"Location: {self.location}")
        print(f"Capacity: {self.capacity}")
        print(f"Schedule: {self.schedule}")

class Schedule:
    def __init__(self, schedule_id: int, course: str, professor: str, time_slot: str, location: str):
        self.schedule_id = schedule_id
        self.course = course
        self.professor = professor
        self.time_slot = time_slot
        self.location = location
    def assign_schedule(self) -> None:
        print(f"Schedule {self.schedule_id} assigned: {self.course} with {self.professor} at {self.time_slot} in {self.location}.")
    def update_schedule(self, time_slot: str = None, location: str = None) -> None:
        if time_slot:
            self.time_slot = time_slot
        if location:
            self.location = location
        print(f"Schedule {self.schedule_id} updated.")
    def view_schedule(self) -> None:
        print(f"Schedule ID: {self.schedule_id}")
        print(f"Course: {self.course}")
        print(f"Professor: {self.professor}")
        print(f"Time Slot: {self.time_slot}")
        print(f"Location: {self.location}")

class Exam:
    def __init__(self, exam_id: int, course: str, date: str, duration: str, student_results: dict):
        self.exam_id = exam_id
        self.course = course
        self.date = date
        self.duration = duration
        self.student_results = student_results
    def schedule_exam(self) -> None:
        print(f"Exam {self.exam_id} scheduled for {self.course} on {self.date} for {self.duration}.")
    def record_results(self, student_id: int, score: float) -> None:
        self.student_results[student_id] = score
        print(f"Result recorded for student {student_id} in exam {self.exam_id}.")
    def view_exam_info(self) -> None:
        print(f"Exam ID: {self.exam_id}")
        print(f"Course: {self.course}")
        print(f"Date: {self.date}")
        print(f"Duration: {self.duration}")
        print(f"Student Results: {self.student_results}")
 
class Library:
    def __init__(self, library_id: int, books: list, students_registered: list):
        self.library_id = library_id
        self.books = books
        self.students_registered = students_registered
    def borrow_book(self, student_id: int, book_title: str) -> None:
        if book_title in self.books:
            print(f"Book '{book_title}' borrowed by student {student_id}.")
        else:
            print(f"Book '{book_title}' is not available.")
    def return_book(self, student_id: int, book_title: str) -> None:
        print(f"Book '{book_title}' returned by student {student_id}.")
    def check_availability(self, book_title: str) -> bool:
        return book_title in self.books 

class Feedback:
    def __init__(self, feedback_id: int, student_id: int, professor_id: int, course_id: int, rating: int, comments: str):
        self.feedback_id = feedback_id
        self.student_id = student_id
        self.professor_id = professor_id
        self.course_id = course_id
        self.rating = rating
        self.comments = comments
 
    def submit_feedback(self) -> None:
        print(f"Feedback submitted: ID {self.feedback_id}, Student {self.student_id}, Professor {self.professor_id}, Course {self.course_id}, Rating {self.rating}.")
        print(f"Comments: {self.comments}")

    def view_feedback(self) -> None:
        print(f"Feedback ID: {self.feedback_id}")
        print(f"Student ID: {self.student_id}")
        print(f"Professor ID: {self.professor_id}")
        print(f"Course ID: {self.course_id}")
        print(f"Rating: {self.rating}")
        print(f"Comments: {self.comments}")

     def generate_report(self) -> str:
        report = (
            f"Feedback Report:\n"
            f"  Feedback ID: {self.feedback_id}\n"
            f"  Student ID: {self.student_id}\n"
            f"  Professor ID: {self.professor_id}\n"
            f"  Course ID: {self.course_id}\n"
            f"  Rating: {self.rating}\n"
            f"  Comments: {self.comments}\n"
        )
        return report



