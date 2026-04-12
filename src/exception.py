import sys
from src.logger import logging


def error_message_details(error: Exception, error_detail: sys) -> str:
    """
    Returns detailed error message including script name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    error_message = (
        f"Error occurred in python script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"error message: [{str(error)}]"
    )

    return error_message


class CustomException(Exception):
    """
    Custom exception class to capture detailed project errors.
    """

    def __init__(self, error: Exception, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_detail)

    def __str__(self) -> str:
        return self.error_message


# Testing block
# if __name__ == "__main__":

#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.error("Divide by Zero Error")
#         raise CustomException(e, sys)