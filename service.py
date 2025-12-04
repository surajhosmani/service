import sys

if len(sys.argv) == 4:
    service_date = sys.argv[1]
    service_amount = sys.argv[2]
    service_center = sys.argv[3]

else:
    service_date = "04-12-2025"
    service_amount = "2000"
    service_center = "Hubli"

print("---- CAR SERVICE INVOICE ----")
print(f"Service Date     : {service_date}")
print(f"Service Amount   : {service_amount}")
print(f"Service Centre   : {service_center}")
print("-----------------------------------------")
print("Thank you for servicing your car with us!")
