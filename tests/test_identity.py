"""SDK JWT identity verification belirteci (ES256) testleri."""

import base64
import json

import pytest

cryptography = pytest.importorskip("cryptography")

from cryptography.hazmat.primitives import hashes, serialization  # noqa: E402
from cryptography.hazmat.primitives.asymmetric import ec  # noqa: E402
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature  # noqa: E402

from pushizo import Pushizo, identity_token  # noqa: E402


def _decode(part: str) -> bytes:
    return base64.urlsafe_b64decode(part + "=" * (-len(part) % 4))


def _key_pem():
    key = ec.generate_private_key(ec.SECP256R1())
    pem = key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()).decode()
    return key, pem


def test_baslik_talepler_ve_imza_dogrulanir():
    key, pem = _key_pem()
    token = identity_token(pem, "main", "app_1", "kullanici-1", expires_in=600, now=1_800_000_000)
    header, payload, sig = token.split(".")
    assert json.loads(_decode(header)) == {"alg": "ES256", "typ": "JWT", "kid": "main"}
    assert json.loads(_decode(payload)) == {"sub": "kullanici-1", "aud": "app_1", "iat": 1_800_000_000, "exp": 1_800_000_600}
    raw = _decode(sig)
    assert len(raw) == 64
    der = encode_dss_signature(int.from_bytes(raw[:32], "big"), int.from_bytes(raw[32:], "big"))
    key.public_key().verify(der, f"{header}.{payload}".encode(), ec.ECDSA(hashes.SHA256()))


def test_statik_yardimci_ve_omur_siniri():
    _, pem = _key_pem()
    assert Pushizo.identity_token(pem, "k", "a", "e").count(".") == 2
    with pytest.raises(ValueError):
        identity_token(pem, "k", "a", "e", expires_in=90_000)
