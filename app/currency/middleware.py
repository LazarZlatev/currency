from time import time
from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print('BEFORE IN MIDDLEWARE')  # noqa:
        start = time()

        response = self.get_response(request)
        end = time()

        response_log = RequestResponseLog.objects.create(path=request.build_absolute_uri(),
                                                         request_method=request.method,
                                                         request_time=end - start)
        print(f'AFTER IN MIDDLEWARE: ' # noqa:
              f'Path: {response_log.path}, ' # noqa:
              f'Method: {response_log.request_method}, ' # noqa:
              f'Time: {response_log.request_time }') # noqa:

        return response
