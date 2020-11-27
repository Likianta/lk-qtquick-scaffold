import QtQuick 2.15
import "./LCButtons/LCRadioButton.qml" as LCRadioButton

LCListView {
    id: _root

    property var   p_childrenProps: Object()
    property int   p_default: -1
    // extend props:
    //      p_currentIndex
    //      p_delegate
    //      p_model
    //      p_spacing
    //      r_count
    //      r_currentItem

    function clicked(i, item) {}

    p_delegate: LCRadioButton {
        id: _item
        p_text: modelData
        property int p_index: model.index

        onClicked: {
            _root.currentIndex = p_index
            fn_clicked(p_index, _item)
        }

        Component.onCompleted: {
            _item.checked = (p_default == p_index)

            for (let k in p_childrenProps) {
                _item[k] = p_childrenProps[k]
            }
        }
    }

    Component.onCompleted: {
        if (p_default > -1) {
            _root.currentIndex = p_default
        }
    }
}