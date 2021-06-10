from marshmallow import fields, validate, Schema
from marshmallow_utils.fields import SanitizedUnicode
from oarepo_invenio_model.marshmallow import InvenioRecordMetadataSchemaV1Mixin
from marshmallow.fields import List
class PersonOrOrganizationSchema(Schema):
    """Person or Organization schema."""

    type = SanitizedUnicode()
    name = SanitizedUnicode()
class ContributorSchema(Schema):
    """Contributor schema."""
    person_or_org = fields.Nested(PersonOrOrganizationSchema)

class SampleSchemaV1(InvenioRecordMetadataSchemaV1Mixin):
    title = fields.String(validate=validate.Length(min=2), required=True)
    creators = List(fields.Nested(ContributorSchema))
    publication_year = fields.String()
    kc = fields.String(validate=validate.Length(min=5), required=True)
