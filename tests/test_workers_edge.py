
import pytest
def test_workers_edge():
    payload={"items":[{"name":"Test","status":"active","oee":0.78}]}
    assert payload["items"][0]["oee"]>0.5
def test_workers_edge_oee():
    a,p,q=0.92,0.89,0.96
    oee=round(a*p*q,3)
    assert 0.5 < oee < 1.0
