
from __future__ import absolute_import

from . import trajectory

__all__ = [ "trajectory" ]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
