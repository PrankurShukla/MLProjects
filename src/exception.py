import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error.detail.exc_info()
    file_name=exc_tb.tb_frame.f.code.co_filename

    return error_message_detail

class CustomExcepton(Exception):
    def __init__(self,error_message,error_detail:sys):
        super()._init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message