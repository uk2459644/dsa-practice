
class Solution:
    def countStudents(self,students:list[int],sandwiches:list[int]):
        while len(students)>0:
            if sandwiches[0]==students[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                tp=students.pop(0)
                students.append(tp)
            
            if len(sandwiches)>0 and sandwiches[0] not in students:
                break

            return len(students)





