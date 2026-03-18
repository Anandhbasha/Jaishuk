person = {
    "stuName":"xyz",
    "studentRollNumber":"111ME105",
    "Std":"10th",
    "TotalMarks":80.56,
    "Mobile":978424650,
    "Attendence":True,
    "family":{
        "mom":"abc",
        "dad":"def",
        "siblings":{
            "sister":"jkh",
            "brother":"hyj"
        }
    }
}

print(person["stuName"],person["Mobile"])
# print(person["family"])
# print(person["family"]["siblings"])
print(person["family"]["siblings"]["brother"])