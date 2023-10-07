import argparse
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["healthcare_database"]
collection = db["patients"]

def create_record(args):
    data = {
        "name": args.name,
        "age": args.age,
        "gender": args.gender,
        "condition": args.condition,
        "doctor": args.doctor
    }

    try:
        inserted_record = collection.insert_one(data)
        print(f"Patient record with ID {inserted_record.inserted_id} created successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

def read_records(args):
    try:
        records = collection.find()
        for record in records:
            print(f"Name: {record['name']}, Age: {record['age']}, Gender: {record['gender']}, Condition: {record['condition']}, Doctor: {record['doctor']}")
    except Exception as e:
        print(f"Error: {str(e)}")

def update_record(args):
    query = {"name": args.existing_name}
    new_data = {
        "$set": {
            "name": args.new_name,
            "age": args.new_age,
            "gender": args.new_gender,
            "condition": args.new_condition,
            "doctor": args.new_doctor
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

def delete_record(args):
    query = {"name": args.name_to_delete}

    try:
        deleted_record = collection.delete_one(query)
        if deleted_record.deleted_count > 0:
            print("Patient record deleted successfully.")
        else:
            print("No records matched the query.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Healthcare System Command Line Application")
    subparsers = parser.add_subparsers(title="Subcommands", dest="subcommand")

    # Subparser for create
    create_parser = subparsers.add_parser("create", help="Create a new patient record")
    create_parser.add_argument("--name", required=True, help="Patient's name")
    create_parser.add_argument("--age", required=True, type=int, help="Patient's age")
    create_parser.add_argument("--gender", required=True, help="Patient's gender")
    create_parser.add_argument("--condition", required=True, help="Patient's condition")
    create_parser.add_argument("--doctor", required=True, help="Patient's doctor")

    # Subparser for read
    read_parser = subparsers.add_parser("read", help="Read patient records")

    # Subparser for update
    update_parser = subparsers.add_parser("update", help="Update an existing patient record")
    update_parser.add_argument("--existing_name", required=True, help="Existing patient's name")
    update_parser.add_argument("--new_name", required=True, help="New name")
    update_parser.add_argument("--new_age", required=True, type=int, help="New age")
    update_parser.add_argument("--new_gender", required=True, help="New gender")
    update_parser.add_argument("--new_condition", required=True, help="New condition")
    update_parser.add_argument("--new_doctor", required=True, help="New doctor")

    # Subparser for delete
    delete_parser = subparsers.add_parser("delete", help="Delete a patient record")
    delete_parser.add_argument("--name_to_delete", required=True, help="Name of the patient to delete")

    args = parser.parse_args()

    if args.subcommand == "create":
        create_record(args)
    elif args.subcommand == "read":
        read_records(args)
    elif args.subcommand == "update":
        update_record(args)
    elif args.subcommand == "delete":
        delete_record(args)


# python3 lab_prog.py  create --name "Cavin Stanley" --age 30 --gender "Male" --condition "Condition1" --doctor "Dr. Smith"
# python3 lab_prog.py read
# python3 lab_prog.py update --existing_name "Cavin Stanley" --new_name "Carol Stanley" --new_age 35 --new_gender "Female" --new_condition "Updated Condition" --new_doctor "Updated Doctor"
# python3 lab_prog.py delete --name_to_delete "Carol Stanley"
