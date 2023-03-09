import sys
from src import logger

logger.setup()


def detail_error(message, sys_hook: sys) -> str:
    sys_hook.exc_info
    _, _, trace_back_obj = sys_hook.exc_info()  # get error traceback object
    file_name = trace_back_obj.tb_frame.f_code.co_filename
    line_no = trace_back_obj.tb_lineno
    error_message = f"Error occured in file:[{file_name}], at line-no:[{line_no}], error-message:[{message}]"
    return error_message


class CustomException(Exception):
    def __init__(self, message, sys_hook: sys):
        super().__init__()
        self.error_message = detail_error(message, sys_hook)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        1 / 0
    except Exception as e:
        logger.log(CustomException(e, sys))
