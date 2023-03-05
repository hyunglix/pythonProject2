import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log', filemode='w',
                    format='We have next logging message: '
                            '%(asctime)s:%(levelname)s-%(message)s'
                    )
logging.debug('debug')
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    print(10/0)
except Exception:
    logging.exception('Exception')

# if 2+2==4:
#     print('In fact, 2+2 equals 4')
#
# assert 2+2==5, "wrong assert"
#
# # """
# # >>> 2+2
# # 5
# # """
# # if __name__=="__main__":
# #     import doctest
# #     doctest.testmod()