sub1 = int(input("Enter first subject\n"))
sub2 = int(input("Enter second subjest\n"))
sub3 = int(input("Enter third subjest\n"))

if(sub1<33 or sub2<33 or sub3<33):

    print("you r fail")

elif(sub1+sub2+sub3)/3 < 40:

    print("you r fail due to total percentage less than 40")

else:

    print("congratulation! you r pass in the examination")
