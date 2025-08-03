import sys
from src.logger import logging

def error_message_detail(error,error_detail: sys):
    """
    This function will return error message detail
    :param error: Exception object
    :param error_detail: sys.exc_info() result, which is a tuple of three values (type, value, traceback)
    :return: error message
    """
    _, _, exc_tb = error_detail.exc_info()
    import pdb; pdb.set_trace()  # This line is for debugging purposes, can be removed in production
    error_message = f"Error occurred in script: [{exc_tb.tb_frame.f_code.co_filename}] at line number: [{exc_tb.tb_lineno}] with message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Constructor for CustomException class
        :param error_message: error message in string format
        :param error_detail: object of sys module
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        """
        Returns the error message string for this exception.
        """

        return self.error_message
    

if __name__ == "__main__":
    try:      
        a = 1/0                       
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        raise CustomException(e,sys)