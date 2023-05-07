# function that read all excel files in a folder, and join them in a single dataframe
import pandas as pd
import glob

folder_path = "./data/gdl"


def read_all_excel_files(folder_path):
    all_files = glob.glob(folder_path + "*.xlsx")
    df_list = []
    for file in all_files:
        df = pd.read_excel(file)
        df_list.append(df)
    return pd.concat(df_list)

joined_df = read_all_excel_files(folder_path)
print(joined_df)

# function that read all excel files in a folder create a dataframe for each one and print the head of each one, also print the name of each file
def read_all_excel_files_and_print_head(folder_path):
    all_files = glob.glob(folder_path + "*.xlsx")
    for file in all_files:
        df = pd.read_excel(file)
        print(df.head())
        print(file)


# function that read all xls files in a folder create a dataframe for each one and join the dataframes together, each xls file have columns in diferent order
def read_all_excel_files_and_join_df(folder_path):
    all_files = glob.glob(folder_path + "*.xlsx")
        df_list = []
    for file in all_files:
        df = pd.read_excel(file)
        df_list.append(df)
        