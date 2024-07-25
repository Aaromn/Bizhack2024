import pandas as pd
import numpy as np
from faker import Faker
import os
import tech_data

fake = Faker()

# Number of mock records
num_employees = 10
num_courses = 100
num_goals = 10
num_applications = 5

# Generate Employee Profiles (combined with InfyMe)
employees = []
for _ in range(num_employees):
    employees.append({
        'EmployeeID': fake.unique.random_int(min=100000, max=999999),
        'Name': fake.name(),
        'Company': fake.random_element(elements=('Infosys Lmt', 'Infosys BPM', 'Edgeverve')),
        'JobTitle': fake.random_element(elements=tech_data.job_titles),
        'DateOfJoining': fake.date_between(start_date='-5y', end_date='today'),
        'ContactInfo': fake.phone_number(),
        'Address': fake.address(),
        'EmergencyContact': fake.phone_number(),
        # 'HRNotes': fake.paragraph(),
        'NumberOfLeaves': fake.random_int(min=0, max=30),
        'WorkfromHome': fake.random_int(min=0, max=15),
        'Birthday': fake.date_of_birth(minimum_age=22, maximum_age=60),
        'Skills': [fake.random_element(elements=tech_data.skills) for _ in range(fake.random_int(min=1, max=5))]
    })
employees_df = pd.DataFrame(employees)

# Generate Courses (LeX)
courses = []
for _ in range(num_courses):
    courses.append({
        'EmployeeID': fake.random_element(elements=employees_df['EmployeeID']),
        'CourseID': fake.unique.random_int(min=100, max=999),
        'CourseName': fake.random_element(elements=tech_data.courses),
        'CompletionStatus': fake.random_element(elements=('Completed', 'In Progress')),
        'DateOfEnrollment': fake.date_between(start_date='-1y', end_date='today'),
        'DateOfCompletion': fake.date_between(start_date='-1y', end_date='today') if fake.random_element(elements=('Completed', 'In Progress')) == 'Completed' else None
    })
courses_df = pd.DataFrame(courses)

# Generate Goals and Projects (iCount)
goals = []
for _ in range(num_goals):
    goals.append({
        'EmployeeID': fake.random_element(elements=employees_df['EmployeeID']),
        'GoalID': fake.unique.random_int(min=1000, max=9999),
        'ProjectAssigned': fake.random_element(elements=tech_data.projects),
        'DateAssigned': fake.date_between(start_date='-1y', end_date='today'),
        'DueDate': fake.date_between(start_date='today', end_date='+1y'),
        'CompletionStatus': fake.random_element(elements=('Completed', 'In Progress'))
    })
goals_df = pd.DataFrame(goals)

# Generate Job Applications (StepUp)
applications = []
for _ in range(num_applications):
    applications.append({
        'ApplicationID': fake.unique.random_int(min=1000, max=9999),
        'EmployeeID': fake.random_element(elements=employees_df['EmployeeID']),
        'JobTitleAppliedFor': fake.random_element(elements=tech_data.job_titles),
        'ApplicationStatus': fake.random_element(elements=('Applied', 'Interviewed', 'Accepted', 'Rejected')),
        'DateOfApplication': fake.date_between(start_date='-1y', end_date='today')
    })
applications_df = pd.DataFrame(applications)

# Display DataFrames for verification
print("Mock Employee Profiles:")
print(employees_df.head())

print("\nMock Courses:")
print(courses_df.head())

print("\nMock Goals and Projects:")
print(goals_df.head())

print("\nMock Job Applications:")
print(applications_df.head())


# Create a folder to save the CSV files
folder_name = 'dataset'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save the dataframes to CSV files in the folder
employees_df.to_json(os.path.join(folder_name, 'mock_employees.json'), index=False)
courses_df.to_json(os.path.join(folder_name, 'mock_courses.json'), index=False)
goals_df.to_json(os.path.join(folder_name, 'mock_goals.json'), index=False)
applications_df.to_json(os.path.join(folder_name, 'mock_applications.json'), index=False)

print(f"Mock data saved to folder '{folder_name}'")

# test