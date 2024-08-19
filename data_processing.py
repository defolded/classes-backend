import pandas as pd

def load_course_data(file_path: str):
    return pd.read_csv(file_path).to_dict(orient='records')

def process_requirements(file_path: str):
    return pd.read_csv(file_path).to_dict(orient='list')
