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

def calculate_break_even(fixed_monthly_costs, revenue_per_patient):
    """
    Calculate the number of patients needed to break even.
    
    Args:
        fixed_monthly_costs (float): Total fixed monthly costs
        revenue_per_patient (float): Average revenue per patient
    
    Returns:
        float: Number of patients needed per month to break even
    """
    if revenue_per_patient <= 0:
        raise ValueError("Revenue per patient must be greater than zero")
    
    return fixed_monthly_costs / revenue_per_patient

def print_break_even_analysis():
    """
    Print break-even analysis based on business plan data.
    """
    print("\nBREAK-EVEN ANALYSIS")
    print("=" * 30)
    
    # Constants based on business plan data
    FIXED_MONTHLY_COSTS = 47160  # ~$47,160/month from business plan
    YEAR_2_CONCIERGE_MEMBERS = 100  # Avg members active during Year 2
    YEAR_2_INSURANCE_VISITS_PER_MONTH = 100  # Insurance visits per month in Year 2
    YEAR_2_MEMBER_VISITS_PER_MONTH = 80  # Member visits billed per month in Year 2
    YEAR_2_CONCIERGE_MEMBERSHIP_FEE = 2400  # Annual membership fee per concierge member
    YEAR_2_AVERAGE_REIMBURSEMENT = 225  # Average reimbursement per insurance visit
    WORKING_DAYS_PER_MONTH = 22  # Typical business days in a month
    BUSINESS_PLAN_BREAK_EVEN_CONCIERGE = 110  # Concierge members in business plan break-even scenario
    BUSINESS_PLAN_BREAK_EVEN_INSURANCE_VISITS = 100  # Insurance visits in business plan break-even scenario
    
    # Calculate revenue components from business plan data
    YEAR_2_MEMBERSHIP_REVENUE = YEAR_2_CONCIERGE_MEMBERS * YEAR_2_CONCIERGE_MEMBERSHIP_FEE  # $240,000
    YEAR_2_INSURANCE_REVENUE = YEAR_2_INSURANCE_VISITS_PER_MONTH * 12 * YEAR_2_AVERAGE_REIMBURSEMENT  # $270,000
    YEAR_2_MEMBER_VISIT_REVENUE = YEAR_2_MEMBER_VISITS_PER_MONTH * 12 * YEAR_2_AVERAGE_REIMBURSEMENT  # $216,000
    
    # Calculate total Year 2 revenue from components
    YEAR_2_TOTAL_REVENUE = YEAR_2_MEMBERSHIP_REVENUE + YEAR_2_INSURANCE_REVENUE + YEAR_2_MEMBER_VISIT_REVENUE  # $726,000
    
    # Calculate revenue per unit from business plan data
    # Average revenue per concierge member per month
    avg_revenue_per_concierge = YEAR_2_MEMBERSHIP_REVENUE / 12 / YEAR_2_CONCIERGE_MEMBERS  # $200/month per concierge member
    
    # Total insurance visits per month = insurance visits + member visits
    total_insurance_visits_per_month = YEAR_2_INSURANCE_VISITS_PER_MONTH + YEAR_2_MEMBER_VISITS_PER_MONTH  # 180 visits/month
    
    # Total insurance-related revenue for Year 2
    total_insurance_revenue = YEAR_2_INSURANCE_REVENUE + YEAR_2_MEMBER_VISIT_REVENUE  # $486,000
    
    # Average revenue per insurance visit
    avg_revenue_per_insurance_visit = total_insurance_revenue / 12 / total_insurance_visits_per_month  # $225/visit
    
    print(f"Fixed Monthly Costs: ${FIXED_MONTHLY_COSTS:,}")
    
    print(f"\nRevenue Per Unit (Year 2 Data):")
    print(f"Average Revenue per Concierge Member: ${avg_revenue_per_concierge:,.0f}/month")
    print(f"Average Revenue per Insurance Visit: ${avg_revenue_per_insurance_visit:,.0f}/visit")
    
    # Calculate break-even points
    concierge_break_even = calculate_break_even(FIXED_MONTHLY_COSTS, avg_revenue_per_concierge)
    insurance_break_even = calculate_break_even(FIXED_MONTHLY_COSTS, avg_revenue_per_insurance_visit)
    
    print(f"\nBreak-even Points:")
    print(f"Concierge Members Needed: {concierge_break_even:.0f} members")
    print(f"Insurance Visits Needed: {insurance_break_even:.0f} visits/month")
    
    # Business plan projection: 6-7 patients/day to break even in Year 2
    patients_per_day = insurance_break_even / WORKING_DAYS_PER_MONTH
    
    print(f"Daily Patients Needed: {patients_per_day:.1f} patients/day")
    
    # Business plan also mentions break-even with 110 concierge members + 100 insurance visits/month
    business_plan_revenue = (BUSINESS_PLAN_BREAK_EVEN_CONCIERGE * avg_revenue_per_concierge + 
                            BUSINESS_PLAN_BREAK_EVEN_INSURANCE_VISITS * avg_revenue_per_insurance_visit)
    
    print(f"\nBusiness Plan Break-even Scenario:")
    print(f"{BUSINESS_PLAN_BREAK_EVEN_CONCIERGE} concierge members + {BUSINESS_PLAN_BREAK_EVEN_INSURANCE_VISITS} insurance visits/month = ${business_plan_revenue:,.0f}/month")
    print(f"Note: Business plan projects break-even in Month 18-22 (Year 2)")

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
    
    # Print break-even analysis
    print_break_even_analysis()
