# Pushizo Python SDK

Pushizo public API'si için Python sunucu SDK'sı (Python 3.9+, [httpx](https://www.python-httpx.org/)).
Modeller ve kaynak metotları `api/openapi.yaml`'dan üretilir; kimlik doğrulama, yeniden deneme, idempotency,
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
