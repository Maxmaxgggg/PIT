#
#
#           ФАЙЛ СОДЕРЖИТ КАСТОМНЫЕ КОМБОБОКСЫ
#
#


from PySide6.QtWidgets import QComboBox, QCompleter, QLineEdit
from PySide6.QtCore import QStringListModel, Qt


class addressComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.placeholderLED = QLineEdit(self)
        self.setLineEdit(self.placeholderLED)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.line_edit = self.lineEdit()
        self.completer = QCompleter(self)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setModel(QStringListModel())
        self.line_edit.setCompleter(self.completer)


class ownerComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.placeholderLED = QLineEdit(self)
        self.setLineEdit(self.placeholderLED)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.line_edit = self.lineEdit()

        self.completer = QCompleter(self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setModel(QStringListModel())
        self.line_edit.setCompleter(self.completer)