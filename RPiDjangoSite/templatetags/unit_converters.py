from django import template

register = template.Library()

# Convert Celsius to Fahrenheit 
@register.filter
def celsius_to_fahrenheit(value):
    return float(value) * 9/5 + 32

# Convert Farenheit to Celsius
@register.filter
def fahrenheit_to_celsius(value):
    return (float(value) - 32) * 5/9

# Convert millibars to inches Hg
@register.filter
def mbar_to_hg(value):
    return float(value) / 33.864

# Convert inches Hg to millibars
@register.filter
def hg_to_mbar(value):
    return float(value) * 33.864