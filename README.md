# **Columbia University Engineering, New York FinTech BootCamp** 
# **August 2022 Cohort**
## *Module 2, Challenge*

This is a command line interface (CLI) data processing application for bank loan pre-qualification screening.  This application matches loan applicants with banks and associated bank loans for which they may qualify.

The screening application is processed via applicant query for applicant specific data.  The user will input applicant's credit score, current debt level, income, the size of the loan desired, and the value of the applicant's collateral (i.e. current home value).  These data points are compared against the loan criteria of various lenders contained within a comma separated values (CSV) file, `daily_rate_sheet`.  

Through processing the loan applicant provided data and comparing it to the loan criteria of various lenders, the loan applicant's eligibility for the loan they are seeking is determined.  The program will output for the applicant their calculated monthly debt to income (DTI) ratio, loan to value (LTV) ratio, and, if they qualify, the number of banks with a list of those banks to which they are pre-qualified will be outputted.  The program will then offer to save the list of banks and loan data.  Upon selcting to save the data, the list of banks and loan data within a comma separated values (CSV) file, `bank_loan_list`.

---
## **Methods**

The command line interface operator/user will input

    file path for the `daily_rate_sheet`
    applicant's

        credit score
        monthly debt
        monthly income
        desired loan size
        current home value

    * the app will output as to available matches found or none found,
    * if no matches are found, the user / operator will be be prompted as to desire to save,
    * if no matches are identified, but user / operator indicates desire to save, output message will indicate there is none to save,
    * if matches are found and user / operator indicates desire to save,
    * the user / operator will be be prompted for a file path to where the list should be saved,
    * the user / operator will be be notified that the file has been saved to the specified path that has been in putted by the user / operator 

![Loan Qualifier Prompts](images/gen_methods.png)

---
## **Technologies**
---
### **Dependencies**

This project leverages python 3.7 with the following packages:

* [sys](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys) - System-specific parameters and functions

* [pathlib](https://docs.python.org/3/library/pathlib.html) - Object-oriented filesystem paths
  
* [csv](https://docs.python.org/3/library/csv.html?highlight=csv#module-csv) - File Reading and Writing

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs


### **Hardware used for development**

MacBook Pro (16-inch, 2021)

    Chip Appple M1 Max
    macOS Monterey version 12.5.1

### **Development Software**

Homebrew 3.5.10

    Homebrew/homebrew-core (git revision 0b6b6d9004e; last commit 2022-08-30)
    Homebrew/homebrew-cask (git revision 63ae652861; last commit 2022-08-30)

anaconda Command line client 1.10.0

    conda 4.13.0
    Python 3.7.13

pip 22.1.2 from /opt/anaconda3/envs/dev/lib/python3.7/site-packages/pip (python 3.7)

    fire 0.4.0
    questionary 1.10.0

git version 2.37.2

Visual Studio Code version: 1.71.0 (Universal)

---
## *Pre-Installation Guide*

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```
![Loan Qualifier Prompts](images/install_fire.png)
![Loan Qualifier Prompts](images/install_questionary.png)

* if difficulties with installation, please refer to additional instructions as below:*
  
  [fire](https://github.com/google/python-fire#installation) - for expanded information and installation instructions

---
## *Installation of application (i.e. github clone)*

 In the terminal, navigate to directory where you want to install this application from the repository and enter the following command

```python
git clone git@github.com:Billie-LS/FinTech_Homeworks.git
```

---
## **Usage**

From terminal, the installed application is run from the installed directory by typing at prompt:

```python
  python app.py
```
![Loan Qualifier Prompts](images/app_on.png)

the following images will display sequential steps and prompts under four example protypical applicant scenarios.

###    scenario 1 - typical good candidate
        credit score 750, 
        monthly debt $1200, 
        monthly income $7500, 
        desired loan size $100000,
        current home value $140000

![Loan Qualifier Prompts](images/perfect_app1.png)
![Loan Qualifier Prompts](images/perfect_app2.png)
![Loan Qualifier Prompts](images/perfect_app_complete.png)

###    scenario 2 - good candidate, mistakenly enterred wrong / inadequate credit score
![Loan Qualifier Prompts](images/perfect_mistake1.png)
![Loan Qualifier Prompts](images/perfect_mistake_complete.png)

###    scenario 3 - candidate with inadequate credit score 
![Loan Qualifier Prompts](images/too_low1.png)
![Loan Qualifier Prompts](images/too_low2.png)
![Loan Qualifier Prompts](images/too_low_complete.png)

###    scenario 4 - good candidate seeking too large a loan
![Loan Qualifier Prompts](images/too_much.png)
![Loan Qualifier Prompts](images/too_much_complete.png)

---
## **Requirements**
### user stories and acceptance criteria

    Provided in directory `y_stories`

---
## **Version control**

This project was transferred to its current / new repository location.  For current / post-transfer GitHub repository version control history information please follow hyperlink.

[post-transfer-repository](https://github.com/Billie-LS/loan_prequal_qualifier_app)

For earlier / pre-transfer GitHub repository version control history information please follow hyperlink.

[pre-transfer-repository](https://github.com/Billie-LS/FinTech_Homeworks/commits/main/Challenge2)

---
## **Contributors**

### **Author**

Loki 'billie' Skylizard
[LinkedIn](https://www.linkedin.com/in/l-s-6a0316244)



### **BootCamp lead instructor**

Vinicio De Sola



### **BootCamp teaching assistants**

Corey Recai

Santiago Pedemonte



### **BootCamp classmates**

Dinesh Mandal

Will Conyea
[@GitHub](https://github.com/willkanye)


### **Slack application, student support services via 'askBCS'**

Laanu Adeyeye

Tristen Ortiz



### **GitHub example and reference**

Daniel Martinez
[@GitHub](https://github.com/dcmar18/LoanQualifierApp.git)

---
## **License**

MIT License

Copyright (c) [2022] [Loki 'billie' Skylizard]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

