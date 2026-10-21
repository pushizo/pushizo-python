<!-- pushizo:header -->
<p align="center">
  <a href="https://pushizo.com"><img src="https://raw.githubusercontent.com/pushizo/.github/main/profile/assets/mark.svg" alt="Pushizo" width="56" height="56"></a>
</p>
<p align="center">
  <a href="https://docs.pushizo.com/docs/sdk/python"><img src="https://img.shields.io/badge/docs-docs.pushizo.com-5b4bdb" alt="Docs"></a>
  <a href="https://docs.pushizo.com/docs/api"><img src="https://img.shields.io/badge/API-reference-b44fc4" alt="API reference"></a>
  <a href="https://github.com/pushizo/pushizo-python/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-16130f" alt="License: MIT"></a>
</p>
<p align="center"><a href="#english">English</a> · <a href="#türkçe">Türkçe</a></p>

## English

**Pushizo Python SDK** — Server-side SDK for Python with synchronous and asyncio clients. Models and resources are generated from the Pushizo OpenAPI schema; retries, idempotency, pagination and webhook verification are built in.

> **Status:** Publishing to PyPI is in progress.<br>
> **Durum:** PyPI yayını hazırlanıyor.

**Install from GitHub until then · O zamana kadar GitHub'dan kurulum:**

```bash
pip install https://github.com/pushizo/pushizo-python/releases/download/v0.1.0/pushizo-0.1.0-py3-none-any.whl
```

**After publication · Yayından sonra:**

```bash
pip install pushizo
```

The detailed guide below is in Turkish; code samples are language-neutral. Full documentation:
[docs.pushizo.com/docs/sdk/python](https://docs.pushizo.com/docs/sdk/python) · API reference: [docs.pushizo.com/docs/api](https://docs.pushizo.com/docs/api).

## Türkçe
<!-- /pushizo:header -->

# Pushizo Python SDK

Pushizo public API'si için Python sunucu SDK'sı (Python 3.9+, [httpx](https://www.python-httpx.org/)).
Modeller ve kaynak metotları [Pushizo OpenAPI şemasından](https://github.com/pushizo/pushizo-openapi) üretilir; kimlik doğrulama, yeniden deneme, idempotency,
sayfalama ve webhook imza doğrulaması el yazımı katmandadır.

## Kurulum

```bash
pip install pushizo
```

## Kullanım

```python
import os
from pushizo import Pushizo

hs = Pushizo(api_key=os.environ["HS_API_KEY"], app_id="app_…")  # yerelde base_url="http://localhost:4000"

# Bildirim gönder (Idempotency-Key verilmezse otomatik UUID üretilir; yeniden denemelerde aynı anahtar kullanılır)
res = hs.notifications.create(
    {
        "target": {"include_aliases": {"external_id": ["user-42"]}},
        "contents": {"en": "Your order shipped", "tr": "Siparişiniz kargoya verildi"},
    },
    idempotency_key="order-1001",
)
print(res["id"], res["status"])

# Kullanıcı oluştur/güncelle ve abonelik ekle
hs.users.upsert({"external_id": "user-42", "tags": {"plan": "pro"}})
hs.users.add_subscription("external_id", "user-42", {"channel": "email", "token": "ayse@example.com"})

# Cursor sayfalama: tüm sayfaları tek tek dolaşır
for segment in hs.segments.list_all(limit=100):
    print(segment["name"])

# Başka bir app için tek çağrı
hs.apps.get(app_id="app_diger")

# SDK identity verification: identity_hash = HMAC-SHA256(sdk_secret, external_id)
identity_hash = Pushizo.identity_hash(os.environ["HS_SDK_SECRET"], "user-42")
```

Modeller çalışma zamanında sade `dict`'tir; tipler `pushizo._generated.models` içindeki `TypedDict`'lerle
(`CreateNotificationDto`, `Message` …) editörde görünür. SDK'da metodu olmayan uçlar ve JSON dışı yanıtlar için
`hs.request("GET", "/v1/apps/app_…/analytics/messages", query={"format": "csv"})` kullanılabilir.

### Ayarlar

| Parametre | Varsayılan | Açıklama |
|-----------|------------|----------|
| `api_key` | — | `hs_live_…` API anahtarı (Bearer) |
| `app_id` | `None` | Çağrıda `app_id=` verilmezse kullanılan app |
| `base_url` | `https://api.pushizo.com` | API adresi |
| `timeout` | `30` | Deneme başına zaman aşımı (sn) |
| `max_retries` | `3` | En fazla yeniden deneme (politika: aşağıda) |
| `auto_idempotency_key` | `True` | `Idempotency-Key` destekleyen çağrılarda otomatik UUID |
| `http_client` | — | Özel `httpx.Client` (proxy, TLS) |

Her çağrı `request_options={"timeout": 5, "max_retries": 0, "headers": {...}}` ile ayrıca ayarlanabilir.

### Hatalar

429 her metotta; 5xx ve ağ hataları GET/HEAD/OPTIONS/PUT/DELETE'te, POST/PATCH'te yalnızca `Idempotency-Key` varsa (otomatik anahtar dahil) veya istek sunucuya hiç gönderilemediyse (bağlantı reddi, DNS hatası, bağlantı zaman aşımı) üstel geri çekilmeyle (0,3 / 1 / 3 sn) yeniden denenir; `Retry-After` başlığına uyulur.
Kalıcı hatalar HTTP durumuna göre tiplendirilir; hepsi `PushizoError`'dan türer ve `status`, `code` (`HS_…`),
`request_id`, `details` taşır:

```python
from pushizo import ErrorCode, NotFoundError, RateLimitError, PushizoError

try:
    hs.notifications.get("msg_yok")
except NotFoundError as e:
    print(e.code == ErrorCode.NOT_FOUND, e.request_id)
except RateLimitError:
    ...
except PushizoError as e:  # InvalidRequestError, AuthenticationError, PermissionDeniedError, ConflictError, ServerError, NetworkError
    print(e.status, e.code, e.message)
```

## Webhook imza doğrulaması

Pushizo her webhook isteğini `Pushizo-Signature: t=<unix>,v1=<hex>` başlığıyla imzalar
(`v1 = HMAC-SHA256(secret, f"{t}.{ham_gövde}")`). Ham gövdeyi (JSON'u ayrıştırmadan) doğrulayın:

```python
from flask import Flask, request
from pushizo import WebhookSignatureError, construct_webhook_events

app = Flask(__name__)

@app.post("/hooks/pushizo")
def pushizo_hook():
    try:
        events = construct_webhook_events(
            request.get_data(),                         # ham gövde
            request.headers.get("Pushizo-Signature"),
            os.environ["HS_WEBHOOK_SECRET"],            # rotasyonda [eski, yeni] verilebilir
        )
    except WebhookSignatureError as e:
        return e.reason, 400
    for event in events:                              # tekil veya batch gövde
        ...                                           # Pushizo-Event-Id ile tekrarları ayıklayın
    return "", 204
```

Zaman damgası 5 dakikadan eskiyse (`tolerance_seconds`) istek tekrar (replay) sayılır ve reddedilir.

## Geliştirme

```bash
pip install -e ".[dev]"
pytest                                   # sdk/python içinde
node sdk/scripts/generate-server-sdks.mjs --lang python   # depo kökünde; modeller/kaynaklar yeniden üretilir
```

`src/pushizo/_generated/` elle düzenlenmez. Webhook testleri `sdk/testdata/webhook-signature-vectors.json`
ortak vektörlerini kullanır (Node, PHP, Go, Java, .NET ve Ruby SDK'larıyla aynı).

<!-- pushizo:footer -->
---

## Support · Destek

- **Guide · Rehber:** [docs.pushizo.com/docs/sdk/python](https://docs.pushizo.com/docs/sdk/python)
- **API reference & OpenAPI · API referansı ve OpenAPI:** [docs.pushizo.com/docs/api](https://docs.pushizo.com/docs/api) ·
  [pushizo-openapi](https://github.com/pushizo/pushizo-openapi)
- **Bugs & ideas · Hata ve öneri:** [Issues](https://github.com/pushizo/pushizo-python/issues)
- **Security · Güvenlik:** please do not open public issues; email [security@pushizo.com](mailto:security@pushizo.com) ·
  herkese açık issue açmayın, bu adrese yazın.
- **Help · Destek:** [support@pushizo.com](mailto:support@pushizo.com)

This repository is mirrored automatically from the Pushizo main repository on every release. Please open an issue
instead of a pull request; fixes land in the main repository and ship with the next release.
Bu depo her sürümde Pushizo ana deposundan otomatik yansıtılır. Pull request yerine issue açın; düzeltmeler ana depoda
yapılır ve bir sonraki sürümle buraya gelir.

Released under the MIT License · MIT lisanslıdır — [LICENSE](https://github.com/pushizo/pushizo-python/blob/main/LICENSE).
<!-- /pushizo:footer -->
