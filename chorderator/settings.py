import logging
import os

AUDIO_OVER_WRITE = False

LOG_LEVEL = logging.INFO
LOG_FORMAT = '@Chorderator %(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

PROJECT_DIR = "/".join(os.path.abspath(__file__).split("/")[:-2]) + '/'
BASE_DIR = PROJECT_DIR + "chorderator/"
STATIC_DIR = BASE_DIR + "static/"
RESOURCE_DIR = PROJECT_DIR + "resource/"

static_storage = {
    'lib': STATIC_DIR + 'source_base.pnt',
    'trans': STATIC_DIR + 'transition_score.mdch',
    'concat_major': STATIC_DIR + 'major_score.mdch',
    'concat_minor': STATIC_DIR + 'minor_score.mdch',
}
