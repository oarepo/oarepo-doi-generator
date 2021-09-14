import responses

from oarepo_doi_generator.api import doi_approved, doi_request
from sample.record import SampleRecord


def test_doi_request(app, db):
    record = SampleRecord.create({ "id": "1234", "InvenioID": "1234","title": "Fir", "_primary_community": "cesnet", "identifiers": [
    {
      "identifier": "123456",
      "scheme": "cosi"
    }
  ]
                                   })

    rec= doi_request(record=record)
    assert rec == {
        'id': '1234', "InvenioID": "1234", 'title': 'Fir',
        '_primary_community': 'cesnet',
        'identifiers': [{'identifier': '123456', 'scheme': 'cosi'},
                        {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]
        , '$schema': 'https://localhost:5000/schemas/sample/sample-v1.0.0.json'}

    record = SampleRecord.create({"id": "1234", "InvenioID": "1234", "title": "Fir", "_primary_community": "cesnet"})
    rec = doi_request(record=record)
    assert rec == {
        'id': '1234', "InvenioID": "1234", 'title': 'Fir',
        '_primary_community': 'cesnet',
        'identifiers': [
                        {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]
        , '$schema': 'https://localhost:5000/schemas/sample/sample-v1.0.0.json'}

    record = SampleRecord.create({"id": "1234", "InvenioID": "1234", "title": "Fir", "_primary_community": "cesnet", 'identifiers': [
            {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]})
    rec = doi_request(record=record)
    assert rec == {
        'id': '1234', "InvenioID": "1234", 'title': 'Fir',
        '_primary_community': 'cesnet',
        'identifiers': [
            {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]
        , '$schema': 'https://localhost:5000/schemas/sample/sample-v1.0.0.json'}


def test_doi_registration(app, db):
    record = SampleRecord.create({
        'id': '1234', "InvenioID": "1234", 'title': 'Fir',
        '_primary_community': 'cesnet',
        'identifiers': [
            {'identifier': '', 'scheme': 'doi', 'status': 'requested'}]
        , '$schema': 'https://localhost:5000/schemas/sample/sample-v1.0.0.json'})

    mock_response = b'{"data": {"id": "10.23644/ydc3-1692"}}'
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST ,'https://api.test.datacite.org/dois',
                 body=mock_response, status=201,
                 content_type='application/vnd.api+json')
        resp = doi_approved(record=record, pid_type="neco", test_mode=True)
        assert resp == {'id': '1234', "InvenioID": "1234", 'title': 'Fir', '_primary_community': 'cesnet', 'identifiers': [{'identifier': '10.23644/ydc3-1692', 'scheme': 'doi'}], '$schema': 'https://localhost:5000/schemas/sample/sample-v1.0.0.json'}

