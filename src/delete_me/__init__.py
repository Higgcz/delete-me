"""Top-level package for delete-me."""

__all__ = (
    "__version__",
    "__author__",
    "__email__",
)
__author__ = "Vojtech Micka"
__email__ = "vojtech@nnaisense.com"

try:
    from .__version import __version__ as __version__
except ImportError:
    import sys

    print(
        "Please install the package to ensure correct behavior.\nFrom root folder:\n\tpip install -e .", file=sys.stderr
    )
    __version__ = "undefined"
