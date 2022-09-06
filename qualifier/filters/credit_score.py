# -*- coding: utf-8 -*-
"""Credit Score Filter.

This script filters a bank list by the user's minimum credit score.

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
# I want to filter the bank list by checking if the customer's credit score is equal to or greater than the minimum allowed credit score defined by the bank
# so that we can know which banks are willing to offer a loan to the customer


def filter_credit_score(credit_score, bank_list):
    """Filters the bank list by the mininim allowed credit score set by the bank.

    Args:
        credit_score (int): The applicant's credit score.
        bank_list (list of lists): The available bank loans.

    Returns:
        A list of qualifying bank loans.
    """

    credit_score_approval_list = []
    for bank in bank_list:
        if credit_score >= int(bank[4]):
            credit_score_approval_list.append(bank)
    return credit_score_approval_list
