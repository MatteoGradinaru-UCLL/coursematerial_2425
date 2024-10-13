def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    
    skipped_test=0
    taken_test=0
    total_grade=0

    if grade1 is not None:
        taken_test += 1
        total_grade += grade1

    else:
        skipped_test += 1


    if grade2 is not None:
        taken_test += 1
        total_grade += grade2

    else:
        skipped_test += 1


    if grade3 is not None:
        taken_test += 1
        total_grade += grade3

    else:
        skipped_test += 1

    if grade4 is not None:
        taken_test += 1
        total_grade += grade4

    else:
        skipped_test += 1


    if grade5 is not None:
        taken_test += 1
        total_grade += grade5

    else:
        skipped_test += 1



    if skipped_test >= 2:
        return False

    if (total_grade / taken_test) >= 12:
        return True
    else:
        return False


print(entrance_exam(12, 12, 12, 12, 12))
print(entrance_exam(12, 12, 12, None, 12))
print(entrance_exam(12, 12, 12, 2, 12))
print(entrance_exam(20, 20, 20, None, None))