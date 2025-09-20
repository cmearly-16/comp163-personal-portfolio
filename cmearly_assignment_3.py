#Personal Info Storage
full_name = "Christopher Early"
email = "cmearly@aggies.ncat.edu"
hometown = "Raeford, NC"
graduation_semester = "Spring 2029"
major = "Computer Engineering"

#Academic Data Organization
current_courses = ["AERO 121, AERO 131, COMP 163, ECEN 101, GEEN 100, MATH 131"]
completed_courses_nocreds = ["None"]
completed_courses_creds = ["None"]
credit_hours = [3, 3, 3, 3, 3, 3]
gpa_history = [3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
cumulative_gpa = sum(gpa_history) / len(gpa_history)
study_hours = {
    "Programming:": 3,
    "Math:": 2,
    "Engineering:": 3,
    "Aero:": 1,
}
total_hours = study_hours["Programming:"] + study_hours["Math:"] + study_hours["Engineering:"] + study_hours["Aero:"]

#Contact Info Storage
emergency_contact = ("Tia Early (Mom) - 123-456-7890")
home_address = ("377 Peaceford Avenue, Raeford, NC 28376")
instagram = ("Instagram, @chris.emarcellus16,", "36")
twitter = ("Twitter, @LostFromLight16,", "2")
birthday = ("Birthday,", "11, 16, 2006")

#Interest Tracking
current_skills = {'Time management', 'Engineering Basics', 'Problem solving', 'HTML', 'Python basics'}
skills_learn = {'Types', 'Variables', 'Expressions', 'Git', 'Public speaking'}
career_interests = {'Hardware Engineering', 'Game development', 'Web development'}
hobbies = {"Gaming", "Workouts", "Reading", "Soccer", "Music"}
entertainment_backlog = {"Breaking Bad", "Fate", "Spiderman", "Star Wars", "Markiplier"}

#Organizational Mapping
course_credits = {
    "COMP 163": 3,
    "ECEN 101": 3,
    "GEEN 100": 3,
    "MATH 131": 3,
    "AERO 121": 3,
    "AERO 131": 3,
}
course_professors = {
    "COMP 163": "Prof. Rhodes",
    "ECEN 101": "Prof. Osareh",
    "GEEN 100": "Prof. Alford",
    "MATH 131": "Prof. Rastigeyev",
    "AERO 121": "Capt. Blanton",
    "AERO 131": "Capt. Blanton",
}
course_rooms = {
    "COMP 163": "Gibbs 337",
    "ECEN 101": "Martin 200",
    "GEEN 100": "Graham 208",
    "MATH 131": "Marteena 222",
    "AERO 121": "Campbell 126 ",
    "AERO 131": "Proctor 160",
}
monthly_budget = {
    "Food:": 100,
    "Entertainment:": 60,
    "Transportation:": 50,
    "Books:": 1,
}
study_hours = {
    "Programming:": 3,
    "Math:": 2,
    "Engineering": 3,
    "Aero": 1,
}
contact_directory = {
    "Mom:": "123-456-7890",
    "Roommate:": "123-456-7890",
    "Academic Advisor:": "123-456-7890",
}

#Required Calculations
total_hours = study_hours["Programming:"] + study_hours["Math:"] + study_hours["Engineering"] + study_hours["Aero"]
total_budget = monthly_budget["Food:"] + monthly_budget["Entertainment:"] +monthly_budget["Books:"] +monthly_budget["Transportation:"]
food_budget = round(monthly_budget["Food:"] / 30, 2)
annual_budget = (total_budget * 12)
study_cost = round(monthly_budget["Books:"] / total_hours, 2)

#Analytics Calculations
instagram_followers = int(instagram[1])
twitter_followers = int(twitter[1])
total_followers = (instagram_followers + twitter_followers)
current_count = len(current_skills)
learn_count = len(skills_learn)
total_skills = current_count + learn_count
workload_assessment = sum(credit_hours) + total_hours

print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {full_name:s} | Email: {email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major:s}")
print("")
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {sum(credit_hours)} credits across {len(completed_courses_nocreds)} courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {total_hours} hours")
print(f"Academic Investment: ${study_cost} per study hour")
print("")
print("Current Courses:")
print(f"COMP 163 - {course_credits['COMP 163']} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"ECEN 101 - {course_credits['ECEN 101']} credits - {course_professors['ECEN 101']} - {course_rooms['ECEN 101']}")
print(f"GEEN 100 - {course_credits['GEEN 100']} credits - {course_professors['GEEN 100']} - {course_rooms['GEEN 100']}")
print(f"MATH 131 - {course_credits['MATH 131']} credits - {course_professors['MATH 131']} - {course_rooms['MATH 131']}")
print(f"AERO 121 - {course_credits['AERO 121']} credits - {course_professors['AERO 121']} - {course_rooms['AERO 121']}")
print(f"AERO 131 - {course_credits['AERO 131']} credits - {course_professors['AERO 131']} - {course_rooms['AERO 131']}")
print("")
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_learn}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_learn)}")
print("")
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${sum(monthly_budget.values())}")
print(f"Food: ${monthly_budget['Food:']} (${monthly_budget['Food:'] / 30:.1f}/day)")
print(f"Entertainment: ${monthly_budget['Entertainment:']}")
print(f"Books: ${monthly_budget['Books:']}")
print(f"Transportation: ${monthly_budget['Transportation:']}")
print(f"Annual Projection: ${sum(monthly_budget.values()) * 12}")
print("")
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact}")
print(f"Home Address: {home_address}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory")
print("")
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {len(completed_courses_creds)}")
print(f"Current Academic Load: {workload_assessment} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("================================================================")