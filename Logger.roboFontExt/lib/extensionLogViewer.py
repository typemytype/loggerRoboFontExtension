from lib.eventTools.eventManager import getObserverLog

from vanilla import *

from mojo.events import addObserver, removeObserver

from AppKit import *


class Log(object):
    
    def __init__(self):
        self.w = Window((500, 400), "Log Viewer", minSize=(300, 200))
        self.w.bind('close', self.close)
        log = getObserverLog()
        columnDescriptions = [
                dict(title="observer"),
                dict(title="method"),
                dict(title="event"),
                dict(title="count"),
                dict(title="time"),
                dict(title="average")
            ]
        self.w.l = List((0, 0, -0, -0), log, columnDescriptions=columnDescriptions)
        
        query = "observer <> 'Log'"
        query = NSPredicate.predicateWithFormat_(query)
        
        controller = self.w.l.getNSTableView().dataSource()
        controller.setFilterPredicate_(query)
                
        addObserver(self, "notification", None)
        self.w.open()
    
    def notification(self, notification):
        log = getObserverLog()
        self.w.l.set(log)
        
    def close(self, sender):
        removeObserver(self, None)
        

Log()