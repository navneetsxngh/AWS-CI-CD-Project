import logging
import os

# Create logs directory
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Fixed log file name
LOG_FILE_PATH = os.path.join(LOGS_DIR, "log_file.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="a",
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# if __name__=="__main__":
#     logging.info("Logging Has Started")
