import pandas as pd 
import numpy as np
import re
from tkinter import filedialog as fd

curr_file = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
curr_data = pd.read_csv(curr_file, encoding = "ISO-8859-1")

# INDIVIDUAL TESTING
dataset = curr_data.loc[(curr_data['contact'] != 'SPAM SPAM') & (curr_data['resolution_code'] != 'Spam')].reset_index(drop=True)


###### 9/8/2020 ######

# FUNCTIONS APPLY CURRENT CLEANING STEPS INTO ENTIRE DATASET

def subject_clean(subject_line):
    regex_sol = re.sub(r'https?://\S+', '', subject_line) # removes URL links
    regex_sol = re.sub(r"\S*@\S*\s?", "", regex_sol) # removes email accounts
    regex_sol = regex_sol.replace("\n", "").replace("< >","").replace("\r", "") # removes newline and <> and \r
    regex_sol = re.sub(r"\d+", "", regex_sol) # removes integers 
    regex_sol = re.sub(r"([^\s\w]|_)+", " ", regex_sol) # removes non-alphanumeric characters, but maintains whitespace
    regex_sol = regex_sol.encode("ASCII", "replace").decode("utf-8").replace("?", " ") # removes all non-ASCII characters
    regex_sol = regex_sol.lower() # lower case string
    return regex_sol

def case_line_clean(case_line):
    regex_sol_2 = re.sub(r"[?](CS)[0-9]+", "", case_line) # removes ending "?CS###"
    regex_sol_2 = re.sub(r"\d+", "", regex_sol_2) # removes integers
    regex_sol_2 = re.sub(r"([^\s\w]|_)+", " ", regex_sol_2) # removes non-characters, but maintains whitespace
    regex_sol_2 = regex_sol_2.lower()
    return regex_sol_2

dataset['description'] = dataset['description'].apply(subject_clean)
dataset['case'] = dataset['case'].apply(case_line_clean)

# dataset.to_csv("mod_test.csv")

###############

