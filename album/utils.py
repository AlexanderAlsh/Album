import magic
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
import datetime
import uuslug


@deconstructible
class ImageValidator(object):
    """Валидатор загружаемых изображений"""
    error_messages = {
        'max_size': ("Размер загружаемого файла не должен превышать: %(max_size)s."
                     "Размер вашего файла: %(size)s."),
        'min_size': ("Минимальный размер файла: %(min_size)s. "
                     "Размер вашего файла: %(size)s."),
        'content_type': "Тип фотографий %(content_type)s не поддерживается.",
    }

    def __init__(self, max_size=4 * 1024 * 1024, min_size=None, content_types=("image/png", "image/jpeg", "image/jpg")):
        self.max_size = max_size
        self.min_size = min_size
        self.content_types = content_types

    def __call__(self, data):
        if self.max_size is not None and data.size > self.max_size:
            params = {
                'max_size': filesizeformat(self.max_size),
                'size': filesizeformat(data.size),
            }
            raise ValidationError(self.error_messages['max_size'],
                                  'max_size', params)

        if self.min_size is not None and data.size < self.min_size:
            params = {
                'min_size': filesizeformat(self.min_size),
                'size': filesizeformat(data.size)
            }
            raise ValidationError(self.error_messages['min_size'],
                                  'min_size', params)

        if self.content_types:
            content_type = magic.from_buffer(data.read(), mime=True)
            data.seek(0)

            if content_type not in self.content_types:
                params = {'content_type': content_type}
                raise ValidationError(self.error_messages['content_type'],
                                      'content_type', params)

    def __eq__(self, other):
        return (
                isinstance(other, ImageValidator) and
                self.max_size == other.max_size and
                self.min_size == other.min_size and
                self.content_types == other.content_types
        )


validate_image = ImageValidator(max_size=5242880,
                                content_types=("image/png", "image/jpg", "image/jpeg"))


def uploader(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.date.today()
    filename = f'{uuslug.slugify(".".join(filename.split(".")[:-1]))}.{ext}'
    return f'uploads/{today.year}/{today.month}/{filename}'
