from typing import TYPE_CHECKING

from qtpy.QtWidgets import QHBoxLayout, QTableView, QWidget

if TYPE_CHECKING:
    pass

from napari.utils.notifications import show_info

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

        self.view.doubleClicked.connect(self.on_double_click)

    def on_double_click(self):
        selected_index = self.view.selectionModel().currentIndex()
        if selected_index.isValid():
            selected_row = selected_index.row()
            selected_column = selected_index.column()
            model = self.view.model()
            selected_data = model.data(selected_index)
            show_info(
                f"The data at ({selected_row}, {selected_column}) is {selected_data}"
            )
