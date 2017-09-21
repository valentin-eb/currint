currint
=======

Integer based, fixed-precision currency calculation.

A set of helper libraries to do currency calculations using only integers,
and with currency safety (you can't add two different currencies together).

Represents all values as integer amounts in the minor unit (using
ISO 4217 exponent values), and can render numbers to strings or decimals too.

Prevents addition of different currencies, inexact division, and a few other
things you really shouldn't be doing with currencies.

Usage
-----

Create values using ``currint.Amount.from_value_and_major`` if you have Decimals or strings::

    >> currint.Amount.from_code_and_major("USD", "1.23")
    <Amount USD, 123>

Or using ``currint.Amount.from_value_and_minor`` if you already have minor values::

    >> currint.Amount.from_code_and_minor("GBP", "4223")
    <Amount GBP, 4223>

You can then perform safe mathematics::

    amount.apply_factor(2)
    amount.divide_and_round(1.34)

And output as decimals of major units if needed::

    >> amount.to_major_decimal()
    "42.23"

Or directly use the minor values::

    >> amount.value
    4223
    >> amount.currency.code
    "GBP"
