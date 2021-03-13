import os
import re

import pandas as pd

resources_dir = "../resources/"



#step-1
def get_target_files(prefix):
    return [file for file in os.listdir(resources_dir) if file.startswith(prefix)]

#step-2
def concat_df(files):
    df_list = [pd.read_csv(resources_dir + file) for file in files]
    combined_df = pd.concat(df_list)
    return combined_df


#step-3
def get_monthly_payment(string):
    regex = "monthly payment:\s*\${0,1}(\d+)"
    match = re.search(regex, string, re.I)
    try:
        payment = match.group(1)
        return payment
    except AttributeError:
        print(f"no match found for string: {string}")
        return None
    