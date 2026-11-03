# Bu dosya api/openapi.yaml'dan sdk/scripts/generate-server-sdks.mjs ile üretilmiştir; elle düzenlemeyin.
"""API kaynakları; her metot bir OpenAPI işlemine karşılık gelir."""

from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Optional

from .._types import FileInput, RequestOptions
from .models import *  # noqa: F401,F403

if TYPE_CHECKING:  # pragma: no cover
    from .._client import Pushizo


class NotificationsResource:
    """Bildirim gönderme, durum, iptal, teslimatlar ve geçmiş dışa aktarımı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def create(
        self,
        body: "CreateNotificationDto",
        *,
        app_id: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CreateNotificationResult":
        """Bildirim oluştur (202, asenkron teslimat)

        ``POST /v1/notifications``
        """
        return self._client._call(
            "POST",
            "/v1/notifications",
            path_params={},
            body=body,
            app_id=app_id,
            body_app_id=True,
            idempotent=True,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        source: Optional[str] = None,
        kind: Optional[str] = None,
        status: Optional[str] = None,
        sort: Optional[str] = None,
        label: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "MessageList":
        """Mesaj listesi (app_id zorunlu)

        ``GET /v1/notifications``

        Parametreler:
            source: Değerler: "campaign", "api", "journey", "test".
            kind: Değerler: "campaign", "api", "journey", "test".
            status: Değerler: "queued", "processing", "completed", "cancelled", "failed".
            sort: Değerler: "created_at", "-created_at".
        """
        return self._client._call(
            "GET",
            "/v1/notifications",
            path_params={},
            query={"limit": limit, "cursor": cursor, "source": source, "kind": kind, "status": status, "sort": sort, "label": label},
            app_id=app_id,
            query_app_id=True,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        source: Optional[str] = None,
        kind: Optional[str] = None,
        status: Optional[str] = None,
        sort: Optional[str] = None,
        label: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Message"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                source=source,
                kind=kind,
                status=status,
                sort=sort,
                label=label,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def estimate(
        self,
        body: "EstimateAudienceDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EstimateAudienceResult":
        """Kaydedilmemiş hedef için alıcı sayısı (gönderim yapmaz)

        ``POST /v1/notifications/estimate``
        """
        return self._client._call(
            "POST",
            "/v1/notifications/estimate",
            path_params={},
            body=body,
            app_id=app_id,
            body_app_id=True,
            request_options=request_options,
        )

    def get(
        self,
        message_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Message":
        """Mesaj durumu ve sayaçları

        ``GET /v1/notifications/{messageId}``
        """
        return self._client._call(
            "GET",
            "/v1/notifications/{messageId}",
            path_params={"messageId": message_id},
            app_id=app_id,
            query_app_id=True,
            request_options=request_options,
        )

    def cancel(
        self,
        message_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Message":
        """Zamanlanmış/kuyruktaki mesajı iptal et

        ``DELETE /v1/notifications/{messageId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/notifications/{messageId}",
            path_params={"messageId": message_id},
            app_id=app_id,
            query_app_id=True,
            request_options=request_options,
        )

    def deliveries(
        self,
        message_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "DeliveryList":
        """Abone bazlı teslimat sonuçları (cursor)

        ``GET /v1/notifications/{messageId}/deliveries``

        Parametreler:
            status: Değerler: "pending", "sent", "delivered", "failed", "bounced", "suppressed", "expired", "cancelled".
        """
        return self._client._call(
            "GET",
            "/v1/notifications/{messageId}/deliveries",
            path_params={"messageId": message_id},
            query={"limit": limit, "cursor": cursor, "status": status},
            app_id=app_id,
            query_app_id=True,
            request_options=request_options,
        )

    def deliveries_all(
        self,
        message_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Delivery"]:
        """``deliveries`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.deliveries(
                message_id,
                limit=limit,
                status=status,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def history(
        self,
        message_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Export":
        """Bildirim geçmişi CSV işi (teslimatlar; tamamlanınca download_url)

        ``GET /v1/notifications/{messageId}/history``
        """
        return self._client._call(
            "GET",
            "/v1/notifications/{messageId}/history",
            path_params={"messageId": message_id},
            app_id=app_id,
            query_app_id=True,
            request_options=request_options,
        )

    def export_events(
        self,
        message_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Export":
        """Mesaj olay CSV işi (gönderildi/teslim/açıldı/tıklandı/bounce…; tamamlanınca download_url)

        ``POST /v1/notifications/{messageId}/export_events``
        """
        return self._client._call(
            "POST",
            "/v1/notifications/{messageId}/export_events",
            path_params={"messageId": message_id},
            app_id=app_id,
            query_app_id=True,
            request_options=request_options,
        )


class UsersResource:
    """Kullanıcı oluşturma/güncelleme (tag, özellik), arama ve abonelik ekleme."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        sort: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        last_active_after: Optional[str] = None,
        last_active_before: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserList":
        """Kullanıcı listesi

        ``GET /v1/apps/{appId}/users``

        Parametreler:
            sort: Değerler: "last_active_at", "-last_active_at".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users",
            path_params={},
            query={"limit": limit, "cursor": cursor, "sort": sort, "q": q, "tag": tag, "last_active_after": last_active_after, "last_active_before": last_active_before},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        sort: Optional[str] = None,
        q: Optional[str] = None,
        tag: Optional[str] = None,
        last_active_after: Optional[str] = None,
        last_active_before: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["User"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                sort=sort,
                q=q,
                tag=tag,
                last_active_after=last_active_after,
                last_active_before=last_active_before,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def upsert(
        self,
        body: "UpsertUserDto",
        *,
        app_id: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserDetail":
        """Kullanıcı oluştur/güncelle (external_id ile, isteğe bağlı aboneliklerle)

        ``POST /v1/apps/{appId}/users``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/users",
            path_params={},
            body=body,
            app_id=app_id,
            idempotent=True,
            idempotency_key=idempotency_key,
            request_options=request_options,
        )

    def search(
        self,
        body: "UsersSearchBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserList":
        """Segment tanımı ile kullanıcı arama

        ``POST /v1/apps/{appId}/users/search``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/users/search",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get_by_alias(
        self,
        label: str,
        value: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserDetail":
        """Alias ile kullanıcı (hs_id, external_id veya özel etiket)

        ``GET /v1/apps/{appId}/users/by/{label}/{value}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users/by/{label}/{value}",
            path_params={"label": label, "value": value},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        label: str,
        value: str,
        body: "PatchUserDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserDetail":
        """Tag/property merge-patch ve deltas

        ``PATCH /v1/apps/{appId}/users/by/{label}/{value}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/users/by/{label}/{value}",
            path_params={"label": label, "value": value},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        label: str,
        value: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Kullanıcıyı sil (abonelikler silinir, olaylar anonimleşir)

        ``DELETE /v1/apps/{appId}/users/by/{label}/{value}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/users/by/{label}/{value}",
            path_params={"label": label, "value": value},
            app_id=app_id,
            request_options=request_options,
        )

    def get_identity(
        self,
        label: str,
        value: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserIdentity":
        """Kullanıcının tüm kimlikleri (hs_id, external_id, özel alias'lar)

        ``GET /v1/apps/{appId}/users/by/{label}/{value}/identity``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users/by/{label}/{value}/identity",
            path_params={"label": label, "value": value},
            app_id=app_id,
            request_options=request_options,
        )

    def export(
        self,
        label: str,
        value: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserExport":
        """Kullanıcı verisini dışa aktar (KVKK/GDPR taşınabilirlik): profil, alias, abonelik, son olaylar

        ``GET /v1/apps/{appId}/users/by/{label}/{value}/export``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users/by/{label}/{value}/export",
            path_params={"label": label, "value": value},
            app_id=app_id,
            request_options=request_options,
        )

    def add_subscription(
        self,
        label: str,
        value: str,
        body: "AddSubscriptionDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Subscription":
        """Kullanıcıya abonelik ekle

        ``POST /v1/apps/{appId}/users/by/{label}/{value}/subscriptions``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/users/by/{label}/{value}/subscriptions",
            path_params={"label": label, "value": value},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class AliasesResource:
    """Kullanıcı kimlikleri (alias): ekleme ve kaldırma."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def add(
        self,
        label: str,
        value: str,
        body: "AddAliasDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserDetail":
        """Alias ekle

        ``PATCH /v1/apps/{appId}/users/by/{label}/{value}/identity``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/users/by/{label}/{value}/identity",
            path_params={"label": label, "value": value},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        label: str,
        value: str,
        alias_label: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserDetail":
        """Alias kaldır

        ``DELETE /v1/apps/{appId}/users/by/{label}/{value}/identity/{aliasLabel}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/users/by/{label}/{value}/identity/{aliasLabel}",
            path_params={"label": label, "value": value, "aliasLabel": alias_label},
            app_id=app_id,
            request_options=request_options,
        )


class SubscriptionsResource:
    """Abonelik (cihaz/e-posta/SMS) okuma, güncelleme, silme ve sahip atama."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def get(
        self,
        subscription_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Subscription":
        """Abonelik detayı

        ``GET /v1/apps/{appId}/subscriptions/{subscriptionId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/subscriptions/{subscriptionId}",
            path_params={"subscriptionId": subscription_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        subscription_id: str,
        body: "PatchSubscriptionDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Subscription":
        """Abonelik güncelle

        ``PATCH /v1/apps/{appId}/subscriptions/{subscriptionId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/subscriptions/{subscriptionId}",
            path_params={"subscriptionId": subscription_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        subscription_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Aboneliği sil

        ``DELETE /v1/apps/{appId}/subscriptions/{subscriptionId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/subscriptions/{subscriptionId}",
            path_params={"subscriptionId": subscription_id},
            app_id=app_id,
            request_options=request_options,
        )

    def get_user_identity(
        self,
        subscription_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserIdentity":
        """Aboneliğin sahibi kullanıcının kimlikleri

        ``GET /v1/apps/{appId}/subscriptions/{subscriptionId}/user/identity``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/subscriptions/{subscriptionId}/user/identity",
            path_params={"subscriptionId": subscription_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update_by_token(
        self,
        token_type: str,
        token: str,
        body: "PatchSubscriptionDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Subscription":
        """Token ile abonelik güncelle (token_type: ios_push, android_push, hms_push, web_push, email, sms veya eski sağlayıcı adları iOSPush, AndroidPush, HuaweiPush, ChromePush, FirefoxPush, SafariPush, Email, SMS)

        ``PATCH /v1/apps/{appId}/subscriptions_by_token/{tokenType}/{token}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/subscriptions_by_token/{tokenType}/{token}",
            path_params={"tokenType": token_type, "token": token},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def set_owner(
        self,
        subscription_id: str,
        body: "SetOwnerDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Subscription":
        """Aboneliği external_id ile kullanıcıya bağla

        ``POST /v1/apps/{appId}/subscriptions/{subscriptionId}/owner``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/subscriptions/{subscriptionId}/owner",
            path_params={"subscriptionId": subscription_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class EventsResource:
    """Özel olay gönderimi ve olay tanımları."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def send(
        self,
        body: "ApiEventsDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EventsAccepted":
        """Toplu olay gönder (en fazla 500)

        ``POST /v1/apps/{appId}/events``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/events",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def list_definitions(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EventDefinitionList":
        """Olay tanımları

        ``GET /v1/apps/{appId}/events/definitions``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/events/definitions",
            path_params={},
            query={"limit": limit, "cursor": cursor},
            app_id=app_id,
            request_options=request_options,
        )

    def list_definitions_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["EventDefinition"]:
        """``list_definitions`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list_definitions(
                limit=limit,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def get_definition(
        self,
        name: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EventDefinitionDetail":
        """Olay detayı

        ``GET /v1/apps/{appId}/events/definitions/{name}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/events/definitions/{name}",
            path_params={"name": name},
            app_id=app_id,
            request_options=request_options,
        )

    def update_definition(
        self,
        name: str,
        body: "PatchEventDefinitionDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EventDefinition":
        """Görünen ad / dönüşüm işareti

        ``PATCH /v1/apps/{appId}/events/definitions/{name}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/events/definitions/{name}",
            path_params={"name": name},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class SegmentsResource:
    """Segment yönetimi, önizleme ve kitle tahmini."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        q: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SegmentPage":
        """Segment listesi

        ``GET /v1/apps/{appId}/segments``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/segments",
            path_params={},
            query={"limit": limit, "cursor": cursor, "q": q},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        q: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Segment"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                q=q,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "SegmentsCreateBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Segment":
        """Segment oluştur

        ``POST /v1/apps/{appId}/segments``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/segments",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def preview(
        self,
        body: "SegmentsPreviewBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SegmentPreview":
        """Tanım ile sayım ve örnek kullanıcılar

        ``POST /v1/apps/{appId}/segments/preview``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/segments/preview",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        segment_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Segment":
        """Segment detayı

        ``GET /v1/apps/{appId}/segments/{segmentId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/segments/{segmentId}",
            path_params={"segmentId": segment_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        segment_id: str,
        body: "SegmentsUpdateBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Segment":
        """Segment güncelle

        ``PATCH /v1/apps/{appId}/segments/{segmentId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/segments/{segmentId}",
            path_params={"segmentId": segment_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        segment_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Segment sil

        ``DELETE /v1/apps/{appId}/segments/{segmentId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/segments/{segmentId}",
            path_params={"segmentId": segment_id},
            app_id=app_id,
            request_options=request_options,
        )

    def used_by(
        self,
        segment_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SegmentCampaigns":
        """Segmenti kullanan kampanyalar

        ``GET /v1/apps/{appId}/segments/{segmentId}/campaigns``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/segments/{segmentId}/campaigns",
            path_params={"segmentId": segment_id},
            app_id=app_id,
            request_options=request_options,
        )

    def estimate(
        self,
        segment_id: str,
        *,
        force: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SegmentEstimate":
        """Tahmini sayım

        ``POST /v1/apps/{appId}/segments/{segmentId}/estimate``

        Parametreler:
            force: true: önbelleği atla, tam sayım Değerler: "true", "false".
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/segments/{segmentId}/estimate",
            path_params={"segmentId": segment_id},
            query={"force": force},
            app_id=app_id,
            request_options=request_options,
        )


class TemplatesResource:
    """Şablon yönetimi, sürümler ve önizleme."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        q: Optional[str] = None,
        channel: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "TemplatePage":
        """Şablon listesi

        ``GET /v1/apps/{appId}/templates``

        Parametreler:
            channel: Değerler: "ios_push", "android_push", "hms_push", "adm_push", "wns_push", "web_push", "email", "sms", "whatsapp", "rcs".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/templates",
            path_params={},
            query={"limit": limit, "cursor": cursor, "q": q, "channel": channel},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        q: Optional[str] = None,
        channel: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Template"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                q=q,
                channel=channel,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "CreateTemplateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Template":
        """Şablon oluştur

        ``POST /v1/apps/{appId}/templates``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/templates",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        template_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Template":
        """Şablon detayı

        ``GET /v1/apps/{appId}/templates/{templateId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/templates/{templateId}",
            path_params={"templateId": template_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        template_id: str,
        body: "UpdateTemplateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Template":
        """Şablon güncelle

        ``PATCH /v1/apps/{appId}/templates/{templateId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/templates/{templateId}",
            path_params={"templateId": template_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        template_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Şablon sil

        ``DELETE /v1/apps/{appId}/templates/{templateId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/templates/{templateId}",
            path_params={"templateId": template_id},
            app_id=app_id,
            request_options=request_options,
        )

    def stats(
        self,
        template_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "TemplateStats":
        """Şablon analitiği

        ``GET /v1/apps/{appId}/templates/{templateId}/stats``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/templates/{templateId}/stats",
            path_params={"templateId": template_id},
            app_id=app_id,
            request_options=request_options,
        )

    def copy_to_app(
        self,
        template_id: str,
        body: "CopyTemplateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Template":
        """Şablonu aynı organizasyondaki başka bir app'e kopyala

        ``POST /v1/apps/{appId}/templates/{templateId}/copy_to_app``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/templates/{templateId}/copy_to_app",
            path_params={"templateId": template_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def versions(
        self,
        template_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "TemplateVersionList":
        """Sürüm geçmişi

        ``GET /v1/apps/{appId}/templates/{templateId}/versions``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/templates/{templateId}/versions",
            path_params={"templateId": template_id},
            app_id=app_id,
            request_options=request_options,
        )

    def render(
        self,
        template_id: str,
        body: "RenderTemplateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RenderPreview":
        """Şablonu örnek verilerle render et

        ``POST /v1/apps/{appId}/templates/{templateId}/render``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/templates/{templateId}/render",
            path_params={"templateId": template_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class CampaignsResource:
    """Kampanya yaşam döngüsü (zamanlama, gönderim, duraklatma, onay) ve istatistikler."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        q: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        channel: Optional[str] = None,
        label: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CampaignPage":
        """Kampanya listesi

        ``GET /v1/apps/{appId}/campaigns``

        Parametreler:
            status: Değerler: "draft", "scheduled", "running", "paused", "completed", "cancelled", "failed".
            type: Değerler: "one_time", "scheduled", "recurring", "automated", "transactional".
            channel: Değerler: "ios_push", "android_push", "hms_push", "adm_push", "wns_push", "web_push", "email", "sms", "whatsapp", "rcs".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/campaigns",
            path_params={},
            query={"limit": limit, "cursor": cursor, "q": q, "status": status, "type": type, "channel": channel, "label": label},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        q: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        channel: Optional[str] = None,
        label: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Campaign"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                q=q,
                status=status,
                type=type,
                channel=channel,
                label=label,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "CampaignsCreateBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Kampanya oluştur

        ``POST /v1/apps/{appId}/campaigns``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Kampanya detayı

        ``GET /v1/apps/{appId}/campaigns/{campaignId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/campaigns/{campaignId}",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        campaign_id: str,
        body: "CampaignsUpdateBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Kampanya güncelle

        ``PATCH /v1/apps/{appId}/campaigns/{campaignId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/campaigns/{campaignId}",
            path_params={"campaignId": campaign_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Kampanya sil

        ``DELETE /v1/apps/{appId}/campaigns/{campaignId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/campaigns/{campaignId}",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def schedule(
        self,
        campaign_id: str,
        body: "ScheduleCampaignDto",
        *,
        force: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Zamanla; e-posta liste koruması 409 → force=true (admin kapsamı)

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/schedule``

        Parametreler:
            force: Değerler: "true", "false".
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/schedule",
            path_params={"campaignId": campaign_id},
            query={"force": force},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def send(
        self,
        campaign_id: str,
        *,
        force: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Hemen gönder; e-posta liste koruması 409 → force=true (admin kapsamı)

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/send``

        Parametreler:
            force: Değerler: "true", "false".
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/send",
            path_params={"campaignId": campaign_id},
            query={"force": force},
            app_id=app_id,
            request_options=request_options,
        )

    def email_risk(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CampaignEmailRisk":
        """E-posta liste riski (tahmini geçersiz oranı, 7/30 gün bounce oranı)

        ``GET /v1/apps/{appId}/campaigns/{campaignId}/email-risk``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/campaigns/{campaignId}/email-risk",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def pause(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Duraklat

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/pause``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/pause",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def resume(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Sürdür

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/resume``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/resume",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def cancel(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """İptal

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/cancel``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/cancel",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def duplicate(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Çoğalt

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/duplicate``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/duplicate",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def approve(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Onayla

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/approve``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/approve",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def stats(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CampaignStats":
        """İstatistikler

        ``GET /v1/apps/{appId}/campaigns/{campaignId}/stats``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/campaigns/{campaignId}/stats",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def variant_stats(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CampaignVariantStats":
        """A/B varyant karşılaştırması

        ``GET /v1/apps/{appId}/campaigns/{campaignId}/variants/stats``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/campaigns/{campaignId}/variants/stats",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def select_winner(
        self,
        campaign_id: str,
        body: "SelectWinnerDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """A/B kazananını seç

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/winner``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/winner",
            path_params={"campaignId": campaign_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def deliveries(
        self,
        campaign_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "DeliveryList":
        """Abone bazlı teslimatlar

        ``GET /v1/apps/{appId}/campaigns/{campaignId}/deliveries``

        Parametreler:
            status: Değerler: "pending", "sent", "delivered", "failed", "bounced", "suppressed", "expired", "cancelled".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/campaigns/{campaignId}/deliveries",
            path_params={"campaignId": campaign_id},
            query={"limit": limit, "cursor": cursor, "status": status},
            app_id=app_id,
            request_options=request_options,
        )

    def deliveries_all(
        self,
        campaign_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Delivery"]:
        """``deliveries`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.deliveries(
                campaign_id,
                limit=limit,
                status=status,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def resend_failed(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Başarısız teslimatlara yeniden gönder

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/resend-failed``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/resend-failed",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def messages(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "MessageList":
        """Kampanya çalıştırmaları

        ``GET /v1/apps/{appId}/campaigns/{campaignId}/messages``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/campaigns/{campaignId}/messages",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )


class InAppMessagesResource:
    """Uygulama içi (in-app) mesaj yönetimi ve durum değişiklikleri."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InAppMessagePage":
        """In-app mesajlar (durum filtresi; istatistik dahil)

        ``GET /v1/apps/{appId}/in-app-messages``

        Parametreler:
            status: Değerler: "draft", "active", "paused", "archived".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/in-app-messages",
            path_params={},
            query={"limit": limit, "cursor": cursor, "status": status},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["InAppMessage"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                status=status,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "CreateInAppDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InAppMessage":
        """In-app mesaj oluştur (taslak)

        ``POST /v1/apps/{appId}/in-app-messages``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/in-app-messages",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        message_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InAppMessage":
        """In-app mesaj detayı ve istatistikleri

        ``GET /v1/apps/{appId}/in-app-messages/{messageId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/in-app-messages/{messageId}",
            path_params={"messageId": message_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        message_id: str,
        body: "UpdateInAppDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InAppMessage":
        """In-app mesajı düzenle

        ``PATCH /v1/apps/{appId}/in-app-messages/{messageId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/in-app-messages/{messageId}",
            path_params={"messageId": message_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        message_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """In-app mesajı sil

        ``DELETE /v1/apps/{appId}/in-app-messages/{messageId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/in-app-messages/{messageId}",
            path_params={"messageId": message_id},
            app_id=app_id,
            request_options=request_options,
        )

    def status(
        self,
        message_id: str,
        body: "InAppStatusDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InAppMessage":
        """Yayınla / duraklat / arşivle

        ``POST /v1/apps/{appId}/in-app-messages/{messageId}/status``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/in-app-messages/{messageId}/status",
            path_params={"messageId": message_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def select_winner(
        self,
        message_id: str,
        body: "InAppWinnerDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InAppMessage":
        """A/B kazananını elle seç

        ``POST /v1/apps/{appId}/in-app-messages/{messageId}/winner``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/in-app-messages/{messageId}/winner",
            path_params={"messageId": message_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def winner(
        self,
        message_id: str,
        body: "InAppWinnerDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InAppMessage":
        """A/B kazananını elle seç

        ``POST /v1/apps/{appId}/in-app-messages/{messageId}/winner``

        .. deprecated:: ``select_winner`` kullanın; bu ad geriye dönük uyumluluk için korunur.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/in-app-messages/{messageId}/winner",
            path_params={"messageId": message_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class InboxResource:
    """Kullanıcı bildirim kutusu (inbox): listeleme, okundu işaretleme ve arşivleme."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def teams(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxTeamList":
        """Takımlar

        ``GET /v1/apps/{appId}/inbox/teams``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/inbox/teams",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def agents(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxAgentList":
        """Temsilciler ve varlık durumu

        ``GET /v1/apps/{appId}/inbox/agents``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/inbox/agents",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def settings(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxSettings":
        """Gelen kutusu ayarları

        ``GET /v1/apps/{appId}/inbox/settings``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/inbox/settings",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def update_settings(
        self,
        body: "InboxSettingsUpdateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxSettings":
        """Gelen kutusu ayarlarını güncelle

        ``PUT /v1/apps/{appId}/inbox/settings``
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/inbox/settings",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def metrics(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        channel: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxMetrics":
        """Gelen kutusu metrikleri (ilk yanıt/çözüm ort. ve p90, SLA, temsilci tablosu)

        ``GET /v1/apps/{appId}/inbox/metrics``

        Parametreler:
            channel: Değerler: "sms", "whatsapp", "rcs", "email", "chat".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/inbox/metrics",
            path_params={},
            query={"from": from_, "to": to, "channel": channel},
            app_id=app_id,
            request_options=request_options,
        )

    def list(
        self,
        label: str,
        value: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        include_archived: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxPage":
        """Kullanıcının bildirim kutusu (okunmamış sayısı dahil)

        ``GET /v1/apps/{appId}/users/by/{label}/{value}/inbox``

        Parametreler:
            include_archived: Değerler: "true", "false".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users/by/{label}/{value}/inbox",
            path_params={"label": label, "value": value},
            query={"limit": limit, "cursor": cursor, "include_archived": include_archived},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        label: str,
        value: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        include_archived: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["InboxItem"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                label,
                value,
                limit=limit,
                include_archived=include_archived,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def read_all(
        self,
        label: str,
        value: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxReadAllResult":
        """Tümünü okundu işaretle

        ``POST /v1/apps/{appId}/users/by/{label}/{value}/inbox/read-all``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/users/by/{label}/{value}/inbox/read-all",
            path_params={"label": label, "value": value},
            app_id=app_id,
            request_options=request_options,
        )

    def read(
        self,
        label: str,
        value: str,
        item_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxItem":
        """Okundu işaretle

        ``POST /v1/apps/{appId}/users/by/{label}/{value}/inbox/{itemId}/read``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/users/by/{label}/{value}/inbox/{itemId}/read",
            path_params={"label": label, "value": value, "itemId": item_id},
            app_id=app_id,
            request_options=request_options,
        )

    def archive(
        self,
        label: str,
        value: str,
        item_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Kutudan kaldır (arşivle)

        ``DELETE /v1/apps/{appId}/users/by/{label}/{value}/inbox/{itemId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/users/by/{label}/{value}/inbox/{itemId}",
            path_params={"label": label, "value": value, "itemId": item_id},
            app_id=app_id,
            request_options=request_options,
        )


class SuppressionsResource:
    """E-posta/SMS gönderim engeli (suppression) listesi."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        channel: Optional[str] = None,
        reason: Optional[str] = None,
        value: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SuppressionPage":
        """Suppression list (e-posta/SMS gönderilmeyecek adresler; kanal/neden/değer filtresi)

        ``GET /v1/apps/{appId}/suppressions``

        Parametreler:
            channel: Değerler: "email", "sms", "whatsapp", "rcs".
            reason: Değerler: "bounce", "complaint", "manual", "unsubscribe_link", "stop".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/suppressions",
            path_params={},
            query={"limit": limit, "cursor": cursor, "channel": channel, "reason": reason, "value": value},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        channel: Optional[str] = None,
        reason: Optional[str] = None,
        value: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Suppression"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                channel=channel,
                reason=reason,
                value=value,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "CreateSuppressionDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Suppression":
        """Adres ekle (manuel engel; değer saklanmaz, özet + maskeli gösterim)

        ``POST /v1/apps/{appId}/suppressions``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/suppressions",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        suppression_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Kaydı kaldır (adres yeniden gönderim alabilir)

        ``DELETE /v1/apps/{appId}/suppressions/{suppressionId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/suppressions/{suppressionId}",
            path_params={"suppressionId": suppression_id},
            app_id=app_id,
            request_options=request_options,
        )


class ExportsResource:
    """Veri dışa aktarma işleri."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def create(
        self,
        body: "CreateExportDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Export":
        """Export işi başlat

        ``POST /v1/apps/{appId}/exports``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/exports",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ExportList":
        """Export işleri

        ``GET /v1/apps/{appId}/exports``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/exports",
            path_params={},
            query={"limit": limit, "cursor": cursor},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Export"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def get(
        self,
        export_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Export":
        """Export durumu (download_url)

        ``GET /v1/apps/{appId}/exports/{exportId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/exports/{exportId}",
            path_params={"exportId": export_id},
            app_id=app_id,
            request_options=request_options,
        )


class ImportsResource:
    """Veri içe aktarma işleri (CSV, multipart)."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def create(
        self,
        type: str,
        file: FileInput,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Import":
        """Import işi başlat (multipart: type, file)

        ``POST /v1/apps/{appId}/imports``

        Parametreler:
            type: Değerler: "legacy_players", "csv_users".
            file: CSV dosyası (UTF-8, en fazla 50 MB)
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/imports",
            path_params={},
            form={"type": type},
            files={"file": file},
            app_id=app_id,
            request_options=request_options,
        )

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ImportList":
        """Import işleri

        ``GET /v1/apps/{appId}/imports``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/imports",
            path_params={},
            query={"limit": limit, "cursor": cursor},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Import"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def get(
        self,
        import_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Import":
        """Import durumu

        ``GET /v1/apps/{appId}/imports/{importId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/imports/{importId}",
            path_params={"importId": import_id},
            app_id=app_id,
            request_options=request_options,
        )


class WebhooksResource:
    """Giden webhook uç noktaları, teslimatlar ve yeniden gönderim."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebhookList":
        """Webhook endpoint'leri

        ``GET /v1/apps/{appId}/webhooks``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/webhooks",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateWebhookDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebhookWithSecret":
        """Endpoint oluştur (secret yalnızca bu yanıtta döner)

        ``POST /v1/apps/{appId}/webhooks``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/webhooks",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def preview(
        self,
        body: "WebhookPreviewDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebhookPreviewResult":
        """Event Streams önizlemesi: örnek olay + şablon + filtre → gövde/hata (gönderim yapmaz)

        ``POST /v1/apps/{appId}/webhooks/preview``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/webhooks/preview",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        webhook_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Webhook":
        """Endpoint detayı

        ``GET /v1/apps/{appId}/webhooks/{webhookId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/webhooks/{webhookId}",
            path_params={"webhookId": webhook_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        webhook_id: str,
        body: "UpdateWebhookDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Webhook":
        """Endpoint güncelle (URL, olaylar, batch, başlıklar, etkinleştir/durdur)

        ``PATCH /v1/apps/{appId}/webhooks/{webhookId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/webhooks/{webhookId}",
            path_params={"webhookId": webhook_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        webhook_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Endpoint sil

        ``DELETE /v1/apps/{appId}/webhooks/{webhookId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/webhooks/{webhookId}",
            path_params={"webhookId": webhook_id},
            app_id=app_id,
            request_options=request_options,
        )

    def rotate_secret(
        self,
        webhook_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebhookWithSecret":
        """Secret rotasyonu (eski secret 24 saat ikinci imza olarak gönderilir)

        ``POST /v1/apps/{appId}/webhooks/{webhookId}/rotate-secret``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/webhooks/{webhookId}/rotate-secret",
            path_params={"webhookId": webhook_id},
            app_id=app_id,
            request_options=request_options,
        )

    def test(
        self,
        webhook_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebhookDeliveryDetail":
        """Test olayı gönder (anında, sonuç döner)

        ``POST /v1/apps/{appId}/webhooks/{webhookId}/test``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/webhooks/{webhookId}/test",
            path_params={"webhookId": webhook_id},
            app_id=app_id,
            request_options=request_options,
        )

    def deliveries(
        self,
        webhook_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        event_type: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebhookDeliveryPage":
        """Teslim geçmişi (cursor; durum/olay türü filtresi)

        ``GET /v1/apps/{appId}/webhooks/{webhookId}/deliveries``

        Parametreler:
            status: Değerler: "pending", "success", "failed", "dead".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/webhooks/{webhookId}/deliveries",
            path_params={"webhookId": webhook_id},
            query={"limit": limit, "cursor": cursor, "status": status, "event_type": event_type},
            app_id=app_id,
            request_options=request_options,
        )

    def deliveries_all(
        self,
        webhook_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        event_type: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["WebhookDeliveryPageDataItem"]:
        """``deliveries`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.deliveries(
                webhook_id,
                limit=limit,
                status=status,
                event_type=event_type,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def replay(
        self,
        delivery_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebhookDeliveryDetail":
        """Teslimi yeniden gönder (aynı olay kimliğiyle)

        ``POST /v1/apps/{appId}/webhooks/deliveries/{deliveryId}/replay``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/webhooks/deliveries/{deliveryId}/replay",
            path_params={"deliveryId": delivery_id},
            app_id=app_id,
            request_options=request_options,
        )


class ChannelsResource:
    """Kanal (APNs, FCM, Web Push, e-posta, SMS) yapılandırması ve doğrulaması."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelList":
        """Kanal yapılandırmaları

        ``GET /v1/apps/{appId}/channels``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/channels",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def upsert(
        self,
        channel: str,
        body: Any,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelConfig":
        """Kimlik bilgisi yükle (APNs p8, FCM servis hesabı, VAPID, mock)

        ``PUT /v1/apps/{appId}/channels/{channel}``
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/channels/{channel}",
            path_params={"channel": channel},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def validate(
        self,
        channel: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelValidation":
        """Sağlayıcıya test bağlantısı

        ``POST /v1/apps/{appId}/channels/{channel}/validate``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/channels/{channel}/validate",
            path_params={"channel": channel},
            app_id=app_id,
            request_options=request_options,
        )


class AnalyticsResource:
    """Analitik raporları."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def overview(
        self,
        *,
        range: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "OverviewStats":
        """Genel bakış KPI

        ``GET /v1/apps/{appId}/analytics/overview``

        Parametreler:
            range: Değerler: "7d", "30d".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/analytics/overview",
            path_params={},
            query={"range": range, "from": from_, "to": to},
            app_id=app_id,
            request_options=request_options,
        )

    def messages(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        compare: Optional[str] = None,
        format: Optional[str] = None,
        group_by: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "MessagesReport":
        """Teslimat raporu

        ``GET /v1/apps/{appId}/analytics/messages``

        Parametreler:
            compare: Değerler: "true", "false".
            format: Değerler: "json", "csv".
            group_by: Değerler: "day", "channel", "campaign".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/analytics/messages",
            path_params={},
            query={"from": from_, "to": to, "compare": compare, "format": format, "group_by": group_by},
            app_id=app_id,
            request_options=request_options,
        )

    def subscriptions(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        compare: Optional[str] = None,
        format: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SubscriptionsReport":
        """Abonelik büyümesi

        ``GET /v1/apps/{appId}/analytics/subscriptions``

        Parametreler:
            compare: Değerler: "true", "false".
            format: Değerler: "json", "csv".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/analytics/subscriptions",
            path_params={},
            query={"from": from_, "to": to, "compare": compare, "format": format},
            app_id=app_id,
            request_options=request_options,
        )

    def events(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        compare: Optional[str] = None,
        format: Optional[str] = None,
        name: Optional[str] = None,
        group_by: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EventsReport":
        """Olay hacmi

        ``GET /v1/apps/{appId}/analytics/events``

        Parametreler:
            compare: Değerler: "true", "false".
            format: Değerler: "json", "csv".
            group_by: Değerler: "day", "name".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/analytics/events",
            path_params={},
            query={"from": from_, "to": to, "compare": compare, "format": format, "name": name, "group_by": group_by},
            app_id=app_id,
            request_options=request_options,
        )

    def conversions(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        compare: Optional[str] = None,
        format: Optional[str] = None,
        campaign_id: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ConversionsReport":
        """Dönüşüm/atribüsyon

        ``GET /v1/apps/{appId}/analytics/conversions``

        Parametreler:
            compare: Değerler: "true", "false".
            format: Değerler: "json", "csv".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/analytics/conversions",
            path_params={},
            query={"from": from_, "to": to, "compare": compare, "format": format, "campaign_id": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def paths(
        self,
        body: "PathBodyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PathReport":
        """Yol analizi

        ``POST /v1/apps/{appId}/analytics/paths``

        Başlangıç olayından sonra veya önce kullanıcıların izlediği yollar.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/analytics/paths",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def funnel(
        self,
        body: "FunnelBodyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "FunnelReport":
        """Funnel

        ``POST /v1/apps/{appId}/analytics/funnels``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/analytics/funnels",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def providers(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        compare: Optional[str] = None,
        format: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ProvidersReport":
        """Sağlayıcı sağlığı

        ``GET /v1/apps/{appId}/analytics/providers``

        Parametreler:
            compare: Değerler: "true", "false".
            format: Değerler: "json", "csv".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/analytics/providers",
            path_params={},
            query={"from": from_, "to": to, "compare": compare, "format": format},
            app_id=app_id,
            request_options=request_options,
        )

    def retention(
        self,
        *,
        weeks: Optional[int] = None,
        format: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RetentionReport":
        """Retention kohortu

        ``GET /v1/apps/{appId}/analytics/retention``

        Parametreler:
            format: Değerler: "json", "csv".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/analytics/retention",
            path_params={},
            query={"weeks": weeks, "format": format},
            app_id=app_id,
            request_options=request_options,
        )

    def engagement(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        compare: Optional[str] = None,
        format: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EngagementReport":
        """Etkileşim ısı haritası

        ``GET /v1/apps/{appId}/analytics/engagement``

        Parametreler:
            compare: Değerler: "true", "false".
            format: Değerler: "json", "csv".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/analytics/engagement",
            path_params={},
            query={"from": from_, "to": to, "compare": compare, "format": format},
            app_id=app_id,
            request_options=request_options,
        )


class AppsResource:
    """App listesi ve ayarları."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> "AppList":
        """App listesi (org geneli admin anahtarı)

        ``GET /v1/apps``
        """
        return self._client._call(
            "GET",
            "/v1/apps",
            path_params={},
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateAppDto",
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> "App":
        """App oluştur (org geneli admin anahtarı)

        ``POST /v1/apps``
        """
        return self._client._call(
            "POST",
            "/v1/apps",
            path_params={},
            body=body,
            request_options=request_options,
        )

    def get(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "App":
        """App detayı

        ``GET /v1/apps/{appId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        body: "UpdateAppDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "App":
        """App ayarlarını güncelle

        ``PATCH /v1/apps/{appId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class ApiKeysResource:
    """App API anahtarları: oluşturma, kapsam/IP izin listesi güncelleme, rotasyon ve iptal."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ApiKeyList":
        """App'e bağlı API anahtarları

        ``GET /v1/apps/{appId}/api-keys``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/api-keys",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateAppApiKeyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CreatedApiKey":
        """App'e bağlı API anahtarı oluştur (ham anahtar yalnızca bu yanıtta)

        ``POST /v1/apps/{appId}/api-keys``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/api-keys",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        key_id: str,
        body: "UpdateApiKeyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ApiKey":
        """Anahtarı güncelle (ad, kapsam, IP izin listesi, bitiş)

        ``PATCH /v1/apps/{appId}/api-keys/{keyId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/api-keys/{keyId}",
            path_params={"keyId": key_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def revoke(
        self,
        key_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Anahtarı iptal et

        ``DELETE /v1/apps/{appId}/api-keys/{keyId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/api-keys/{keyId}",
            path_params={"keyId": key_id},
            app_id=app_id,
            request_options=request_options,
        )

    def rotate(
        self,
        key_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CreatedApiKey":
        """Anahtarı döndür (eski değer anında geçersiz)

        ``POST /v1/apps/{appId}/api-keys/{keyId}/rotate``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/api-keys/{keyId}/rotate",
            path_params={"keyId": key_id},
            app_id=app_id,
            request_options=request_options,
        )


class OrganizationResource:
    """Organizasyon, üyeler ve denetim kayıtları."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def get(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> "Org":
        """Anahtarın ait olduğu organizasyon (org geneli admin anahtarı)

        ``GET /v1/organization``
        """
        return self._client._call(
            "GET",
            "/v1/organization",
            path_params={},
            request_options=request_options,
        )

    def members(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> "MemberList":
        """Organizasyon üyeleri (org geneli admin anahtarı)

        ``GET /v1/organization/members``
        """
        return self._client._call(
            "GET",
            "/v1/organization/members",
            path_params={},
            request_options=request_options,
        )

    def audit_logs(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        action: Optional[str] = None,
        actor_id: Optional[str] = None,
        app_id: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AuditPage":
        """Audit log (org geneli admin anahtarı; action/actor/app/tarih filtreleri, cursor)

        ``GET /v1/organization/audit-logs``
        """
        return self._client._call(
            "GET",
            "/v1/organization/audit-logs",
            path_params={},
            query={"limit": limit, "cursor": cursor, "action": action, "actor_id": actor_id, "app_id": app_id, "from": from_, "to": to},
            request_options=request_options,
        )

    def audit_logs_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        action: Optional[str] = None,
        actor_id: Optional[str] = None,
        app_id: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["AuditEntry"]:
        """``audit_logs`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.audit_logs(
                limit=limit,
                action=action,
                actor_id=actor_id,
                app_id=app_id,
                from_=from_,
                to=to,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def usage(
        self,
        *,
        days: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UsageReport":
        """Organizasyon kullanımı ve plan kotaları (org geneli anahtar)

        ``GET /v1/organization/usage``
        """
        return self._client._call(
            "GET",
            "/v1/organization/usage",
            path_params={},
            query={"days": days},
            request_options=request_options,
        )


class AdsResource:
    """ads kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list_accounts(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAccountList":
        """Bağlı reklam hesapları

        ``GET /v1/apps/{appId}/ads/accounts``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/accounts",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def list_audiences(
        self,
        *,
        ad_account_id: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAudienceList":
        """Reklam kitleleri

        ``GET /v1/apps/{appId}/ads/audiences``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/audiences",
            path_params={},
            query={"ad_account_id": ad_account_id},
            app_id=app_id,
            request_options=request_options,
        )

    def create_audience(
        self,
        body: "CreateAdAudienceDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAudience":
        """Reklam kitlesi oluştur

        ``POST /v1/apps/{appId}/ads/audiences``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/ads/audiences",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get_audience(
        self,
        audience_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAudience":
        """Reklam kitlesi ayrıntısı

        ``GET /v1/apps/{appId}/ads/audiences/{audienceId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/audiences/{audienceId}",
            path_params={"audienceId": audience_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update_audience(
        self,
        audience_id: str,
        body: "UpdateAdAudienceDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAudience":
        """Reklam kitlesini güncelle

        ``PATCH /v1/apps/{appId}/ads/audiences/{audienceId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/ads/audiences/{audienceId}",
            path_params={"audienceId": audience_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def remove_audience(
        self,
        audience_id: str,
        *,
        delete_on_platform: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdOk":
        """Reklam kitlesini sil

        ``DELETE /v1/apps/{appId}/ads/audiences/{audienceId}``

        Parametreler:
            delete_on_platform: Değerler: "true", "false".
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/ads/audiences/{audienceId}",
            path_params={"audienceId": audience_id},
            query={"delete_on_platform": delete_on_platform},
            app_id=app_id,
            request_options=request_options,
        )

    def sync(
        self,
        audience_id: str,
        body: "SyncAdAudienceDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAudienceSyncQueued":
        """Senkronu şimdi çalıştır

        ``POST /v1/apps/{appId}/ads/audiences/{audienceId}/sync``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/ads/audiences/{audienceId}/sync",
            path_params={"audienceId": audience_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def syncs(
        self,
        audience_id: str,
        *,
        limit: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAudienceSyncList":
        """Senkron geçmişi

        ``GET /v1/apps/{appId}/ads/audiences/{audienceId}/syncs``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/audiences/{audienceId}/syncs",
            path_params={"audienceId": audience_id},
            query={"limit": limit},
            app_id=app_id,
            request_options=request_options,
        )

    def lookalike(
        self,
        audience_id: str,
        body: "CreateLookalikeDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAudience":
        """Benzer kitle (lookalike) oluştur

        ``POST /v1/apps/{appId}/ads/audiences/{audienceId}/lookalikes``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/ads/audiences/{audienceId}/lookalikes",
            path_params={"audienceId": audience_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def list(
        self,
        *,
        ad_account_id: Optional[str] = None,
        level: Optional[str] = None,
        parent_id: Optional[str] = None,
        status: Optional[str] = None,
        q: Optional[str] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        limit: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdEntityList":
        """Kampanya / reklam seti / reklam listesi ve metrikler

        ``GET /v1/apps/{appId}/ads/campaigns``

        Parametreler:
            level: Değerler: "campaign", "ad_set", "ad".
            status: Değerler: "active", "paused", "pending", "rejected", "archived", "deleted", "unknown".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/campaigns",
            path_params={},
            query={"ad_account_id": ad_account_id, "level": level, "parent_id": parent_id, "status": status, "q": q, "from": from_, "to": to, "limit": limit},
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        entity_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdEntity":
        """Kampanya / reklam seti / reklam ayrıntısı

        ``GET /v1/apps/{appId}/ads/campaigns/{entityId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/campaigns/{entityId}",
            path_params={"entityId": entity_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        entity_id: str,
        body: "UpdateAdCampaignDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdEntity":
        """Durum ve günlük bütçe değişikliği

        ``PATCH /v1/apps/{appId}/ads/campaigns/{entityId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/ads/campaigns/{entityId}",
            path_params={"entityId": entity_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def refresh(
        self,
        account_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdRefreshQueued":
        """Kampanyaları ve metrikleri şimdi yenile

        ``POST /v1/apps/{appId}/ads/accounts/{accountId}/refresh``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/ads/accounts/{accountId}/refresh",
            path_params={"accountId": account_id},
            app_id=app_id,
            request_options=request_options,
        )

    def spend(
        self,
        *,
        from_: str,
        to: str,
        currency: Optional[str] = None,
        group_by: Optional[str] = None,
        ad_account_id: Optional[str] = None,
        campaign_id: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdSpendReport":
        """Harcama ve performans raporu

        ``GET /v1/apps/{appId}/ads/reports/spend``

        Parametreler:
            group_by: Değerler: "day", "platform", "account", "campaign", "ad_set".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/reports/spend",
            path_params={},
            query={"from": from_, "to": to, "currency": currency, "group_by": group_by, "ad_account_id": ad_account_id, "campaign_id": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def attribution(
        self,
        *,
        from_: str,
        to: str,
        model: Optional[str] = None,
        window_days: Optional[int] = None,
        half_life_days: Optional[int] = None,
        currency: Optional[str] = None,
        group_by: Optional[str] = None,
        conversion_events: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdAttributionReport":
        """Birleşik atribüsyon raporu (ROAS, CAC)

        ``GET /v1/apps/{appId}/ads/reports/attribution``

        Parametreler:
            model: Değerler: "last_click", "first_click", "linear", "time_decay".
            group_by: Değerler: "channel", "campaign", "ad_set".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/reports/attribution",
            path_params={},
            query={"from": from_, "to": to, "model": model, "window_days": window_days, "half_life_days": half_life_days, "currency": currency, "group_by": group_by, "conversion_events": conversion_events},
            app_id=app_id,
            request_options=request_options,
        )

    def ltv(
        self,
        *,
        months: Optional[int] = None,
        cohorts: Optional[int] = None,
        currency: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdLtvReport":
        """Kohort LTV raporu

        ``GET /v1/apps/{appId}/ads/reports/ltv``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/reports/ltv",
            path_params={},
            query={"months": months, "cohorts": cohorts, "currency": currency},
            app_id=app_id,
            request_options=request_options,
        )

    def capi_configs(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdCapiConfigList":
        """Conversions API yapılandırmaları

        ``GET /v1/apps/{appId}/ads/conversions-api/configs``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/conversions-api/configs",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def capi_deliveries(
        self,
        *,
        config_id: Optional[str] = None,
        status: Optional[str] = None,
        limit: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdCapiDeliveryList":
        """Conversions API teslim geçmişi

        ``GET /v1/apps/{appId}/ads/conversions-api/deliveries``

        Parametreler:
            status: Değerler: "pending", "sent", "failed", "skipped".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/conversions-api/deliveries",
            path_params={},
            query={"config_id": config_id, "status": status, "limit": limit},
            app_id=app_id,
            request_options=request_options,
        )

    def rules(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdBudgetAlertRuleList":
        """Bütçe uyarı kuralları

        ``GET /v1/apps/{appId}/ads/alert-rules``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/alert-rules",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create_rule(
        self,
        body: "CreateBudgetAlertRuleDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdBudgetAlertRule":
        """Bütçe uyarı kuralı oluştur

        ``POST /v1/apps/{appId}/ads/alert-rules``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/ads/alert-rules",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def update_rule(
        self,
        rule_id: str,
        body: "UpdateBudgetAlertRuleDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdBudgetAlertRule":
        """Bütçe uyarı kuralını güncelle

        ``PATCH /v1/apps/{appId}/ads/alert-rules/{ruleId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/ads/alert-rules/{ruleId}",
            path_params={"ruleId": rule_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def remove_rule(
        self,
        rule_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdOk":
        """Bütçe uyarı kuralını sil

        ``DELETE /v1/apps/{appId}/ads/alert-rules/{ruleId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/ads/alert-rules/{ruleId}",
            path_params={"ruleId": rule_id},
            app_id=app_id,
            request_options=request_options,
        )

    def alert_history(
        self,
        *,
        rule_id: Optional[str] = None,
        limit: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AdBudgetAlertList":
        """Tetiklenen bütçe uyarıları

        ``GET /v1/apps/{appId}/ads/alerts``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/ads/alerts",
            path_params={},
            query={"rule_id": rule_id, "limit": limit},
            app_id=app_id,
            request_options=request_options,
        )


class CannedResponsesResource:
    """cannedResponses kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def canned(
        self,
        *,
        q: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CannedResponseList":
        """Hazır yanıtlar

        ``GET /v1/apps/{appId}/canned-responses``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/canned-responses",
            path_params={},
            query={"q": q},
            app_id=app_id,
            request_options=request_options,
        )

    def create_canned(
        self,
        body: "CannedInputDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CannedResponse":
        """Hazır yanıt oluştur

        ``POST /v1/apps/{appId}/canned-responses``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/canned-responses",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def update_canned(
        self,
        canned_id: str,
        body: "CannedUpdateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CannedResponse":
        """Hazır yanıtı güncelle

        ``PATCH /v1/apps/{appId}/canned-responses/{cannedId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/canned-responses/{cannedId}",
            path_params={"cannedId": canned_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete_canned(
        self,
        canned_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Hazır yanıtı sil

        ``DELETE /v1/apps/{appId}/canned-responses/{cannedId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/canned-responses/{cannedId}",
            path_params={"cannedId": canned_id},
            app_id=app_id,
            request_options=request_options,
        )


class CatalogsResource:
    """catalogs kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CatalogList":
        """Ürün katalogları

        ``GET /v1/apps/{appId}/catalogs``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/catalogs",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateCatalogDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Catalog":
        """Katalog oluştur

        ``POST /v1/apps/{appId}/catalogs``

        Şablonda `{% catalog_item '<ad>' id: custom_data.product_id as urun %}{{ urun.title }}`.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/catalogs",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        catalog_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Catalog":
        """Katalog ayrıntısı

        ``GET /v1/apps/{appId}/catalogs/{catalogId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/catalogs/{catalogId}",
            path_params={"catalogId": catalog_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        catalog_id: str,
        body: "UpdateCatalogDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Catalog":
        """Kataloğu güncelle

        ``PATCH /v1/apps/{appId}/catalogs/{catalogId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/catalogs/{catalogId}",
            path_params={"catalogId": catalog_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        catalog_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Kataloğu sil

        ``DELETE /v1/apps/{appId}/catalogs/{catalogId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/catalogs/{catalogId}",
            path_params={"catalogId": catalog_id},
            app_id=app_id,
            request_options=request_options,
        )

    def items(
        self,
        catalog_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        q: Optional[str] = None,
        category: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CatalogItemsPage":
        """Ürünler

        ``GET /v1/apps/{appId}/catalogs/{catalogId}/items``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/catalogs/{catalogId}/items",
            path_params={"catalogId": catalog_id},
            query={"limit": limit, "offset": offset, "q": q, "category": category},
            app_id=app_id,
            request_options=request_options,
        )

    def upsert(
        self,
        catalog_id: str,
        body: "UpsertCatalogItemsDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CatalogUpsertResult":
        """Ürünleri ekle veya güncelle (en fazla 1000)

        ``PUT /v1/apps/{appId}/catalogs/{catalogId}/items``

        Listede olmayan ürünlere dokunulmaz. Listedeki ürünün verilmeyen alanları temizlenir.
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/catalogs/{catalogId}/items",
            path_params={"catalogId": catalog_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def upload(
        self,
        catalog_id: str,
        file: FileInput,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CatalogUpsertResult":
        """CSV ile ürün ekle veya güncelle

        ``POST /v1/apps/{appId}/catalogs/{catalogId}/items/upload``

        Parametreler:
            file: UTF-8 CSV. Zorunlu sütunlar: id, title. Bilinen: description, image_url, url, price, sale_price, currency, category, brand, in_stock. Diğerleri özellik olur. En fazla 100.000 satır, 20 MB.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/catalogs/{catalogId}/items/upload",
            path_params={"catalogId": catalog_id},
            form={},
            files={"file": file},
            app_id=app_id,
            request_options=request_options,
        )

    def item(
        self,
        catalog_id: str,
        item_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CatalogItem":
        """Ürün ayrıntısı

        ``GET /v1/apps/{appId}/catalogs/{catalogId}/items/{itemId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/catalogs/{catalogId}/items/{itemId}",
            path_params={"catalogId": catalog_id, "itemId": item_id},
            app_id=app_id,
            request_options=request_options,
        )

    def remove_item(
        self,
        catalog_id: str,
        item_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Ürünü sil

        ``DELETE /v1/apps/{appId}/catalogs/{catalogId}/items/{itemId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/catalogs/{catalogId}/items/{itemId}",
            path_params={"catalogId": catalog_id, "itemId": item_id},
            app_id=app_id,
            request_options=request_options,
        )

    def list_recommendations(
        self,
        catalog_id: str,
        *,
        strategy: str,
        limit: Optional[int] = None,
        user_id: Optional[str] = None,
        external_id: Optional[str] = None,
        item_id: Optional[str] = None,
        category: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Recommendations":
        """Ürün önerileri

        ``GET /v1/apps/{appId}/catalogs/{catalogId}/recommendations``

        Stokta olmayan ve kullanıcının satın aldığı ürünler çıkmaz. Sonuç yetmezse yedek kaynakla tamamlanır.

        Parametreler:
            strategy: Değerler: "personalized", "popular", "trending", "similar", "category", "recently_viewed", "new_arrivals".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/catalogs/{catalogId}/recommendations",
            path_params={"catalogId": catalog_id},
            query={"strategy": strategy, "limit": limit, "user_id": user_id, "external_id": external_id, "item_id": item_id, "category": category},
            app_id=app_id,
            request_options=request_options,
        )

    def config(
        self,
        catalog_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RecommendationConfig":
        """Öneri modeli

        ``GET /v1/apps/{appId}/catalogs/{catalogId}/recommendations/config``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/catalogs/{catalogId}/recommendations/config",
            path_params={"catalogId": catalog_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update_config(
        self,
        catalog_id: str,
        body: "UpdateRecommendationConfigDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RecommendationConfig":
        """Öneri modelini ayarla

        ``PUT /v1/apps/{appId}/catalogs/{catalogId}/recommendations/config``

        Model açıksa öneriler kayıttan sonra yeniden hesaplanır.
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/catalogs/{catalogId}/recommendations/config",
            path_params={"catalogId": catalog_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def compute(
        self,
        catalog_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RecommendationConfig":
        """Önerileri yeniden hesapla

        ``POST /v1/apps/{appId}/catalogs/{catalogId}/recommendations/compute``

        İş kuyruğa alınır; ilerleme `status` alanından izlenir.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/catalogs/{catalogId}/recommendations/compute",
            path_params={"catalogId": catalog_id},
            app_id=app_id,
            request_options=request_options,
        )


class CategoriesResource:
    """categories kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "MessageCategoryList":
        """Mesaj kategorileri

        ``GET /v1/apps/{appId}/categories``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/categories",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateCategoryDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "MessageCategory":
        """Kategori oluştur

        ``POST /v1/apps/{appId}/categories``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/categories",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        category_id: str,
        body: "UpdateCategoryDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "MessageCategory":
        """Kategori güncelle

        ``PATCH /v1/apps/{appId}/categories/{categoryId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/categories/{categoryId}",
            path_params={"categoryId": category_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        category_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Kategori sil

        ``DELETE /v1/apps/{appId}/categories/{categoryId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/categories/{categoryId}",
            path_params={"categoryId": category_id},
            app_id=app_id,
            request_options=request_options,
        )


class ChannelScoresResource:
    """channelScores kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def config(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelScoreConfig":
        """Kanal skoru ayarı

        ``GET /v1/apps/{appId}/channel-scores/config``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/channel-scores/config",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        body: "UpdateChannelScoreConfigDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelScoreConfig":
        """Kanal skorunu ayarla

        ``PUT /v1/apps/{appId}/channel-scores/config``

        Açıkken skorlar kayıttan sonra yeniden hesaplanır; kapatınca silinir.
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/channel-scores/config",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def compute(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelScoreConfig":
        """Kanal skorlarını yeniden hesapla

        ``POST /v1/apps/{appId}/channel-scores/compute``

        İş kuyruğa alınır; ilerleme `status` alanından izlenir.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/channel-scores/compute",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def overview(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelScoreOverview":
        """En iyi kanal dağılımı

        ``GET /v1/apps/{appId}/channel-scores/overview``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/channel-scores/overview",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def users(
        self,
        *,
        channel: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelScoreUsersPage":
        """En iyi kanalı belli kullanıcılar

        ``GET /v1/apps/{appId}/channel-scores/users``

        Parametreler:
            channel: Değerler: "push", "email", "whatsapp", "rcs", "sms".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/channel-scores/users",
            path_params={},
            query={"channel": channel, "limit": limit, "cursor": cursor},
            app_id=app_id,
            request_options=request_options,
        )

    def user(
        self,
        user_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ChannelScoreUser":
        """Kullanıcının kanal skorları

        ``GET /v1/apps/{appId}/channel-scores/users/{userId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/channel-scores/users/{userId}",
            path_params={"userId": user_id},
            app_id=app_id,
            request_options=request_options,
        )


class ContentTablesResource:
    """contentTables kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list_tables(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ContentTableList":
        """İçerik tabloları

        ``GET /v1/apps/{appId}/content-tables``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/content-tables",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create_table_upload(
        self,
        file: FileInput,
        name: str,
        key_column: str,
        *,
        description: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ContentTable":
        """CSV ile içerik tablosu oluştur

        ``POST /v1/apps/{appId}/content-tables``

        Şablonda `{% lookup '<ad>' key: user.tags.<etiket> as satir %}{{ satir.<sütun> }}`.

        Parametreler:
            file: UTF-8 CSV; ilk satır başlık. En fazla 100.000 satır, 20 MB.
            name: Liquid tablo adı (küçük harf, rakam, alt çizgi).
            key_column: Satır seçiminde kullanılan anahtar sütunu (değerleri benzersiz).
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/content-tables",
            path_params={},
            form={"name": name, "key_column": key_column, "description": description},
            files={"file": file},
            app_id=app_id,
            request_options=request_options,
        )

    def get_table(
        self,
        table_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ContentTable":
        """İçerik tablosu ayrıntısı

        ``GET /v1/apps/{appId}/content-tables/{tableId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/content-tables/{tableId}",
            path_params={"tableId": table_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update_table(
        self,
        table_id: str,
        body: "UpdateContentTableDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ContentTable":
        """İçerik tablosu açıklamasını güncelle

        ``PATCH /v1/apps/{appId}/content-tables/{tableId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/content-tables/{tableId}",
            path_params={"tableId": table_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete_table(
        self,
        table_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """İçerik tablosunu sil

        ``DELETE /v1/apps/{appId}/content-tables/{tableId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/content-tables/{tableId}",
            path_params={"tableId": table_id},
            app_id=app_id,
            request_options=request_options,
        )

    def replace_table_upload(
        self,
        table_id: str,
        file: FileInput,
        *,
        key_column: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ContentTable":
        """İçerik tablosunu yeniden yükle (sürüm artar)

        ``PUT /v1/apps/{appId}/content-tables/{tableId}/rows``

        Parametreler:
            file: Yeni CSV (tablonun tüm satırları değiştirilir, sürüm artar).
            key_column: İsteğe bağlı yeni anahtar sütunu.
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/content-tables/{tableId}/rows",
            path_params={"tableId": table_id},
            form={"key_column": key_column},
            files={"file": file},
            app_id=app_id,
            request_options=request_options,
        )

    def table_rows(
        self,
        table_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        q: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ContentTableRows":
        """İçerik tablosu satırları

        ``GET /v1/apps/{appId}/content-tables/{tableId}/rows``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/content-tables/{tableId}/rows",
            path_params={"tableId": table_id},
            query={"limit": limit, "offset": offset, "q": q},
            app_id=app_id,
            request_options=request_options,
        )


class ConversationsResource:
    """conversations kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        channel: Optional[str] = None,
        status: Optional[str] = None,
        unread: Optional[str] = None,
        q: Optional[str] = None,
        assignee: Optional[str] = None,
        team_id: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ConversationPage":
        """Konuşmalar (SMS, WhatsApp, RCS, e-posta, canlı sohbet; son mesaja göre; kanal/durum/okunmamış/atanan/takım/kişi filtresi)

        ``GET /v1/apps/{appId}/conversations``

        Parametreler:
            channel: Değerler: "sms", "whatsapp", "rcs", "email", "chat".
            status: Değerler: "open", "pending", "resolved", "closed".
            unread: Değerler: "true", "false".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/conversations",
            path_params={},
            query={"limit": limit, "cursor": cursor, "channel": channel, "status": status, "unread": unread, "q": q, "assignee": assignee, "team_id": team_id},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        channel: Optional[str] = None,
        status: Optional[str] = None,
        unread: Optional[str] = None,
        q: Optional[str] = None,
        assignee: Optional[str] = None,
        team_id: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Conversation"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                channel=channel,
                status=status,
                unread=unread,
                q=q,
                assignee=assignee,
                team_id=team_id,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def get(
        self,
        conversation_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Conversation":
        """Konuşma (atama, SLA, bot durumu, WhatsApp oturum penceresi ve açık rıza dahil)

        ``GET /v1/apps/{appId}/conversations/{conversationId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/conversations/{conversationId}",
            path_params={"conversationId": conversation_id},
            app_id=app_id,
            request_options=request_options,
        )

    def set_status(
        self,
        conversation_id: str,
        body: "ConversationUpdateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Conversation":
        """Konuşma durumu: open / pending / resolved (closed = resolved)

        ``PATCH /v1/apps/{appId}/conversations/{conversationId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/conversations/{conversationId}",
            path_params={"conversationId": conversation_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def messages(
        self,
        conversation_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        after_seq: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ConversationMessagePage":
        """Konuşma mesajları (yeniden eskiye; `after_seq` ile eskiden yeniye; giden mesaj durumu teslimattan veya okundu işaretçisinden)

        ``GET /v1/apps/{appId}/conversations/{conversationId}/messages``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/conversations/{conversationId}/messages",
            path_params={"conversationId": conversation_id},
            query={"limit": limit, "cursor": cursor, "after_seq": after_seq},
            app_id=app_id,
            request_options=request_options,
        )

    def messages_all(
        self,
        conversation_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        after_seq: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["ConversationMessagePageDataItem"]:
        """``messages`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.messages(
                conversation_id,
                limit=limit,
                after_seq=after_seq,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def reply(
        self,
        conversation_id: str,
        body: "ConversationReplyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ConversationReplyResult":
        """Yanıt gönder (client_message_id ile tekilleşir). Sohbet: doğrudan; e-posta: yanıt adresli işlemsel e-posta; WhatsApp: açık rıza zorunlu, son gelen mesajdan 24 saat içinde metin/medya, pencere dışında yalnızca onaylı şablon (aksi 422 WHATSAPP_WINDOW_CLOSED).

        ``POST /v1/apps/{appId}/conversations/{conversationId}/messages``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/conversations/{conversationId}/messages",
            path_params={"conversationId": conversation_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def read(
        self,
        conversation_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Conversation":
        """Gelen mesajları okundu işaretle (sohbette ziyaretçiye okundu bilgisi gider)

        ``POST /v1/apps/{appId}/conversations/{conversationId}/read``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/conversations/{conversationId}/read",
            path_params={"conversationId": conversation_id},
            app_id=app_id,
            request_options=request_options,
        )

    def assign(
        self,
        conversation_id: str,
        body: "ConversationAssignDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Conversation":
        """Konuşmayı temsilciye ve/veya takıma ata (inbox.manage olmadan yalnızca kendine)

        ``POST /v1/apps/{appId}/conversations/{conversationId}/assign``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/conversations/{conversationId}/assign",
            path_params={"conversationId": conversation_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def tags(
        self,
        conversation_id: str,
        body: "ConversationTagsDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ConversationTagsResult":
        """Sohbetten kişiye etiket ekle/kaldır

        ``POST /v1/apps/{appId}/conversations/{conversationId}/tags``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/conversations/{conversationId}/tags",
            path_params={"conversationId": conversation_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def activity(
        self,
        conversation_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ConversationActivity":
        """Konuşma zaman çizelgesi (atama, durum, ilk yanıt, bot devri)

        ``GET /v1/apps/{appId}/conversations/{conversationId}/activity``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/conversations/{conversationId}/activity",
            path_params={"conversationId": conversation_id},
            app_id=app_id,
            request_options=request_options,
        )


class DataFeedsResource:
    """dataFeeds kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list_feeds(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "DataFeedList":
        """Data feed listesi

        ``GET /v1/apps/{appId}/data-feeds``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/data-feeds",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create_feed(
        self,
        body: "CreateDataFeedDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "DataFeed":
        """Data feed oluştur

        ``POST /v1/apps/{appId}/data-feeds``

        URL şablonu Liquid ile kişiselleştirilir (ör. `https://api.ornek.com/u/{{ user.external_id }}`); şablonda `{{ feed.<ad>.alan }}`.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/data-feeds",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get_feed(
        self,
        feed_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "DataFeed":
        """Data feed ayrıntısı

        ``GET /v1/apps/{appId}/data-feeds/{feedId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/data-feeds/{feedId}",
            path_params={"feedId": feed_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update_feed(
        self,
        feed_id: str,
        body: "UpdateDataFeedDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "DataFeed":
        """Data feed güncelle

        ``PATCH /v1/apps/{appId}/data-feeds/{feedId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/data-feeds/{feedId}",
            path_params={"feedId": feed_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete_feed(
        self,
        feed_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Data feed sil

        ``DELETE /v1/apps/{appId}/data-feeds/{feedId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/data-feeds/{feedId}",
            path_params={"feedId": feed_id},
            app_id=app_id,
            request_options=request_options,
        )

    def test_feed(
        self,
        feed_id: str,
        body: "TestDataFeedDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "DataFeedTestResult":
        """Data feed'i örnek kullanıcıyla dene

        ``POST /v1/apps/{appId}/data-feeds/{feedId}/test``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/data-feeds/{feedId}/test",
            path_params={"feedId": feed_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class EmailDeliverabilityResource:
    """emailDeliverability kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def settings(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EmailDeliverabilitySettings":
        """E-posta teslim ayarları (BCC/arşiv, gönderim öncesi adres doğrulama, üçüncü taraf doğrulayıcı)

        ``GET /v1/apps/{appId}/email-deliverability``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/email-deliverability",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        body: "DeliverabilitySettingsDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EmailDeliverabilitySettings":
        """E-posta teslim ayarlarını güncelle (doğrulayıcı anahtarı zarf şifreli saklanır, geri okunmaz)

        ``PUT /v1/apps/{appId}/email-deliverability``
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/email-deliverability",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def verify(
        self,
        body: "VerifyAddressDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EmailAddressCheck":
        """Adres doğrulama testi (sözdizimi, MX, tek kullanımlık alan adı, rol hesabı, üçüncü taraf)

        ``POST /v1/apps/{appId}/email-deliverability/verify-address``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/email-deliverability/verify-address",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def plans(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EmailWarmupPlanList":
        """Isındırma planları (bugünkü limit/kullanım ve ileri günlere ayrılmış gönderimler)

        ``GET /v1/apps/{appId}/email-deliverability/warmup-plans``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/email-deliverability/warmup-plans",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateWarmupPlanDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EmailWarmupPlan":
        """Isındırma planı oluştur (günlük limit eğrisi veya başlangıç/çarpan/hedef; sağlayıcı payları)

        ``POST /v1/apps/{appId}/email-deliverability/warmup-plans``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/email-deliverability/warmup-plans",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        plan_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EmailWarmupPlan":
        """Isındırma planı

        ``GET /v1/apps/{appId}/email-deliverability/warmup-plans/{planId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/email-deliverability/warmup-plans/{planId}",
            path_params={"planId": plan_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update_plan(
        self,
        plan_id: str,
        body: "UpdateWarmupPlanDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EmailWarmupPlan":
        """Isındırma planını güncelle (duraklat/sürdür, eğri, paylar)

        ``PATCH /v1/apps/{appId}/email-deliverability/warmup-plans/{planId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/email-deliverability/warmup-plans/{planId}",
            path_params={"planId": plan_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        plan_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Isındırma planını sil

        ``DELETE /v1/apps/{appId}/email-deliverability/warmup-plans/{planId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/email-deliverability/warmup-plans/{planId}",
            path_params={"planId": plan_id},
            app_id=app_id,
            request_options=request_options,
        )

    def usage(
        self,
        plan_id: str,
        *,
        days: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "EmailWarmupUsage":
        """Isındırma planı gün × sağlayıcı kullanımı

        ``GET /v1/apps/{appId}/email-deliverability/warmup-plans/{planId}/usage``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/email-deliverability/warmup-plans/{planId}/usage",
            path_params={"planId": plan_id},
            query={"days": days},
            app_id=app_id,
            request_options=request_options,
        )

    def postmaster(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PostmasterStats":
        """Google Postmaster itibar kayıtları

        ``GET /v1/apps/{appId}/email-deliverability/postmaster``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/email-deliverability/postmaster",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def sync_postmaster(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PostmasterStats":
        """Google Postmaster dünkü itibarını oku

        ``POST /v1/apps/{appId}/email-deliverability/postmaster/sync``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/email-deliverability/postmaster/sync",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )


class FeatureFlagsResource:
    """featureFlags kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AppFlagList":
        """Özellik bayrakları

        ``GET /v1/apps/{appId}/feature-flags``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/feature-flags",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateAppFlagDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AppFlag":
        """Bayrak oluştur

        ``POST /v1/apps/{appId}/feature-flags``

        Değerler uygulama kimliğini bilen herkesçe okunabilir; gizli bilgi yazmayın.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/feature-flags",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def evaluate(
        self,
        body: "EvaluateAppFlagsDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AppFlagEvaluation":
        """Bayrakları bir kullanıcı için değerlendir

        ``POST /v1/apps/{appId}/feature-flags/evaluate``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/feature-flags/evaluate",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        flag_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AppFlag":
        """Bayrak ayrıntısı

        ``GET /v1/apps/{appId}/feature-flags/{flagId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/feature-flags/{flagId}",
            path_params={"flagId": flag_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        flag_id: str,
        body: "UpdateAppFlagDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "AppFlag":
        """Bayrağı güncelle

        ``PATCH /v1/apps/{appId}/feature-flags/{flagId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/feature-flags/{flagId}",
            path_params={"flagId": flag_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        flag_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Bayrağı sil

        ``DELETE /v1/apps/{appId}/feature-flags/{flagId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/feature-flags/{flagId}",
            path_params={"flagId": flag_id},
            app_id=app_id,
            request_options=request_options,
        )


class FormsResource:
    """forms kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "FormPage":
        """Formlar

        ``GET /v1/apps/{appId}/forms``

        Parametreler:
            status: Değerler: "active", "archived".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/forms",
            path_params={},
            query={"limit": limit, "cursor": cursor, "status": status},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Form"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                status=status,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "CreateFormDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Form":
        """Form oluştur

        ``POST /v1/apps/{appId}/forms``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/forms",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        form_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Form":
        """Form detayı

        ``GET /v1/apps/{appId}/forms/{formId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/forms/{formId}",
            path_params={"formId": form_id},
            app_id=app_id,
            request_options=request_options,
        )

    def submissions(
        self,
        form_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        since: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "FormSubmissionPage":
        """Form gönderimleri

        ``GET /v1/apps/{appId}/forms/{formId}/submissions``

        Parametreler:
            status: Değerler: "accepted", "pending_confirmation", "confirmed".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/forms/{formId}/submissions",
            path_params={"formId": form_id},
            query={"limit": limit, "cursor": cursor, "status": status, "since": since},
            app_id=app_id,
            request_options=request_options,
        )

    def submissions_all(
        self,
        form_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        since: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["FormSubmission"]:
        """``submissions`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.submissions(
                form_id,
                limit=limit,
                status=status,
                since=since,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def submit(
        self,
        form_id: str,
        body: "PublicFormSubmitDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "FormSubmitResult":
        """Sunucu tarafı form gönderimi (`external_id` verilirse o kullanıcının profili güncellenir)

        ``POST /v1/apps/{appId}/forms/{formId}/submissions``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/forms/{formId}/submissions",
            path_params={"formId": form_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class GeofencesResource:
    """geofences kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "GeofenceList":
        """Bölgeler

        ``GET /v1/apps/{appId}/geofences``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/geofences",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateGeofenceDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Geofence":
        """Bölge oluştur

        ``POST /v1/apps/{appId}/geofences``

        Konum paylaşan abonelik bölgeye girip çıktığında `geofence_enter` ve `geofence_exit` olayları oluşur.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/geofences",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        geofence_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Geofence":
        """Bölge ayrıntısı

        ``GET /v1/apps/{appId}/geofences/{geofenceId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/geofences/{geofenceId}",
            path_params={"geofenceId": geofence_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        geofence_id: str,
        body: "UpdateGeofenceDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Geofence":
        """Bölgeyi güncelle

        ``PATCH /v1/apps/{appId}/geofences/{geofenceId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/geofences/{geofenceId}",
            path_params={"geofenceId": geofence_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        geofence_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Bölgeyi sil

        ``DELETE /v1/apps/{appId}/geofences/{geofenceId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/geofences/{geofenceId}",
            path_params={"geofenceId": geofence_id},
            app_id=app_id,
            request_options=request_options,
        )


class GlobalControlResource:
    """globalControl kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def get(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "GlobalControl":
        """Genel kontrol grubu ayarı

        ``GET /v1/apps/{appId}/global-control``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/global-control",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        body: "UpdateGlobalControlDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "GlobalControl":
        """Genel kontrol grubunu ayarla

        ``PUT /v1/apps/{appId}/global-control``

        Gruptaki kullanıcılar kampanya, otomasyon ve uygulama içi mesajları almaz. API ve işlemsel gönderimler etkilenmez.
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/global-control",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def reset(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "GlobalControl":
        """Grubu yeniden kur (üyelik değişir, ölçüm baştan başlar)

        ``POST /v1/apps/{appId}/global-control/reset``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/global-control/reset",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def report(
        self,
        *,
        days: Optional[int] = None,
        event: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "GlobalControlReport":
        """Kontrol ve mesaj alan grubun dönüşüm karşılaştırması

        ``GET /v1/apps/{appId}/global-control/report``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/global-control/report",
            path_params={},
            query={"days": days, "event": event},
            app_id=app_id,
            request_options=request_options,
        )


class IdentityKeysResource:
    """identityKeys kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "IdentityKeyList":
        """SDK kimlik doğrulama (JWT) genel anahtarları

        ``GET /v1/apps/{appId}/identity-keys``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/identity-keys",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: "CreateIdentityKeyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "IdentityKey":
        """Genel anahtar ekle (ES256)

        ``POST /v1/apps/{appId}/identity-keys``

        SDK JWT identity verification için ES256 (EC P-256) genel anahtarı ekler; özel anahtar gönderilmez. Belirteç sunucunuzda imzalanır (`sub` = external_id, `aud` = app_id, `exp` ≤ 24 saat) ve SDK isteklerinde `Authorization: Bearer <jwt>` başlığıyla taşınır. Kip app ayarında `identity_verification_mode` ile seçilir.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/identity-keys",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def revoke(
        self,
        key_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "IdentityKey":
        """Genel anahtarı iptal et

        ``DELETE /v1/apps/{appId}/identity-keys/{keyId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/identity-keys/{keyId}",
            path_params={"keyId": key_id},
            app_id=app_id,
            request_options=request_options,
        )


class IntegrationsResource:
    """integrations kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def me(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ZapierMe":
        """Zapier bağlantı testi: anahtarın app’i ve kapsamları

        ``GET /v1/apps/{appId}/integrations/zapier/me``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/integrations/zapier/me",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def subscribe(
        self,
        body: "ZapierSubscribeDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ZapierHook":
        """REST Hook aboneliği (Zap açıldı)

        ``POST /v1/apps/{appId}/integrations/zapier/hooks``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/integrations/zapier/hooks",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def unsubscribe(
        self,
        hook_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "IntegrationOk":
        """REST Hook aboneliğini sil (Zap kapatıldı)

        ``DELETE /v1/apps/{appId}/integrations/zapier/hooks/{hookId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/integrations/zapier/hooks/{hookId}",
            path_params={"hookId": hook_id},
            app_id=app_id,
            request_options=request_options,
        )

    def samples(
        self,
        *,
        event: str,
        event_name: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> List["ZapierSamplesItem"]:
        """Tetik örnekleri (performList): son kayıtlar, abonelik gövdesiyle aynı biçim

        ``GET /v1/apps/{appId}/integrations/zapier/samples``

        Parametreler:
            event: Değerler: "subscription.created", "subscription.unsubscribed", "event.received", "delivery.delivered", "delivery.opened", "delivery.clicked", "user.created", "user.updated", "conversion.created", "campaign.completed".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/integrations/zapier/samples",
            path_params={},
            query={"event": event, "event_name": event_name},
            app_id=app_id,
            request_options=request_options,
        )


class JourneysResource:
    """journeys kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        q: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyPage":
        """Journey listesi

        ``GET /v1/apps/{appId}/journeys``

        Parametreler:
            status: Değerler: "draft", "active", "paused", "archived".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/journeys",
            path_params={},
            query={"limit": limit, "cursor": cursor, "status": status, "q": q},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        q: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Journey"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                status=status,
                q=q,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "JourneysCreateBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Journey oluştur (taslak)

        ``POST /v1/apps/{appId}/journeys``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/journeys",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        journey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Journey detayı

        ``GET /v1/apps/{appId}/journeys/{journeyId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/journeys/{journeyId}",
            path_params={"journeyId": journey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        journey_id: str,
        body: "UpdateJourneyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Ad / açıklama

        ``PATCH /v1/apps/{appId}/journeys/{journeyId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/journeys/{journeyId}",
            path_params={"journeyId": journey_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        journey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Hiç yayınlanmamış journey'i sil

        ``DELETE /v1/apps/{appId}/journeys/{journeyId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/journeys/{journeyId}",
            path_params={"journeyId": journey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def save_draft(
        self,
        journey_id: str,
        body: "JourneysSaveDraftBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Taslağı kaydet

        ``PUT /v1/apps/{appId}/journeys/{journeyId}/draft``
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/journeys/{journeyId}/draft",
            path_params={"journeyId": journey_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def update_node(
        self,
        journey_id: str,
        node_id: str,
        body: "UpdateNodeDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Taslaktaki düğümü güncelle

        ``PATCH /v1/apps/{appId}/journeys/{journeyId}/nodes/{nodeId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/journeys/{journeyId}/nodes/{nodeId}",
            path_params={"journeyId": journey_id, "nodeId": node_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def versions(
        self,
        journey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyVersionList":
        """Sürümler

        ``GET /v1/apps/{appId}/journeys/{journeyId}/versions``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/journeys/{journeyId}/versions",
            path_params={"journeyId": journey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def restore_version(
        self,
        journey_id: str,
        version: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Eski sürümü yeni taslak olarak geri yükle (yayındaki sürüm değişmez)

        ``POST /v1/apps/{appId}/journeys/{journeyId}/versions/{version}/restore``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/journeys/{journeyId}/versions/{version}/restore",
            path_params={"journeyId": journey_id, "version": version},
            app_id=app_id,
            request_options=request_options,
        )

    def publish(
        self,
        journey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyPublishResult":
        """Yayınla

        ``POST /v1/apps/{appId}/journeys/{journeyId}/publish``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/journeys/{journeyId}/publish",
            path_params={"journeyId": journey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def pause(
        self,
        journey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Duraklat

        ``POST /v1/apps/{appId}/journeys/{journeyId}/pause``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/journeys/{journeyId}/pause",
            path_params={"journeyId": journey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def resume(
        self,
        journey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Devam ettir

        ``POST /v1/apps/{appId}/journeys/{journeyId}/resume``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/journeys/{journeyId}/resume",
            path_params={"journeyId": journey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def archive(
        self,
        journey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Arşivle

        ``POST /v1/apps/{appId}/journeys/{journeyId}/archive``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/journeys/{journeyId}/archive",
            path_params={"journeyId": journey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def duplicate(
        self,
        journey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Kopyala

        ``POST /v1/apps/{appId}/journeys/{journeyId}/duplicate``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/journeys/{journeyId}/duplicate",
            path_params={"journeyId": journey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def stats(
        self,
        journey_id: str,
        *,
        version: Optional[int] = None,
        all_versions: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyStats":
        """Düğüm bazlı istatistik

        ``GET /v1/apps/{appId}/journeys/{journeyId}/stats``

        Parametreler:
            all_versions: Değerler: "true", "false".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/journeys/{journeyId}/stats",
            path_params={"journeyId": journey_id},
            query={"version": version, "all_versions": all_versions},
            app_id=app_id,
            request_options=request_options,
        )

    def runs(
        self,
        journey_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        user_id: Optional[str] = None,
        version: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyRunPage":
        """Run listesi

        ``GET /v1/apps/{appId}/journeys/{journeyId}/runs``

        Parametreler:
            status: Değerler: "active", "waiting", "completed", "exited", "failed".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/journeys/{journeyId}/runs",
            path_params={"journeyId": journey_id},
            query={"limit": limit, "cursor": cursor, "status": status, "user_id": user_id, "version": version},
            app_id=app_id,
            request_options=request_options,
        )

    def runs_all(
        self,
        journey_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        user_id: Optional[str] = None,
        version: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["JourneyRun"]:
        """``runs`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.runs(
                journey_id,
                limit=limit,
                status=status,
                user_id=user_id,
                version=version,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def trigger(
        self,
        journey_id: str,
        body: "TriggerRunDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyTriggerResult":
        """Kullanıcıyı journey'e sok (external_id, user_id veya alias; context Liquid custom_data)

        ``POST /v1/apps/{appId}/journeys/{journeyId}/runs``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/journeys/{journeyId}/runs",
            path_params={"journeyId": journey_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def run(
        self,
        journey_id: str,
        run_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyRunDetail":
        """Run detayı ve adımlar

        ``GET /v1/apps/{appId}/journeys/{journeyId}/runs/{runId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/journeys/{journeyId}/runs/{runId}",
            path_params={"journeyId": journey_id, "runId": run_id},
            app_id=app_id,
            request_options=request_options,
        )

    def exit_run(
        self,
        journey_id: str,
        run_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyRunDetail":
        """Run'ı sonlandır

        ``DELETE /v1/apps/{appId}/journeys/{journeyId}/runs/{runId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/journeys/{journeyId}/runs/{runId}",
            path_params={"journeyId": journey_id, "runId": run_id},
            app_id=app_id,
            request_options=request_options,
        )

    def list_for_user(
        self,
        label: str,
        value: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserJourneyRuns":
        """Kullanıcının journey run'ları

        ``GET /v1/apps/{appId}/users/by/{label}/{value}/journeys``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users/by/{label}/{value}/journeys",
            path_params={"label": label, "value": value},
            app_id=app_id,
            request_options=request_options,
        )


class LandingPagesResource:
    """landingPages kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LandingPageList":
        """Landing sayfaları

        ``GET /v1/apps/{appId}/landing-pages``

        Parametreler:
            status: Değerler: "draft", "published", "archived".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/landing-pages",
            path_params={},
            query={"limit": limit, "cursor": cursor, "status": status},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["LandingPageListDataItem"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                status=status,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def get(
        self,
        page_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LandingPage":
        """Landing sayfası detayı

        ``GET /v1/apps/{appId}/landing-pages/{pageId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/landing-pages/{pageId}",
            path_params={"pageId": page_id},
            app_id=app_id,
            request_options=request_options,
        )

    def publish(
        self,
        page_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LandingPage":
        """Taslağı yayınla

        ``POST /v1/apps/{appId}/landing-pages/{pageId}/publish``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/landing-pages/{pageId}/publish",
            path_params={"pageId": page_id},
            app_id=app_id,
            request_options=request_options,
        )

    def unpublish(
        self,
        page_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LandingPage":
        """Yayından kaldır

        ``POST /v1/apps/{appId}/landing-pages/{pageId}/unpublish``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/landing-pages/{pageId}/unpublish",
            path_params={"pageId": page_id},
            app_id=app_id,
            request_options=request_options,
        )


class LiveActivitiesResource:
    """liveActivities kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list_types(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LiveActivityTypeList":
        """Live Activity türleri

        ``GET /v1/apps/{appId}/live-activities/types``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/live-activities/types",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create_type(
        self,
        body: "CreateLiveActivityTypeDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LiveActivityType":
        """Live Activity türü oluştur

        ``POST /v1/apps/{appId}/live-activities/types``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/live-activities/types",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def update_type(
        self,
        activity_type: str,
        body: "UpdateLiveActivityTypeDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LiveActivityType":
        """Live Activity türünü güncelle

        ``PATCH /v1/apps/{appId}/live-activities/types/{activityType}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/live-activities/types/{activityType}",
            path_params={"activityType": activity_type},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete_type(
        self,
        activity_type: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LiveActivityTokenResult":
        """Live Activity türünü sil

        ``DELETE /v1/apps/{appId}/live-activities/types/{activityType}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/live-activities/types/{activityType}",
            path_params={"activityType": activity_type},
            app_id=app_id,
            request_options=request_options,
        )

    def start(
        self,
        activity_type: str,
        body: "StartLiveActivityDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LiveActivitySendResult":
        """Live Activity başlat (push-to-start)

        ``POST /v1/apps/{appId}/live-activities/{activityType}/start``

        Hedefteki iOS aboneliklerinin push-to-start belirteçleriyle etkinliği uzaktan başlatır (iOS 17.2+). `attributes` ve `content_state` türün şemasına uymalıdır. Dönen `activity_id` ile sonraki update/end yapılır.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/live-activities/{activityType}/start",
            path_params={"activityType": activity_type},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        activity_type: str,
        body: "UpdateLiveActivityDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LiveActivitySendResult":
        """Live Activity güncelle

        ``POST /v1/apps/{appId}/live-activities/{activityType}/update``

        Etkinliğin cihazlardan bildirilen güncelleme belirteçlerine yeni içerik durumu gönderir. Sessiz saat ve frekans sınırı uygulanmaz; priority 5 Apple bütçesini korur.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/live-activities/{activityType}/update",
            path_params={"activityType": activity_type},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def end(
        self,
        activity_type: str,
        body: "EndLiveActivityDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "LiveActivitySendResult":
        """Live Activity bitir

        ``POST /v1/apps/{appId}/live-activities/{activityType}/end``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/live-activities/{activityType}/end",
            path_params={"activityType": activity_type},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class McpResource:
    """mcp kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def create_campaign_draft(
        self,
        body: "McpCreateCampaignDraftBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Kampanya taslağı oluştur (MCP onaylı mod; gönderim yapmaz)

        ``POST /v1/apps/{appId}/mcp/campaign-drafts``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/mcp/campaign-drafts",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def create_segment_draft(
        self,
        body: "McpCreateSegmentDraftBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Segment":
        """Segment taslağı oluştur (MCP onaylı mod; dinamik segment)

        ``POST /v1/apps/{appId}/mcp/segment-drafts``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/mcp/segment-drafts",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def create_template_draft(
        self,
        body: "CreateTemplateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Template":
        """Şablon oluştur (MCP onaylı mod; şablon tek başına gönderim yapmaz)

        ``POST /v1/apps/{appId}/mcp/template-drafts``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/mcp/template-drafts",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def create_journey_draft(
        self,
        body: "McpCreateJourneyDraftBody",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "JourneyDetail":
        """Journey taslağı oluştur (MCP onaylı mod; yayımlanmaz)

        ``POST /v1/apps/{appId}/mcp/journey-drafts``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/mcp/journey-drafts",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def create_in_app_draft(
        self,
        body: "CreateInAppDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InAppMessage":
        """In-app mesaj taslağı oluştur (MCP onaylı mod; etkinleştirilmez)

        ``POST /v1/apps/{appId}/mcp/in-app-drafts``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/mcp/in-app-drafts",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def test_send(
        self,
        body: "TestPushDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CreateNotificationResult":
        """Test gönderimi (yalnızca app’in test cihazlarına; MCP onaylı mod)

        ``POST /v1/apps/{appId}/mcp/test-sends``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/mcp/test-sends",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class PreferencesResource:
    """preferences kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def get(
        self,
        label: str,
        value: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserPreferences":
        """Kullanıcının tercihleri (alias ile)

        ``GET /v1/apps/{appId}/users/by/{label}/{value}/preferences``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users/by/{label}/{value}/preferences",
            path_params={"label": label, "value": value},
            app_id=app_id,
            request_options=request_options,
        )

    def set(
        self,
        label: str,
        value: str,
        body: "SetPreferencesDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserPreferences":
        """Kullanıcı tercihlerini yaz (alias ile)

        ``PUT /v1/apps/{appId}/users/by/{label}/{value}/preferences``
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/users/by/{label}/{value}/preferences",
            path_params={"label": label, "value": value},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class PromoCodeListsResource:
    """promoCodeLists kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list_promo_lists(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PromoCodeListList":
        """Promosyon kodu listeleri

        ``GET /v1/apps/{appId}/promo-code-lists``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/promo-code-lists",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create_promo_list(
        self,
        body: "CreatePromoCodeListDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PromoCodeList":
        """Promosyon kodu listesi oluştur

        ``POST /v1/apps/{appId}/promo-code-lists``

        Şablonda `{% promo_code '<ad>' %}` teslimat başına tek kullanımlık kod verir. Kod kalmazsa teslimat `PromoCodeUnavailable` hatasıyla düşer.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/promo-code-lists",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get_promo_list(
        self,
        list_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PromoCodeList":
        """Promosyon kodu listesi ayrıntısı

        ``GET /v1/apps/{appId}/promo-code-lists/{listId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/promo-code-lists/{listId}",
            path_params={"listId": list_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update_promo_list(
        self,
        list_id: str,
        body: "UpdatePromoCodeListDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PromoCodeList":
        """Promosyon kodu listesini güncelle (açıklama, son kullanma)

        ``PATCH /v1/apps/{appId}/promo-code-lists/{listId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/promo-code-lists/{listId}",
            path_params={"listId": list_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete_promo_list(
        self,
        list_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Promosyon kodu listesini sil

        ``DELETE /v1/apps/{appId}/promo-code-lists/{listId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/promo-code-lists/{listId}",
            path_params={"listId": list_id},
            app_id=app_id,
            request_options=request_options,
        )

    def upload_promo_list(
        self,
        list_id: str,
        file: FileInput,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PromoCodeUploadResult":
        """CSV ile kod ekle (zaten olanlar atlanır)

        ``POST /v1/apps/{appId}/promo-code-lists/{listId}/codes``

        Parametreler:
            file: UTF-8 CSV; kodlar ilk sütunda, başlık isteğe bağlı. En fazla 1.000.000 kod, 20 MB.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/promo-code-lists/{listId}/codes",
            path_params={"listId": list_id},
            form={},
            files={"file": file},
            app_id=app_id,
            request_options=request_options,
        )

    def promo_codes(
        self,
        list_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        q: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "PromoCodesPage":
        """Listedeki kodlar ve atamaları

        ``GET /v1/apps/{appId}/promo-code-lists/{listId}/codes``

        Parametreler:
            status: Değerler: "available", "assigned".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/promo-code-lists/{listId}/codes",
            path_params={"listId": list_id},
            query={"limit": limit, "offset": offset, "q": q, "status": status},
            app_id=app_id,
            request_options=request_options,
        )


class ReverseEtlResource:
    """reverseEtl kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ReverseEtlSyncList":
        """Depodan içeri aktarımlar

        ``GET /v1/apps/{appId}/reverse-etl``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/reverse-etl",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: Any,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ReverseEtlSync":
        """İçeri aktarım oluştur

        ``POST /v1/apps/{appId}/reverse-etl``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/reverse-etl",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def test(
        self,
        body: Any,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseConnectionResult":
        """Kaydetmeden bağlantı testi

        ``POST /v1/apps/{appId}/reverse-etl/test-connection``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/reverse-etl/test-connection",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        sync_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ReverseEtlSync":
        """İçeri aktarım detayı

        ``GET /v1/apps/{appId}/reverse-etl/{syncId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/reverse-etl/{syncId}",
            path_params={"syncId": sync_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        sync_id: str,
        body: "UpdateReverseEtlDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ReverseEtlSync":
        """İçeri aktarımı güncelle

        ``PATCH /v1/apps/{appId}/reverse-etl/{syncId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/reverse-etl/{syncId}",
            path_params={"syncId": sync_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        sync_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """İçeri aktarımı sil

        ``DELETE /v1/apps/{appId}/reverse-etl/{syncId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/reverse-etl/{syncId}",
            path_params={"syncId": sync_id},
            app_id=app_id,
            request_options=request_options,
        )

    def test_saved(
        self,
        sync_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseConnectionResult":
        """Kayıtlı içeri aktarımın bağlantı testi

        ``POST /v1/apps/{appId}/reverse-etl/{syncId}/test``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/reverse-etl/{syncId}/test",
            path_params={"syncId": sync_id},
            app_id=app_id,
            request_options=request_options,
        )

    def run(
        self,
        sync_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ReverseEtlRun":
        """Şimdi içeri aktar

        ``POST /v1/apps/{appId}/reverse-etl/{syncId}/run``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/reverse-etl/{syncId}/run",
            path_params={"syncId": sync_id},
            app_id=app_id,
            request_options=request_options,
        )

    def runs(
        self,
        sync_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "ReverseEtlRunPage":
        """İçeri aktarım geçmişi

        ``GET /v1/apps/{appId}/reverse-etl/{syncId}/runs``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/reverse-etl/{syncId}/runs",
            path_params={"syncId": sync_id},
            query={"limit": limit, "cursor": cursor},
            app_id=app_id,
            request_options=request_options,
        )

    def runs_all(
        self,
        sync_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["ReverseEtlRun"]:
        """``runs`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.runs(
                sync_id,
                limit=limit,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )


class RfmResource:
    """rfm kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def config(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RfmConfig":
        """RFM modeli

        ``GET /v1/apps/{appId}/rfm/config``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/rfm/config",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        body: "UpdateRfmConfigDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RfmConfig":
        """RFM modelini ayarla

        ``PUT /v1/apps/{appId}/rfm/config``

        Model açıksa skorlar kayıttan sonra yeniden hesaplanır.
        """
        return self._client._call(
            "PUT",
            "/v1/apps/{appId}/rfm/config",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def compute(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RfmConfig":
        """Skorları yeniden hesapla

        ``POST /v1/apps/{appId}/rfm/compute``

        İş kuyruğa alınır; ilerleme `status` alanından izlenir.
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/rfm/compute",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def overview(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RfmOverview":
        """Segment dağılımı

        ``GET /v1/apps/{appId}/rfm/overview``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/rfm/overview",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def transitions(
        self,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RfmTransitions":
        """İki tarih arası segment geçişleri

        ``GET /v1/apps/{appId}/rfm/transitions``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/rfm/transitions",
            path_params={},
            query={"from": from_, "to": to},
            app_id=app_id,
            request_options=request_options,
        )

    def users(
        self,
        *,
        segment: Optional[str] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RfmUsersPage":
        """Skoru olan kullanıcılar

        ``GET /v1/apps/{appId}/rfm/users``

        Parametreler:
            segment: Değerler: "champions", "loyal", "potential", "new", "promising", "need_attention", "about_to_sleep", "at_risk", "cant_lose", "hibernating", "lost".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/rfm/users",
            path_params={},
            query={"segment": segment, "limit": limit, "cursor": cursor},
            app_id=app_id,
            request_options=request_options,
        )


class SmsKeywordsResource:
    """smsKeywords kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def keywords(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SmsKeywordList":
        """İki yönlü mesaj anahtar sözcükleri (org geneli + bu app) ve yasal (ayrılmış) sözcükler

        ``GET /v1/apps/{appId}/sms-keywords``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/sms-keywords",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create_keyword(
        self,
        body: "CreateKeywordDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SmsKeyword":
        """Anahtar sözcük oluştur (tag ekle/kaldır, olay → journey tetiği, otomatik yanıt, abonelik)

        ``POST /v1/apps/{appId}/sms-keywords``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/sms-keywords",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def update_keyword(
        self,
        keyword_id: str,
        body: "UpdateKeywordDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SmsKeyword":
        """Anahtar sözcüğü güncelle

        ``PATCH /v1/apps/{appId}/sms-keywords/{keywordId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/sms-keywords/{keywordId}",
            path_params={"keywordId": keyword_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete_keyword(
        self,
        keyword_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Anahtar sözcüğü sil

        ``DELETE /v1/apps/{appId}/sms-keywords/{keywordId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/sms-keywords/{keywordId}",
            path_params={"keywordId": keyword_id},
            app_id=app_id,
            request_options=request_options,
        )


class SurveysResource:
    """surveys kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SurveyPage":
        """Anketler

        ``GET /v1/apps/{appId}/surveys``

        Parametreler:
            status: Değerler: "draft", "active", "closed".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/surveys",
            path_params={},
            query={"limit": limit, "cursor": cursor, "status": status},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["Survey"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                status=status,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "CreateSurveyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Survey":
        """Anket oluştur (taslak)

        ``POST /v1/apps/{appId}/surveys``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/surveys",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        survey_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Survey":
        """Anket detayı

        ``GET /v1/apps/{appId}/surveys/{surveyId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/surveys/{surveyId}",
            path_params={"surveyId": survey_id},
            app_id=app_id,
            request_options=request_options,
        )

    def status(
        self,
        survey_id: str,
        body: "SurveyStatusDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Survey":
        """Etkinleştir / kapat

        ``POST /v1/apps/{appId}/surveys/{surveyId}/status``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/surveys/{surveyId}/status",
            path_params={"surveyId": survey_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def report(
        self,
        survey_id: str,
        *,
        days: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SurveyReport":
        """NPS / CSAT raporu

        ``GET /v1/apps/{appId}/surveys/{surveyId}/report``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/surveys/{surveyId}/report",
            path_params={"surveyId": survey_id},
            query={"days": days},
            app_id=app_id,
            request_options=request_options,
        )

    def responses(
        self,
        survey_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        text_question: Optional[str] = None,
        nps_category: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SurveyResponsePage":
        """Anket yanıtları

        ``GET /v1/apps/{appId}/surveys/{surveyId}/responses``

        Parametreler:
            nps_category: Değerler: "promoter", "passive", "detractor".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/surveys/{surveyId}/responses",
            path_params={"surveyId": survey_id},
            query={"limit": limit, "cursor": cursor, "text_question": text_question, "nps_category": nps_category},
            app_id=app_id,
            request_options=request_options,
        )

    def responses_all(
        self,
        survey_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        text_question: Optional[str] = None,
        nps_category: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["SurveyResponse"]:
        """``responses`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.responses(
                survey_id,
                limit=limit,
                text_question=text_question,
                nps_category=nps_category,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def respond(
        self,
        survey_id: str,
        body: "PublicSurveyResponseDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SurveyResponseResult":
        """Sunucu tarafı anket yanıtı (`external_id` ile kullanıcıya bağlanır)

        ``POST /v1/apps/{appId}/surveys/{surveyId}/responses``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/surveys/{surveyId}/responses",
            path_params={"surveyId": survey_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class VerifyResource:
    """verify kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def start(
        self,
        body: "StartVerifyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SmsVerification":
        """SMS doğrulama kodu gönder

        ``POST /v1/apps/{appId}/verify/sms``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/verify/sms",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def check(
        self,
        body: "CheckVerifyDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SmsVerificationCheck":
        """SMS doğrulama kodunu kontrol et

        ``POST /v1/apps/{appId}/verify/sms/check``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/verify/sms/check",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class WarehouseExportsResource:
    """warehouseExports kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def tables(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseTables":
        """Dışa aktarılabilir tablolar, kolonlar ve şema sürümleri

        ``GET /v1/apps/{appId}/warehouse-exports/tables``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/warehouse-exports/tables",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def test(
        self,
        body: Any,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseConnectionResult":
        """Kaydetmeden bağlantı testi

        ``POST /v1/apps/{appId}/warehouse-exports/test-connection``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/warehouse-exports/test-connection",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def list(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseExportList":
        """Veri ambarı dışa aktarımları

        ``GET /v1/apps/{appId}/warehouse-exports``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/warehouse-exports",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )

    def create(
        self,
        body: Any,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseExport":
        """Dışa aktarım oluştur (kimlik bilgisi şifreli saklanır, yanıtta dönmez)

        ``POST /v1/apps/{appId}/warehouse-exports``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/warehouse-exports",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        export_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseExport":
        """Dışa aktarım detayı

        ``GET /v1/apps/{appId}/warehouse-exports/{exportId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/warehouse-exports/{exportId}",
            path_params={"exportId": export_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        export_id: str,
        body: "UpdateWarehouseExportDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseExport":
        """Dışa aktarımı güncelle (ad, tablolar, zamanlama, etkin/duraklat, hedef ayarı, kimlik bilgisi)

        ``PATCH /v1/apps/{appId}/warehouse-exports/{exportId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/warehouse-exports/{exportId}",
            path_params={"exportId": export_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def delete(
        self,
        export_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Dışa aktarımı sil (hedefteki veriler silinmez)

        ``DELETE /v1/apps/{appId}/warehouse-exports/{exportId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/warehouse-exports/{exportId}",
            path_params={"exportId": export_id},
            app_id=app_id,
            request_options=request_options,
        )

    def test_saved(
        self,
        export_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseConnectionResult":
        """Kayıtlı dışa aktarımın bağlantı testi

        ``POST /v1/apps/{appId}/warehouse-exports/{exportId}/test``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/warehouse-exports/{exportId}/test",
            path_params={"exportId": export_id},
            app_id=app_id,
            request_options=request_options,
        )

    def run(
        self,
        export_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseExportRun":
        """Şimdi çalıştır (son başarılı imleçten itibaren)

        ``POST /v1/apps/{appId}/warehouse-exports/{exportId}/run``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/warehouse-exports/{exportId}/run",
            path_params={"exportId": export_id},
            app_id=app_id,
            request_options=request_options,
        )

    def runs(
        self,
        export_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WarehouseExportRunPage":
        """Çalıştırma geçmişi (cursor)

        ``GET /v1/apps/{appId}/warehouse-exports/{exportId}/runs``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/warehouse-exports/{exportId}/runs",
            path_params={"exportId": export_id},
            query={"limit": limit, "cursor": cursor},
            app_id=app_id,
            request_options=request_options,
        )

    def runs_all(
        self,
        export_id: str,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["WarehouseExportRun"]:
        """``runs`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.runs(
                export_id,
                limit=limit,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )


class WebCampaignsResource:
    """webCampaigns kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def list(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebCampaignPage":
        """Web kampanyaları

        ``GET /v1/apps/{appId}/web-campaigns``

        Parametreler:
            status: Değerler: "draft", "active", "paused", "archived".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/web-campaigns",
            path_params={},
            query={"limit": limit, "cursor": cursor, "status": status},
            app_id=app_id,
            request_options=request_options,
        )

    def list_all(
        self,
        *,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Iterator["WebCampaign"]:
        """``list`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list(
                limit=limit,
                status=status,
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def create(
        self,
        body: "CreateWebCampaignDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebCampaign":
        """Web kampanyası oluştur (taslak)

        ``POST /v1/apps/{appId}/web-campaigns``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/web-campaigns",
            path_params={},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def get(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebCampaign":
        """Web kampanyası detayı ve istatistikleri

        ``GET /v1/apps/{appId}/web-campaigns/{campaignId}``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/web-campaigns/{campaignId}",
            path_params={"campaignId": campaign_id},
            app_id=app_id,
            request_options=request_options,
        )

    def update(
        self,
        campaign_id: str,
        body: "UpdateWebCampaignDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebCampaign":
        """Web kampanyasını düzenle

        ``PATCH /v1/apps/{appId}/web-campaigns/{campaignId}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/web-campaigns/{campaignId}",
            path_params={"campaignId": campaign_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def report(
        self,
        campaign_id: str,
        *,
        days: Optional[int] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebCampaignReport":
        """Günlük seri

        ``GET /v1/apps/{appId}/web-campaigns/{campaignId}/report``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/web-campaigns/{campaignId}/report",
            path_params={"campaignId": campaign_id},
            query={"days": days},
            app_id=app_id,
            request_options=request_options,
        )

    def status(
        self,
        campaign_id: str,
        body: "WebCampaignStatusDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WebCampaign":
        """Yayınla / duraklat / arşivle

        ``POST /v1/apps/{appId}/web-campaigns/{campaignId}/status``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/web-campaigns/{campaignId}/status",
            path_params={"campaignId": campaign_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )


class WhatsappResource:
    """whatsapp kaynağı."""

    def __init__(self, client: "Pushizo") -> None:
        self._client = client

    def templates(
        self,
        *,
        status: Optional[str] = None,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WhatsAppTemplateList":
        """WhatsApp şablonları (Meta onay durumu ile)

        ``GET /v1/apps/{appId}/whatsapp/templates``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/whatsapp/templates",
            path_params={},
            query={"status": status},
            app_id=app_id,
            request_options=request_options,
        )

    def sync(
        self,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "WhatsAppTemplateSync":
        """WhatsApp şablonlarını Meta Graph API’den senkronla

        ``POST /v1/apps/{appId}/whatsapp/templates/sync``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/whatsapp/templates/sync",
            path_params={},
            app_id=app_id,
            request_options=request_options,
        )


class GeneratedResources:
    """İstemciye kaynak alanlarını ekleyen üretilmiş karışım (mixin) sınıfı."""

    notifications: NotificationsResource
    users: UsersResource
    aliases: AliasesResource
    subscriptions: SubscriptionsResource
    events: EventsResource
    segments: SegmentsResource
    templates: TemplatesResource
    campaigns: CampaignsResource
    in_app_messages: InAppMessagesResource
    inbox: InboxResource
    suppressions: SuppressionsResource
    exports: ExportsResource
    imports: ImportsResource
    webhooks: WebhooksResource
    channels: ChannelsResource
    analytics: AnalyticsResource
    apps: AppsResource
    api_keys: ApiKeysResource
    organization: OrganizationResource
    ads: AdsResource
    canned_responses: CannedResponsesResource
    catalogs: CatalogsResource
    categories: CategoriesResource
    channel_scores: ChannelScoresResource
    content_tables: ContentTablesResource
    conversations: ConversationsResource
    data_feeds: DataFeedsResource
    email_deliverability: EmailDeliverabilityResource
    feature_flags: FeatureFlagsResource
    forms: FormsResource
    geofences: GeofencesResource
    global_control: GlobalControlResource
    identity_keys: IdentityKeysResource
    integrations: IntegrationsResource
    journeys: JourneysResource
    landing_pages: LandingPagesResource
    live_activities: LiveActivitiesResource
    mcp: McpResource
    preferences: PreferencesResource
    promo_code_lists: PromoCodeListsResource
    reverse_etl: ReverseEtlResource
    rfm: RfmResource
    sms_keywords: SmsKeywordsResource
    surveys: SurveysResource
    verify: VerifyResource
    warehouse_exports: WarehouseExportsResource
    web_campaigns: WebCampaignsResource
    whatsapp: WhatsappResource

    def _init_resources(self) -> None:
        self.notifications = NotificationsResource(self)  # type: ignore[arg-type]
        self.users = UsersResource(self)  # type: ignore[arg-type]
        self.aliases = AliasesResource(self)  # type: ignore[arg-type]
        self.subscriptions = SubscriptionsResource(self)  # type: ignore[arg-type]
        self.events = EventsResource(self)  # type: ignore[arg-type]
        self.segments = SegmentsResource(self)  # type: ignore[arg-type]
        self.templates = TemplatesResource(self)  # type: ignore[arg-type]
        self.campaigns = CampaignsResource(self)  # type: ignore[arg-type]
        self.in_app_messages = InAppMessagesResource(self)  # type: ignore[arg-type]
        self.inbox = InboxResource(self)  # type: ignore[arg-type]
        self.suppressions = SuppressionsResource(self)  # type: ignore[arg-type]
        self.exports = ExportsResource(self)  # type: ignore[arg-type]
        self.imports = ImportsResource(self)  # type: ignore[arg-type]
        self.webhooks = WebhooksResource(self)  # type: ignore[arg-type]
        self.channels = ChannelsResource(self)  # type: ignore[arg-type]
        self.analytics = AnalyticsResource(self)  # type: ignore[arg-type]
        self.apps = AppsResource(self)  # type: ignore[arg-type]
        self.api_keys = ApiKeysResource(self)  # type: ignore[arg-type]
        self.organization = OrganizationResource(self)  # type: ignore[arg-type]
        self.ads = AdsResource(self)  # type: ignore[arg-type]
        self.canned_responses = CannedResponsesResource(self)  # type: ignore[arg-type]
        self.catalogs = CatalogsResource(self)  # type: ignore[arg-type]
        self.categories = CategoriesResource(self)  # type: ignore[arg-type]
        self.channel_scores = ChannelScoresResource(self)  # type: ignore[arg-type]
        self.content_tables = ContentTablesResource(self)  # type: ignore[arg-type]
        self.conversations = ConversationsResource(self)  # type: ignore[arg-type]
        self.data_feeds = DataFeedsResource(self)  # type: ignore[arg-type]
        self.email_deliverability = EmailDeliverabilityResource(self)  # type: ignore[arg-type]
        self.feature_flags = FeatureFlagsResource(self)  # type: ignore[arg-type]
        self.forms = FormsResource(self)  # type: ignore[arg-type]
        self.geofences = GeofencesResource(self)  # type: ignore[arg-type]
        self.global_control = GlobalControlResource(self)  # type: ignore[arg-type]
        self.identity_keys = IdentityKeysResource(self)  # type: ignore[arg-type]
        self.integrations = IntegrationsResource(self)  # type: ignore[arg-type]
        self.journeys = JourneysResource(self)  # type: ignore[arg-type]
        self.landing_pages = LandingPagesResource(self)  # type: ignore[arg-type]
        self.live_activities = LiveActivitiesResource(self)  # type: ignore[arg-type]
        self.mcp = McpResource(self)  # type: ignore[arg-type]
        self.preferences = PreferencesResource(self)  # type: ignore[arg-type]
        self.promo_code_lists = PromoCodeListsResource(self)  # type: ignore[arg-type]
        self.reverse_etl = ReverseEtlResource(self)  # type: ignore[arg-type]
        self.rfm = RfmResource(self)  # type: ignore[arg-type]
        self.sms_keywords = SmsKeywordsResource(self)  # type: ignore[arg-type]
        self.surveys = SurveysResource(self)  # type: ignore[arg-type]
        self.verify = VerifyResource(self)  # type: ignore[arg-type]
        self.warehouse_exports = WarehouseExportsResource(self)  # type: ignore[arg-type]
        self.web_campaigns = WebCampaignsResource(self)  # type: ignore[arg-type]
        self.whatsapp = WhatsappResource(self)  # type: ignore[arg-type]


RESOURCE_NAMES = (
    "notifications",
    "users",
    "aliases",
    "subscriptions",
    "events",
    "segments",
    "templates",
    "campaigns",
    "in_app_messages",
    "inbox",
    "suppressions",
    "exports",
    "imports",
    "webhooks",
    "channels",
    "analytics",
    "apps",
    "api_keys",
    "organization",
    "ads",
    "canned_responses",
    "catalogs",
    "categories",
    "channel_scores",
    "content_tables",
    "conversations",
    "data_feeds",
    "email_deliverability",
    "feature_flags",
    "forms",
    "geofences",
    "global_control",
    "identity_keys",
    "integrations",
    "journeys",
    "landing_pages",
    "live_activities",
    "mcp",
    "preferences",
    "promo_code_lists",
    "reverse_etl",
    "rfm",
    "sms_keywords",
    "surveys",
    "verify",
    "warehouse_exports",
    "web_campaigns",
    "whatsapp",
)
