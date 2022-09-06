# -*- coding: utf-8 -*-
"""determines and returns list of banks and associated loans

this script takes in a potential loan applicant's pre-qualification data.
processes appropriate data and runs it against filters.
returns the number of pre-qualified banks
returns a list of the pre-qualified banks

"""

# required imports

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

# This function implements the following user story:
# As a customer,
# I want to know what are the best loans in the market according to my financial profile
# so that I can choose the best option according to my needs


def got_qualifying_loans(bank_data, credit_score, debt, income, loan_amount, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        # changed loan to loan_amount
        loan_amount (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    # print out the monthly debt ratio
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    # changed loan to loan_amount
    loan_to_value_ratio = calculate_loan_to_value_ratio(
        loan_amount, home_value)
    # print out the loan to value ratio
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    # changed loan to loan_amount
    bank_data_filtered = filter_max_loan_size(loan_amount, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(
        monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(
        loan_to_value_ratio, bank_data_filtered)

    # print out the number of pre-qualified banks using len()
    print(
        f'Found {len(bank_data_filtered)} qualifying loans.')
    # print out the list of banks and associated loans
    print(f'{bank_data_filtered}')

    return bank_data_filtered
