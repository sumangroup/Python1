class studentbasics:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display_basic_info(self):
        print(self.name)
        print(self.rollno)

class ExtracurricularActivities:

    def __init__(self,activities=None):
        self.activities= activities if activities else []

    def add_activity(self,activity):
        self.activities.append(activity)

        
    def display_activities(self):
        print(self.activities)

class Skills:
    def __init__(self, skills=None):
        self.skills = skills if skills else []

    def add_skill(self, skill):
        self.skills.append(skill)

    def display_skills(self):
        print(self.skills)


class StudentProfile(studentbasics, ExtracurricularActivities, Skills):
    def __init__(self, name, rollno, activities=None, skills=None):
         studentbasics.__init__(self, name, rollno)
         ExtracurricularActivities.__init__(self, activities)
         Skills.__init__(self, skills)

    def get_full_profile(self):
        print("\n--- Full Student Profile ---")
        self.display_basic_info()
        self.display_activities()
        self.display_skills()



student1 = StudentProfile(name="Priya Sharma", rollno="S205",
                            activities=["Debate Club", "Coding Club"],
                            skills=["Python", "Public Speaking"])

student1.add_activity("cricket")
student1.get_full_profile()
        







