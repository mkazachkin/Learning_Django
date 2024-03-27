import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Second app index accessed')
    return HttpResponse('Second app!')
