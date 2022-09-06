# -*- coding: utf-8 -*-
"""uses applicants information to determine and return list of banks and associated loans

this script takes in a potential loan applicant's pre-qualification data.
processes appropriate data and runs it against filters.

this script also runs a validation step whereby
it specifically checks the credit score against the minimum credit score in the bank list.
this validation is then rechecked and confirmed.

returns the number of pre-qualified banks
returns a list of the pre-qualified banks

"""
# required imports

import sys
from ast import If
import questionary


def prompt_user_inputs():
    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text(
        "What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score, debt, income, loan_amount, home_value = validate_user_inputs(
        credit_score, debt, income, loan_amount, home_value)

    return credit_score, debt, income, loan_amount, home_value


# preliminary credit score validation criteria
# this will screen to check if applicant's individual
# credit score is compatible with the minimum value 550
# listed by the banks from daily_rate_sheet.csv
def validate_user_inputs(credit_score, debt, income, loan_amount, home_value):
    valid_credit_score = False

    # test provided credit score value against bank list minimum value
    if int(credit_score) >= 550:
        valid_credit_score = True
    # while loop test
    while valid_credit_score == False:

        # initial notification that provided credit score invalid
        # opportunity to change / correct initial credit score provided
        credit_score = questionary.text(
            'Credit score provided appears to be invalid. Please reenter your credit score?').ask()
        if not int(credit_score) >= 550:
            # confirming value entered /re-entered
            # final opportunity to recognize data entry error
            valid_credit_score = questionary.confirm(
                f'Is {int(credit_score)} your credit score?').ask()

            # finalization that minimum credit score value has not been met
            # termination of pre-qualification process
            # hard exit
            if valid_credit_score:
                sys.exit(
                    "Unfortunately, you do not meet the criteria for this pre-qualification screaning. Your credit score must be at least 550.")
        else:
            valid_credit_score = True

    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)
    return int(credit_score), debt, income, loan_amount, home_value
