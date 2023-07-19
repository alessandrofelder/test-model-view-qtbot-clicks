from typing import TYPE_CHECKING

from qtpy.QtWidgets import QHBoxLayout, QTableView, QWidget

if TYPE_CHECKING:
    pass

from test_model_view_qtbot_clicks.model import RandomModel


class ExampleQWidget(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        self.view = QTableView()
        model = RandomModel([["Pi", 3.14], ["Random number", 1.236]])
        self.view.setModel(model)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.view)
