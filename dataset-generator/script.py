import pandas as pd
import numpy as np
from faker import Faker
import os

fake = Faker()
# test
# Number of mock records
num_employees = 100
num_courses = 50
num_goals = 200
num_applications = 100

# Generate Employee Profiles (combined with InfyMe)
employees = []
for _ in range(num_employees):
    leaves_start = fake.date_between(start_date='-1y', end_date='today')
    leaves_end = fake.date_between(start_date=leaves_start, end_date='+1y')
    employees.append({
        'EmployeeID': fake.unique.random_int(min=1000, max=9999),
        'Name': fake.name(),
        'Company': fake.random_element(elements=('Infosys', 'Edgeverse', 'Helix', 'Accenture', 'Cognizant')),
        'Department': fake.random_element(elements=('HR', 'Engineering', 'Sales', 'Marketing', 'Finance')),
        'JobTitle': fake.job(),
        'DateOfJoining': fake.date_between(start_date='-5y', end_date='today'),
        'ContactInfo': fake.phone_number(),
        'Address': fake.address(),
        'EmergencyContact': fake.phone_number(),
        'HRNotes': fake.paragraph(),
        'NumberOfLeaves': fake.random_int(min=0, max=30),
        'LeavePeriod': f"{leaves_start} to {leaves_end}",
        'Birthday': fake.date_of_birth(minimum_age=22, maximum_age=60)
    })
employees_df = pd.DataFrame(employees)

# Generate Courses (LeX)
courses = []
for _ in range(num_courses):
    courses.append({
        'CourseID': fake.unique.random_int(min=100, max=999),
        'CourseName': fake.bs(),
        'EmployeeID': fake.random_element(elements=employees_df['EmployeeID']),
        'CompletionStatus': fake.random_element(elements=('Completed', 'In Progress')),
        'DateOfCompletion': fake.date_between(start_date='-1y', end_date='today') if fake.random_element(elements=('Completed', 'In Progress')) == 'Completed' else None,
        'RecommendedCourses': [fake.bs() for _ in range(3)],
        'Skills': [fake.word() for _ in range(5)]
    })
courses_df = pd.DataFrame(courses)

# Generate Goals and Projects (iCount)
goals = []
for _ in range(num_goals):
    goals.append({
        'GoalID': fake.unique.random_int(min=1000, max=9999),
        'GoalDescription': fake.sentence(),
        'EmployeeID': fake.random_element(elements=employees_df['EmployeeID']),
        'ProjectAssigned': fake.bs(),
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
        'JobTitleAppliedFor': fake.random_element(elements=('Software Engineer', 'Data Analyst', 'HR Manager', 'Sales Executive', 'Marketing Specialist')),
        'ApplicationStatus': fake.random_element(elements=('Applied', 'Interviewed', 'Accepted', 'Rejected')),
        'DateOfApplication': fake.date_between(start_date='-1y', end_date='today')
    })
applications_df = pd.DataFrame(applications)

# Save to CSV (if needed)
employees_df.to_csv('mock_employees.csv', index=False)
courses_df.to_csv('mock_courses.csv', index=False)
goals_df.to_csv('mock_goals.csv', index=False)
applications_df.to_csv('mock_applications.csv', index=False)

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
folder_name = 'mock_data'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save the dataframes to CSV files in the folder
employees_df.to_csv(os.path.join(folder_name, 'mock_employees.csv'), index=False)
courses_df.to_csv(os.path.join(folder_name, 'mock_courses.csv'), index=False)
goals_df.to_csv(os.path.join(folder_name, 'mock_goals.csv'), index=False)
applications_df.to_csv(os.path.join(folder_name, 'mock_applications.csv'), index=False)

print(f"Mock data saved to folder '{folder_name}'")
