import requests

vehicle_number = input("Enter Vehicle Number: ").strip().upper()

API_URL = "https://dummyjson.com/c/054f-472e-4910-bc3e"
response = requests.get(API_URL)
vehicles = response.json()

vehicle_found = False
for vehicle in vehicles:

    if vehicle["registration_number"].upper() == vehicle_number:
        vehicle_found = True

        print("\n" + "=" * 40)
        print("         VEHICLE DETAILS")
        print("=" * 40)

        print("Registration Number :", vehicle["registration_number"])
        print("Owner               :", vehicle["owner"])
        print("Manufacturer        :", vehicle["manufacturer"])
        print("Model               :", vehicle["model"])
        print("Fuel Type           :", vehicle["fuel_type"])
        print("Color               :", vehicle["color"])
        print("RTO                 :", vehicle["rto"])
        print("Insurance Valid     :", vehicle["insurance_valid"])
        print("PUC Valid           :", vehicle["puc_valid"])

        print("=" * 40)
        break
    
if not vehicle_found:
    print("\nVehicle not found!")