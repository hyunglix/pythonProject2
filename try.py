# try:
#     print('start code')
#     print(10/0)
#     print('No errors')
# except ZeroDivisionError:
#     print('We have an error')
#
# print('code after capsule')


# try:
#     print('start code')
#     print('No errors')
# except NameError as error:
#     print(error)
# else:
#     print('I am else')
# finally:
#     print('Finally code')



# def checker(var_1):
#     if type(var_1)!= str:
#         raise TypeError (f"Sorry, we can't work with {type(var_1)},"
#                          f"we need class str")
#     else :
#         return print(var_1)
#
# first_var="10"
# checker(first_var)


import warnings
warnings.warn('Warning, no code here ', SyntaxWarning)