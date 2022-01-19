import json
from functools import lru_cache

import wtforms.form
import pytest
import pathlib


@lru_cache()
def load_file(name):
    return json.loads(
        (pathlib.Path(__file__).parent / 'fixtures' / name).read_text()
    )


@pytest.fixture(scope="session")
def product_schema(request):
    path = pathlib.Path(__file__).parent / 'product.json'
    with path.open('r') as fp:
        return json.load(fp)


@pytest.fixture(scope="session")
def person_schema(request):
    path = pathlib.Path(__file__).parent / 'person.json'
    with path.open('r') as fp:
        return json.load(fp)


@pytest.fixture(scope="session")
def address_schema(request):
    path = pathlib.Path(__file__).parent / 'address.json'
    with path.open('r') as fp:
        return json.load(fp)


@pytest.fixture(scope="session")
def geo_schema(request):
    path = pathlib.Path(__file__).parent / 'geo.json'
    with path.open('r') as fp:
        return json.load(fp)


@pytest.fixture(scope="session")
def refs_and_defs_schema(request):
    path = pathlib.Path(__file__).parent / 'refs_defs.json'
    with path.open('r') as fp:
        return json.load(fp)


@pytest.fixture(scope="session")
def network_form(request):
    """
    class NetworkForm(pydantic.BaseModel):
        any_ip: IPvAnyAddress
        any_ip_interface: IPvAnyInterface
        any_ip_network: IPvAnyNetwork
    """
    return load_file('network_form.json')


class DummyField:
    data = None

    @property
    def raw_data(self):
        return [self.data]


@pytest.fixture
def dummy_field():
    return DummyField()


@pytest.fixture(scope="function")
def form():
    return wtforms.form.Form()
