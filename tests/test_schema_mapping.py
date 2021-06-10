import json

from oarepo_doi_generator.json_schema_mapping import schema_mapping
from sample.record import SampleRecord

def test_response(app, db, client):
    record = SampleRecord.create({ "id": "1234","title": "Fir"})

    with app.app_context():
        data = schema_mapping(record=record, pid_type="drecid", test_mode=True)
    assert data == {
        'data':
            {'id': '1234', 'type': 'drecid', 'attributes':
                {'event': 'publish', 'prefix': '12345',
                 'creators': [{'name': 'Various authors'}],
                 'titles': 'First title', 'types': {'resourceTypeGeneral': 'Dataset'},
                 'url': 'https://repozitar-test.cesnet.cz/localhost:5000/records/1234',
                 'schemaVersion': 'http://datacite.org/schema/kernel-4', 'publisher': None
                 }
             }
    }

  #   record = SampleRecord.create({"id": "1234","publication_year": "1970","title": "First title", "creators": [
  #   {
  #     "person_or_org": {
  #       "name": "Alzp Pokorna"
  #     }
  #   },
  #       {
  #           "person_or_org": {
  #               "name": "Kch kch"
  #           }
  #       }
  # ],})
  #
  #   with app.app_context():
  #       data = schema_mapping(record=record, pid_type="drecid", test_mode=True)
  #   print(data)
  #   assert data == {
  #       'data':
  #           {'id': '1234', 'type': 'drecid', 'attributes':
  #               {'event': 'publish', 'prefix': '12345',
  #                'creators': [{'name': 'Various authors'}],
  #                'titles': 'First title', 'types': {'resourceTypeGeneral': 'Dataset'},
  #                'url': 'https://repozitar-test.cesnet.cz/localhost:5000/records/1234',
  #                'schemaVersion': 'http://datacite.org/schema/kernel-4', 'publisher': None
  #                }
  #            }
  #   }

def test_schema_mapping(app):
    dataset = {
        "creators": [
            {
                "person_or_org": {
                    "family_name": "Vera Erbes",
                    "given_name": "Vera Erbes",
                    "name": "Vera Erbes, Vera Erbes",
                    "type": "personal"
                }
            }
        ],
        "id": "dat-7w607-k0s56",
        "publication_date": "2019-11-15",
        "resource_type": {
            "type": [
                {
                    "is_ancestor": False,
                    "level": 1,
                    "links": {
                        "self": "http://127.0.0.1:5000/api/2.0/taxonomies/resourceType/datasets"
                    },
                    "title": {
                        "cs": "Datasety",
                        "en": "Datasets"
                    }
                }
            ]
        },
        "title": {
            "_": "Code and data for colouration experiment 'WFS in listening room'",
            "en": "Code and data for colouration experiment 'WFS in listening room'"
        },
        "canonical_url": 'https://127.0.0.1:5000/cesnet/datasets/dat-7w607-k0s56'
    }
    #canonical_url = 'https://127.0.0.1:5000/cesnet/datasets/dat-7w607-k0s56'

    setattr(dataset, 'canonical_url', 'https://127.0.0.1:5000/cesnet/datasets/dat-7w607-k0s56')
    with app.app_context():
       data =  schema_mapping(record = dataset, pid_type="drecid", test_mode=True)
    print(data)
