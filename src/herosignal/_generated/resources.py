# Bu dosya api/openapi.yaml'dan sdk/scripts/generate-server-sdks.mjs ile üretilmiştir; elle düzenlemeyin.
"""API kaynakları; her metot bir OpenAPI işlemine karşılık gelir."""

from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Optional

from .._types import FileInput, RequestOptions
from .models import *  # noqa: F401,F403

if TYPE_CHECKING:  # pragma: no cover
    from .._client import HeroSignal


class NotificationsResource:
    """Bildirim gönderme, durum, iptal, teslimatlar ve geçmiş dışa aktarımı."""

    def __init__(self, client: "HeroSignal") -> None:
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
            query={"limit": limit, "cursor": cursor, "source": source, "kind": kind, "status": status, "sort": sort},
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
                app_id=app_id,
                request_options=request_options,
                cursor=next_cursor,
            ),
            cursor,
        )

    def estimate(
        self,
        body: "EstimateRecipientsDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "RecipientEstimate":
        """Kaydedilmemiş hedef için alıcı sayımı (kanal kırılımıyla; gönderim yapmaz)

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
        request_options: Optional[RequestOptions] = None,
    ) -> "Export":
        """Bildirim geçmişi CSV işi (teslimatlar; tamamlanınca download_url)

        ``GET /v1/notifications/{messageId}/history``
        """
        return self._client._call(
            "GET",
            "/v1/notifications/{messageId}/history",
            path_params={"messageId": message_id},
            request_options=request_options,
        )

    def export_events(
        self,
        message_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> "Export":
        """Mesaj olayları CSV işi (teslim, açılma, tıklama, bounce…; tamamlanınca download_url)

        ``POST /v1/notifications/{messageId}/export-events``
        """
        return self._client._call(
            "POST",
            "/v1/notifications/{messageId}/export-events",
            path_params={"messageId": message_id},
            request_options=request_options,
        )


class UsersResource:
    """Kullanıcı oluşturma/güncelleme (tag, özellik), arama ve abonelik ekleme."""

    def __init__(self, client: "HeroSignal") -> None:
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
        """Kullanıcının tüm kimlikleri (hs_id, external_id, alias'lar)

        ``GET /v1/apps/{appId}/users/by/{label}/{value}/identity``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users/by/{label}/{value}/identity",
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

    def export_user(
        self,
        label: str,
        value: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "UserExport":
        """Kullanıcı verisini dışa aktar (KVKK/GDPR veri taşınabilirliği): profil, alias, abonelik, son olaylar

        ``GET /v1/apps/{appId}/users/by/{label}/{value}/export``
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/users/by/{label}/{value}/export",
            path_params={"label": label, "value": value},
            app_id=app_id,
            request_options=request_options,
        )

    def list_inbox(
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
        """Kullanıcının bildirim kutusu

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

    def list_inbox_all(
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
        """``list_inbox`` sonuçlarını ``next_cursor`` ile tüm sayfalar boyunca tek tek döndürür."""
        return self._client._paginate(
            lambda next_cursor: self.list_inbox(
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

    def read_inbox_item(
        self,
        label: str,
        value: str,
        item_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "InboxItem":
        """Bildirim kutusu öğesini okundu işaretle

        ``POST /v1/apps/{appId}/users/by/{label}/{value}/inbox/{itemId}/read``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/users/by/{label}/{value}/inbox/{itemId}/read",
            path_params={"label": label, "value": value, "itemId": item_id},
            app_id=app_id,
            request_options=request_options,
        )

    def archive_inbox_item(
        self,
        label: str,
        value: str,
        item_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Ok":
        """Bildirim kutusu öğesini kaldır (arşivle)

        ``DELETE /v1/apps/{appId}/users/by/{label}/{value}/inbox/{itemId}``
        """
        return self._client._call(
            "DELETE",
            "/v1/apps/{appId}/users/by/{label}/{value}/inbox/{itemId}",
            path_params={"label": label, "value": value, "itemId": item_id},
            app_id=app_id,
            request_options=request_options,
        )


class AliasesResource:
    """Kullanıcı kimlikleri (alias): ekleme ve kaldırma."""

    def __init__(self, client: "HeroSignal") -> None:
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

    def __init__(self, client: "HeroSignal") -> None:
        self._client = client

    def subscription_identity(
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

    def patch_subscription_by_token(
        self,
        channel: str,
        token: str,
        body: "PatchSubscriptionDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Subscription":
        """Aboneliği kanal + token ile güncelle (APNs/FCM token, e-posta, E.164 telefon)

        ``PATCH /v1/apps/{appId}/subscriptions/by-token/{channel}/{token}``
        """
        return self._client._call(
            "PATCH",
            "/v1/apps/{appId}/subscriptions/by-token/{channel}/{token}",
            path_params={"channel": channel, "token": token},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

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

    def __init__(self, client: "HeroSignal") -> None:
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
            app_id=app_id,
            request_options=request_options,
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

    def __init__(self, client: "HeroSignal") -> None:
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
        force: str,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "SegmentEstimate":
        """Tahmini sayım

        ``POST /v1/apps/{appId}/segments/{segmentId}/estimate``
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

    def __init__(self, client: "HeroSignal") -> None:
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
            channel: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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

    def copy(
        self,
        template_id: str,
        body: "CopyTemplateDto",
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Template":
        """Şablonu aynı organizasyondaki başka bir app'e kopyala (org anahtarı gerekir)

        ``POST /v1/apps/{appId}/templates/{templateId}/copy``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/templates/{templateId}/copy",
            path_params={"templateId": template_id},
            body=body,
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

    def __init__(self, client: "HeroSignal") -> None:
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
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "CampaignPage":
        """Kampanya listesi

        ``GET /v1/apps/{appId}/campaigns``

        Parametreler:
            status: Değerler: "draft", "scheduled", "running", "paused", "completed", "cancelled", "failed".
            type: Değerler: "one_time", "scheduled", "recurring", "automated", "transactional".
            channel: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
        """
        return self._client._call(
            "GET",
            "/v1/apps/{appId}/campaigns",
            path_params={},
            query={"limit": limit, "cursor": cursor, "q": q, "status": status, "type": type, "channel": channel},
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
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Zamanla

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/schedule``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/schedule",
            path_params={"campaignId": campaign_id},
            body=body,
            app_id=app_id,
            request_options=request_options,
        )

    def send(
        self,
        campaign_id: str,
        *,
        app_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> "Campaign":
        """Hemen gönder

        ``POST /v1/apps/{appId}/campaigns/{campaignId}/send``
        """
        return self._client._call(
            "POST",
            "/v1/apps/{appId}/campaigns/{campaignId}/send",
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


class SuppressionsResource:
    """E-posta/SMS gönderim engeli (suppression) listesi."""

    def __init__(self, client: "HeroSignal") -> None:
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
            channel: Değerler: "email", "sms".
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

    def __init__(self, client: "HeroSignal") -> None:
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

    def __init__(self, client: "HeroSignal") -> None:
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
            type: Değerler: "eski sağlayıcı_players", "csv_users".
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

    def __init__(self, client: "HeroSignal") -> None:
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

    def __init__(self, client: "HeroSignal") -> None:
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

    def __init__(self, client: "HeroSignal") -> None:
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

    def __init__(self, client: "HeroSignal") -> None:
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


class OrganizationResource:
    """Organizasyon, üyeler ve denetim kayıtları."""

    def __init__(self, client: "HeroSignal") -> None:
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


class ApiKeysResource:
    """apiKeys kaynağı."""

    def __init__(self, client: "HeroSignal") -> None:
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


class InAppMessagesResource:
    """inAppMessages kaynağı."""

    def __init__(self, client: "HeroSignal") -> None:
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
        """In-app mesaj detayı

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
        """In-app mesajı sil (gösterim kayıtlarıyla birlikte)

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
    suppressions: SuppressionsResource
    exports: ExportsResource
    imports: ImportsResource
    webhooks: WebhooksResource
    channels: ChannelsResource
    analytics: AnalyticsResource
    apps: AppsResource
    organization: OrganizationResource
    api_keys: ApiKeysResource
    in_app_messages: InAppMessagesResource

    def _init_resources(self) -> None:
        self.notifications = NotificationsResource(self)  # type: ignore[arg-type]
        self.users = UsersResource(self)  # type: ignore[arg-type]
        self.aliases = AliasesResource(self)  # type: ignore[arg-type]
        self.subscriptions = SubscriptionsResource(self)  # type: ignore[arg-type]
        self.events = EventsResource(self)  # type: ignore[arg-type]
        self.segments = SegmentsResource(self)  # type: ignore[arg-type]
        self.templates = TemplatesResource(self)  # type: ignore[arg-type]
        self.campaigns = CampaignsResource(self)  # type: ignore[arg-type]
        self.suppressions = SuppressionsResource(self)  # type: ignore[arg-type]
        self.exports = ExportsResource(self)  # type: ignore[arg-type]
        self.imports = ImportsResource(self)  # type: ignore[arg-type]
        self.webhooks = WebhooksResource(self)  # type: ignore[arg-type]
        self.channels = ChannelsResource(self)  # type: ignore[arg-type]
        self.analytics = AnalyticsResource(self)  # type: ignore[arg-type]
        self.apps = AppsResource(self)  # type: ignore[arg-type]
        self.organization = OrganizationResource(self)  # type: ignore[arg-type]
        self.api_keys = ApiKeysResource(self)  # type: ignore[arg-type]
        self.in_app_messages = InAppMessagesResource(self)  # type: ignore[arg-type]


RESOURCE_NAMES = (
    "notifications",
    "users",
    "aliases",
    "subscriptions",
    "events",
    "segments",
    "templates",
    "campaigns",
    "suppressions",
    "exports",
    "imports",
    "webhooks",
    "channels",
    "analytics",
    "apps",
    "organization",
    "api_keys",
    "in_app_messages",
)
