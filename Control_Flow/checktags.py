# -*- coding: utf-8 -*-
#
# File name     : checktags.py
#

class InvalidEntityError(Exception):
    pass

class InvalidNumericEntityError(InvalidEntityError):
    pass

class InvalidAlphaEntityError(InvalidEntityError):
    pass

class InvalidTagContentError(Exception):
    pass

PARSING_ENTITY = 10

# =============================================================================
# def parse(filename):
#     fh = None
#     try:
#         fh = open(filename, encoding = "utf8")
#         errors = False
#         for lino, line in enumerate(fh, start = 1):
#             for column, c in enumerate(line, start = 1):
#                 try:
#                     # ...
#                 elif state == PARSING_ENTITY:
#                     if c == ";":
#                         if entity.startswith("#"):
#                             if frozenset(entity[1:]) - HEXDIGITS:
#                                 raise InvalidNumericEntityError()
#                         elif not entity.isalpha():
#                             raise InvalidAlphaEntityError()
#                     # ...
#                 except (InvalidEntityError, InvalidTagContentError) as err:
#                     if isinstance(err, InvalidNumericEntityError):
#                         error = "invalid numeric entity"
#                     elif isinstance(err, InvalidAlphaEntityError):
#                         error = "invalid alphabetic entity"
#                     elif isinstance(err, InvalidTagContentError):
#                         error = "invalid tag"
#                     print("ERROR {0} in {1} on line {2} column {3}".format(error, filename, lino, column))
#                     if skip_on_first_error:
#                         raise
#     except (InvalidEntityError, InvalidTagContentError):
#         pass    # already handled
#     except EOFError as err:
#         print("ERROR unexpected EOF:", err)
#     except EnvironmentError as err:
#         print(err)
#     finally:
#         if fh is not None:
#             fh.close()
# =============================================================================
