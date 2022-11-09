from django.core.exceptions import ValidationError


def validate_image_less_than_5mb(image):
    fieldsize = image.file.size
    megabyte_limit = 5.0
    if fieldsize > megabyte_limit*1024*1024:
        raise ValidationError(f'Max file size is {megabyte_limit}MB')

