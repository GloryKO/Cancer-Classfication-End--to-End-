import os
import logging

# # Create the "logs" directory if it doesn't exist
# os.makedirs("logs", exist_ok=True)

# # Configure the logging settings
# log_file = "logs/main.log"
# logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# # Perform your program logic
# # ...

# # Write logs using the logging module
# logging.debug("This is a debug message")

def set_logging(message:str)->str:
    os.makedirs("logs",exist_ok=True)
    log_file = "logs/main.log"
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.debug(message)

set_logging("This is a debug message")
