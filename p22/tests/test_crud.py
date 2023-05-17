def test_create(app, client):
    res = client.get('/create')
    assert res.status_code == "" # jsut example to drop the test

    data = {"text": "primer"}
    res = client.post('/create', data=data)
    assert res.status_code == 302

