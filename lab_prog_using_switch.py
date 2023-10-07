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
        try:
            new_age = int(input("Enter new age: "))
        except Exception as e:
            print("Age must be of integer type")
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

def delete_record():
    name_to_delete = input("Enter the name of the patient to delete: ")
    
    # Check if the name exists in the database before proceeding
    if collection.find_one({"name": name_to_delete}):
        query = {"name": name_to_delete}

        try:
            deleted_record = collection.delete_one(query)
            if deleted_record.deleted_count > 0:
                print("Patient record deleted successfully.")
            else:
                print("No records matched the query.")
        except Exception as e:
            print(f"Error: {str(e)}")
    else:
        print(f"Invalid key - Name: {name_to_delete} not found in the database.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Create a patient record")
        print("2. Read patient records")
        print("3. Update a patient record")
        print("4. Delete a patient record")
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
            print("Invalid choice. Please select a valid option.")
