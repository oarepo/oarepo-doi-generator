

from oarepo_doi_generator.json_schema_mapping import schema_mapping
from sample.record import SampleRecord


def test_response(app, db):
    record = SampleRecord.create({ "id": "1234","title": "Fir", "_primary_community": "cesnet", "InvenioID": "1234"})

    with app.app_context():
        data = schema_mapping(record=record, pid_type="drecid")

    assert data == {
        'data': {
            'id': '1234', 'type': 'drecid', 'attributes':
                {'event': 'publish',
                 'prefix': '12345',
                 'creators': [{'name': 'Various authors'}],
                 'titles': 'Fir',
                 'types': {'resourceTypeGeneral': 'Dataset'},
                 'url': 'https://repozitar-test.cesnet.cz/cesnet/datasets/dat-7w607-k0s56',
                 'schemaVersion': 'http://datacite.org/schema/kernel-4', 'publisher': "CESNET"
                 }
        }
    }

    record = SampleRecord.create({"id": "1234", "InvenioID": "1234", "_primary_community": "cesnet","publication_year": "1970","title": "First title", "creators": [
    {
      "person_or_org": {
        "name": "Alzp Pokorna"
      }
    },
        {
            "person_or_org": {
                "name": "Kch kch"
            }
        }
  ],})

    with app.app_context():
        data = schema_mapping(record=record, pid_type="drecid")

    assert data == {'data': {'attributes': {'creators': [{'name': 'Alzp Pokorna'},
                                      {'name': 'Kch kch'}],
                         'event': 'publish',
                         'prefix': '12345',
                         'publicationYear': '1970',
                         'publisher': "CESNET",
                         'schemaVersion': 'http://datacite.org/schema/kernel-4',
                         'titles': 'First title',
                         'types': {'resourceTypeGeneral': 'Dataset'},
                         'url': 'https://repozitar-test.cesnet.cz/cesnet/datasets/dat-7w607-k0s56'},
          'id': '1234',
          'type': 'drecid'}}

    record = SampleRecord.create(
        {"id": "1234", "InvenioID": "1234", "_primary_community": "cesnet", "document_type": "book", "publication_year": "1970", "title": "First title", "creators": [
            {
                "person_or_org": {
                    "name": "Alzp Pokorna"
                }
            },
            {
                "person_or_org": {
                    "name": "Kch kch"
                }
            }
        ], })

    with app.app_context():
        data = schema_mapping(record=record, pid_type="drecid")

    assert data == {'data': {'attributes': {'creators': [{'name': 'Alzp Pokorna'},
                                                         {'name': 'Kch kch'}],
                                            'event': 'publish',
                                            'prefix': '12345',
                                            'publicationYear': '1970',
                                            'publisher': "CESNET",
                                            'schemaVersion': 'http://datacite.org/schema/kernel-4',
                                            'titles': 'First title',
                                            'types': {'resourceTypeGeneral': 'Book'},
                                            'url': 'https://repozitar-test.cesnet.cz/cesnet/datasets/dat-7w607-k0s56'},
                             'id': '1234',
                             'type': 'drecid'}}
    app.config.update(DOI_DATACITE_PUBLISHER = "Alzp")

    with app.app_context():
        data = schema_mapping(record=record, pid_type="drecid")

    assert data == {'data': {'attributes': {'creators': [{'name': 'Alzp Pokorna'},
                                                         {'name': 'Kch kch'}],
                                            'event': 'publish',
                                            'prefix': '12345',
                                            'publicationYear': '1970',
                                            'publisher': "Alzp",
                                            'schemaVersion': 'http://datacite.org/schema/kernel-4',
                                            'titles': 'First title',
                                            'types': {'resourceTypeGeneral': 'Book'},
                                            'url': 'https://repozitar-test.cesnet.cz/cesnet/datasets/dat-7w607-k0s56'},
                             'id': '1234',
                             'type': 'drecid'}}
