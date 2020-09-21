import QtQuick 2.14
import QtQuick.Window 2.14
import LightClean 1.0

// https://qml.guide/live-reloading-hot-reloading-qml/+&cd=1&hl=zh-CN&ct=clnk&gl=sg
// https://stackoverflow.com/questions/58716153/how-to-force-loader-to-reload-reset-or-delete-the-cache-of-preloaded-qml-page
//  ^ this seems not work.

Window {
    visible: true
    width: 300; height: 120
    title: "Qml Hot Reloader"

    property string p_target: ""  // You must define the target to use.

    Loader {
        id: _loader
        anchors.centerIn: parent

        function reload() {
            source = ""
            // QmlEngine.clearComponentCache()
            PyHandler.main('clearComponentCache')
            source = p_target
        }
    }

    LCButton {
        anchors.fill: parent
        p_text: "Click to reload"
        onClicked: _loader.reload()
    }
}
