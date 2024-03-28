try:
    from importlib.metadata import version as get_version
    version = get_version(__name__)
except ImportError:
    from pkg_resources import get_distribution
    version = get_distribution(__name__).version

from .ct5 import CT5Reader
