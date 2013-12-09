#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © %YEAR% %USER% <%MAIL%>
#
# Distributed under terms of the %LICENSE% license.

"""
%HERE%
"""
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
log = logging.getLogger('name')
if __name__ == '__main__':
    import doctest
    doctest.testmod()
