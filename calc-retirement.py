# Console program to calculate the money that need to save now for our retirement.

# Function to calculate the future value based on inflation
def calculate_future_value(today_value, inflation_rate, years):
    future_value = today_value * (1 + inflation_rate) ** years
    return future_value

# Function to calculate the balance needed to live on a monthly basis at age 65
def calculate_required_balance(monthly_expense, years_to_live, annual_return_rate):
    # Assuming that the balance is invested and earns interest (e.g., annual return rate)
    # Using the Present Value formula for annuities to calculate the required balance
    return monthly_expense * ((1 - (1 + annual_return_rate/12) ** (-years_to_live * 12)) / (annual_return_rate / 12))

# Function to calculate the monthly savings needed to reach the required balance
def calculate_monthly_savings(required_balance, years_until_65, annual_return_rate):
    months_until_65 = years_until_65 * 12
    # Using Future Value formula for regular monthly savings
    monthly_savings = required_balance / (((1 + annual_return_rate/12) ** months_until_65 - 1) / (annual_return_rate / 12))
    return monthly_savings

# Main Program
def main():
    # Input: Amount you want to live on today (in today's dollars)
    today_value = float(input("How much in today's dollars do you want to live on monthly? $"))

    # Constants
    inflation_rate = 0.03  # 3% inflation rate
    annual_return_rate = 0.05  # 5% annual return rate on savings/investments
    current_age = int(input("What is your current age? "))
    target_age = 65  # Age when you want to calculate the future value

    # Calculate the number of years until you turn 65
    years_until_65 = target_age - current_age

    # Calculate the future monthly expense at age 65
    future_monthly_expense = calculate_future_value(today_value, inflation_rate, years_until_65)

    # Assume you need 30 years of retirement (for example, from 65 to 95)
    years_to_live = 30  # Adjust if you want to simulate a different retirement duration

    # Calculate the required balance at age 65 to support that future monthly expense
    required_balance = calculate_required_balance(future_monthly_expense, years_to_live, annual_return_rate)

    # Calculate the monthly savings required to reach that balance by age 65
    monthly_savings = calculate_monthly_savings(required_balance, years_until_65, annual_return_rate)

    # Output the results
    print(f"\n1) At 3% inflation, your monthly expense at age 65 will be: ${future_monthly_expense:,.2f}")
    print(f"2) You will need a balance of: ${required_balance:,.2f} at age 65 to live on that monthly.")
    print(f"3) To reach your goal, you need to save: ${monthly_savings:,.2f} each month until you turn 65.")

# Run the program
if __name__ == "__main__":
    main()
