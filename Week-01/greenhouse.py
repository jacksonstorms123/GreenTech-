print ("===GREENTECH MONITORING SYSTEM===")

temperature = float(input("Enter temperature (C): "))
humidity = float(input("Enter humidity (%): "))
soil = float(input("Enter soil moisture (%): "))

print ("===GREENHOUSE REPORT==")

if temperature > 28:
    print("WARNING: Temperature is too high!")
else:
    print("Temperature: Normal")

if humidity < 40:
    print("WARNING: Humidity is too low!")
else:
    print("Humidity: Normal")

if soil < 30:
    print("WARNING: Soil is too dry")
else:
    print("Soil moisture: Normal")

print ("Monitoring Complete!")