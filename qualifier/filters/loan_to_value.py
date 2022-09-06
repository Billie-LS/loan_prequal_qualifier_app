# -*- coding: utf-8 -*-
"""Loan to Value Filter.
This script filters the bank list by the applicant's maximum home loan
to home value ratio.

"""
"""
CSV file column indices
0 - Lender
1 - Max Loan Amount
2 - Max LTV
3 - Max DTI
4 - Min Credit Score
5 - Interest Rate
"""

# Define a function that implements the following user story:
# As a lender,
# I want to filter the bank list by checking if the customer's loan-to-value is equal to or less than the maximum loan-to-value ratio allowed by the bank
# so that we assess if the customer's home value is worth as an asset to secure the loan


def filter_loan_to_value(loan_to_value_ratio, bank_list):
    """Filters the bank list by the maximum loan to value ratio.

    Args:
        loan_to_value_ratio (float): The applicant's loan to value ratio.
        bank_list (list of lists): The available bank loans.

    Returns:
        A list of qualifying bank loans.
    """

    loan_to_value_approval_list = []

    for bank in bank_list:
        if loan_to_value_ratio <= float(bank[2]):
            loan_to_value_approval_list.append(bank)
    return loan_to_value_approval_list
