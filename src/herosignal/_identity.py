"""SDK JWT identity verification belirteci (ES256; ADR-0023 §9)."""

import base64
import json
import time
from typing import Optional

MAX_LIFETIME_SECONDS = 86_400


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def identity_token(
    private_key_pem: str,
    kid: str,
    app_id: str,
    external_id: str,
    expires_in: int = 3600,
    now: Optional[int] = None,
) -> str:
    """İstemci SDK'sına verilecek ES256 JWT: ``sub`` = external_id, ``aud`` = app_id, ömür en çok 24 saat.

    Uygulamanız belirteci kendi sunucusundan alır ve ``login(external_id, jwt=...)`` ile SDK'ya verir. İmza için
    ``cryptography`` paketi gerekir: ``pip install "herosignal[jwt]"``.
    """
    if expires_in <= 0 or expires_in > MAX_LIFETIME_SECONDS:
        raise ValueError("expires_in 1…86400 aralığında olmalı.")
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import ec
        from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
    except ImportError as exc:  # pragma: no cover - kurulum hatası iletisi
        raise ImportError('identity_token için cryptography gerekli: pip install "herosignal[jwt]"') from exc

    key = serialization.load_pem_private_key(private_key_pem.encode("utf-8"), password=None)
    if not isinstance(key, ec.EllipticCurvePrivateKey) or key.curve.name != "secp256r1":
        raise ValueError("ES256 için P-256 (secp256r1) EC özel anahtarı gerekli.")
    iat = int(time.time()) if now is None else now
    header = _b64url(json.dumps({"alg": "ES256", "typ": "JWT", "kid": kid}, separators=(",", ":")).encode())
    payload = _b64url(
        json.dumps({"sub": external_id, "aud": app_id, "iat": iat, "exp": iat + expires_in}, separators=(",", ":")).encode()
    )
    der = key.sign(f"{header}.{payload}".encode("ascii"), ec.ECDSA(hashes.SHA256()))
    r, s = decode_dss_signature(der)
    # JWS ES256 imzası DER değil r||s (her biri 32 bayt).
    return f"{header}.{payload}.{_b64url(r.to_bytes(32, 'big') + s.to_bytes(32, 'big'))}"
