import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["mydatabase"]
collection = db["student"]

def create_record():
    usn = input("Enter USN: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    address = input("Enter Address: ")
    addhar = input("Enter Aadhar Number: ")
    record = {"usn": usn, "name": name, "age": age, "address": address, "addhar": addhar}
    collection.insert_one(record)
    print("Record created su3ccessfully!")

def read_records():
    for record in collection.find():
        usn = record.get('usn', "N/A")
        name = record.get('name', "N/A")
        age = record.get('age', "N/A")
        address = record.get('address', "N/A")
        addhar = record.get('addhar', "N/A")
        print(f"USN: {usn}, Name: {name}, Age: {age}, Address: {address}, Aadhar: {addhar}")

def update_record():
    usn_to_update = input("Enter the USN to update: ")
    print("\nSelect the Field to update:")
    fields = {
        "1": "usn",
        "2": "name",
        "3": "age",
        "4": "address",
        "5": "aadhar"
    }
    choice = input("Enter your choice: ")
    if choice in fields:
        new_value = input(f"Enter the new {fields[choice]}: ")
        collection.update_one({"usn": usn_to_update}, {"$set": {fields[choice]: new_value}})
        print("Successfully Updated")
    else:
        print("Invalid choice")

def delete_record():
    usn_to_delete = input("Enter the USN to delete: ")
    collection.delete_one({"usn": usn_to_delete})
    print("Record deleted successfully!")

while True:
    print("\nMenu:")
    print("1. Create Record")
    print("2. Read Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_record()
    elif choice == "2":
        read_records()
    elif choice == "3":
        update_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")