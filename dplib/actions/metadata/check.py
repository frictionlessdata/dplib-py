from typing import List, Union

from jsonschema.validators import validator_for  # type: ignore

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.profile import read_profile
from ...models import Profile


# TODO: validate against metadata.profile as well (extension)
def metadata_check(
    metadata: Union[str, types.IDict], *, profile_name: str
) -> List[MetadataError]:
    # Prepare metadata/profile
    profile = Profile.from_dict(read_profile(profile_name))
    if isinstance(metadata, str):
        metadata = read_data(metadata)

    # Create validator
    Validator = validator_for(profile.jsonSchema)  # type: ignore
    validator = Validator(profile.jsonSchema)  # type: ignore

    # Fetch errors
    errors: List[MetadataError] = []
    for validation_error in validator.iter_errors(metadata):  # type: ignore
        errors.append(MetadataError(validation_error))  # type: ignore

    return errors
