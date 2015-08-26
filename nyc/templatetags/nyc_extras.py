from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter
@stringfilter
def sentence_case(value):
    return value.replace("_", " ").capitalize()

@register.filter
@stringfilter
def facet_name(value):
    if value == 'bill_type': return 'Legislation type'
    if value == 'sponsorships': return 'Sponsor'
    if value == 'from_organization': return 'Legislative body'

@register.filter
@stringfilter
def remove_action_subj(bill_action_desc):
	# removes 'by X' from bill action descriptions & expands abbrevs
	# for more readable action labels
	clean_action = re.sub(r'\bComm\b', 'Committee', bill_action_desc)
	clean_action = re.sub(r'\bRecved\b', 'Received', clean_action)
	clean_action = re.sub(r'[,\s]*by\s[^\s]*', '', clean_action)
	return clean_action