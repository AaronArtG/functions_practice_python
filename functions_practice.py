def hello():
    print("hello, user!")

hello()

def pack(arg1, arg2, arg3):
    packed_list = [arg1, arg2, arg3]
    return packed_list

result = pack("apple", 42, True)
print(result)

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {food_list[0]}")
        for food in food_list[1:]:
            print(f"Next I eat {food}")

lunch = ["sandwich", "chips", "apple"]
eat_lunch(lunch)