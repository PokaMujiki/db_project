from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_gte_0(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is less or equals 0'),
            params={'value': value},
        )


def validate_gt_0(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s is less or equals 0'),
            params={'value': value},
        )


def validate_empty_string(value):
    if value == '':
        raise ValidationError(
            _('%(value)s is empty string'),
            params={'value': value},
        )
