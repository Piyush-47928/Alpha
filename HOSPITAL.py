
import mysql.connector

class HospitalManagementSystem:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.create_patient_table()

    def create_patient_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                pID VARCHAR(5) PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                gender VARCHAR(10),
                diagnosis VARCHAR(255),
                admitted DATE,
                discharge DATE
            )
        """)
        self.conn.commit()

    def add_patient(self, pID, name, age, gender, diagnosis, admitted):
        self.cursor.execute("""
            INSERT INTO patients (pID, name, age, gender, diagnosis, admitted)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (pID, name, age, gender, diagnosis, admitted))
        self.conn.commit()

    def get_all_patients(self):
        self.cursor.execute("SELECT * FROM patients")
        return self.cursor.fetchall()

    def search_patient(self, p_ID):
        self.cursor.execute("SELECT * FROM patients WHERE pID = %s", (p_ID,))
        return self.cursor.fetchall()

    def delete_patient(self, p_ID):
        self.cursor.execute("DELETE FROM patients WHERE pID = %s", (p_ID,))
        print("Data deleted successfully")
        self.conn.commit()

    def update_name(self, nme, p_ID):
        self.cursor.execute("UPDATE patients SET name = %s WHERE pID = %s", (nme, p_ID))
        print("Data updated successfully")
        self.conn.commit()

    def update_age(self, age, p_ID):
        self.cursor.execute("UPDATE patients SET age = %s WHERE pID = %s", (age, p_ID))
        print("Data updated successfully")
        self.conn.commit()

    def update_diagnosis(self, dig, p_ID):
        self.cursor.execute("UPDATE patients SET diagnosis = %s WHERE pID = %s", (dig, p_ID))
        print("Data updated successfully")
        self.conn.commit()

    def update_discharge_date(self, dchg, p_ID):
        self.cursor.execute("UPDATE patients SET discharge = %s WHERE pID = %s", (dchg, p_ID))
        print("Data updated successfully")
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def create_staff_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS staff (
                staffID VARCHAR(5) PRIMARY KEY,
                name VARCHAR(255),
                position VARCHAR(255),
                department VARCHAR(255)
            )
        """)
        self.conn.commit()

    def add_staff(self, staffID, name, position, department):
        self.cursor.execute("""
            INSERT INTO staff (staffID, name, position, department)
            VALUES (%s, %s, %s, %s)
        """, (staffID, name, position, department))
        self.conn.commit()

    def get_all_staff(self):
        self.cursor.execute("SELECT * FROM staff")
        return self.cursor.fetchall()

    def search_staff(self, staff_ID):
        self.cursor.execute("SELECT * FROM staff WHERE staffID = %s", (staff_ID,))
        return self.cursor.fetchall()

    def delete_staff(self, staff_ID):
        self.cursor.execute("DELETE FROM staff WHERE staffID = %s", (staff_ID,))
        print("Staff data deleted successfully")
        self.conn.commit()

    def update_name(self, name, staff_ID):
        self.cursor.execute("UPDATE staff SET name = %s WHERE staffID = %s", (name, staff_ID))
        print("Staff data updated successfully")
        self.conn.commit()

    def update_position(self, position, staff_ID):
        self.cursor.execute("UPDATE staff SET position = %s WHERE staffID = %s", (position, staff_ID))
        print("Staff data updated successfully")
        self.conn.commit()

    def update_department(self, department, staff_ID):
        self.cursor.execute("UPDATE staff SET department = %s WHERE staffID = %s", (department, staff_ID))
        print("Staff data updated successfully")
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def create_stock_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS medicine_stock (
                medicineID VARCHAR(5) PRIMARY KEY,
                name VARCHAR(255),
                quantity INT,
                unit_price DECIMAL(10, 2)
            )
        """)
        self.conn.commit()

    def add_medicine(self, medicineID, name, quantity, unit_price):
        self.cursor.execute("""
            INSERT INTO medicine_stock (medicineID, name, quantity, unit_price)
            VALUES (%s, %s, %s, %s)
        """, (medicineID, name, quantity, unit_price))
        self.conn.commit()

    def get_all_medicines(self):
        self.cursor.execute("SELECT * FROM medicine_stock")
        return self.cursor.fetchall()

    def search_medicine(self, medicineID):
        self.cursor.execute("SELECT * FROM medicine_stock WHERE medicineID = %s", (medicineID,))
        return self.cursor.fetchall()

    def delete_medicine(self, medicineID):
        self.cursor.execute("DELETE FROM medicine_stock WHERE medicineID = %s", (medicineID,))
        print("Medicine data deleted successfully")
        self.conn.commit()

    def update_quantity(self, quantity, medicineID):
        self.cursor.execute("UPDATE medicine_stock SET quantity = %s WHERE medicineID = %s", (quantity, medicineID))
        print("Medicine data updated successfully")
        self.conn.commit()

    def update_unit_price(self, unit_price, medicineID):
        self.cursor.execute("UPDATE medicine_stock SET unit_price = %s WHERE medicineID = %s", (unit_price, medicineID))
        print("Medicine data updated successfully")
        self.conn.commit()



def main():
    host = "localhost"  # Corrected the host name
    user = "root"
    password = "RADUPIAS"
    database = "hospital_management"

    hospital_system = HospitalManagementSystem(host, user, password, database)

    try:
        print('''
            ========================================================
            ========================================================
            -----------------WELCOME TO HOSPITAL DATABASE-----------------------------
            ========================================================
            ========================================================
            ''')
        pswrd = "HOSPITAL"
        b = input("Enter the password please:")  # password = HOSPITAL
        if b == pswrd:
            while True:
                print('''
                    Enter A - Using database related to patient
                    Enter B - Using Database related to staff
                    Enter C - Using database related to Medicine
                    Enter D - Exit
                ''')
                dec = input("Enter your option:")

                if dec=="A":
                    print('''==================================================
                                  ==================================================
                                   ----------------WELCOME TO PATIENT DATABASE---------------------
                                  ==================================================
                                  ==================================================
                          ''')
                    print('''
                        Enter 1 - For adding a new patient to the database.
                        Enter 2 - For searching a patient.
                        Enter 3 - For deleting the patient record.
                        Enter 4 - For updating the patient record.
                        Enter 5 - For entering the discharge date.
                        Enter 6 - Exit
                        ''')
                    a = int(input("Enter your option: "))
                    if a == 1:
                        p_ID = input("Enter patient ID: ")
                        nme = input('Enter the patient name: ')
                        age = int(input('Enter the patient\'s age: '))
                        gen = input("Enter the patient's gender: ")
                        dig = input("Enter the diagnosis: ")
                        dt = input("Enter the date when the patient is admitted in YYYY-MM-DD format: ")
                        hospital_system.add_patient(p_ID, nme, age, gen, dig, dt)
                        print("New patient added successfully")

                    elif a == 2:
                        print('''
                            Enter A- If you want to search all the patients.
                            Enter B - If you want to search a particular patient.
                            ''')
                        srch = input("Enter your option: ")
                        if srch == 'A':
                            print("All Patients:")
                            patients = hospital_system.get_all_patients()
                            for patient in patients:
                                print(patient)
                        elif srch == 'B':
                            trgt_pt = input("Enter patient ID: ")
                            search_result = hospital_system.search_patient(trgt_pt)
                            print("\nSearch Result for ", trgt_pt, ":")
                            for patient in search_result:
                                print(patient)

                    elif a == 3:
                        na = input("Enter the ID of the patient whose record you want to delete: ")
                        hospital_system.delete_patient(na)

                    elif a == 4:
                        print('''
                            Enter A- If you want to update the name.
                            Enter B - If you want to update the age.
                            Enter C - If you want to update the diagnosis.
                            ''')
                        opt = input("Enter your option: ")
                        if opt == 'A':
                            p_ID = input("Enter patient ID: ")
                            nme = input("Enter patient name: ")
                            hospital_system.update_name(nme, p_ID)

                        elif opt == 'B':
                            p_ID = input("Enter patient ID: ")
                            age = int(input("Enter patient age: "))
                            hospital_system.update_age(age, p_ID)

                        elif opt == 'C':
                            p_ID = input("Enter patient ID: ")
                            dig = input("Enter patient diagnosis: ")
                            hospital_system.update_diagnosis(dig, p_ID)

                    elif a == 5:
                        p_ID = input("Enter patient ID: ")
                        dchg = input("Enter the discharge date in YYYY-MM-DD format: ")
                        hospital_system.update_discharge_date(dchg, p_ID)

                    elif a== 6:
                         continue
                    
                    else:
                            print("Invalid option. Please try again.")

                elif dec =="B":
                    print('''==================================================
                                  ==================================================
                                   -----------------WELCOME TO STAFF DATABASE-----------------------
                                   ==================================================
                                   ==================================================
                          ''')
                    print('''
                    Enter 1 - For adding a new staff member.
                    Enter 2 - For searching a staff member.
                    Enter 3 - For deleting a staff member.
                    Enter 4 - For updating staff information.
                    Enter 5 - Exit
                    ''')
                    choice = int(input("Enter your option: "))

                    if choice == 1:
                        staff_ID = input("Enter staff ID: ")
                        name = input("Enter staff name: ")
                        position = input("Enter staff position: ")
                        department = input("Enter staff department: ")
                        hospital_system.add_staff(staff_ID, name, position, department)
                        print("New staff member added successfully")

                    elif choice == 2:
                        staff_ID = input("Enter staff ID to search: ")
                        search_result = hospital_system.search_staff(staff_ID)
                        print("\nSearch Result for Staff ID", staff_ID, ":")
                        for staff_member in search_result:
                            print(staff_member)

                    elif choice == 3:
                        staff_ID = input("Enter staff ID to delete: ")
                        hospital_system.delete_staff(staff_ID)

                    elif choice == 4:
                        print('''
                            Enter A - If you want to update the name.
                            Enter B - If you want to update the position.
                            Enter C - If you want to update the department.
                            ''')
                        update_option = input("Enter your option: ")
                        staff_ID = input("Enter staff ID: ")

                        if update_option == 'A':
                            name = input("Enter new name: ")
                            hospital_system.update_name(name, staff_ID)

                        elif update_option == 'B':
                            position = input("Enter new position: ")
                            hospital_system.update_position(position, staff_ID)

                        elif update_option == 'C':
                            department = input("Enter new department: ")
                            hospital_system.update_department(department, staff_ID)

                        elif a== 5:
                         continue

                        else:
                            print("Invalid option. Please try again.")

                elif dec == "C":
                    print('''==================================================
                                  ==================================================
                                  --------------------WELCOME TO MEDICINE DATABASE---------------
                                  ==================================================
                                  ==================================================
                          ''')
                    print('''
                            Enter 1 - For adding a new medicine to the stock.
                            Enter 2 - For searching a medicine in the stock.
                            Enter 3 - For deleting a medicine from the stock.
                            Enter 4 - For updating medicine information.
                            Enter 5 - Exit
                            ''')
                    choice = int(input("Enter your option: "))

                    if choice == 1:
                        
                        medicineID = input("Enter medicine ID: ")
                        name = input("Enter medicine name: ")
                        quantity = int(input("Enter quantity: "))
                        unit_price = float(input("Enter unit price: "))
                        hospital_system.add_medicine(medicineID, name, quantity, unit_price)
                        print("New medicine added to the stock successfully")

                    elif choice == 2:
                        medicineID = input("Enter medicine ID to search: ")
                        search_result = hospital_system.search_medicine(medicineID)
                        print("\nSearch Result for Medicine ID", medicineID, ":")
                        for medicine in search_result:
                            print(medicine)

                    elif choice == 3:
                        medicineID = input("Enter medicine ID to delete: ")
                        hospital_system.delete_medicine(medicineID)

                    elif choice == 4:
                        print('''
                            Enter A - If you want to update the quantity.
                            Enter B - If you want to update the unit price.
                            ''')
                        update_option = input("Enter your option: ")
                        medicineID = input("Enter medicine ID: ")

                        if update_option == 'A':
                            quantity = int(input("Enter new quantity: "))
                            hospital_system.update_quantity(quantity, medicineID)

                        elif update_option == 'B':
                            unit_price = float(input("Enter new unit price: "))
                            hospital_system.update_unit_price(unit_price, medicineID)

                        elif a== 5:
                         continue

                        else:
                            print("Invalid option. Please try again.")
    
                elif dec == "D":
                    print('''
                        =====================================================
                        =====================================================
                        -----------Thank you for using the Hospital database---------------------
                        =====================================================
                        =====================================================
                        ''')
                    hospital_system.close_connection()
                    break

                else:
                            print("Invalid option. Please try again.")

        else:
            print("Enter the correct password")

    except mysql.connector.Error as err:
        print("Error:", err)

if __name__ == "__main__":
    main()
