from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute
from typing import Callable
import time
from app.logging.my_logging import logger


class LogRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            # response.headers["X-Response-Time"] = str(duration)
            logger.info(str(request.url) + " __ " + str(request.method) + " __ return:" +
                        str(response.status_code) + " __ " + str(duration))
            # logger.info(request._json)
            logger.info(vars(request))
            logger.info(response.body)

            return response

        return custom_route_handler
