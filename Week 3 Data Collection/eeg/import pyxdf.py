import pyxdf
import pandas as pd

# Define the input and output file paths
input_file =  r'c:\Users\Shrimi Agrawal\OneDrive\Documents\CurrentStudy\sub-P001\ses-S001\eeg\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'
output_file = r'C:\Users\Shrimi Agrawal\OneDrive\Documents\CurrentStudy\sub-P001\ses-S001\eeg\first_data.xlsx'

# Load the XDF file
streams, _ = pyxdf.load_xdf(input_file)

# Assuming the EEG data is in the first stream 
eeg_stream = streams[0]

# Convert the EEG data to a pandas DataFrame
data = eeg_stream['time_series']

# Create a DataFrame with the data
df = pd.DataFrame(data, columns=['Var1', 'Var2', 'Output1', 'Output2', 'Var5', 'Var6', 'Var7', 'Var8'])

# Select the desired columns
selected_columns = df[['Output1', 'Output2']]

# Save the selected columns to an Excel file
selected_columns.to_excel(output_file, index=False)
