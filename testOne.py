# create amd call a function that prints your name
# execute the script


def display_name():
    print("David")


def list_one():
    print("Working with lists (arrays)")
    names = ["David", "John"]
    # add values to the list
    names.append("Juan")
    names.append("Carlos")
    # get the values
    print(names[0])
    print(names[3])

    print(names)

    # for loop
    for i in names:
        print(i)


def list_two():
    print("-" * 30)

    nums = [123, 456, 123, 3456, 6, 689, 23, 6, 8, 7887, 123, 46, 3, 89, 12, 9, 9, 565, 8, 33, 1, -200, 23]
    result = 0
    for i in nums:
        result += i
    print(result)

    # print numbers lowers than 50
    # count how many numbers are lower than 50
    count = 0
    for i in nums:
        if i < 50:
            print(i)
            count += 1
    print(f"There are: {count} nums lower than 50")
    # find the smallest number in the list
    # variable that start with any number from the list (first)
    # for loop
    # compare if the num is lower that your smallest number
    smallest = nums[0]
    for i in nums:
        if i < smallest:
            smallest = i
    print(f"The smallest in the list is: {smallest}")


def dict_one():
    print("Dictionary tests ONE -----------------")

    me = {
        "name": "David",
        "last": "Paredes",
        "age": 33,
        "occupation": "Package Handler",
        "hobbies": [],
        "address": {
            "street": "Walker",
            "number": 2345,
            "city": "Ranger"
        }
    }

    print(me["name"] + " " + me["last"])
    me["email"] = "davewalls329@gmail.com"
    print(me)

    #print the full address in a single line

    full_address = ""
    for key, value in me["address"].items():
        full_address += f"{key}: {value} "
    print(full_address)


display_name()
list_one()
list_two()
dict_one()
