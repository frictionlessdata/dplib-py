from typing import List

from jsonschema.exceptions import ValidationError
from jsonschema.validators import validator_for  # type: ignore

from ... import types
from ...models import Profile


def profile_check(profile: Profile, *, data: types.IDict) -> List[ValidationError]:
    Validator = validator_for(profile.jsonSchema)  # type: ignore
    validator = Validator(profile.jsonSchema)  # type: ignore
    errors: List[ValidationError] = list(validator.iter_errors(data))  # type: ignore
    return errors
