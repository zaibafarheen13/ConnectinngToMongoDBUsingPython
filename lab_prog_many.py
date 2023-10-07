import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["healthcare_database"]
collection = db["patients"]

def create_record():
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    gender = input("Enter patient's gender: ")
    condition = input("Enter patient's condition: ")
    doctor = input("Enter patient's doctor: ")

    data = {
        "name": name,
        "age": age,
        "gender": gender,
        "condition": condition,
        "doctor": doctor
    }

    try:
        inserted_record = collection.insert_one(data)
        print(f"Patient record with ID {inserted_record.inserted_id} created successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

def create_records():
    num_records = int(input("Enter the number of patient records to create: "))
    records = []

    for _ in range(num_records):
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        gender = input("Enter patient's gender: ")
        condition = input("Enter patient's condition: ")
        doctor = input("Enter patient's doctor: ")

        data = {
            "name": name,
            "age": age,
            "gender": gender,
            "condition": condition,
            "doctor": doctor
        }
        records.append(data)

    try:
        inserted_records = collection.insert_many(records)
        print(f"{len(inserted_records.inserted_ids)} patient records created successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

def read_records():
    try:
        records = collection.find()
        for record in records:
            print(f"Name: {record['name']}, Age: {record['age']}, Gender: {record['gender']}, Condition: {record['condition']}, Doctor: {record['doctor']}")
    except Exception as e:
        print(f"Error: {str(e)}")

def update_record():
    existing_name = input("Enter the name of the existing patient record to update: ")
    
    # Check if the name exists in the database before proceeding
    if collection.find_one({"name": existing_name}):
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_gender = input("Enter new gender: ")
        new_condition = input("Enter new condition: ")
        new_doctor = input("Enter new doctor: ")

        query = {"name": existing_name}
        new_data = {
            "$set": {
                "name": new_name,
                "age": new_age,
                "gender": new_gender,
                "condition": new_condition,
                "doctor": new_doctor
            }
        }

        try:
            updated_record = collection.update_one(query, new_data)
            if updated_record.modified_count > 0:
                print("Patient record updated successfully.")
            else:
                print("No records matched the query.")
        except Exception as e:
            print(f"Error: {str(e)}")
    else:
        print(f"Invalid key - Name: {existing_name} not found in the database.")

def update_records_by_age():
    age_to_update = int(input("Enter the age to update records for: "))
    new_doctor = input("Enter the new doctor: ")

    query = {"age": age_to_update}
    new_data = {"$set": {"doctor": new_doctor}}

    try:
        updated_records = collection.update_many(query, new_data)
        print(f"{updated_records.modified_count} patient records updated successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

def retrieve_records_by_name():
    name_to_retrieve = input("Enter the name to retrieve records for: ")

    try:
        records = collection.find({"name": name_to_retrieve})
        for record in records:
            print(f"Name: {record['name']}, Age: {record['age']}, Gender: {record['gender']}, Condition: {record['condition']}, Doctor: {record['doctor']}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Create a patient record")
        print("2. Create multiple patient records")
        print("3. Read patient records")
        print("4. Update a patient record")
        print("5. Update records by age")
        print("6. Retrieve records by name")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_record()
        elif choice == "2":
            create_records()
        elif choice == "3":
            read_records()
        elif choice == "4":
            update_record()
        elif choice == "5":
            update_records_by_age()
        elif choice == "6":
            retrieve_records_by_name()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please select a valid option.")
