from hachoir_core.error import HachoirError
from hachoir_core.stream import InputIOStream
from hachoir_parser import guessParser
from hachoir_metadata import extractMetadata

def addVideo(vidFile):
    #f = open(vidFile, 'rb')
    metadata = getMetadata(vidFile)
    print metadata
    params = {}
    #params['timestamp'] = metadata.get("created_date")
    #params['primary'] = ( not event.primary )
    return params

def setEvent(videoId, event):
    vid = getVideo(videoId)
    vid.event = event
    vid.offset = getOffset(event, vid.timestamp)

def getVideo(videoId):
    Video.get_by_id(videoId)

def getOffset(event, timestamp):
    return (timestamp - event.primary.timestamp).total_seconds

def getMetadata(vidFile):
    try:
        vidFile.seek(0)
    except (AttributeError, IOError):
        return None

    stream = InputIOStream(vidFile, None, tags=[])
    parser = guessParser(stream)

    if not parser:
        return None

    try:
        metadata = extractMetadata(parser)
    except HachoirError:
        return None

    return metadata
