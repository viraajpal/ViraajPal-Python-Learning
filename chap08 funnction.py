# marks = [34, 77, 99, 88]
# percentage1 = (sum(marks)/400)*100
#
# marks2 = [76, 77, 99, 88]
# percentage2 = (sum(marks2)/400)*100
# print(percentage1, percentage2)
#
# marks = [34, 77, 99, 88]
# percentage1 =((marks[0] +marks[1] +marks[2] +marks[3])/400)*100
#
# marks2 = [76, 77, 99, 88]
# percentage2 = ((marks2[0] +marks2[1] +marks2[2] +marks2[3])/400)*100
# print(percentage1, percentage2)


def percent(marks):
    p = ((marks[0] +marks[1] +marks[2] +marks[3])/400)*100
    return p
marks1 = [34, 77, 99, 88]

percentage1 = percent(marks1)

marks2 = [76, 77, 99, 88]
percentage2 = percent(marks2)
print(percentage1, percentage2)