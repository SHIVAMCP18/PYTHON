marks = {
    "Shivam" : 100,
    "Utkarsh" : 90,
    "Om" : 80,
    "list" : [1 , 2 , 3]
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Shivam" : 99})
print(marks)

print(marks.get("Shivam1")) # Prints None
print(marks["Shivam1"]) #Returns an error