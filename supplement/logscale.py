import logging
import os

import requests


header_api_token = "bearer" + os.environ["LogScaleIngestToken"]
logscale_header = {'content-type': 'application/json', 'Authorization': header_api_token}
async def send_log(log_body):
#    logging.info(log_body)
    return requests.post(os.environ["LogScaleURL"], headers = logscale_header, data = log_body)