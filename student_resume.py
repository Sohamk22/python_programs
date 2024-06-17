def get_student_details():
    """
    Collects student details from the user.
    """
    print("Welcome! Let's create your resume.")
    name = input("Enter your full name: ")
    age = input("Enter your age: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    address = input("Enter your address: ")
    educational_background = input("Enter your educational background (B.Tech, university, etc.): ")
    grades = input("Enter your recent grades or GPA: ")
    accomplishments = input("List any notable accomplishments (projects, awards, etc.): ")
    skills = input("List the skills you are learning or proficient in: ")
    current_year = input("Enter your current academic year: ")

    return {
        "name": name,
        "age": age,
        "dob": dob,
        "address": address,
        "educational_background": educational_background,
        "grades": grades,
        "accomplishments": accomplishments,
        "skills": skills,
        "current_year": current_year,
    }

def generate_resume(student_details):
    """
    Generates a sample resume based on student details.
    """
    resume = f"""
    Resume for {student_details['name']}

    Personal Details:
    - Age: {student_details['age']}
    - Date of Birth: {student_details['dob']}
    - Address: {student_details['address']}

    Educational Background:
    - Pursuing B.Tech in {student_details['educational_background']}
    - Recent Grades/GPA: {student_details['grades']}

    Accomplishments:
    - {student_details['accomplishments']}

    Skills:
    - {student_details['skills']}

    Current Year: {student_details['current_year']}
    """

    return resume

if __name__ == "__main__":
    student_info = get_student_details()
    resume_text = generate_resume(student_info)
    print("\nGenerated Resume:\n")
    print(resume_text)
