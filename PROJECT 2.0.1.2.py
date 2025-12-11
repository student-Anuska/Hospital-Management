import pickle

# ---------------- PATIENT FUNCTIONS ----------------

# Insert new patient
def insertPatient():
    name = input("Enter patient's name: ")
    patientID = int(input("Enter Patient ID: "))
    phoneNo = int(input("Enter phone number: "))
    disease = input("Enter disease: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")

    rec = {
        'patientID': patientID,
        'name': name,
        'phoneNo': phoneNo,
        'disease': disease,
        'age': age,
        'gender': gender
    }

    f = open('hospital.dat', 'ab')
    pickle.dump(rec, f)
    f.close()
    print("Patient record added successfully!\n")


# Display all patients
def displayPatients():
    try:
        f = open('hospital.dat', 'rb')
    except FileNotFoundError:
        print("No patient records found!\n")
        return

    while True:
        try:
            rec = pickle.load(f)
            print("Patient Name:", rec['name'])
            print("Patient ID:", rec['patientID'])
            print("Gender:", rec['gender'])
            print("Disease:", rec['disease'])
            print("Age:", rec['age'])
            print("---------------------------")
        except EOFError:
            break
    f.close()


# Search patient by ID
def searchPatientID(patientID):
    try:
        f = open('hospital.dat', 'rb')
    except FileNotFoundError:
        print("No patient records found!")
        return

    found = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['patientID'] == patientID:
                print("Patient ID:", rec['patientID'])
                print("Name:", rec['name'])
                print("Disease:", rec['disease'])
                print("Age:", rec['age'])
                found = True
        except EOFError:
            break
    f.close()

    if not found:
        print("SORRY! No patient found.\n")


# Delete patient
def deleteRec(patientID):
    try:
        f = open('hospital.dat', 'rb')
    except FileNotFoundError:
        print("No patient records found!")
        return

    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()

    f = open('hospital.dat', 'wb')
    for x in reclst:
        if x['patientID'] == patientID:
            continue
        pickle.dump(x, f)
    f.close()
    print("Patient deleted successfully!\n")



# ---------------- DOCTOR FUNCTIONS ----------------

# Add Doctor
def addDoctor():
    doctorID = int(input("Enter Doctor ID: "))
    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    timing = input("Enter Timing: ")

    rec = {
        'doctorID': doctorID,
        'name': name,
        'specialization': specialization,
        'timing': timing
    }

    f = open('doctor.dat', 'ab')
    pickle.dump(rec, f)
    f.close()
    print("Doctor added successfully!\n")


# Display Doctors
def displayDoctors():
    try:
        f = open('doctor.dat', 'rb')
    except FileNotFoundError:
        print("No doctor records found!\n")
        return

    while True:
        try:
            rec = pickle.load(f)
            print("Doctor ID:", rec['doctorID'])
            print("Name:", rec['name'])
            print("Specialization:", rec['specialization'])
            print("Timing:", rec['timing'])
            print("---------------------------")
        except EOFError:
            break
    f.close()


# Search doctor by ID
def searchDoctor(doctorID):
    try:
        f = open('doctor.dat', 'rb')
    except FileNotFoundError:
        print("No doctor records found!")
        return

    found = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['doctorID'] == doctorID:
                print("Doctor ID:", rec['doctorID'])
                print("Name:", rec['name'])
                print("Specialization:", rec['specialization'])
                print("Timing:", rec['timing'])
                found = True
        except EOFError:
            break
    f.close()

    if not found:
        print("SORRY! No doctor found.\n")


# Delete doctor
def deleteDoctor(doctorID):
    try:
        f = open('doctor.dat', 'rb')
    except FileNotFoundError:
        print("No doctor records found!")
        return

    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()

    f = open('doctor.dat', 'wb')
    for x in reclst:
        if x['doctorID'] == doctorID:
            continue
        pickle.dump(x, f)
    f.close()
    print("Doctor deleted successfully!\n")



# ---------------- BOOKING SYSTEM ----------------

def bookAdoctor():
    try:
        f = open('doctor.dat', 'rb')
    except FileNotFoundError:
        print("No doctors available for booking!")
        return

    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()

    patientID = int(input("Enter Patient ID: "))
    patientName = input("Enter Patient Name: ")
    doctorName = input("Enter Doctor Name: ")
    disease = input("Enter Disease: ")
    payment = float(input("Enter Payment Amount: "))
    timing = input("Enter Preferred Timing: ")

    found = False
    for doc in reclst:
        if doc['name'].lower() == doctorName.lower():
            found = True
            booking = {
                'patientID': patientID,
                'patientName': patientName,
                'doctorName': doctorName,
                'disease': disease,
                'payment': payment,
                'timing': timing
            }

            f = open('booking.dat', 'ab')
            pickle.dump(booking, f)
            f.close()
            print("Doctor booked successfully!\n")
            break

    if not found:
        print("Doctor NOT found! Please check doctor name.\n")



# Show all bookings
def showBookings():
    try:
        f = open('booking.dat', 'rb')
    except FileNotFoundError:
        print("No bookings found!\n")
        return

    while True:
        try:
            rec = pickle.load(f)
            print("Patient ID:", rec['patientID'])
            print("Patient Name:", rec['patientName'])
            print("Doctor Name:", rec['doctorName'])
            print("Disease:", rec['disease'])
            print("Timing:", rec['timing'])
            print("Payment:", rec['payment'])
            print("---------------------------")
        except EOFError:
            break
    f.close()



# ---------------- MENU ----------------

while True:
    print("\n------ Hospital Management System ------")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Search Patient by ID")
    print("4. Delete Patient")
    print("5. Add Doctor")
    print("6. Display Doctors")
    print("7. Search Doctor by ID")
    print("8. Delete Doctor")
    print("9. Book a Doctor")
    print("10. Show All Bookings")
    print("11. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        insertPatient()
    elif ch == 2:
        displayPatients()
    elif ch == 3:
        pid = int(input("Enter Patient ID: "))
        searchPatientID(pid)
    elif ch == 4:
        pid = int(input("Enter Patient ID: "))
        deleteRec(pid)
    elif ch == 5:
        addDoctor()
    elif ch == 6:
        displayDoctors()
    elif ch == 7:
        did = int(input("Enter Doctor ID: "))
        searchDoctor(did)
    elif ch == 8:
        did = int(input("Enter Doctor ID: "))
        deleteDoctor(did)
    elif ch == 9:
        bookAdoctor()
    elif ch == 10:
        showBookings()
    elif ch == 11:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!\n")
