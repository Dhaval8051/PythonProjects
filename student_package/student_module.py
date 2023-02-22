class student:
    school_name = None
    school_address = None

    def __init__(self, student_id=None, student_name=None, student_mailid=None, student_percentage=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mailid = student_mailid
        self.student_percentage = student_percentage

    def get_student_name(self):
        return self.student_name

    def  get_name_with_percentgae(self):
        return "Hi ," + self.studnet_name + " - Your percentage " + str(self.student_percentage)
    def get_school_details():
        returnSstudent.school_name+ "is slocated at " +Student.school_address

