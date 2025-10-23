# Import libraries
import pandas as pd
import numpy as np
import os

# Create a data for DataFrame
attributes = ["Name", "Age", "Gender"]
values = np.array([["Jeet", 22, "Male"], ["Suman", 23, "Male"], ["Tridibesh", 22, "Male"]])

# Create DataFrame
data = pd.DataFrame(data=values, columns=attributes)

# Create a output directory
folder_path = "data"
os.makedirs(folder_path, exist_ok=True)

# Define the data path
data_path = os.path.join(folder_path, "student_info.csv")

# Now store the DataFrame on that folder as a CSV file
data.to_csv(data_path, index=False)