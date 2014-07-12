from Data import Video

from hachoir_core.error import HachoirError
from hachoir_core.stream import InputIOStream
from hachoir_parser import guessParser
from hachoir_metadata import extractMetadata

def addVideo(vidFile, event):
    metadata = getMetadata(vidFile)
    vid = Video()
    vid.event = event
    vid.timestamp = metadata.get("created_date")
    vid.primary = ( not event.primary )
    vid.offset = getOffset(event, vid.timestamp)
    vid.put()
    retrun vid.key.id()

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
