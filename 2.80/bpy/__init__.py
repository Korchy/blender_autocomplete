import sys
import typing
from . import types
from . import props
from . import ops
from . import utils
from . import app
from . import context
from . import path

context: 'types.Context' = None

data: 'types.BlendData' = None
'''Access to Blenders internal data '''
