month = input("Enter a month (e.g., January): ").strip().lower()

if month in ["december", "january", "february"]:
    print("It's winter.")
elif month in ["march", "april", "may"]:
    print("It's spring.")
elif month in ["june", "july", "august"]:
    print("It's summer.")
elif month in ["september", "october", "november"]:
    print("It's autumn.")
else:
    print("Invalid month.")
