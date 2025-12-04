import sys

# There must be 4 arguments in total (including program name)
if len(sys.argv) == 4:
    service_date = sys.argv[1]
    service_amount = sys.argv[2]
    service_center = sys.argv[3]

    print("-- CAR SERVICE INVOICE --")
    print(f"Service Date   : {service_date}")
    print(f"Service Amount : ₹{service_amount}")
    print(f"Service Centre : {service_center}")
    print("---- Thank You ----")

else:
    print("Error: Missing Arguments!")
    print("Usage: python invoice.py <service_date> <service_amount> <service_center>")
