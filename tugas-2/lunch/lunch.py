class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        while any(s == sandwiches[0] for s in students):
            student =  students.pop(0)
            if student == sandwiches[0]:
                sandwiches.pop(0)
                continue
            else:
                students.append(student)
        return len(students)