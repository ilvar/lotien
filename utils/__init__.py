from django.conf import settings
from django.core.files.storage import get_storage_class

thumbnail_storage = get_storage_class(settings.THUMBNAIL_DEFAULT_STORAGE)()
