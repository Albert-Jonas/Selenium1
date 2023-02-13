from hitel import torlesztoreszlet_ho
import pytest


@pytest.mark.parametrize("hitelosszeg, eves_kamat,futamido_ev,expected", [
    (10000, 5, 1, 875), (2000000, 3, 3, 60707), (1350000, 5, 2, 62015)])
def test_torlesztoreszlet_ho(hitelosszeg, eves_kamat, futamido_ev, expected):
    assert torlesztoreszlet_ho(hitelosszeg, eves_kamat, futamido_ev) == expected