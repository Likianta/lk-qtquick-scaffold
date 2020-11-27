"""
@Author  : likianta <likianta@foxmail.com>
@Module  : launcher.py
@Created : 2020-08-30
@Updated : 2020-11-27
@Version : 0.2.9
@Desc    :
"""
from PySide2.QtCore import QObject
from PySide2.QtQml import QQmlApplicationEngine, QQmlContext
from PySide2.QtWidgets import QApplication


class Application(QApplication):
    """
    Attributes:
        engine (QQmlApplicationEngine)
        root (QQmlContext)
        _entrance (str): see `__init__`
        __holder (dict): __holder 只是为了在整个生命周期中持续持有实例, 以防止
            Python 垃圾回收机制误杀注入到 QML 全局变量的对象, 本身没有其他用处.
    """
    
    def __init__(self, entrance: str, qmldir='', **kwargs):
        """
        Args:
            entrance: 启动时要载入的 .qml 文件. 通常为 '{somedir}/main.qml'
                或 '{somedir}/view.qml'.
            qmldir: 要引入外部自定义 QML 模块, 则填写该模块的父目录路径. 例如:
                    |- myprj
                        |- main.py
                    |- scaffold
                        |- ComponentLibX
                            |- ComponentA.qml
                            |- ComponentB.qml
                            |- ComponentC.qml
                            |- qmldir  # The folder must include a 'qmldir' file
                我们要在 myprj 中引入 scaffold 项目下的 ComponentLibX 组件库, 那
                么:
                    qmldir = '../scaffold'
                
        Keyword Args:
            organization (str): default 'dev.likianta.lk_qtquick_scaffold'
        """
        super().__init__()
        self.setOrganizationName(kwargs.get(
            'organization', 'dev.likianta.lk_qtquick_scaffold'))
        #   该步骤是为了避免在 QML 中使用 QtQuick.Dialogs.FileDialog 时, 出现警
        #   告信息:
        #       QML Settings: The following application identifiers have not
        #       been set: QVector("organizationName", "organizationDomain")
        
        self.engine = QQmlApplicationEngine()
        self.root = self.engine.rootContext()
        self._entrance = entrance
        self.__holder = {}
        
        if not qmldir:
            from os import path
            qmldir = path.join(path.dirname(__file__), 'theme')
            #   i.e. the abspath of '../theme'.
            #   TODO: test whether '../theme/LightClean' worked as '../theme'
        self.engine.addImportPath(qmldir)
    
    def register_pyobj(self, name, obj):
        """ 将 Python 中定义好的 (继承自 QObject 的) 对象作为全局变量加载到 QML
            的上下文当中.
            
        Args:
            name (str): Object name, 建议使用大驼峰式命名, 并建议以 "Py" 开头,
                例如: "PyHooks"
            obj (QObject): A Python class instance inherits QObject
            
        Notes:
            1. 在调用 self.start() 前使用本方法
            2. 这些对象可以在 QML 布局中全局使用
        """
        self.root.setContextProperty(name, obj)
        # 令 self.__holder 持有该实例, 避免 Python 误将 handler 引用计数归零.
        self.__holder[name] = obj
    
    def start(self):
        self.engine.load(self._entrance)
        self.exec_()


if __name__ == '__main__':
    _app = Application('../tests/Demo/LightCleanDemo.qml', './theme')
    _app.start()
