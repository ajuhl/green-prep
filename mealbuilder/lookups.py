from selectable.base import ModelLookup
from selectable.registry import registry, LookupAlreadyRegistered
from .models import Food

class FoodLookup(ModelLookup):
  model = Food
  search_field = 'name__contains'

try:
  registry.register(FoodLookup)
except LookupAlreadyRegistered:
  pass