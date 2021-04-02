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