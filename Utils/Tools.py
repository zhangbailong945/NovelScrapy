import logging
import os

from PyQt5.QtCore import QFile,QIODevice,QTextStream,QTextCodec

log=logging.getLogger("NovelScrapy")

def readData(path):
    file=QFile(path)
    if not file.open(QIODevice.ReadOnly):
        log.warn("读取样式文件失败")
        return ''
    stream=QTextStream(file)
    stream.setCodec(QTextCodec.codecForName('utf-8'))
    data=stream.readAll()
    del stream
    return data

def initLog(file=None,level=logging.DEBUG,formatter=None):
    formatter=formatter or logging.Formatter(
        '[%(asctime)s %(name)s %(module)s:%(funcName)s:%(lineno)s] %(levelname)-8 %(message)s'
        if level==logging.DEBUG else '[%(asctime)s %(name)s] %(levelname)-8s %(message)s'
    )
    logger=logging.getLogger('NovelScrapy')
    logger.setLevel(level)

    stream_handler=logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if file and os.path.abspath(file):
        file_handler=logging.FileHandler(file,mode='w')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)







