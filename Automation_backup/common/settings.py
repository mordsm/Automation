
import sys
from datetime import datetime


def COMMON(name):
    try:
        return getattr(sys.modules[__name__], name)
    except AttributeError:
        return None


FREEMIUM = False
CONTENT_SCAN = False

def get_context():
    return {
            'year':datetime.now().year,
            'freemium': FREEMIUM,
        }

class ContextViewMixIn:
    context = get_context()
    
    def update_context(self, d):
        self.context.update(d)
