import logging

import azure.functions as func


def main(myblob: func.InputStream):
    if myblob.name and myblob.length:
        logging.info(f"Python blob trigger function processed blob \n"
                    f"Name: {myblob.name}\n"
                    f"Blob Size: {myblob.length} bytes")

