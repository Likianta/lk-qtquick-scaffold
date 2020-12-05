"""
@Author  : likianta <likianta@foxmail.com>
@Module  : main.py
@Created : 2020-09-20
@Updated : 2020-12-03
@Version : 0.2.6
@Desc    :
    Usage:
        from lk_qtquick_scaffold.debugger import HotReloader
        reloader = HotReloader('./my_view.qml')
        reloader.start()
"""
from os.path import abspath, dirname

from lk_qtquick_scaffold import app


class HotReloader:
    
    def __init__(self, target: str):
        """
        Args:
            target: A .qml file for hot loading.
        """
        self.curr_dir = dirname(__file__)
        self.loader = abspath(f'{self.curr_dir}/LKDebugger/HotReloader.qml')
        self.target = abspath(target)
        
        from platform import system
        if system() == 'Windows':
            self.target = 'file:///' + self.target
    
    def start(self):
        # register hot reloader runtime functions
        from lk_qtquick_scaffold import pyhandler
        pyhandler.register_pyfunc(app.engine.clearComponentCache,
                                  'clear_component_cache')
        pyhandler.register_pyfunc(self.get_target)
        
        # start app
        app.start(self.loader)
    
    def get_target(self):
        return self.target


if __name__ == '__main__':
    reloader = HotReloader(abspath('../../tests/qml/view.qml'))
    reloader.start()