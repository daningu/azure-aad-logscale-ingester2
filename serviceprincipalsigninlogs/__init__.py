import logging
import os
import azure.functions as func

from supplement import logscale

async def main(events: func.EventHubEvent):
    for event in events:
        await logscale.send_log(event.get_body().decode('utf-8'))
         