#!/usr/bin/env python3
"""
Loan Calculator for Business Plan

Calculates monthly payment, annual payment, and total interest for a loan.
"""

def calculate_loan_payment(principal, annual_rate, years):
    """
    Calculate loan payment details.
    
    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate (as decimal, e.g., 0.095 for 9.5%)
        years (int): Loan term in years
    
    Returns:
        dict: Dictionary containing payment details
    """
    monthly_rate = annual_rate / 12
    months = years * 12
    
    # Calculate monthly payment
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    
    # Calculate annual payment and total interest
    annual_payment = monthly_payment * 12
    total_payment = annual_payment * years
    total_interest = total_payment - principal
    
    return {
        'principal': principal,
        'annual_rate': annual_rate,
        'years': years,
        'monthly_payment': monthly_payment,
        'annual_payment': annual_payment,
        'total_payment': total_payment,
        'total_interest': total_interest
    }

def print_loan_details(details):
    """
    Print formatted loan details.
    
    Args:
        details (dict): Loan payment details
    """
    print(f"Loan Amount: ${details['principal']:,.2f}")
    print(f"Interest Rate: {details['annual_rate']*100:.2f}%")
    print(f"Loan Term: {details['years']} years")
    print(f"Monthly Payment: ${details['monthly_payment']:,.2f}")
    print(f"Annual Payment: ${details['annual_payment']:,.2f}")
    print(f"Total Payment: ${details['total_payment']:,.2f}")
    print(f"Total Interest: ${details['total_interest']:,.2f}")

def generate_amortization_schedule(principal, annual_rate, years):
    """
    Generate an amortization schedule.
    
    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate (as decimal)
        years (int): Loan term in years
    
    Returns:
        list: List of dictionaries containing yearly amortization details
    """
    monthly_rate = annual_rate / 12
    months = years * 12
    
    # Calculate monthly payment
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    
    # Generate yearly schedule
    schedule = []
    balance = principal
    
    for year in range(1, years + 1):
        year_interest = 0
        year_principal = 0
        
        # Calculate payments for each month in the year
        for month in range(1, 13):
            interest_payment = balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            year_interest += interest_payment
            year_principal += principal_payment
            balance -= principal_payment
            
            # Break if balance is paid off
            if balance <= 0:
                balance = 0
                break
        
        schedule.append({
            'year': year,
            'beginning_balance': principal if year == 1 else schedule[-1]['ending_balance'],
            'principal_payment': year_principal,
            'interest_payment': year_interest,
            'total_payment': year_principal + year_interest,
            'ending_balance': balance
        })
        
        # Break if balance is paid off
        if balance <= 0:
            break
    
    return schedule

def print_amortization_table(schedule):
    """
    Print formatted amortization table.
    
    Args:
        schedule (list): Amortization schedule
    """
    print("\nAmortization Schedule:")
    print("-" * 80)
    print(f"{'Year':<4} {'Beginning':<12} {'Principal':<12} {'Interest':<12} {'Total':<12} {'Ending':<12}")
    print(f"{'':<4} {'Balance':<12} {'Payment':<12} {'Payment':<12} {'Payment':<12} {'Balance':<12}")
    print("-" * 80)
    
    for row in schedule:
        print(f"{row['year']:<4} "
              f"${row['beginning_balance']:>10,.0f} "
              f"${row['principal_payment']:>10,.0f} "
              f"${row['interest_payment']:>10,.0f} "
              f"${row['total_payment']:>10,.0f} "
              f"${row['ending_balance']:>10,.0f}")

if __name__ == "__main__":
    # Loan details for Olney GI Associates
    principal = 493400  # $493,400 loan
    annual_rate = 0.095  # 9.5% interest rate
    years = 10  # 10-year term
    
    # Calculate loan payment details
    loan_details = calculate_loan_payment(principal, annual_rate, years)
    
    print("LOAN PAYMENT CALCULATION")
    print("=" * 30)
    print_loan_details(loan_details)
    
    # Generate and print amortization schedule
    schedule = generate_amortization_schedule(principal, annual_rate, years)
    print_amortization_table(schedule)