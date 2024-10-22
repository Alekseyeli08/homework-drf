from rest_framework.serializers import ValidationError


def validate_forbidden_url(value):
    if 'youtube.com'not in value.lower():
        raise ValidationError('Использованна запрещенная ссылка')
