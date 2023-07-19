from qtpy.QtCore import QPoint, Qt

from test_model_view_qtbot_clicks._widget import ExampleQWidget


def test_double_click(make_napari_viewer, qtbot, mocker):
    show_info_mock = mocker.patch(
        "test_model_view_qtbot_clicks._widget.show_info"
    )
    viewer = make_napari_viewer
    widget = ExampleQWidget(viewer)

    viewport_x = widget.view.columnViewportPosition(1)
    viewport_y = widget.view.rowViewportPosition(0)
    qtbot.mouseDClick(
        widget.view.viewport(),
        Qt.LeftButton,
        pos=QPoint(viewport_x, viewport_y),
    )

    show_info_mock.assert_called_once_with("The data at (0, 1) is 3.14")
