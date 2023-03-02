import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='mama.log', filemode='w',
                    format='We have next logging message: '
                            '%(asctime)s:%(levelname)s-%(message)s'
                    )

logging.info("info")
