import datetime

# function definition
def prepare_khinkali():
    # function body
    print("ვამზადებ ხორცს")
    print("ვამზადებ ცომს")
    print("ხორცი დავდე ცომზე")
    print("ვუკეთებ ნაოჭებს")
    timestamp = datetime.datetime.now()
    return timestamp


def make_batch_of_khinkali(count = 20):
    # count is parameter that is kinda like a variable
    # that can be set from outside
    # count is now a default value
    plate = []
    # plate variable shadows global "plate" variable

    for i in range(count):
        khinkali_preparation_date = prepare_khinkali()
        plate.append(khinkali_preparation_date)
        print(khinkali_preparation_date)

    return plate


# function call
plate = make_batch_of_khinkali()
# plate is a global variabla that can be access by all functions

print(f"We have {len(plate)} khinkali on plate")
print(f"First khinkali in this batch was created on: {plate[0]}")


for i in range(5):
    print("Ate khinkali")
    stem = plate.pop()
    print(f"I ate khinkali: {stem}")


# plate2 = make_batch_of_khinkali(10)
# for i in range(len(plate2)):
#     plate.append(plate2.pop())
# print(f"We have {len(plate2)} khinkali on plate 2")
plate.extend(make_batch_of_khinkali(10))

print(f"We have {len(plate)} khinkali on plate")


print(print("Hello"))