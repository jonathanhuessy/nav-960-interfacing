from queue import Queue, Full, Empty
from collections import defaultdict
from copy import deepcopy

import threading
import logging

class ObserverManager():
    """ObserverManager aka. the Subject in an observer pattern
    
    All observers must implement the HandlePacket(packetId, packet) method!!
    """
    def __init__(self):
        """We allow observers to listen for specific "keys" or message ids"""
        self._packetIdObserverMap = defaultdict(list)

    def RegisterObserver(self, packetIdSet, observer):
        for PacketId in packetIdSet:
            ObserverList = self._packetIdObserverMap.setdefault(
                PacketId, list())
            if observer not in ObserverList:
                ObserverList.append(observer)

    def UnregisterObserver(self, observer):
        for ObserverList in self._packetIdObserverMap.values():
            if observer in ObserverList:
                ObserverList.remove(observer)
                break

    def NotifyObservers(self, packetId, packetData):
        if packetId in self._packetIdObserverMap:
            observerList = self._packetIdObserverMap[packetId]
            for observer in observerList:
                observer.HandlePacket(packetId, deepcopy(packetData))
    
    # Check if we have the observer
    def HasObserver(self, observer):
        for ObserverList in self._packetIdObserverMap.values():
            if observer in ObserverList:
                return True

    def GetObserverFor(self, packetId):
        """Only to be used to find BlockingObservers"""
        if packetId in self._packetIdObserverMap:
            observerList = self._packetIdObserverMap[packetId]
            for observer in observerList:
                if observer._tid == threading.get_ident():
                    return observer
        return None

    """    
    #==========================================
    # Wait for a specific response packet
    #==========================================
    """
    def waitForResponse(self, packetId, secTimeout):
        watcher = BlockingObserver(packetId)
        if self.HasObserver(watcher):
            watcher = self.GetObserverFor(packetId)
        else:
            self.RegisterObserver([packetId], watcher)
        item = watcher.waitForPacket(secTimeout)
        self.UnregisterObserver(watcher)
        return item


class BlockingObserver():
    def __init__(self, packetId):
        self._waitingId = packetId
        self._msgQueue = Queue()
        self._tid = threading.get_ident()

    def __eq__(self, other):
        """override equality test so that each thread can only have one blocking observer per id"""
        return isinstance(other, BlockingObserver) and other._tid == self._tid and self._waitingId == other._waitingId
    
    def HandlePacket(self, packetId, packet):
        if self._waitingId == packetId:
            try:
                self._msgQueue.put_nowait(packet)
            except Full:
                self._msgQueue.get() # discard one piece of data
                self._msgQueue.put(packet)

    def waitForPacket(self, timeout):
        try:
            item = self._msgQueue.get(True, timeout)
        except Empty:
            item = None
            
        return item
        
