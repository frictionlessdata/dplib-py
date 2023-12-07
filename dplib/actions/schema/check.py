#  from pydantic import BaseModel, ValidationError
#  from pydantic_core import ErrorDetails

#  def schema_check(cls, descriptor: Dict[str, Any]):
#  errors: List[ErrorDetails] = []
#  try:
#  cls.model_validate(descriptor)
#  except ValidationError as e:
#  errors = e.errors()
#  return errors


def schema_check():
    pass
