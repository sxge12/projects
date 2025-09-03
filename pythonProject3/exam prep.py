students = [
        {"name": "Alice", "grades": {"Math": 90, "English": 85}, "status": ("enrolled", 1001)},
        {"name": "Bob", "grades": {"Math": 70, "English": 80}, "status": ("enrolled", 1002)}]

grade_filters = [ lambda grade: grade >= 90, lambda grade : grade >= 50, lambda grade : grade >= 30,
                  lambda grade : grade < 30]

def student_main():


    def studentgrades(studentss, filterr):
        return list(filter(filterr, studentss))




