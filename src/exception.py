# pyright: reportOptionalMemberAccess=false
# pyright: reportShadowedImports=false

import sys
from src import logger

logger.setup()


class CustomException(Exception):
    def __init__(self, message):
        super().__init__()
        _, _, trace_back_obj = sys.exc_info()  # get error traceback object
        file_name = trace_back_obj.tb_frame.f_code.co_filename
        line_no = trace_back_obj.tb_lineno  # type: ignore
        self.error_message = f"Error occured in file:[{file_name}], at line-no:[{line_no}], error-message:[{message}]"

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        x = 1 / 0
    except Exception as e:
        logger.log(CustomException(e))
