from datetime import datetime
import os
import random

def audio_file_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'media/audio/{year}/{month}/{day}/{audio_id}/{basename}{randomstring}{ext}'.format(
        audio_id=instance.store.domainKey, 
        basename=basefilename, randomstring=randomstr, ext=file_extension,
        year=_now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d')
        )