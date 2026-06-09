from decimal import Decimal, InvalidOperation

from django import template


register = template.Library()


@register.filter
def currency(value, symbol='$'):
    if value in (None, ''):
        return f"{symbol}0.00"

    try:
        amount = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        return f"{symbol}0.00"

    return f"{symbol}{amount:,.2f}"
