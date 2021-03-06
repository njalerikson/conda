# -*- coding: utf-8 -*-
# source: https://raw.githubusercontent.com/tqdm/tqdm/v4.14.0/tqdm/__init__.py
# version: 4.14.0
# date: 2017-06-18

from ._tqdm import tqdm
from ._tqdm import trange
from ._tqdm_gui import tqdm_gui
from ._tqdm_gui import tgrange
from ._tqdm_pandas import tqdm_pandas
from ._main import main
from ._version import __version__  # NOQA
from ._tqdm import TqdmTypeError, TqdmKeyError, TqdmDeprecationWarning

__all__ = ['tqdm', 'tqdm_gui', 'trange', 'tgrange', 'tqdm_pandas',
           'tqdm_notebook', 'tnrange', 'main',
           'TqdmTypeError', 'TqdmKeyError', 'TqdmDeprecationWarning',
           '__version__']


def tqdm_notebook(*args, **kwargs):  # pragma: no cover
    """See tqdm._tqdm_notebook.tqdm_notebook for full documentation"""
    from ._tqdm_notebook import tqdm_notebook as _tqdm_notebook
    return _tqdm_notebook(*args, **kwargs)


def tnrange(*args, **kwargs):  # pragma: no cover
    """
    A shortcut for tqdm_notebook(xrange(*args), **kwargs).
    On Python3+ range is used instead of xrange.
    """
    from ._tqdm_notebook import tnrange as _tnrange
    return _tnrange(*args, **kwargs)
