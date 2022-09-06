# -*- coding: utf-8 -*-
"""Max Loan Size Filter.

This script filters the bank list by comparing the user's loan value
against the bank's maximum loan size.

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
# I want to filter the bank list by comparing the customer's desired loan against the bank's maximum loan size
# so that we can know which banks offer the loan amount requested by the customer


def filter_max_loan_size(loan_amount, bank_list):
    """Filters the bank list by the maximum allowed loan amount.

    Args:
        loan_amount (int): The requested loan amount.
        bank_list (list of lists): The available bank loans.

    Returns:
        A list of qualifying bank loans.
    """

    loan_size_approval_list = []

    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list
