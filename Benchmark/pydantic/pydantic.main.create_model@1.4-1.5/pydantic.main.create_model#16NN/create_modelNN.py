from pydantic import BaseModel, create_model, Field, validator
from typing import Optional

class MyBaseModel(BaseModel):
    base_field: int = Field(default=0, title='Base Field')

@validator('dynamic_field', check_fields=False)
def validate_dynamic_field(cls, value):
    if value < 0:
        raise ValueError('Value must be non-negative')
    return value
field_definitions = {'dynamic_field': (int, Field(default=42, gt=0)), 'optional_field': (Optional[str], None)}
DynamicModel = create_model(model_name='DynamicModel', __config__=None, __module__=None, __validators__={'validate_dynamic_field': validate_dynamic_field}, __base__=MyBaseModel)
model_instance = DynamicModel(dynamic_field=10, base_field=5, optional_field='Hello')
print(model_instance)
