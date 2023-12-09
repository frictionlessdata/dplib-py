from typing import List

from jsonschema.validators import validator_for  # type: ignore

from ... import types
from ...errors.metadata import MetadataError
from ...models import Profile


# TODO: validate against metadata.profile as well (extension)
def metadata_check(metadata: types.IDict, *, profile: Profile) -> List[MetadataError]:
    Validator = validator_for(profile.jsonSchema)  # type: ignore
    validator = Validator(profile.jsonSchema)  # type: ignore
    errors: List[MetadataError] = []
    for validation_error in validator.iter_errors(metadata):  # type: ignore
        errors.append(MetadataError(validation_error))  # type: ignore
    return errors
