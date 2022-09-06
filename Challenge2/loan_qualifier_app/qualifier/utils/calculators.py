# -*- coding: utf-8 -*-
"""A Collection of Financial Calculators.
This script contains a variety of financial calculator functions needed to
determine loan qualifications.
"""


# This function implements the following user story:
# As a lender,
# I want to calculate applicant's monthly debt-to-income ratio
# so that we can assess, pre-qualify their ability to pay for the loan
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    """Calculates users monthly debt to income ratio.

    Args:
        monthly_debt_payment (int): The total monthly debt.
        monthly_income (int): The total monthly income.

    Returns:
        The monthly debt ratio
    """
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio


# This function implements the following user story:
# As a lender,
# I want to calculate the applicant's loan-to-value ratio
# so that we can evaluate the risk of lending money to the borrower
def calculate_loan_to_value_ratio(loan_amount, home_value):
    """Calculates users loan to value ratio based on inputs.

    Args:
        loan_amount (int): The requested loan amount.
        home_value (int): The home value.

    Returns:
        The loan-to-value ratio.
    """
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio
