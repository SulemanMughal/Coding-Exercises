def get_student_top_notes(students):
    return [max(i['notes'] + [0]) for i in students]