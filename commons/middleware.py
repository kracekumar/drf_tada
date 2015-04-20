# -*- coding: utf-8 -*-

import traceback
import sys


class CustomExceptionHandler(object):
    def process_exception(self, request, exception):
        exc = self._get_traceback()
        print(exc,)

    def _get_traceback(self, exc_info=None):
        """Helper function to return the traceback as a string"""
        return '\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))
