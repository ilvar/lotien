from PIL import Image
from StringIO import StringIO

from django.core.files.uploadedfile import SimpleUploadedFile


def resize_attachment(file_):
    size = (960, 9999)
    try:
        temp = StringIO()
        image = Image.open(file_)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(temp, 'jpeg')
        temp.seek(0)
        return SimpleUploadedFile(file_.name, temp.read(), content_type='image/jpeg')
    except Exception as ex:
        return file_
