"""See https://stackoverflow.com/questions/12604739/how-can-you-edit-a-qtableview-cell-from-a-qtest-unit-test/12604740#12604740

and thanks to Daniel Althviz More!
"""

from qtpy.QtCore import QPoint, Qt

from test_model_view_qtbot_clicks._widget import ExampleQWidget


def test_double_click_viewport(make_napari_viewer, qtbot, mocker):

    show_info_mock = mocker.patch(
        "test_model_view_qtbot_clicks._widget.show_info"
    )
    viewer = make_napari_viewer
    widget = ExampleQWidget(viewer)

    viewport_x = widget.view.columnViewportPosition(1)
    viewport_y = widget.view.rowViewportPosition(0)
    
    qtbot.mouseClick(
        widget.view.viewport(),
        Qt.MouseButton.LeftButton,
        pos=QPoint(viewport_x, viewport_y),
    )
    
    qtbot.mouseDClick(
        widget.view.viewport(),
        Qt.MouseButton.LeftButton,
        pos=QPoint(viewport_x, viewport_y),
    )


    show_info_mock.assert_called_once_with("The data at (0, 1) is 3.14")


def test_double_click_select_row_column(make_napari_viewer, qtbot, mocker):
    show_info_mock = mocker.patch(
        "test_model_view_qtbot_clicks._widget.show_info"
    )
    viewer = make_napari_viewer
    widget = ExampleQWidget(viewer)

    widget.view.selectColumn(1)
    widget.view.selectRow(0)

    qtbot.mouseClick(
        widget.view,
        Qt.MouseButton.LeftButton,
    )
    qtbot.mouseDClick(widget.view, Qt.MouseButton.LeftButton)


    show_info_mock.assert_called_once_with("The data at (0, 1) is 3.14")

### tests below not expected to pass, because tableview is only accessible via it's viewport!

def test_double_click_select_model_index(make_napari_viewer, qtbot, mocker):
    show_info_mock = mocker.patch(
        "test_model_view_qtbot_clicks._widget.show_info"
    )
    viewer = make_napari_viewer
    widget = ExampleQWidget(viewer)

    model_index = widget.view.model().index(0, 1)
    widget.view.setCurrentIndex(model_index)
    
    qtbot.mouseClick(
        widget.view,
        Qt.MouseButton.LeftButton,
    )

    qtbot.mouseDClick(widget.view, Qt.MouseButton.LeftButton)

    qtbot.wait(10000)  # give Qt plenty of time to catch up!
    from time import sleep

    sleep(5)

    show_info_mock.assert_called_once_with("The data at (0, 1) is 3.14")
