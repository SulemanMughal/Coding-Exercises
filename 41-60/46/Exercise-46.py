def get_best_student(grades):
    return max(grades, key=lambda student: sum(grades[student]))