import QtQuick 2.15
import QtQuick.Controls 2.15
import "../"
import "../LCStyle/dimension.js" as LCDimension
import "../LCStyle/palette.js" as LCPalette

CheckBox {
    id: _root
    // height: LCDimension.BarHeightS

    property alias p_text: _txt.p_text
    property alias __active: _root.checked
    
    // onCheckedChanged: {
    //     console.log("LCCheckBox", "check changed", __active)
    // }
    
    background: LCRectangle {
        id: _bg
        implicitWidth: LCDimension.ButtonWidthM; implicitHeight: LCDimension.ButtonHeightM
        p_border.width: 0
        p_color: "transparent"
    }

    contentItem: LCText {
        id: _txt
        anchors.fill: parent
        anchors.leftMargin: _indicator.width + LCDimension.HSpacingS
        p_alignment: "vcenter"
        p_bold: __active
    }

    indicator: LCRectangle {
        id: _indicator
        anchors.verticalCenter: parent.verticalCenter
        clip: true
        width: LCDimension.IndicatorCheckWidth; height: LCDimension.IndicatorCheckHeight

        p_border.width: 1; p_border.color: __active ? LCPalette.ButtonChecked : LCPalette.ButtonUnchecked
        p_radius: LCDimension.IndicatorCheckRadius

        LCRectangleBg {
            id: _indicator_filler
            anchors.fill: parent
            // anchors.margins: 1

            p_active: __active
            p_border.width: 0
            p_color0: LCPalette.Transparent; p_color1: LCPalette.ButtonChecked
            p_radius: parent.radius
        }
    }
}