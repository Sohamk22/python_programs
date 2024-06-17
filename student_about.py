def get_student_details():
    """
    Collects student details from the user.
    """
    print("Welcome! Let's create your personalized resume.")
    name = input("Enter your full name: ")
    age = input("Enter your age: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    educational_background = input("Enter your educational background (B.Tech, university, etc.): ")
    major = input("Enter your major or specialization: ")
    graduation_year = input("Expected graduation year: ")
    gpa = input("Enter your current GPA: ")
    accomplishments = input("List any notable accomplishments (projects, awards, etc.): ")
    skills = input("List the skills you are learning or proficient in (comma-separated): ")
    relevant_courses = input("List relevant courses you've taken: ")
    certifications = input("List any certifications you hold: ")
    internships = input("Describe any relevant internships or work experience: ")
    projects = input("Highlight significant projects you've worked on: ")
    leadership_experience = input("Describe any leadership roles or extracurricular activities: ")
    hobbies = input("Share your hobbies and interests: ")
    languages = input("List any programming languages you're proficient in: ")
    about_me = input("Tell me about yourself (specifically for computer science students): ")

    return {
        "name": name,
        "age": age,
        "dob": dob,
        "address": address,
        "phone_number": phone_number,
        "email": email,
        "educational_background": educational_background,
        "major": major,
        "graduation_year": graduation_year,
        "gpa": gpa,
        "accomplishments": accomplishments,
        "skills": skills,
        "relevant_courses": relevant_courses,
        "certifications": certifications,
        "internships": internships,
        "projects": projects,
        "leadership_experience": leadership_experience,
        "hobbies": hobbies,
        "languages": languages,
        "about_me": about_me,
    }

def generate_resume(student_details):
    """
    Generates a personalized resume based on student details.
    """
    resume = f"""
    Resume for {student_details['name']}

    Personal Details:
    - Age: {student_details['age']}
    - Date of Birth: {student_details['dob']}
    - Address: {student_details['address']}
    - Phone: {student_details['phone_number']}
    - Email: {student_details['email']}

    Educational Background:
    - Pursuing B.Tech in {student_details['educational_background']}
    - Major: {student_details['major']}
    - Expected Graduation Year: {student_details['graduation_year']}
    - GPA: {student_details['gpa']}

    Accomplishments:
    - {student_details['accomplishments']}

    Skills:
    - {student_details['skills']}

    Relevant Courses:
    - {student_details['relevant_courses']}

    Certifications:
    - {student_details['certifications']}

    Internships and Work Experience:
    - {student_details['internships']}

    Notable Projects:
    - {student_details['projects']}

    Leadership and Extracurriculars:
    - {student_details['leadership_experience']}

    Hobbies and Interests:
    - {student_details['hobbies']}

    Programming Languages:
    - {student_details['languages']}

    About Me:
    {student_details['about_me']}

    Let's connect! Feel free to reach out if you'd like to discuss coding, share ideas, or collaborate on exciting projects.

    Thank you for considering my application!

    Sincerely,
    {student_details['name']}
    """

    return resume

if __name__ == "__main__":
    student_info = get_student_details()
    resume_text = generate_resume(student_info)
    print("\nGenerated Resume:\n")
    print(resume_text)
 