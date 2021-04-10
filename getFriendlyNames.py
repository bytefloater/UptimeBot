def monitorType(typeIndex):
    types = {'1': 'HTTP(s)',
             '2': 'Keyword',
             '3': 'Ping',
             '4': 'Port',
             '5': 'Heartbeat'}
    return types[typeIndex]

def logType(typeIndex):
    types = {'1': 'down',
             '2': 'up',
             '99': 'paused',
             '98': 'started'}
    return types[typeIndex]

def monitorStatus(statusIndex):
    statuses = {'0': 'paused',
                '1': 'not checked yet',
                '2': 'up',
                '8': 'seems down',
                '9': 'down'}
    return statuses[statusIndex]

def pspStatus(statusIndex):
    statuses = {'0': 'paused',
                '1': 'active'}
    return statuses[statusIndex]

def pspSort(sortIndex):
    sorts = {'1': 'friendly name (a-z)',
             '2': 'friendly name (z-a)',
             '3': 'status (up-down-paused)',
             '4': 'status (down-up-paused)'}
    return sorts[sortIndex]
