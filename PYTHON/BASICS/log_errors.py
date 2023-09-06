import traceback
import os

#variables
log_file_path = f'C:\\Users\\{os.getlogin()}\\Documents\\TADAUWAL_DATA\\logfile.log'

def log_errors(error_message, log_file_path = log_file_path):
    try:
        # Print the error message to the console
        print(error_message)

        # Write the error message to the log file
        with open(log_file_path, 'a') as log_file:
            log_file.write(error_message + '\n')

        # Get the traceback information
        traceback_info = traceback.format_exc()

        # Append the traceback to the log file
        with open(log_file_path, 'a') as log_file:
            log_file.write(traceback_info + '\n')

    except Exception as e:
        # If an error occurs while logging, print the error message
        print(f"Error occurred while logging: {str(e)}")