def f(s,x):
    patt = re.compile(x)
    matches = patt.finditer(s)
    for match in matches:
        print(match)
import regex
import re

s = """KName: John Doe
Address: 123 Main Street, Cityville, State, Zip Code
Telephone: 555-1234
Sex: Male
Email: john.doe@example.com

Education:
- Degree: Bachelor of Science in Computer Science
- School: University of XYZ
- Year: 2020

Experience:
1. Position: Software Engineer
   Company: Tech Solutions Inc.
   Location: Cityville
   Start Date: 2020
   End Date: Present
   Responsibilities:
     - Developing and maintaining software applications.
     - Collaborating with cross-functional teams.
     - Troubleshooting and debugging code.

2. Position: Intern
   Company: ABC Corporation
   Location: Townsville
   Start Date: 2019
   End Date: 2020
   Responsibilities:
     - Assisting with software development projects.
     - Learning and applying new technologies.
     - Providing support to the development team.

Skills:
- Python
- Java
- JavaScript
- Database Management
- Problem Solving

Languages:
- English (Fluent)
- Spanish (Basic)

References:
1. Name: Jane Smith
   Position: Senior Software Engineer
   Company: Tech Solutions Inc.
   Telephone: 555-5678
   Email: jane.smith@example.com

2. Name: Bob Johnson
   Position: Head of Engineering
   Company: ABC Corporation
   Telephone: 555-8765
   Email: bob.johnson@example.com"""

# patt = re.compile(r'Pos')
# matches = patt.finditer(s)

# for match in matches:
#     print(match)


# f(s,r'.')
f(s,r'.Name')
print("---------------------")
f(s,r'Name')
print("---------------------")
f(s,r'\d{3}-\d{4}') ## CHECKS PHONE NUMBER

# f(s, r'^Name')