def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("🩺 BMI (Body Mass Index) Calculator")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        
        bmi = calculate_bmi(weight, height)
        category = interpret_bmi(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Health Status: {category}")
    except ValueError:
        print("⚠️ Please enter valid numerical values.")

if __name__ == "__main__":
    main()