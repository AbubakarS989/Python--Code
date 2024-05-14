
#  We can raise our own errors through raise keyword


height=float(input("Height"))
Weight=int(input("Weight"))
if height>3:
    raise ValueError("Height must be within limits")


BMI=Weight/(height*height)
print(BMI)