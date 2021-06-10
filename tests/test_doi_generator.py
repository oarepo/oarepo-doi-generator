import requests
import responses
from sample.record import SampleRecord

from oarepo_doi_generator.api import doi_approved, doi_request


def test_doi_request(app, db, client):
    #todo test article
    record = SampleRecord.create({ "id": "1234","title": "Fir", "_primary_community": "cesnet", "identifiers": [
    {
      "identifier": "123456",
      "scheme": "cosi"
    }
  ]
                                   })
    # body = {
    #     'data': {
    #         'id': '1234', 'type': 'drecid', 'attributes':
    #             {'event': 'publish',
    #              'prefix': '12345',
    #              'creators': [{'name': 'Various authors'}],
    #              'titles': 'Fir',
    #              'types': {'resourceTypeGeneral': 'Dataset'},
    #              'url': 'https://repozitar-test.cesnet.cz/cesnet/datasets/dat-7w607-k0s56',
    #              'schemaVersion': 'http://datacite.org/schema/kernel-4', 'publisher': "CESNET"
    #              }
    #     }
    # }
    rec= doi_request(record=record)
    assert rec == {
        'id': '1234', 'title': 'Fir',
        '_primary_community': 'cesnet',
        'identifiers': [{'identifier': '123456', 'scheme': 'cosi'},
                        {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]
        , '$schema': 'https://localhost:5000/schemas/sample/sample-v1.0.0.json'}

    record = SampleRecord.create({"id": "1234", "title": "Fir", "_primary_community": "cesnet"})
    rec = doi_request(record=record)
    assert rec == {
        'id': '1234', 'title': 'Fir',
        '_primary_community': 'cesnet',
        'identifiers': [
                        {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]
        , '$schema': 'https://localhost:5000/schemas/sample/sample-v1.0.0.json'}

    record = SampleRecord.create({"id": "1234", "title": "Fir", "_primary_community": "cesnet", 'identifiers': [
            {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]})
    rec = doi_request(record=record)
    assert rec == {
        'id': '1234', 'title': 'Fir',
        '_primary_community': 'cesnet',
        'identifiers': [
            {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]
        , '$schema': 'https://localhost:5000/schemas/sample/sample-v1.0.0.json'}
    #rec = doi_approved(record=record, pid_type="neco", test_mode=True)

    # with responses.RequestsMock() as rsps:
    #     rsps.add(responses.POST ,'https://api.test.datacite.org/dois',
    #              body=body, status=201,
    #              content_type='application/vnd.api+json')



