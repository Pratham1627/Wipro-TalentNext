# Read purchase details from a file and calculate the bill.
try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")

    lines = file.readlines()

    file.close()

    items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        data = line.split()

        # Check for discount line
        if data[0].lower() == "discount":
            discount = int(data[1])

        # Check for free items
        elif data[1].lower() == "free":
            free_items += 1

        # Paid items
        else:
            items += 1
            amount += int(data[1])

    final_amount = amount - discount

    print("No of items purchased:", items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("File does not exist.")

except Exception as e:
    print("Error:", e)
