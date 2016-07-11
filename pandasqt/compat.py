import logging
log = logging.getLogger(__name__)

import sip
try:
    sip.setapi('QString', 2)
    sip.setapi('QVariant', 2)
except ValueError as e:
    log.error(e)

import sys
if sys.version_info.major != 2:
    unicode = str

try:
    from PyQt4 import QtCore as QtCore_
    from PyQt4 import QtGui as QtGui_
    from PyQt4 import QtGui as QtWidgets_
    from PyQt4.QtCore import pyqtSlot as Slot, pyqtSignal as Signal, QT_VERSION_STR as qt_version
    QT_WRAPPER = 'PyQt4'
except ImportError as e:
    try:
        from PyQt5 import QtCore as QtCore_
        from PyQt5 import QtGui as QtGui_
        from PyQt5 import QtWidgets as QtWidgets_
        from PyQt5.QtCore import pyqtSlot as Slot, pyqtSignal as Signal, QT_VERSION_STR as qt_version
        QT_WRAPPER = 'PyQt5'
    except ImportError as e:
        from PySide import QtCore as QtCore_
        from PySide import QtGui as QtGui_
        from PySide import QtGui as QtWidgets_
        from PySide.QtCore import Slot, Signal, QT_VERSION_STR as qt_version
        QT_WRAPPER = 'PySide'


QtCore = QtCore_
QtGui = QtGui_
QtWidgets = QtWidgets_
Qt = QtCore_.Qt
qt_version_short = qt_version[0]

__all__ = ['QtCore', 'QtGui', 'QtWidgets', 'Qt', 'Signal', 'Slot', 'qt_version', 'qt_version_short']


