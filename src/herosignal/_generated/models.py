# Bu dosya api/openapi.yaml'dan sdk/scripts/generate-server-sdks.mjs ile üretilmiştir; elle düzenlemeyin.
"""API şemalarının TypedDict karşılıkları (çalışma zamanında sade ``dict``)."""

from typing import Any, Dict, List, Optional, TypedDict


class AddAliasDto(TypedDict, total=False):
    """AddAliasDto şeması."""

    #: Zorunlu.
    identity: Dict[str, str]


class AddSubscriptionDto(TypedDict, total=False):
    """AddSubscriptionDto şeması."""

    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu.
    token: str
    device: "AddSubscriptionDtoDevice"
    #: Değerler: "subscribed", "unsubscribed".
    status: str
    opt_in: "AddSubscriptionDtoOptIn"


class AddSubscriptionDtoDevice(TypedDict, total=False):
    """AddSubscriptionDtoDevice şeması."""

    model: str
    os: str
    os_version: str
    app_version: Optional[str]
    sdk_version: str
    sdk_platform: str
    carrier: str
    locale: str
    timezone: str
    push_capable: bool
    #: Değerler: "sandbox", "production".
    push_environment: str


class AddSubscriptionDtoOptIn(TypedDict, total=False):
    """AddSubscriptionDtoOptIn şeması."""

    #: Zorunlu.
    source: str
    at: str


class ApiEventsDto(TypedDict, total=False):
    """ApiEventsDto şeması."""

    #: Zorunlu.
    events: List["ApiEventsDtoEventsItem"]


class ApiEventsDtoEventsItem(TypedDict, total=False):
    """ApiEventsDtoEventsItem şeması."""

    #: Zorunlu.
    name: str
    properties: Dict[str, Any]
    value: float
    occurred_at: str
    event_id: str
    subscription_id: str
    external_id: str


class ApiKey(TypedDict, total=False):
    """ApiKey şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    org_id: str
    #: Zorunlu.
    app_id: Optional[str]
    #: Zorunlu.
    name: str
    #: Zorunlu.
    prefix: str
    #: Zorunlu.
    scopes: List[str]
    #: Zorunlu.
    last_used_at: Optional[str]
    #: Zorunlu.
    expires_at: Optional[str]
    #: Zorunlu.
    revoked_at: Optional[str]
    #: Zorunlu.
    ip_allowlist: List[str]
    #: Zorunlu.
    rotated_at: Optional[str]
    #: Zorunlu.
    created_by: Optional[str]
    #: Zorunlu.
    created_at: str


class ApiKeyList(TypedDict, total=False):
    """ApiKeyList şeması."""

    #: Zorunlu.
    data: List["ApiKey"]


class App(TypedDict, total=False):
    """App şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    org_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    slug: str
    #: Zorunlu.
    platform_flags: "AppPlatformFlags"
    #: Zorunlu.
    icon_url: Optional[str]
    #: Zorunlu.
    default_language: str
    #: Zorunlu.
    timezone: str
    #: Zorunlu.
    settings: "AppSettings"
    #: Zorunlu. Değerler: "hmac", "jwt", "both".
    identity_verification_mode: str
    #: Zorunlu. Değerler: "active", "suspended", "deleted".
    status: str
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class AppList(TypedDict, total=False):
    """AppList şeması."""

    #: Zorunlu.
    data: List["App"]


class AppPlatformFlags(TypedDict, total=False):
    """AppPlatformFlags şeması."""

    ios: bool
    android: bool
    web: bool
    email: bool
    sms: bool


class AppSettings(TypedDict, total=False):
    """AppSettings şeması."""

    quietHours: Optional["AppSettingsQuietHours"]
    frequencyCap: Optional["AppSettingsFrequencyCap"]
    frequencyCaps: List["AppSettingsFrequencyCapsItem"]
    inApp: "AppSettingsInApp"
    androidChannels: List["AppSettingsAndroidChannelsItem"]
    sms: "AppSettingsSms"
    preferenceCenter: "AppSettingsPreferenceCenter"
    defaultTtlSeconds: int
    identityVerificationRequired: bool
    allowedOrigins: List[str]
    campaignApprovalRequired: bool
    webPush: "AppSettingsWebPush"
    onboarding: "AppSettingsOnboarding"
    sdkSetup: Optional["AppSettingsSdkSetup"]


class AppSettingsAndroidChannelsItem(TypedDict, total=False):
    """AppSettingsAndroidChannelsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    description: str
    #: Zorunlu. Değerler: "low", "default", "high", "urgent".
    importance: str
    sound: str
    vibration: bool
    group: str


class AppSettingsFrequencyCap(TypedDict, total=False):
    """AppSettingsFrequencyCap şeması."""

    #: Zorunlu.
    max: int
    #: Zorunlu.
    windowHours: int


class AppSettingsFrequencyCapsItem(TypedDict, total=False):
    """AppSettingsFrequencyCapsItem şeması."""

    #: Zorunlu.
    max: int
    #: Zorunlu.
    window: "AppSettingsFrequencyCapsItemWindow"
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]


class AppSettingsFrequencyCapsItemWindow(TypedDict, total=False):
    """AppSettingsFrequencyCapsItemWindow şeması."""

    #: Zorunlu.
    value: int
    #: Zorunlu. Değerler: "minutes", "hours", "days", "weeks".
    unit: str


class AppSettingsInApp(TypedDict, total=False):
    """AppSettingsInApp şeması."""

    minIntervalSeconds: int


class AppSettingsOnboarding(TypedDict, total=False):
    """AppSettingsOnboarding şeması."""

    #: Zorunlu.
    step: int
    simulation: bool
    completed_at: Optional[str]
    version: int
    #: Değerler: "ios", "android", "huawei", "web".
    platforms: List[str]
    #: Değerler: "native", "flutter", "react-native", "unity", "capacitor", "cordova", "maui".
    framework: str
    #: Değerler: "code", "wordpress".
    web_integration: str


class AppSettingsPreferenceCenter(TypedDict, total=False):
    """AppSettingsPreferenceCenter şeması."""

    enabled: bool
    brandName: str
    logoUrl: str
    accentColor: str
    customUnsubscribeUrl: str
    texts: Dict[str, "AppSettingsPreferenceCenterTextsValue"]


class AppSettingsPreferenceCenterTextsValue(TypedDict, total=False):
    """AppSettingsPreferenceCenterTextsValue şeması."""

    title: str
    description: str
    unsubscribeAll: str
    saved: str


class AppSettingsQuietHours(TypedDict, total=False):
    """AppSettingsQuietHours şeması."""

    #: Zorunlu.
    start: str
    #: Zorunlu.
    end: str
    #: Zorunlu. Değerler: "user", "app".
    timezoneMode: str


class AppSettingsSdkSetup(TypedDict, total=False):
    """AppSettingsSdkSetup şeması."""

    #: Zorunlu.
    version: int
    #: Zorunlu.
    platform: Optional[str]
    #: Zorunlu.
    step: str
    #: Zorunlu.
    furthest: str
    variant: Optional[str]
    detectedSubscriptionId: Optional[str]
    testMessageId: Optional[str]
    completedAt: Optional[str]


class AppSettingsSms(TypedDict, total=False):
    """AppSettingsSms şeması."""

    helpReply: str
    stopReply: str
    autoReply: bool


class AppSettingsWebPush(TypedDict, total=False):
    """AppSettingsWebPush şeması."""

    serviceWorkerPath: str
    serviceWorkerScope: str
    prompt: "AppSettingsWebPushPrompt"
    welcomeNotification: "AppSettingsWebPushWelcomeNotification"
    clickBehavior: "AppSettingsWebPushClickBehavior"
    customLink: "AppSettingsWebPushCustomLink"
    promptBackoffDays: List[int]


class AppSettingsWebPushClickBehavior(TypedDict, total=False):
    """AppSettingsWebPushClickBehavior şeması."""

    #: Zorunlu. Değerler: "exact", "origin".
    match: str
    #: Zorunlu. Değerler: "navigate", "focus".
    action: str


class AppSettingsWebPushCustomLink(TypedDict, total=False):
    """AppSettingsWebPushCustomLink şeması."""

    #: Zorunlu.
    enabled: bool
    #: Zorunlu. Değerler: "button", "link".
    style: str
    #: Zorunlu. Değerler: "small", "medium", "large".
    size: str
    color: "AppSettingsWebPushCustomLinkColor"
    texts: Dict[str, "AppSettingsWebPushCustomLinkTextsValue"]
    unsubscribeEnabled: bool


class AppSettingsWebPushCustomLinkColor(TypedDict, total=False):
    """AppSettingsWebPushCustomLinkColor şeması."""

    button: str
    text: str


class AppSettingsWebPushCustomLinkTextsValue(TypedDict, total=False):
    """AppSettingsWebPushCustomLinkTextsValue şeması."""

    subscribe: str
    unsubscribe: str
    explanation: str


class AppSettingsWebPushPrompt(TypedDict, total=False):
    """AppSettingsWebPushPrompt şeması."""

    #: Zorunlu.
    enabled: bool
    #: Zorunlu. Değerler: "slidedown", "native".
    type: str
    #: Değerler: "push", "email", "sms", "email_sms".
    collect: str
    delaySeconds: int
    pageViews: int
    scrollPercent: int
    texts: Dict[str, "AppSettingsWebPushPromptTextsValue"]
    categories: List["AppSettingsWebPushPromptCategoriesItem"]
    accentColor: str


class AppSettingsWebPushPromptCategoriesItem(TypedDict, total=False):
    """AppSettingsWebPushPromptCategoriesItem şeması."""

    #: Zorunlu.
    tag: str
    #: Zorunlu.
    label: Dict[str, str]


class AppSettingsWebPushPromptTextsValue(TypedDict, total=False):
    """AppSettingsWebPushPromptTextsValue şeması."""

    title: str
    message: str
    accept: str
    cancel: str


class AppSettingsWebPushWelcomeNotification(TypedDict, total=False):
    """AppSettingsWebPushWelcomeNotification şeması."""

    #: Zorunlu.
    enabled: bool
    url: str
    texts: Dict[str, "AppSettingsWebPushWelcomeNotificationTextsValue"]


class AppSettingsWebPushWelcomeNotificationTextsValue(TypedDict, total=False):
    """AppSettingsWebPushWelcomeNotificationTextsValue şeması."""

    title: str
    message: str


class AuditEntry(TypedDict, total=False):
    """AuditEntry şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    org_id: str
    #: Zorunlu.
    app_id: Optional[str]
    #: Zorunlu. Değerler: "account", "api_key", "system".
    actor_type: str
    #: Zorunlu.
    actor_id: Optional[str]
    #: Zorunlu.
    action: str
    #: Zorunlu.
    target_type: Optional[str]
    #: Zorunlu.
    target_id: Optional[str]
    #: Zorunlu.
    metadata: Dict[str, Any]
    #: Zorunlu.
    ip: Optional[str]
    #: Zorunlu.
    request_id: Optional[str]
    #: Zorunlu.
    created_at: str


class AuditPage(TypedDict, total=False):
    """AuditPage şeması."""

    #: Zorunlu.
    data: List["AuditEntry"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class Campaign(TypedDict, total=False):
    """Campaign şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    labels: List[str]
    #: Zorunlu.
    category: Optional[str]
    #: Zorunlu.
    ab_test: "CampaignAbTest"
    #: Zorunlu.
    variants: List["CampaignVariantsItem"]
    #: Zorunlu. Değerler: "one_time", "scheduled", "recurring", "automated", "transactional".
    type: str
    #: Zorunlu. Değerler: "draft", "scheduled", "running", "paused", "completed", "cancelled", "failed".
    status: str
    #: Zorunlu.
    audience: Dict[str, Any]
    #: Zorunlu.
    content: Dict[str, Any]
    #: Zorunlu.
    template_id: Optional[str]
    #: Zorunlu.
    template_version: Optional[int]
    #: Zorunlu.
    delivery: "CampaignDelivery"
    #: Zorunlu.
    recurrence: Optional["CampaignRecurrence"]
    #: Zorunlu.
    approval: "CampaignApproval"
    #: Zorunlu.
    stats: "CampaignStats2"
    #: Zorunlu.
    send_at: Optional[str]
    #: Zorunlu.
    next_run_at: Optional[str]
    #: Zorunlu.
    last_run_at: Optional[str]
    #: Zorunlu.
    run_count: int
    #: Zorunlu.
    error: Optional[str]
    #: Zorunlu.
    created_by: Optional[str]
    #: Zorunlu.
    started_at: Optional[str]
    #: Zorunlu.
    completed_at: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str
    #: Zorunlu.
    estimated_recipients: Optional[int]


class CampaignAbTest(TypedDict, total=False):
    """CampaignAbTest şeması."""

    enabled: bool
    test_percentage: int
    winner: "CampaignAbTestWinner"
    #: Değerler: "testing", "winner_sent".
    phase: str
    winner_variant_id: str
    decided_at: str
    decided_by: str
    significance: "CampaignAbTestSignificance"


class CampaignAbTestSignificance(TypedDict, total=False):
    """CampaignAbTestSignificance şeması."""

    #: Zorunlu.
    p_value: float
    #: Zorunlu.
    significant: bool
    #: Zorunlu.
    metric: str


class CampaignAbTestWinner(TypedDict, total=False):
    """CampaignAbTestWinner şeması."""

    #: Zorunlu. Değerler: "manual", "auto".
    mode: str
    #: Zorunlu. Değerler: "open_rate", "click_rate", "conversion_rate".
    metric: str
    evaluate_after_minutes: int


class CampaignApproval(TypedDict, total=False):
    """CampaignApproval şeması."""

    #: Zorunlu.
    required: bool
    #: Değerler: "send", "schedule".
    pending_action: str
    requested_by: str
    requested_at: str
    approved_by: str
    approved_at: str
    rejected_by: str
    rejected_at: str


class CampaignDelivery(TypedDict, total=False):
    """CampaignDelivery şeması."""

    #: Değerler: "immediate", "per_user_timezone", "optimized".
    timezone_mode: str
    delivery_time_of_day: str
    throttle_per_minute: int
    ttl: int
    #: Değerler: 5, 10.
    priority: int
    collapse_id: str
    frequency_cap_exempt: bool
    quiet_hours_exempt: bool
    one_per_user: bool


class CampaignPage(TypedDict, total=False):
    """CampaignPage şeması."""

    #: Zorunlu.
    data: List["Campaign"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class CampaignRecurrence(TypedDict, total=False):
    """CampaignRecurrence şeması."""

    #: Zorunlu.
    cron: str
    until: Optional[str]
    timezone: str


class CampaignsCreateBody(TypedDict, total=False):
    """CampaignsCreateBody şeması."""

    name: str
    #: Değerler: "one_time", "scheduled", "recurring".
    type: str
    audience: "CampaignsCreateBodyAudience"
    #: messages.content ile aynı şema (headings, contents, url, buttons…)
    content: Dict[str, Any]
    labels: List[str]
    #: Tercih kategorisi anahtarı; kapalı kullanıcılar bastırılır
    category: Optional[str]
    ab_test: "CampaignsCreateBodyAbTest"
    #: A/B varyantları (ağırlıklar toplamı 100; en fazla bir is_control)
    variants: List["CampaignsCreateBodyVariantsItem"]
    template_id: str
    template_version: int
    delivery: "CampaignsCreateBodyDelivery"
    recurrence: Optional["CampaignsCreateBodyRecurrence"]
    send_at: Optional[str]


class CampaignsCreateBodyAbTest(TypedDict, total=False):
    """CampaignsCreateBodyAbTest şeması."""

    enabled: bool
    test_percentage: int
    winner: "CampaignsCreateBodyAbTestWinner"


class CampaignsCreateBodyAbTestWinner(TypedDict, total=False):
    """CampaignsCreateBodyAbTestWinner şeması."""

    #: Değerler: "manual", "auto".
    mode: str
    #: Değerler: "open_rate", "click_rate", "conversion_rate".
    metric: str
    evaluate_after_minutes: int


class CampaignsCreateBodyAudience(TypedDict, total=False):
    """CampaignsCreateBodyAudience şeması."""

    all: bool
    segments: List[str]
    exclude_segments: List[str]
    #: Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7).
    filters: "CampaignsCreateBodyAudienceFilters"
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]
    test_devices_only: bool


class CampaignsCreateBodyAudienceFilters(TypedDict, total=False):
    """Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7)."""

    all: List[Dict[str, Any]]
    any: List[Dict[str, Any]]
    none: List[Dict[str, Any]]


class CampaignsCreateBodyDelivery(TypedDict, total=False):
    """CampaignsCreateBodyDelivery şeması."""

    #: Değerler: "immediate", "per_user_timezone", "optimized".
    timezone_mode: str
    delivery_time_of_day: str
    throttle_per_minute: int
    ttl: int
    #: Değerler: 5, 10.
    priority: int
    collapse_id: str
    frequency_cap_exempt: bool
    quiet_hours_exempt: bool
    one_per_user: bool


class CampaignsCreateBodyRecurrence(TypedDict, total=False):
    """CampaignsCreateBodyRecurrence şeması."""

    cron: str
    until: Optional[str]
    timezone: str


class CampaignsCreateBodyVariantsItem(TypedDict, total=False):
    """CampaignsCreateBodyVariantsItem şeması."""

    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    content: Optional[Dict[str, Any]]
    is_control: bool


class CampaignStats(TypedDict, total=False):
    """CampaignStats şeması."""

    #: Zorunlu.
    campaign: "Campaign"
    #: Zorunlu.
    rates: "CampaignStatsRates"
    #: Zorunlu.
    channels: List["CampaignStatsChannelsItem"]
    #: Zorunlu.
    hourly: List["CampaignStatsHourlyItem"]
    #: Zorunlu.
    errors: List["CampaignStatsErrorsItem"]
    #: Zorunlu.
    messages: List["Message"]


class CampaignStats2(TypedDict, total=False):
    """CampaignStats2 şeması."""

    runs: int
    targeted: int
    suppressed: int
    sent: int
    delivered: int
    failed: int
    opened: int
    clicked: int
    converted: int
    bounced: int
    complained: int
    unsubscribed: int
    sms_segments: int


class CampaignStatsChannelsItem(TypedDict, total=False):
    """CampaignStatsChannelsItem şeması."""

    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu.
    targeted: int
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int


class CampaignStatsErrorsItem(TypedDict, total=False):
    """CampaignStatsErrorsItem şeması."""

    #: Zorunlu.
    code: str
    #: Zorunlu.
    count: int


class CampaignStatsHourlyItem(TypedDict, total=False):
    """CampaignStatsHourlyItem şeması."""

    #: Zorunlu.
    hour: str
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int


class CampaignStatsRates(TypedDict, total=False):
    """CampaignStatsRates şeması."""

    #: Zorunlu.
    delivery_rate: Optional[float]
    #: Zorunlu.
    open_rate: Optional[float]
    #: Zorunlu.
    click_rate: Optional[float]
    #: Zorunlu.
    failure_rate: Optional[float]
    #: Zorunlu.
    conversion_rate: Optional[float]


class CampaignsUpdateBody(TypedDict, total=False):
    """CampaignsUpdateBody şeması."""

    name: str
    #: Değerler: "one_time", "scheduled", "recurring".
    type: str
    audience: "CampaignsUpdateBodyAudience"
    #: messages.content ile aynı şema (headings, contents, url, buttons…)
    content: Dict[str, Any]
    labels: List[str]
    #: Tercih kategorisi anahtarı; kapalı kullanıcılar bastırılır
    category: Optional[str]
    ab_test: "CampaignsUpdateBodyAbTest"
    #: A/B varyantları (ağırlıklar toplamı 100; en fazla bir is_control)
    variants: List["CampaignsUpdateBodyVariantsItem"]
    template_id: str
    template_version: int
    delivery: "CampaignsUpdateBodyDelivery"
    recurrence: Optional["CampaignsUpdateBodyRecurrence"]
    send_at: Optional[str]


class CampaignsUpdateBodyAbTest(TypedDict, total=False):
    """CampaignsUpdateBodyAbTest şeması."""

    enabled: bool
    test_percentage: int
    winner: "CampaignsUpdateBodyAbTestWinner"


class CampaignsUpdateBodyAbTestWinner(TypedDict, total=False):
    """CampaignsUpdateBodyAbTestWinner şeması."""

    #: Değerler: "manual", "auto".
    mode: str
    #: Değerler: "open_rate", "click_rate", "conversion_rate".
    metric: str
    evaluate_after_minutes: int


class CampaignsUpdateBodyAudience(TypedDict, total=False):
    """CampaignsUpdateBodyAudience şeması."""

    all: bool
    segments: List[str]
    exclude_segments: List[str]
    #: Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7).
    filters: "CampaignsUpdateBodyAudienceFilters"
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]
    test_devices_only: bool


class CampaignsUpdateBodyAudienceFilters(TypedDict, total=False):
    """Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7)."""

    all: List[Dict[str, Any]]
    any: List[Dict[str, Any]]
    none: List[Dict[str, Any]]


class CampaignsUpdateBodyDelivery(TypedDict, total=False):
    """CampaignsUpdateBodyDelivery şeması."""

    #: Değerler: "immediate", "per_user_timezone", "optimized".
    timezone_mode: str
    delivery_time_of_day: str
    throttle_per_minute: int
    ttl: int
    #: Değerler: 5, 10.
    priority: int
    collapse_id: str
    frequency_cap_exempt: bool
    quiet_hours_exempt: bool
    one_per_user: bool


class CampaignsUpdateBodyRecurrence(TypedDict, total=False):
    """CampaignsUpdateBodyRecurrence şeması."""

    cron: str
    until: Optional[str]
    timezone: str


class CampaignsUpdateBodyVariantsItem(TypedDict, total=False):
    """CampaignsUpdateBodyVariantsItem şeması."""

    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    content: Optional[Dict[str, Any]]
    is_control: bool


class CampaignVariantsItem(TypedDict, total=False):
    """CampaignVariantsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    #: Zorunlu.
    content: Optional[Dict[str, Any]]
    #: Zorunlu.
    is_control: bool
    #: Zorunlu.
    position: int


class CampaignVariantStats(TypedDict, total=False):
    """CampaignVariantStats şeması."""

    #: Zorunlu.
    ab_test: "CampaignVariantStatsAbTest"
    #: Zorunlu.
    variants: List["CampaignVariantStatsVariantsItem"]
    #: Zorunlu.
    leader: Optional[str]
    #: Zorunlu.
    significance: "CampaignVariantStatsSignificance"


class CampaignVariantStatsAbTest(TypedDict, total=False):
    """CampaignVariantStatsAbTest şeması."""

    enabled: bool
    test_percentage: int
    winner: "CampaignVariantStatsAbTestWinner"
    #: Değerler: "testing", "winner_sent".
    phase: str
    winner_variant_id: str
    decided_at: str
    decided_by: str
    significance: "CampaignVariantStatsAbTestSignificance"


class CampaignVariantStatsAbTestSignificance(TypedDict, total=False):
    """CampaignVariantStatsAbTestSignificance şeması."""

    #: Zorunlu.
    p_value: float
    #: Zorunlu.
    significant: bool
    #: Zorunlu.
    metric: str


class CampaignVariantStatsAbTestWinner(TypedDict, total=False):
    """CampaignVariantStatsAbTestWinner şeması."""

    #: Zorunlu. Değerler: "manual", "auto".
    mode: str
    #: Zorunlu. Değerler: "open_rate", "click_rate", "conversion_rate".
    metric: str
    evaluate_after_minutes: int


class CampaignVariantStatsSignificance(TypedDict, total=False):
    """CampaignVariantStatsSignificance şeması."""

    #: Zorunlu.
    p_value: float
    #: Zorunlu.
    significant: bool
    #: Zorunlu.
    metric: str


class CampaignVariantStatsVariantsItem(TypedDict, total=False):
    """CampaignVariantStatsVariantsItem şeması."""

    #: Zorunlu.
    variant_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    #: Zorunlu.
    is_control: bool
    #: Zorunlu.
    targeted: int
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    delivered: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int
    #: Zorunlu.
    converted: int
    #: Zorunlu.
    holdout: int
    #: Zorunlu.
    open_rate: float
    #: Zorunlu.
    click_rate: float
    #: Zorunlu.
    conversion_rate: float


class ChannelConfig(TypedDict, total=False):
    """ChannelConfig şeması."""

    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu. Değerler: "apns", "fcm", "hms", "webpush", "smtp", "ses", "resend", "twilio", "netgsm", "meta_whatsapp", "google_rbm", "mock".
    provider: Optional[str]
    #: Zorunlu. Değerler: "unconfigured", "active", "invalid", "suspended".
    status: str
    #: Zorunlu.
    config: "ChannelConfigConfig"
    #: Zorunlu.
    has_secret: bool
    #: Zorunlu.
    has_hook: bool
    #: Zorunlu.
    last_validated_at: Optional[str]
    #: Zorunlu.
    last_error: Optional[str]
    #: Zorunlu.
    updated_at: Optional[str]
    #: Zorunlu.
    suspended_reason: Optional[str]
    #: Zorunlu.
    dns_check: Optional["ChannelConfigDnsCheck"]


class ChannelConfigConfig(TypedDict, total=False):
    """ChannelConfigConfig şeması."""

    #: Değerler: "token", "certificate".
    auth_type: str
    #: Değerler: "sandbox", "production", "universal".
    certificate_environment: str
    certificate_subject: str
    certificate_expires_at: str
    key_id: str
    team_id: str
    bundle_id: str
    #: Değerler: "sandbox", "production".
    environment: str
    project_id: str
    client_email: str
    hms_app_id: str
    high_priority: bool
    subject: str
    vapid_public_key: str
    site_url: str
    from_address: str
    from_name: str
    reply_to: str
    dkim_selector: str
    postal_address: str
    host: str
    port: int
    secure: bool
    username: str
    region: str
    access_key_id: str
    configuration_set: str
    account_sid: str
    from_number: str
    messaging_service_sid: str
    usercode: str
    msgheader: str
    #: Değerler: "0", "11", "12".
    iys_filter: str
    waba_id: str
    phone_number_id: str
    graph_api_version: str
    display_phone_number: str
    verified_name: str
    rbm_agent_id: str
    content_sid: str
    sms_fallback: bool


class ChannelConfigDnsCheck(TypedDict, total=False):
    """ChannelConfigDnsCheck şeması."""

    #: Zorunlu.
    domain: str
    #: Zorunlu.
    checked_at: str
    #: Zorunlu.
    spf: "ChannelConfigDnsCheckSpf"
    #: Zorunlu.
    dkim: "ChannelConfigDnsCheckDkim"
    #: Zorunlu.
    dmarc: "ChannelConfigDnsCheckDmarc"
    #: Zorunlu.
    issues: List[str]


class ChannelConfigDnsCheckDkim(TypedDict, total=False):
    """ChannelConfigDnsCheckDkim şeması."""

    #: Zorunlu.
    ok: bool
    #: Zorunlu.
    selector: str
    #: Zorunlu.
    record: Optional[str]
    #: Zorunlu.
    expected: str


class ChannelConfigDnsCheckDmarc(TypedDict, total=False):
    """ChannelConfigDnsCheckDmarc şeması."""

    #: Zorunlu.
    ok: bool
    #: Zorunlu.
    record: Optional[str]
    #: Zorunlu.
    expected: str


class ChannelConfigDnsCheckSpf(TypedDict, total=False):
    """ChannelConfigDnsCheckSpf şeması."""

    #: Zorunlu.
    ok: bool
    #: Zorunlu.
    record: Optional[str]
    #: Zorunlu.
    expected: str


class ChannelList(TypedDict, total=False):
    """ChannelList şeması."""

    #: Zorunlu.
    data: List["ChannelConfig"]


class ChannelValidation(TypedDict, total=False):
    """ChannelValidation şeması."""

    #: Zorunlu.
    ok: bool
    #: Zorunlu. Değerler: "auth", "config", "transient".
    kind: Optional[str]
    #: Zorunlu.
    code: Optional[str]
    #: Zorunlu.
    message: Optional[str]
    #: Zorunlu.
    details: Optional[Dict[str, Any]]
    #: Zorunlu.
    channel: "ChannelConfig"


class ContentTable(TypedDict, total=False):
    """ContentTable şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu.
    key_column: str
    #: Zorunlu.
    columns: List[str]
    #: Zorunlu.
    row_count: int
    #: Zorunlu.
    version: int
    #: Zorunlu.
    source_file_name: Optional[str]
    #: Zorunlu.
    liquid: str
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class ContentTableList(TypedDict, total=False):
    """ContentTableList şeması."""

    #: Zorunlu.
    data: List["ContentTable"]


class ContentTableRows(TypedDict, total=False):
    """ContentTableRows şeması."""

    #: Zorunlu.
    columns: List[str]
    #: Zorunlu.
    key_column: str
    #: Zorunlu.
    total: int
    #: Zorunlu.
    data: List[Dict[str, str]]


class Conversation(TypedDict, total=False):
    """Conversation şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu. Değerler: "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu. Değerler: "open", "closed".
    status: str
    #: Zorunlu.
    subscription_id: str
    #: Zorunlu.
    subscription_status: str
    #: Zorunlu.
    user_id: Optional[str]
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu.
    contact: str
    #: Zorunlu.
    opted_in: bool
    #: Zorunlu.
    last_message_at: str
    #: Zorunlu.
    last_inbound_at: Optional[str]
    #: Zorunlu. Değerler: "inbound", "outbound".
    last_direction: Optional[str]
    #: Zorunlu.
    last_message_preview: Optional[str]
    #: Zorunlu.
    unread_count: int
    #: Zorunlu.
    window: Optional["ConversationWindow"]
    #: Zorunlu.
    created_at: str


class ConversationMessagePage(TypedDict, total=False):
    """ConversationMessagePage şeması."""

    #: Zorunlu.
    data: List["ConversationMessagePageDataItem"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class ConversationMessagePageDataItem(TypedDict, total=False):
    """ConversationMessagePageDataItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu. Değerler: "inbound", "outbound".
    direction: str
    #: Zorunlu.
    status: str
    #: Zorunlu.
    body: Optional[str]
    #: Zorunlu.
    content: Dict[str, Any]
    #: Zorunlu.
    message_id: Optional[str]
    #: Zorunlu.
    delivery_id: Optional[str]
    #: Zorunlu.
    sent_by: Optional[str]
    #: Zorunlu.
    error_code: Optional[str]
    #: Zorunlu.
    read_at: Optional[str]
    #: Zorunlu.
    created_at: str


class ConversationPage(TypedDict, total=False):
    """ConversationPage şeması."""

    #: Zorunlu.
    data: List["Conversation"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class ConversationReplyDto(TypedDict, total=False):
    """ConversationReplyDto şeması."""

    text: str
    template: "ConversationReplyDtoTemplate"
    media: "ConversationReplyDtoMedia"
    interactive: "ConversationReplyDtoInteractive"


class ConversationReplyDtoInteractive(TypedDict, total=False):
    """ConversationReplyDtoInteractive şeması."""

    #: Zorunlu. Değerler: "button", "list".
    type: str
    header: str
    footer: str
    buttons: List["ConversationReplyDtoInteractiveButtonsItem"]
    list: "ConversationReplyDtoInteractiveList"


class ConversationReplyDtoInteractiveButtonsItem(TypedDict, total=False):
    """ConversationReplyDtoInteractiveButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str


class ConversationReplyDtoInteractiveList(TypedDict, total=False):
    """ConversationReplyDtoInteractiveList şeması."""

    #: Zorunlu.
    button: str
    #: Zorunlu.
    sections: List["ConversationReplyDtoInteractiveListSectionsItem"]


class ConversationReplyDtoInteractiveListSectionsItem(TypedDict, total=False):
    """ConversationReplyDtoInteractiveListSectionsItem şeması."""

    title: str
    #: Zorunlu.
    rows: List["ConversationReplyDtoInteractiveListSectionsItemRowsItem"]


class ConversationReplyDtoInteractiveListSectionsItemRowsItem(TypedDict, total=False):
    """ConversationReplyDtoInteractiveListSectionsItemRowsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str
    description: str


class ConversationReplyDtoMedia(TypedDict, total=False):
    """ConversationReplyDtoMedia şeması."""

    #: Zorunlu. Değerler: "image", "video", "document", "audio".
    type: str
    #: Zorunlu.
    url: str
    filename: str


class ConversationReplyDtoTemplate(TypedDict, total=False):
    """ConversationReplyDtoTemplate şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu.
    language: str
    header: Any
    body_params: List[str]
    button_params: List["ConversationReplyDtoTemplateButtonParamsItem"]


class ConversationReplyDtoTemplateButtonParamsItem(TypedDict, total=False):
    """ConversationReplyDtoTemplateButtonParamsItem şeması."""

    #: Zorunlu.
    index: int
    #: Zorunlu. Değerler: "url", "quick_reply", "copy_code".
    sub_type: str
    #: Zorunlu.
    value: str


class ConversationReplyResult(TypedDict, total=False):
    """ConversationReplyResult şeması."""

    #: Zorunlu.
    message_id: str
    #: Zorunlu.
    conversation_message: "ConversationReplyResultConversationMessage"


class ConversationReplyResultConversationMessage(TypedDict, total=False):
    """ConversationReplyResultConversationMessage şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu. Değerler: "inbound", "outbound".
    direction: str
    #: Zorunlu.
    status: str
    #: Zorunlu.
    body: Optional[str]
    #: Zorunlu.
    content: Dict[str, Any]
    #: Zorunlu.
    message_id: Optional[str]
    #: Zorunlu.
    delivery_id: Optional[str]
    #: Zorunlu.
    sent_by: Optional[str]
    #: Zorunlu.
    error_code: Optional[str]
    #: Zorunlu.
    read_at: Optional[str]
    #: Zorunlu.
    created_at: str


class ConversationWindow(TypedDict, total=False):
    """ConversationWindow şeması."""

    #: Zorunlu.
    open: bool
    #: Zorunlu.
    expires_at: Optional[str]


ConversionsReport = TypedDict(
    "ConversionsReport",
    {
        # Zorunlu.
        "from": str,
        # Zorunlu.
        "to": str,
        # Zorunlu.
        "totals": "ConversionsReportTotals",
        # Zorunlu.
        "previous": Optional["ConversionsReportPrevious"],
        # Zorunlu.
        "by_campaign": List["ConversionsReportByCampaignItem"],
        # Zorunlu.
        "rows": List["ConversionsReportRowsItem"],
    },
    total=False,
)


class ConversionsReportByCampaignItem(TypedDict, total=False):
    """ConversionsReportByCampaignItem şeması."""

    #: Zorunlu.
    campaign_id: Optional[str]
    #: Zorunlu.
    name: str
    #: Zorunlu.
    conversions: int
    #: Zorunlu.
    direct: int
    #: Zorunlu.
    influenced: int
    #: Zorunlu.
    unattributed: int
    #: Zorunlu.
    revenue: float
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    conversion_rate: Optional[float]


class ConversionsReportPrevious(TypedDict, total=False):
    """ConversionsReportPrevious şeması."""

    #: Zorunlu.
    conversions: int
    #: Zorunlu.
    direct: int
    #: Zorunlu.
    influenced: int
    #: Zorunlu.
    unattributed: int
    #: Zorunlu.
    revenue: float


class ConversionsReportRowsItem(TypedDict, total=False):
    """ConversionsReportRowsItem şeması."""

    #: Zorunlu.
    date: str
    #: Zorunlu.
    conversions: int
    #: Zorunlu.
    revenue: float


class ConversionsReportTotals(TypedDict, total=False):
    """ConversionsReportTotals şeması."""

    #: Zorunlu.
    conversions: int
    #: Zorunlu.
    direct: int
    #: Zorunlu.
    influenced: int
    #: Zorunlu.
    unattributed: int
    #: Zorunlu.
    revenue: float


class CopyTemplateDto(TypedDict, total=False):
    """CopyTemplateDto şeması."""

    #: Zorunlu.
    target_app_id: str
    name: str


class CreateAppApiKeyDto(TypedDict, total=False):
    """CreateAppApiKeyDto şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu. Değerler: "admin", "notifications:write", "users:read", "users:write", "events:write", "segments:read", "analytics:read", "mcp:write".
    scopes: List[str]
    #: Değerler: "live", "test".
    environment: str
    expires_at: Optional[str]
    ip_allowlist: List[str]


class CreateAppDto(TypedDict, total=False):
    """CreateAppDto şeması."""

    #: Zorunlu.
    name: str
    slug: str
    platform_flags: "CreateAppDtoPlatformFlags"
    default_language: str
    timezone: str


class CreateAppDtoPlatformFlags(TypedDict, total=False):
    """CreateAppDtoPlatformFlags şeması."""

    ios: bool
    android: bool
    web: bool
    email: bool
    sms: bool


class CreateCategoryDto(TypedDict, total=False):
    """CreateCategoryDto şeması."""

    #: Zorunlu.
    key: str
    #: Zorunlu.
    name: Dict[str, str]
    description: Dict[str, str]
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: Optional[List[str]]
    default_opted_in: bool
    position: int


class CreatedApiKey(TypedDict, total=False):
    """CreatedApiKey şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    org_id: str
    #: Zorunlu.
    app_id: Optional[str]
    #: Zorunlu.
    name: str
    #: Zorunlu.
    prefix: str
    #: Zorunlu.
    scopes: List[str]
    #: Zorunlu.
    last_used_at: Optional[str]
    #: Zorunlu.
    expires_at: Optional[str]
    #: Zorunlu.
    revoked_at: Optional[str]
    #: Zorunlu.
    ip_allowlist: List[str]
    #: Zorunlu.
    rotated_at: Optional[str]
    #: Zorunlu.
    created_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    key: str


class CreateDataFeedDto(TypedDict, total=False):
    """CreateDataFeedDto şeması."""

    #: Zorunlu.
    name: str
    description: Optional[str]
    #: Zorunlu.
    url_template: str
    #: Değerler: "GET", "POST".
    method: str
    body_template: Optional[str]
    headers: Dict[str, str]
    secret_headers: Dict[str, str]
    cache_ttl_seconds: int
    timeout_ms: int
    enabled: bool


class CreateExportDto(TypedDict, total=False):
    """CreateExportDto şeması."""

    #: Zorunlu. Değerler: "users", "subscriptions", "events", "deliveries", "message_events".
    type: str
    filters: "CreateExportDtoFilters"


CreateExportDtoFilters = TypedDict(
    "CreateExportDtoFilters",
    {
        "from": str,
        "to": str,
        "name": str,
        "message_id": str,
        "campaign_id": str,
        "status": str,
        # Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
        "channel": str,
        "segment_id": str,
    },
    total=False,
)


class CreateIdentityKeyDto(TypedDict, total=False):
    """CreateIdentityKeyDto şeması."""

    kid: str
    label: str
    public_jwk: Dict[str, Any]
    public_key_pem: str


class CreateInAppDto(TypedDict, total=False):
    """CreateInAppDto şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu.
    triggers: List[Any]
    trigger_groups: List[List[Any]]
    variants: List["CreateInAppDtoVariantsItem"]
    ab_test: "CreateInAppDtoAbTest"
    #: Zorunlu.
    display: "CreateInAppDtoDisplay"
    audience: "CreateInAppDtoAudience"
    frequency: "CreateInAppDtoFrequency"
    journey_only: bool
    priority: int
    start_at: Optional[str]
    end_at: Optional[str]


class CreateInAppDtoAbTest(TypedDict, total=False):
    """CreateInAppDtoAbTest şeması."""

    winner: "CreateInAppDtoAbTestWinner"


class CreateInAppDtoAbTestWinner(TypedDict, total=False):
    """CreateInAppDtoAbTestWinner şeması."""

    #: Zorunlu. Değerler: "manual", "auto".
    mode: str
    min_impressions: int
    confidence: float


class CreateInAppDtoAudience(TypedDict, total=False):
    """CreateInAppDtoAudience şeması."""

    included_segments: List[str]
    excluded_segments: List[str]


class CreateInAppDtoDisplay(TypedDict, total=False):
    """CreateInAppDtoDisplay şeması."""

    #: Zorunlu. Değerler: "modal", "banner_top", "banner_bottom", "fullscreen".
    layout: str
    background_color: str
    text_color: str
    dismissible: bool
    auto_dismiss_seconds: int
    #: Değerler: "blocks", "html".
    content_type: str
    html: Dict[str, str]
    html_height: int
    #: Zorunlu.
    blocks: List[Any]


class CreateInAppDtoFrequency(TypedDict, total=False):
    """CreateInAppDtoFrequency şeması."""

    max_impressions: int
    min_interval_seconds: int
    stop_after_interaction: bool


class CreateInAppDtoVariantsItem(TypedDict, total=False):
    """CreateInAppDtoVariantsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    #: Zorunlu.
    display: "CreateInAppDtoVariantsItemDisplay"


class CreateInAppDtoVariantsItemDisplay(TypedDict, total=False):
    """CreateInAppDtoVariantsItemDisplay şeması."""

    #: Zorunlu. Değerler: "modal", "banner_top", "banner_bottom", "fullscreen".
    layout: str
    background_color: str
    text_color: str
    dismissible: bool
    auto_dismiss_seconds: int
    #: Değerler: "blocks", "html".
    content_type: str
    html: Dict[str, str]
    html_height: int
    #: Zorunlu.
    blocks: List[Any]


class CreateKeywordDto(TypedDict, total=False):
    """CreateKeywordDto şeması."""

    #: Zorunlu.
    keyword: str
    #: Değerler: "org", "app".
    scope: str
    #: Değerler: "sms", "whatsapp", "rcs".
    channels: List[str]
    #: Zorunlu.
    actions: "CreateKeywordDtoActions"
    enabled: bool
    description: str


class CreateKeywordDtoActions(TypedDict, total=False):
    """CreateKeywordDtoActions şeması."""

    add_tags: Dict[str, str]
    remove_tags: List[str]
    event: "CreateKeywordDtoActionsEvent"
    reply: "CreateKeywordDtoActionsReply"
    opt_in: bool


class CreateKeywordDtoActionsEvent(TypedDict, total=False):
    """CreateKeywordDtoActionsEvent şeması."""

    #: Zorunlu.
    name: str
    properties: Dict[str, str]


class CreateKeywordDtoActionsReply(TypedDict, total=False):
    """CreateKeywordDtoActionsReply şeması."""

    #: Zorunlu.
    text: str


class CreateLiveActivityTypeDto(TypedDict, total=False):
    """CreateLiveActivityTypeDto şeması."""

    #: Zorunlu.
    name: str
    description: str
    #: Zorunlu.
    content_state_schema: "CreateLiveActivityTypeDtoContentStateSchema"
    attributes_schema: "CreateLiveActivityTypeDtoAttributesSchema"


class CreateLiveActivityTypeDtoAttributesSchema(TypedDict, total=False):
    """CreateLiveActivityTypeDtoAttributesSchema şeması."""

    #: Zorunlu. Değerler: "object".
    type: str
    #: Zorunlu.
    properties: Dict[str, "CreateLiveActivityTypeDtoAttributesSchemaPropertiesValue"]
    required: List[str]


class CreateLiveActivityTypeDtoAttributesSchemaPropertiesValue(TypedDict, total=False):
    """CreateLiveActivityTypeDtoAttributesSchemaPropertiesValue şeması."""

    #: Zorunlu. Değerler: "string", "number", "integer", "boolean".
    type: str
    enum: List[Any]
    maxLength: int
    minimum: float
    maximum: float
    description: str


class CreateLiveActivityTypeDtoContentStateSchema(TypedDict, total=False):
    """CreateLiveActivityTypeDtoContentStateSchema şeması."""

    #: Zorunlu. Değerler: "object".
    type: str
    #: Zorunlu.
    properties: Dict[str, "CreateLiveActivityTypeDtoContentStateSchemaPropertiesValue"]
    required: List[str]


class CreateLiveActivityTypeDtoContentStateSchemaPropertiesValue(TypedDict, total=False):
    """CreateLiveActivityTypeDtoContentStateSchemaPropertiesValue şeması."""

    #: Zorunlu. Değerler: "string", "number", "integer", "boolean".
    type: str
    enum: List[Any]
    maxLength: int
    minimum: float
    maximum: float
    description: str


class CreateNotificationDto(TypedDict, total=False):
    """CreateNotificationDto şeması."""

    app_id: str
    idempotency_key: str
    #: Zorunlu.
    target: "CreateNotificationDtoTarget"
    headings: Dict[str, str]
    contents: Dict[str, str]
    subtitle: Dict[str, str]
    url: str
    app_url: str
    data: Dict[str, str]
    buttons: List["CreateNotificationDtoButtonsItem"]
    big_picture: str
    ios_attachments: Dict[str, str]
    ios_sound: str
    #: Değerler: "None", "SetTo", "Increase".
    ios_badge_type: str
    ios_badge_count: int
    #: Değerler: "passive", "active", "time-sensitive", "critical".
    ios_interruption_level: str
    ios_category: str
    thread_id: str
    ios_relevance_score: float
    target_content_identifier: str
    android_channel_id: str
    android_group: str
    android_sound: str
    small_icon: str
    large_icon: str
    android_accent_color: str
    #: Değerler: 1, 0, -1.
    android_visibility: int
    chrome_web_icon: str
    chrome_web_image: str
    chrome_web_badge: str
    web_push_topic: str
    web_buttons: List["CreateNotificationDtoWebButtonsItem"]
    require_interaction: bool
    content_available: bool
    mutable_content: bool
    collapse_id: str
    #: Değerler: 5, 10.
    priority: int
    ttl: int
    send_after: str
    #: Değerler: "timezone", "optimized".
    delayed_option: str
    delivery_time_of_day: str
    template_id: str
    custom_data: Dict[str, Any]
    email_subject: str
    email_body: str
    email_mjml: str
    email_preheader: str
    email_from_name: str
    email_from_address: str
    email_reply_to_address: str
    disable_email_click_tracking: bool
    sms_from: str
    sms_media_urls: List[str]
    disable_sms_link_shortening: bool
    whatsapp_template: "CreateNotificationDtoWhatsappTemplate"
    whatsapp_media: "CreateNotificationDtoWhatsappMedia"
    whatsapp_interactive: "CreateNotificationDtoWhatsappInteractive"
    rcs_card: "CreateNotificationDtoRcsCard"
    rcs_suggestions: List[Any]
    rcs_content_sid: str
    rcs_content_variables: Dict[str, str]
    rcs_fallback_text: Dict[str, str]
    add_to_inbox: bool
    inbox_ttl: int
    frequency_cap_exempt: bool
    quiet_hours_exempt: bool
    one_per_user: bool
    throttle_rate_per_minute: int
    include_unsubscribed: bool
    name: str
    labels: List[str]
    category: str


class CreateNotificationDtoButtonsItem(TypedDict, total=False):
    """CreateNotificationDtoButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class CreateNotificationDtoRcsCard(TypedDict, total=False):
    """CreateNotificationDtoRcsCard şeması."""

    title: Dict[str, str]
    description: Dict[str, str]
    media_url: str
    #: Değerler: "SHORT", "MEDIUM", "TALL".
    media_height: str
    #: Değerler: "VERTICAL", "HORIZONTAL".
    orientation: str


class CreateNotificationDtoTarget(TypedDict, total=False):
    """CreateNotificationDtoTarget şeması."""

    all: bool
    include_subscription_ids: List[str]
    include_external_ids: List[str]
    include_aliases: Dict[str, List[str]]
    included_segments: List[str]
    excluded_segments: List[str]
    filters: Any
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]
    test_devices_only: bool
    email_to: List[str]
    include_phone_numbers: List[str]


class CreateNotificationDtoWebButtonsItem(TypedDict, total=False):
    """CreateNotificationDtoWebButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class CreateNotificationDtoWhatsappInteractive(TypedDict, total=False):
    """CreateNotificationDtoWhatsappInteractive şeması."""

    #: Zorunlu. Değerler: "button", "list".
    type: str
    header: str
    footer: str
    buttons: List["CreateNotificationDtoWhatsappInteractiveButtonsItem"]
    list: "CreateNotificationDtoWhatsappInteractiveList"


class CreateNotificationDtoWhatsappInteractiveButtonsItem(TypedDict, total=False):
    """CreateNotificationDtoWhatsappInteractiveButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str


class CreateNotificationDtoWhatsappInteractiveList(TypedDict, total=False):
    """CreateNotificationDtoWhatsappInteractiveList şeması."""

    #: Zorunlu.
    button: str
    #: Zorunlu.
    sections: List["CreateNotificationDtoWhatsappInteractiveListSectionsItem"]


class CreateNotificationDtoWhatsappInteractiveListSectionsItem(TypedDict, total=False):
    """CreateNotificationDtoWhatsappInteractiveListSectionsItem şeması."""

    title: str
    #: Zorunlu.
    rows: List["CreateNotificationDtoWhatsappInteractiveListSectionsItemRowsItem"]


class CreateNotificationDtoWhatsappInteractiveListSectionsItemRowsItem(TypedDict, total=False):
    """CreateNotificationDtoWhatsappInteractiveListSectionsItemRowsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str
    description: str


class CreateNotificationDtoWhatsappMedia(TypedDict, total=False):
    """CreateNotificationDtoWhatsappMedia şeması."""

    #: Zorunlu. Değerler: "image", "video", "document", "audio".
    type: str
    #: Zorunlu.
    url: str
    filename: str


class CreateNotificationDtoWhatsappTemplate(TypedDict, total=False):
    """CreateNotificationDtoWhatsappTemplate şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu.
    language: str
    header: Any
    body_params: List[str]
    button_params: List["CreateNotificationDtoWhatsappTemplateButtonParamsItem"]


class CreateNotificationDtoWhatsappTemplateButtonParamsItem(TypedDict, total=False):
    """CreateNotificationDtoWhatsappTemplateButtonParamsItem şeması."""

    #: Zorunlu.
    index: int
    #: Zorunlu. Değerler: "url", "quick_reply", "copy_code".
    sub_type: str
    #: Zorunlu.
    value: str


class CreateNotificationResult(TypedDict, total=False):
    """CreateNotificationResult şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu. Değerler: "queued", "processing", "completed", "cancelled", "failed".
    status: str
    #: Zorunlu.
    recipients_estimate: int
    #: Zorunlu.
    external_id_missing: List[str]


class CreateSuppressionDto(TypedDict, total=False):
    """CreateSuppressionDto şeması."""

    #: Zorunlu. Değerler: "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu.
    value: str
    #: Değerler: "manual", "bounce", "complaint", "unsubscribe_link", "stop".
    reason: str
    expires_at: str
    note: str


class CreateTemplateDto(TypedDict, total=False):
    """CreateTemplateDto şeması."""

    #: Zorunlu.
    name: str
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: Optional[str]
    tags: List[str]
    #: Zorunlu.
    content: "CreateTemplateDtoContent"


class CreateTemplateDtoContent(TypedDict, total=False):
    """CreateTemplateDtoContent şeması."""

    headings: Dict[str, str]
    contents: Dict[str, str]
    subtitle: Dict[str, str]
    url: str
    app_url: str
    data: Dict[str, str]
    buttons: List["CreateTemplateDtoContentButtonsItem"]
    big_picture: str
    ios_attachments: Dict[str, str]
    ios_sound: str
    #: Değerler: "None", "SetTo", "Increase".
    ios_badge_type: str
    ios_badge_count: int
    #: Değerler: "passive", "active", "time-sensitive", "critical".
    ios_interruption_level: str
    ios_category: str
    android_channel_id: str
    android_group: str
    android_sound: str
    chrome_web_icon: str
    chrome_web_image: str
    chrome_web_badge: str
    web_push_topic: str
    content_available: bool
    mutable_content: bool
    custom_data: Dict[str, Any]
    email_subject: str
    email_body: str
    email_mjml: str
    email_preheader: str
    email_from_name: str
    email_from_address: str
    email_reply_to_address: str
    disable_email_click_tracking: bool
    sms_from: str
    disable_sms_link_shortening: bool
    add_to_inbox: bool
    inbox_ttl: int
    thread_id: str
    ios_relevance_score: float
    target_content_identifier: str
    small_icon: str
    large_icon: str
    android_accent_color: str
    #: Değerler: 1, 0, -1.
    android_visibility: int
    web_buttons: List["CreateTemplateDtoContentWebButtonsItem"]
    require_interaction: bool
    sms_media_urls: List[str]
    whatsapp_template: "CreateTemplateDtoContentWhatsappTemplate"
    whatsapp_media: "CreateTemplateDtoContentWhatsappMedia"
    whatsapp_interactive: "CreateTemplateDtoContentWhatsappInteractive"
    rcs_card: "CreateTemplateDtoContentRcsCard"
    rcs_suggestions: List[Any]
    rcs_content_sid: str
    rcs_content_variables: Dict[str, str]
    rcs_fallback_text: Dict[str, str]


class CreateTemplateDtoContentButtonsItem(TypedDict, total=False):
    """CreateTemplateDtoContentButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class CreateTemplateDtoContentRcsCard(TypedDict, total=False):
    """CreateTemplateDtoContentRcsCard şeması."""

    title: Dict[str, str]
    description: Dict[str, str]
    media_url: str
    #: Değerler: "SHORT", "MEDIUM", "TALL".
    media_height: str
    #: Değerler: "VERTICAL", "HORIZONTAL".
    orientation: str


class CreateTemplateDtoContentWebButtonsItem(TypedDict, total=False):
    """CreateTemplateDtoContentWebButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class CreateTemplateDtoContentWhatsappInteractive(TypedDict, total=False):
    """CreateTemplateDtoContentWhatsappInteractive şeması."""

    #: Zorunlu. Değerler: "button", "list".
    type: str
    header: str
    footer: str
    buttons: List["CreateTemplateDtoContentWhatsappInteractiveButtonsItem"]
    list: "CreateTemplateDtoContentWhatsappInteractiveList"


class CreateTemplateDtoContentWhatsappInteractiveButtonsItem(TypedDict, total=False):
    """CreateTemplateDtoContentWhatsappInteractiveButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str


class CreateTemplateDtoContentWhatsappInteractiveList(TypedDict, total=False):
    """CreateTemplateDtoContentWhatsappInteractiveList şeması."""

    #: Zorunlu.
    button: str
    #: Zorunlu.
    sections: List["CreateTemplateDtoContentWhatsappInteractiveListSectionsItem"]


class CreateTemplateDtoContentWhatsappInteractiveListSectionsItem(TypedDict, total=False):
    """CreateTemplateDtoContentWhatsappInteractiveListSectionsItem şeması."""

    title: str
    #: Zorunlu.
    rows: List["CreateTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem"]


class CreateTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem(TypedDict, total=False):
    """CreateTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str
    description: str


class CreateTemplateDtoContentWhatsappMedia(TypedDict, total=False):
    """CreateTemplateDtoContentWhatsappMedia şeması."""

    #: Zorunlu. Değerler: "image", "video", "document", "audio".
    type: str
    #: Zorunlu.
    url: str
    filename: str


class CreateTemplateDtoContentWhatsappTemplate(TypedDict, total=False):
    """CreateTemplateDtoContentWhatsappTemplate şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu.
    language: str
    header: Any
    body_params: List[str]
    button_params: List["CreateTemplateDtoContentWhatsappTemplateButtonParamsItem"]


class CreateTemplateDtoContentWhatsappTemplateButtonParamsItem(TypedDict, total=False):
    """CreateTemplateDtoContentWhatsappTemplateButtonParamsItem şeması."""

    #: Zorunlu.
    index: int
    #: Zorunlu. Değerler: "url", "quick_reply", "copy_code".
    sub_type: str
    #: Zorunlu.
    value: str


class CreateWarmupPlanDto(TypedDict, total=False):
    """CreateWarmupPlanDto şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu. Değerler: "domain", "ip".
    kind: str
    #: Zorunlu.
    target: str
    start_date: str
    daily_limits: List[int]
    curve: "CreateWarmupPlanDtoCurve"
    provider_shares: "CreateWarmupPlanDtoProviderShares"
    timezone: str


class CreateWarmupPlanDtoCurve(TypedDict, total=False):
    """CreateWarmupPlanDtoCurve şeması."""

    #: Zorunlu.
    start: int
    #: Zorunlu.
    growth: float
    #: Zorunlu.
    target: int


class CreateWarmupPlanDtoProviderShares(TypedDict, total=False):
    """CreateWarmupPlanDtoProviderShares şeması."""

    #: Zorunlu.
    gmail: float
    #: Zorunlu.
    outlook: float
    #: Zorunlu.
    yahoo: float
    #: Zorunlu.
    other: float


class CreateWebhookDto(TypedDict, total=False):
    """CreateWebhookDto şeması."""

    #: Zorunlu.
    url: str
    description: Optional[str]
    #: Zorunlu. Değerler: "message.queued", "message.completed", "message.failed", "delivery.sent", "delivery.delivered", "delivery.failed", "delivery.opened", "delivery.clicked", "delivery.bounced", "delivery.complained", "delivery.unsubscribed", "in_app.impression", "in_app.clicked", "in_app.dismissed", "subscription.created", "subscription.unsubscribed", "subscription.invalidated", "user.created", "user.updated", "user.merged", "user.deleted", "event.received", "conversion.created", "campaign.scheduled", "campaign.started", "campaign.completed", "journey.entered", "journey.step_completed", "journey.completed", "journey.exited", "audit.created".
    events: List[str]
    event_filters: "CreateWebhookDtoEventFilters"
    batch: bool
    headers: Dict[str, str]
    body_template: Optional[str]
    #: Şablon çıktısının içerik türü (varsayılan application/json). Değerler: "application/json", "text/plain".
    body_content_type: str
    filters: Optional["CreateWebhookDtoFilters"]


class CreateWebhookDtoEventFilters(TypedDict, total=False):
    """CreateWebhookDtoEventFilters şeması."""

    event_names: List[str]


class CreateWebhookDtoFilters(TypedDict, total=False):
    """Olay filtresi: { match: all|any, conditions: [{ field, op, value? }] }."""

    #: Zorunlu. Değerler: "all", "any".
    match: str
    #: Zorunlu.
    conditions: List["CreateWebhookDtoFiltersConditionsItem"]


class CreateWebhookDtoFiltersConditionsItem(TypedDict, total=False):
    """CreateWebhookDtoFiltersConditionsItem şeması."""

    #: Zorunlu.
    field: str
    #: Zorunlu. Değerler: "eq", "neq", "in", "not_in", "starts_with", "contains", "exists", "not_exists".
    op: str
    value: Any


class DataFeed(TypedDict, total=False):
    """DataFeed şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu.
    url_template: str
    #: Zorunlu. Değerler: "GET", "POST".
    method: str
    #: Zorunlu.
    body_template: Optional[str]
    #: Zorunlu.
    headers: Dict[str, str]
    #: Zorunlu.
    secret_header_names: List[str]
    #: Zorunlu.
    cache_ttl_seconds: int
    #: Zorunlu.
    timeout_ms: int
    #: Zorunlu.
    enabled: bool
    #: Zorunlu.
    liquid: str
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class DataFeedList(TypedDict, total=False):
    """DataFeedList şeması."""

    #: Zorunlu.
    data: List["DataFeed"]


class DataFeedTestResult(TypedDict, total=False):
    """DataFeedTestResult şeması."""

    #: Zorunlu. Değerler: "ok", "cached", "timeout", "error", "circuit_open", "blocked", "invalid_json", "too_large", "http_error".
    status: str
    #: Zorunlu.
    http_status: Optional[int]
    #: Zorunlu.
    duration_ms: int
    #: Zorunlu.
    error: Optional[str]
    #: Zorunlu.
    url: Optional[str]
    #: Zorunlu.
    preview: Any
    #: Zorunlu.
    truncated: bool
    #: Zorunlu.
    user: Optional["DataFeedTestResultUser"]


class DataFeedTestResultUser(TypedDict, total=False):
    """DataFeedTestResultUser şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    external_id: Optional[str]


class DeliverabilitySettingsDto(TypedDict, total=False):
    """DeliverabilitySettingsDto şeması."""

    bcc_address: Optional[str]
    validation: "DeliverabilitySettingsDtoValidation"
    verifier: "DeliverabilitySettingsDtoVerifier"


class DeliverabilitySettingsDtoValidation(TypedDict, total=False):
    """DeliverabilitySettingsDtoValidation şeması."""

    #: Zorunlu.
    enabled: bool
    check_mx: bool
    block_disposable: bool
    block_role: bool


class DeliverabilitySettingsDtoVerifier(TypedDict, total=False):
    """DeliverabilitySettingsDtoVerifier şeması."""

    #: Zorunlu. Değerler: "zerobounce", "neverbounce", "mock".
    provider: Optional[str]
    api_key: str


class Delivery(TypedDict, total=False):
    """Delivery şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    message_id: str
    #: Zorunlu.
    subscription_id: str
    #: Zorunlu.
    user_id: Optional[str]
    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu.
    provider: Optional[str]
    #: Zorunlu. Değerler: "pending", "sent", "delivered", "failed", "bounced", "suppressed", "expired", "cancelled".
    status: str
    #: Zorunlu.
    attempt_count: int
    #: Zorunlu.
    provider_message_id: Optional[str]
    #: Zorunlu.
    error_code: Optional[str]
    #: Zorunlu.
    error_message: Optional[str]
    #: Zorunlu.
    suppression_reason: Optional[str]
    #: Zorunlu.
    send_after: Optional[str]
    #: Zorunlu.
    sent_at: Optional[str]
    #: Zorunlu.
    delivered_at: Optional[str]
    #: Zorunlu.
    opened_at: Optional[str]
    #: Zorunlu.
    clicked_at: Optional[str]
    #: Zorunlu.
    failed_at: Optional[str]
    #: Zorunlu.
    created_at: str


class DeliveryList(TypedDict, total=False):
    """DeliveryList şeması."""

    #: Zorunlu.
    data: List["Delivery"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class EmailAddressCheck(TypedDict, total=False):
    """EmailAddressCheck şeması."""

    #: Zorunlu.
    ok: bool
    #: Zorunlu. Değerler: "syntax", "no_mx", "disposable", "role", "verifier_invalid".
    reason: Optional[str]
    #: Zorunlu.
    detail: Optional[str]
    #: Zorunlu.
    checks: List[str]
    #: Zorunlu.
    unknown: List[str]


class EmailDeliverabilitySettings(TypedDict, total=False):
    """EmailDeliverabilitySettings şeması."""

    #: Zorunlu.
    bcc_address: Optional[str]
    #: Zorunlu.
    validation: "EmailDeliverabilitySettingsValidation"
    #: Zorunlu.
    verifier: "EmailDeliverabilitySettingsVerifier"


class EmailDeliverabilitySettingsValidation(TypedDict, total=False):
    """EmailDeliverabilitySettingsValidation şeması."""

    #: Zorunlu.
    enabled: bool
    #: Zorunlu.
    check_mx: bool
    #: Zorunlu.
    block_disposable: bool
    #: Zorunlu.
    block_role: bool


class EmailDeliverabilitySettingsVerifier(TypedDict, total=False):
    """EmailDeliverabilitySettingsVerifier şeması."""

    #: Zorunlu. Değerler: "zerobounce", "neverbounce", "mock".
    provider: Optional[str]
    #: Zorunlu.
    has_key: bool


class EmailWarmupPlan(TypedDict, total=False):
    """EmailWarmupPlan şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu. Değerler: "domain", "ip".
    kind: str
    #: Zorunlu.
    target: str
    #: Zorunlu.
    start_date: str
    #: Zorunlu.
    daily_limits: List[int]
    #: Zorunlu.
    provider_shares: Dict[str, float]
    #: Zorunlu.
    timezone: str
    #: Zorunlu. Değerler: "active", "paused", "completed".
    status: str
    #: Zorunlu.
    today: "EmailWarmupPlanToday"
    #: Zorunlu.
    scheduled_ahead: int
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class EmailWarmupPlanList(TypedDict, total=False):
    """EmailWarmupPlanList şeması."""

    #: Zorunlu.
    data: List["EmailWarmupPlan"]


class EmailWarmupPlanToday(TypedDict, total=False):
    """EmailWarmupPlanToday şeması."""

    #: Zorunlu.
    day: str
    #: Zorunlu.
    index: int
    #: Zorunlu.
    limit: Optional[int]
    #: Zorunlu.
    used: int
    #: Zorunlu.
    buckets: Dict[str, "EmailWarmupPlanTodayBucketsValue"]


class EmailWarmupPlanTodayBucketsValue(TypedDict, total=False):
    """EmailWarmupPlanTodayBucketsValue şeması."""

    #: Zorunlu.
    limit: Optional[int]
    #: Zorunlu.
    used: int


class EmailWarmupUsage(TypedDict, total=False):
    """EmailWarmupUsage şeması."""

    #: Zorunlu.
    data: List["EmailWarmupUsageDataItem"]


class EmailWarmupUsageDataItem(TypedDict, total=False):
    """EmailWarmupUsageDataItem şeması."""

    #: Zorunlu.
    day: str
    #: Zorunlu.
    bucket: str
    #: Zorunlu.
    used: int
    #: Zorunlu.
    limit: Optional[int]


class EndLiveActivityDto(TypedDict, total=False):
    """EndLiveActivityDto şeması."""

    #: Zorunlu.
    activity_id: str
    content_state: Dict[str, Any]
    alert: "EndLiveActivityDtoAlert"
    stale_date: int
    dismissal_date: int
    relevance_score: float
    #: Değerler: 5, 10.
    priority: int
    name: str


class EndLiveActivityDtoAlert(TypedDict, total=False):
    """EndLiveActivityDtoAlert şeması."""

    title: Dict[str, str]
    body: Dict[str, str]
    sound: str


EngagementReport = TypedDict(
    "EngagementReport",
    {
        # Zorunlu.
        "from": str,
        # Zorunlu.
        "to": str,
        # Zorunlu.
        "timezone": str,
        # Zorunlu.
        "totals": "EngagementReportTotals",
        # Zorunlu.
        "previous": Optional["EngagementReportPrevious"],
        # Zorunlu.
        "cells": List["EngagementReportCellsItem"],
        # Zorunlu.
        "rows": List["EngagementReportRowsItem"],
    },
    total=False,
)


class EngagementReportCellsItem(TypedDict, total=False):
    """EngagementReportCellsItem şeması."""

    #: Zorunlu.
    weekday: int
    #: Zorunlu.
    hour: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int


class EngagementReportPrevious(TypedDict, total=False):
    """EngagementReportPrevious şeması."""

    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int


class EngagementReportRowsItem(TypedDict, total=False):
    """EngagementReportRowsItem şeması."""

    #: Zorunlu.
    date: str
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int


class EngagementReportTotals(TypedDict, total=False):
    """EngagementReportTotals şeması."""

    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int


class EstimateAudienceDto(TypedDict, total=False):
    """EstimateAudienceDto şeması."""

    app_id: str
    #: Zorunlu.
    target: "EstimateAudienceDtoTarget"
    include_unsubscribed: bool


class EstimateAudienceDtoTarget(TypedDict, total=False):
    """EstimateAudienceDtoTarget şeması."""

    all: bool
    include_subscription_ids: List[str]
    include_external_ids: List[str]
    include_aliases: Dict[str, List[str]]
    included_segments: List[str]
    excluded_segments: List[str]
    filters: Any
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]
    test_devices_only: bool
    email_to: List[str]
    include_phone_numbers: List[str]


class EstimateAudienceResult(TypedDict, total=False):
    """EstimateAudienceResult şeması."""

    #: Zorunlu.
    recipients: int
    #: Zorunlu.
    by_channel: Dict[str, int]
    #: Zorunlu.
    new_contacts: int
    #: Zorunlu.
    external_id_missing: List[str]


class EventDefinition(TypedDict, total=False):
    """EventDefinition şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    display_name: Optional[str]
    #: Zorunlu.
    properties_schema: Dict[str, str]
    #: Zorunlu.
    is_conversion: bool
    #: Zorunlu.
    outcome_unique: bool
    #: Zorunlu.
    outcome_unattributed: bool
    #: Zorunlu.
    retention_days: Optional[int]
    #: Zorunlu.
    first_seen_at: str
    #: Zorunlu.
    last_seen_at: str
    #: Zorunlu.
    count_30d: int
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class EventDefinitionDetail(TypedDict, total=False):
    """EventDefinitionDetail şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    display_name: Optional[str]
    #: Zorunlu.
    properties_schema: Dict[str, str]
    #: Zorunlu.
    is_conversion: bool
    #: Zorunlu.
    outcome_unique: bool
    #: Zorunlu.
    outcome_unattributed: bool
    #: Zorunlu.
    retention_days: Optional[int]
    #: Zorunlu.
    first_seen_at: str
    #: Zorunlu.
    last_seen_at: str
    #: Zorunlu.
    count_30d: int
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str
    #: Zorunlu.
    daily: List["EventDefinitionDetailDailyItem"]
    #: Zorunlu.
    properties: List["EventDefinitionDetailPropertiesItem"]


class EventDefinitionDetailDailyItem(TypedDict, total=False):
    """EventDefinitionDetailDailyItem şeması."""

    #: Zorunlu.
    date: str
    #: Zorunlu.
    count: int
    #: Zorunlu.
    users: int


class EventDefinitionDetailPropertiesItem(TypedDict, total=False):
    """EventDefinitionDetailPropertiesItem şeması."""

    #: Zorunlu.
    key: str
    #: Zorunlu.
    type: str
    #: Zorunlu.
    values: List["EventDefinitionDetailPropertiesItemValuesItem"]


class EventDefinitionDetailPropertiesItemValuesItem(TypedDict, total=False):
    """EventDefinitionDetailPropertiesItemValuesItem şeması."""

    #: Zorunlu.
    value: str
    #: Zorunlu.
    count: int


class EventDefinitionList(TypedDict, total=False):
    """EventDefinitionList şeması."""

    #: Zorunlu.
    data: List["EventDefinition"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class EventsAccepted(TypedDict, total=False):
    """EventsAccepted şeması."""

    #: Zorunlu.
    accepted: int


EventsReport = TypedDict(
    "EventsReport",
    {
        # Zorunlu.
        "from": str,
        # Zorunlu.
        "to": str,
        # Zorunlu. Değerler: "day", "name".
        "group_by": str,
        # Zorunlu.
        "name": Optional[str],
        # Zorunlu.
        "totals": "EventsReportTotals",
        # Zorunlu.
        "previous": Optional["EventsReportPrevious"],
        # Zorunlu.
        "rows": List["EventsReportRowsItem"],
    },
    total=False,
)


class EventsReportPrevious(TypedDict, total=False):
    """EventsReportPrevious şeması."""

    #: Zorunlu.
    count: int
    #: Zorunlu.
    users: int


class EventsReportRowsItem(TypedDict, total=False):
    """EventsReportRowsItem şeması."""

    #: Zorunlu.
    key: str
    #: Zorunlu.
    count: int
    #: Zorunlu.
    users: int


class EventsReportTotals(TypedDict, total=False):
    """EventsReportTotals şeması."""

    #: Zorunlu.
    count: int
    #: Zorunlu.
    users: int


class Export(TypedDict, total=False):
    """Export şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu. Değerler: "users", "subscriptions", "events", "deliveries", "message_events".
    type: str
    #: Zorunlu.
    filters: "ExportFilters"
    #: Zorunlu. Değerler: "pending", "running", "completed", "failed".
    status: str
    #: Zorunlu.
    row_count: Optional[int]
    #: Zorunlu.
    error: Optional[str]
    #: Zorunlu.
    download_url: Optional[str]
    #: Zorunlu.
    expires_at: Optional[str]
    #: Zorunlu.
    requested_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    completed_at: Optional[str]


ExportFilters = TypedDict(
    "ExportFilters",
    {
        "from": str,
        "to": str,
        "name": str,
        "message_id": str,
        "campaign_id": str,
        "status": str,
        # Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
        "channel": str,
        "segment_id": str,
    },
    total=False,
)


class ExportList(TypedDict, total=False):
    """ExportList şeması."""

    #: Zorunlu.
    data: List["Export"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


FunnelBodyDto = TypedDict(
    "FunnelBodyDto",
    {
        # Zorunlu.
        "steps": List["FunnelBodyDtoStepsItem"],
        "from": str,
        "to": str,
        "window_hours": int,
        "compare": bool,
        # Değerler: "json", "csv".
        "format": str,
    },
    total=False,
)


class FunnelBodyDtoStepsItem(TypedDict, total=False):
    """FunnelBodyDtoStepsItem şeması."""

    #: Zorunlu.
    name: str
    where: "FunnelBodyDtoStepsItemWhere"


class FunnelBodyDtoStepsItemWhere(TypedDict, total=False):
    """FunnelBodyDtoStepsItemWhere şeması."""

    #: Zorunlu.
    key: str
    #: Zorunlu.
    value: str


FunnelReport = TypedDict(
    "FunnelReport",
    {
        # Zorunlu.
        "from": str,
        # Zorunlu.
        "to": str,
        # Zorunlu.
        "window_hours": int,
        # Zorunlu.
        "steps": List["FunnelReportStepsItem"],
        # Zorunlu.
        "overall_rate": Optional[float],
        # Zorunlu.
        "previous": Optional["FunnelReportPrevious"],
    },
    total=False,
)


class FunnelReportPrevious(TypedDict, total=False):
    """FunnelReportPrevious şeması."""

    #: Zorunlu.
    steps: List[int]
    #: Zorunlu.
    overall_rate: Optional[float]


class FunnelReportStepsItem(TypedDict, total=False):
    """FunnelReportStepsItem şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu.
    users: int
    #: Zorunlu.
    conversion_rate: Optional[float]
    #: Zorunlu.
    drop_off: int


class IdentityKey(TypedDict, total=False):
    """IdentityKey şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    kid: str
    #: Zorunlu. Değerler: "ES256".
    alg: str
    #: Zorunlu.
    public_jwk: Dict[str, str]
    #: Zorunlu.
    label: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    revoked_at: Optional[str]


class IdentityKeyList(TypedDict, total=False):
    """IdentityKeyList şeması."""

    #: Zorunlu.
    data: List["IdentityKey"]


class Import(TypedDict, total=False):
    """Import şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu. Değerler: "eski sağlayıcı_players", "csv_users".
    type: str
    #: Zorunlu.
    file_name: Optional[str]
    #: Zorunlu. Değerler: "pending", "running", "completed", "failed".
    status: str
    #: Zorunlu.
    stats: "ImportStats"
    #: Zorunlu.
    error: Optional[str]
    #: Zorunlu.
    error_report_url: Optional[str]
    #: Zorunlu.
    requested_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    completed_at: Optional[str]


class ImportList(TypedDict, total=False):
    """ImportList şeması."""

    #: Zorunlu.
    data: List["Import"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class ImportStats(TypedDict, total=False):
    """ImportStats şeması."""

    processed: int
    created_users: int
    updated_users: int
    created_subscriptions: int
    skipped: int
    errors: int


class InAppMessage(TypedDict, total=False):
    """InAppMessage şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu. Değerler: "draft", "active", "paused", "archived".
    status: str
    #: Zorunlu.
    priority: int
    #: Zorunlu.
    triggers: List[Any]
    #: Zorunlu.
    trigger_groups: Optional[List[List[Any]]]
    #: Zorunlu.
    variants: List["InAppMessageVariantsItem"]
    #: Zorunlu.
    display: "InAppMessageDisplay"
    #: Zorunlu.
    audience: "InAppMessageAudience"
    #: Zorunlu.
    frequency: "InAppMessageFrequency"
    #: Zorunlu.
    journey_only: bool
    #: Zorunlu.
    start_at: Optional[str]
    #: Zorunlu.
    end_at: Optional[str]
    #: Zorunlu.
    stats: "InAppMessageStats"
    #: Zorunlu.
    variant_stats: List["InAppMessageVariantStatsItem"]
    #: Zorunlu.
    ab_test: "InAppMessageAbTest"
    #: Zorunlu.
    variant_significance: Optional["InAppMessageVariantSignificance"]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class InAppMessageAbTest(TypedDict, total=False):
    """InAppMessageAbTest şeması."""

    winner: "InAppMessageAbTestWinner"
    #: Zorunlu.
    winner_variant_id: Optional[str]
    #: Zorunlu.
    decided_at: Optional[str]
    #: Zorunlu.
    decided_by: Optional[str]


class InAppMessageAbTestWinner(TypedDict, total=False):
    """InAppMessageAbTestWinner şeması."""

    #: Zorunlu. Değerler: "manual", "auto".
    mode: str
    min_impressions: int
    confidence: float


class InAppMessageAudience(TypedDict, total=False):
    """InAppMessageAudience şeması."""

    included_segments: List[str]
    excluded_segments: List[str]


class InAppMessageDisplay(TypedDict, total=False):
    """InAppMessageDisplay şeması."""

    #: Zorunlu. Değerler: "modal", "banner_top", "banner_bottom", "fullscreen".
    layout: str
    background_color: str
    text_color: str
    dismissible: bool
    auto_dismiss_seconds: int
    #: Değerler: "blocks", "html".
    content_type: str
    html: Dict[str, str]
    html_height: int
    #: Zorunlu.
    blocks: List[Any]


class InAppMessageFrequency(TypedDict, total=False):
    """InAppMessageFrequency şeması."""

    max_impressions: int
    min_interval_seconds: int
    stop_after_interaction: bool


class InAppMessagePage(TypedDict, total=False):
    """InAppMessagePage şeması."""

    #: Zorunlu.
    data: List["InAppMessage"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class InAppMessageStats(TypedDict, total=False):
    """InAppMessageStats şeması."""

    #: Zorunlu.
    impressions: int
    #: Zorunlu.
    clicks: int
    #: Zorunlu.
    dismissals: int
    #: Zorunlu.
    unique_users: int
    #: Zorunlu.
    ctr: float


class InAppMessageVariantSignificance(TypedDict, total=False):
    """InAppMessageVariantSignificance şeması."""

    #: Zorunlu.
    leader: Optional[str]
    #: Zorunlu.
    p_value: float
    #: Zorunlu.
    significant: bool


class InAppMessageVariantsItem(TypedDict, total=False):
    """InAppMessageVariantsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    #: Zorunlu.
    display: "InAppMessageVariantsItemDisplay"


class InAppMessageVariantsItemDisplay(TypedDict, total=False):
    """InAppMessageVariantsItemDisplay şeması."""

    #: Zorunlu. Değerler: "modal", "banner_top", "banner_bottom", "fullscreen".
    layout: str
    background_color: str
    text_color: str
    dismissible: bool
    auto_dismiss_seconds: int
    #: Değerler: "blocks", "html".
    content_type: str
    html: Dict[str, str]
    html_height: int
    #: Zorunlu.
    blocks: List[Any]


class InAppMessageVariantStatsItem(TypedDict, total=False):
    """InAppMessageVariantStatsItem şeması."""

    #: Zorunlu.
    variant_id: str
    #: Zorunlu.
    impressions: int
    #: Zorunlu.
    clicks: int
    #: Zorunlu.
    ctr: float


class InAppStatusDto(TypedDict, total=False):
    """InAppStatusDto şeması."""

    #: Zorunlu. Değerler: "draft", "active", "paused", "archived".
    status: str


class InAppWinnerDto(TypedDict, total=False):
    """InAppWinnerDto şeması."""

    #: Zorunlu.
    variant_id: str


class InboxItem(TypedDict, total=False):
    """InboxItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    message_id: Optional[str]
    #: Zorunlu.
    title: Optional[str]
    #: Zorunlu.
    body: Optional[str]
    #: Zorunlu.
    url: Optional[str]
    #: Zorunlu.
    image_url: Optional[str]
    #: Zorunlu.
    data: Dict[str, str]
    #: Zorunlu.
    read: bool
    #: Zorunlu.
    read_at: Optional[str]
    #: Zorunlu.
    archived_at: Optional[str]
    #: Zorunlu.
    expires_at: Optional[str]
    #: Zorunlu.
    created_at: str


class InboxPage(TypedDict, total=False):
    """InboxPage şeması."""

    #: Zorunlu.
    data: List["InboxItem"]
    #: Zorunlu.
    unread_count: int
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class InboxReadAllResult(TypedDict, total=False):
    """InboxReadAllResult şeması."""

    #: Zorunlu.
    updated: int
    #: Zorunlu.
    unread_count: int


class IntegrationOk(TypedDict, total=False):
    """IntegrationOk şeması."""

    #: Zorunlu.
    ok: bool


class Journey(TypedDict, total=False):
    """Journey şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu. Değerler: "draft", "active", "paused", "archived".
    status: str
    #: Zorunlu.
    current_version: Optional[int]
    #: Zorunlu.
    draft_version: Optional[int]
    #: Zorunlu.
    trigger_kind: Optional[str]
    #: Zorunlu.
    published_at: Optional[str]
    #: Zorunlu.
    created_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str
    #: Zorunlu.
    summary: "JourneySummary"


class JourneyDetail(TypedDict, total=False):
    """JourneyDetail şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu. Değerler: "draft", "active", "paused", "archived".
    status: str
    #: Zorunlu.
    current_version: Optional[int]
    #: Zorunlu.
    draft_version: Optional[int]
    #: Zorunlu.
    trigger_kind: Optional[str]
    #: Zorunlu.
    published_at: Optional[str]
    #: Zorunlu.
    created_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str
    #: Zorunlu.
    summary: "JourneyDetailSummary"
    #: Zorunlu.
    editing: "JourneyDetailEditing"
    #: Zorunlu.
    issues: List["JourneyDetailIssuesItem"]


class JourneyDetailEditing(TypedDict, total=False):
    """JourneyDetailEditing şeması."""

    #: Zorunlu.
    version: int
    #: Zorunlu.
    graph: Dict[str, Any]
    #: Zorunlu.
    settings: Dict[str, Any]
    #: Zorunlu.
    published_at: Optional[str]
    #: Zorunlu.
    published_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class JourneyDetailIssuesItem(TypedDict, total=False):
    """JourneyDetailIssuesItem şeması."""

    #: Zorunlu.
    code: str
    node_id: str
    edge_id: str
    #: Zorunlu.
    message: str


class JourneyDetailSummary(TypedDict, total=False):
    """JourneyDetailSummary şeması."""

    #: Zorunlu.
    runs_total: int
    #: Zorunlu.
    active: int
    #: Zorunlu.
    completed: int
    #: Zorunlu.
    exited: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    goal_reached: int


class JourneyPage(TypedDict, total=False):
    """JourneyPage şeması."""

    #: Zorunlu.
    data: List["Journey"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class JourneyPublishResult(TypedDict, total=False):
    """JourneyPublishResult şeması."""

    #: Zorunlu.
    journey: "Journey"
    #: Zorunlu.
    version: int
    #: Zorunlu.
    issues: List["JourneyPublishResultIssuesItem"]


class JourneyPublishResultIssuesItem(TypedDict, total=False):
    """JourneyPublishResultIssuesItem şeması."""

    #: Zorunlu.
    code: str
    node_id: str
    edge_id: str
    #: Zorunlu.
    message: str


class JourneyRun(TypedDict, total=False):
    """JourneyRun şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    journey_id: str
    #: Zorunlu.
    version: int
    #: Zorunlu.
    user_id: str
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu. Değerler: "active", "waiting", "completed", "exited", "failed".
    status: str
    #: Zorunlu.
    current_node_id: Optional[str]
    #: Zorunlu.
    next_action_at: Optional[str]
    #: Zorunlu.
    entered_at: str
    #: Zorunlu.
    completed_at: Optional[str]
    #: Zorunlu.
    exit_reason: Optional[str]
    #: Zorunlu.
    goal_id: Optional[str]
    #: Zorunlu.
    goal_reached_at: Optional[str]
    #: Zorunlu.
    context: Dict[str, Any]


class JourneyRunDetail(TypedDict, total=False):
    """JourneyRunDetail şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    journey_id: str
    #: Zorunlu.
    version: int
    #: Zorunlu.
    user_id: str
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu. Değerler: "active", "waiting", "completed", "exited", "failed".
    status: str
    #: Zorunlu.
    current_node_id: Optional[str]
    #: Zorunlu.
    next_action_at: Optional[str]
    #: Zorunlu.
    entered_at: str
    #: Zorunlu.
    completed_at: Optional[str]
    #: Zorunlu.
    exit_reason: Optional[str]
    #: Zorunlu.
    goal_id: Optional[str]
    #: Zorunlu.
    goal_reached_at: Optional[str]
    #: Zorunlu.
    context: Dict[str, Any]
    #: Zorunlu.
    journey_name: str
    #: Zorunlu.
    steps: List["JourneyRunDetailStepsItem"]


class JourneyRunDetailStepsItem(TypedDict, total=False):
    """JourneyRunDetailStepsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    node_id: str
    #: Zorunlu.
    node_type: str
    #: Zorunlu. Değerler: "completed", "waiting", "failed", "skipped".
    status: str
    #: Zorunlu.
    branch: Optional[str]
    #: Zorunlu.
    result: Dict[str, Any]
    #: Zorunlu.
    started_at: str
    #: Zorunlu.
    finished_at: Optional[str]


class JourneyRunPage(TypedDict, total=False):
    """JourneyRunPage şeması."""

    #: Zorunlu.
    data: List["JourneyRun"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class JourneysCreateBody(TypedDict, total=False):
    """JourneysCreateBody şeması."""

    #: Zorunlu.
    name: str
    description: str
    #: React Flow uyumlu journey grafı: { nodes: [{ id, type, position, data }], edges: [{ id, source, target, sourceHandle }] } (docs/journeys.md)
    graph: "JourneysCreateBodyGraph"
    #: Yeniden giriş, yalnızca yeni girenler, çıkış kuralları, çıkış tag'leri, hedefler, takvim (docs/journeys.md)
    settings: Dict[str, Any]


class JourneysCreateBodyGraph(TypedDict, total=False):
    """React Flow uyumlu journey grafı: { nodes: [{ id, type, position, data }], edges: [{ id, source, target, sourceHandle }] } (docs/journeys.md)"""

    #: Zorunlu.
    nodes: List[Dict[str, Any]]
    #: Zorunlu.
    edges: List[Dict[str, Any]]


class JourneysSaveDraftBody(TypedDict, total=False):
    """JourneysSaveDraftBody şeması."""

    #: Zorunlu. React Flow uyumlu journey grafı: { nodes: [{ id, type, position, data }], edges: [{ id, source, target, sourceHandle }] } (docs/journeys.md)
    graph: "JourneysSaveDraftBodyGraph"
    #: Yeniden giriş, yalnızca yeni girenler, çıkış kuralları, çıkış tag'leri, hedefler, takvim (docs/journeys.md)
    settings: Dict[str, Any]


class JourneysSaveDraftBodyGraph(TypedDict, total=False):
    """React Flow uyumlu journey grafı: { nodes: [{ id, type, position, data }], edges: [{ id, source, target, sourceHandle }] } (docs/journeys.md)"""

    #: Zorunlu.
    nodes: List[Dict[str, Any]]
    #: Zorunlu.
    edges: List[Dict[str, Any]]


class JourneyStats(TypedDict, total=False):
    """JourneyStats şeması."""

    #: Zorunlu.
    version: Optional[int]
    #: Zorunlu.
    summary: "JourneyStatsSummary"
    #: Zorunlu.
    nodes: List["JourneyStatsNodesItem"]
    #: Zorunlu.
    goals: List["JourneyStatsGoalsItem"]
    #: Zorunlu.
    exit_reasons: Dict[str, int]


class JourneyStatsGoalsItem(TypedDict, total=False):
    """JourneyStatsGoalsItem şeması."""

    #: Zorunlu.
    goal_id: str
    #: Zorunlu.
    reached: int


class JourneyStatsNodesItem(TypedDict, total=False):
    """JourneyStatsNodesItem şeması."""

    #: Zorunlu.
    node_id: str
    #: Zorunlu.
    node_type: str
    #: Zorunlu.
    entered: int
    #: Zorunlu.
    completed: int
    #: Zorunlu.
    waiting_now: int
    #: Zorunlu.
    skipped: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    branches: Dict[str, int]
    messages: Dict[str, int]
    variants: List["JourneyStatsNodesItemVariantsItem"]


class JourneyStatsNodesItemVariantsItem(TypedDict, total=False):
    """JourneyStatsNodesItemVariantsItem şeması."""

    #: Zorunlu.
    variant_id: str
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int
    #: Zorunlu.
    converted: int
    #: Zorunlu.
    winner: bool


class JourneyStatsSummary(TypedDict, total=False):
    """JourneyStatsSummary şeması."""

    #: Zorunlu.
    runs_total: int
    #: Zorunlu.
    active: int
    #: Zorunlu.
    completed: int
    #: Zorunlu.
    exited: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    goal_reached: int
    #: Zorunlu.
    waiting: int
    #: Zorunlu.
    goal_conversion_rate: float


class JourneySummary(TypedDict, total=False):
    """JourneySummary şeması."""

    #: Zorunlu.
    runs_total: int
    #: Zorunlu.
    active: int
    #: Zorunlu.
    completed: int
    #: Zorunlu.
    exited: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    goal_reached: int


class JourneyTriggerResult(TypedDict, total=False):
    """JourneyTriggerResult şeması."""

    #: Zorunlu.
    entered: bool
    #: Zorunlu.
    run: Optional["JourneyRun"]
    #: Zorunlu. Değerler: "inactive", "outside_schedule", "re_entry", "already_active", "unknown_user".
    reason: Optional[str]


class JourneyVersionList(TypedDict, total=False):
    """JourneyVersionList şeması."""

    #: Zorunlu.
    data: List["JourneyVersionListDataItem"]


class JourneyVersionListDataItem(TypedDict, total=False):
    """JourneyVersionListDataItem şeması."""

    #: Zorunlu.
    version: int
    #: Zorunlu.
    graph: Dict[str, Any]
    #: Zorunlu.
    settings: Dict[str, Any]
    #: Zorunlu.
    published_at: Optional[str]
    #: Zorunlu.
    published_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class LiveActivitySendResult(TypedDict, total=False):
    """LiveActivitySendResult şeması."""

    #: Zorunlu.
    message_id: str
    #: Zorunlu.
    activity_id: str
    #: Zorunlu. Değerler: "start", "update", "end".
    event: str
    #: Zorunlu.
    recipients_estimate: int


class LiveActivityTokenResult(TypedDict, total=False):
    """LiveActivityTokenResult şeması."""

    #: Zorunlu.
    ok: bool


class LiveActivityType(TypedDict, total=False):
    """LiveActivityType şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu.
    content_state_schema: "LiveActivityTypeContentStateSchema"
    #: Zorunlu.
    attributes_schema: "LiveActivityTypeAttributesSchema"
    #: Zorunlu.
    push_to_start_tokens: int
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class LiveActivityTypeAttributesSchema(TypedDict, total=False):
    """LiveActivityTypeAttributesSchema şeması."""

    #: Zorunlu. Değerler: "object".
    type: str
    #: Zorunlu.
    properties: Dict[str, "LiveActivityTypeAttributesSchemaPropertiesValue"]
    required: List[str]


class LiveActivityTypeAttributesSchemaPropertiesValue(TypedDict, total=False):
    """LiveActivityTypeAttributesSchemaPropertiesValue şeması."""

    #: Zorunlu. Değerler: "string", "number", "integer", "boolean".
    type: str
    enum: List[Any]
    maxLength: int
    minimum: float
    maximum: float
    description: str


class LiveActivityTypeContentStateSchema(TypedDict, total=False):
    """LiveActivityTypeContentStateSchema şeması."""

    #: Zorunlu. Değerler: "object".
    type: str
    #: Zorunlu.
    properties: Dict[str, "LiveActivityTypeContentStateSchemaPropertiesValue"]
    required: List[str]


class LiveActivityTypeContentStateSchemaPropertiesValue(TypedDict, total=False):
    """LiveActivityTypeContentStateSchemaPropertiesValue şeması."""

    #: Zorunlu. Değerler: "string", "number", "integer", "boolean".
    type: str
    enum: List[Any]
    maxLength: int
    minimum: float
    maximum: float
    description: str


class LiveActivityTypeList(TypedDict, total=False):
    """LiveActivityTypeList şeması."""

    #: Zorunlu.
    data: List["LiveActivityType"]


class McpCreateCampaignDraftBody(TypedDict, total=False):
    """McpCreateCampaignDraftBody şeması."""

    name: str
    #: Değerler: "one_time", "scheduled", "recurring".
    type: str
    audience: "McpCreateCampaignDraftBodyAudience"
    #: messages.content ile aynı şema (headings, contents, url, buttons…)
    content: Dict[str, Any]
    labels: List[str]
    #: Tercih kategorisi anahtarı; kapalı kullanıcılar bastırılır
    category: Optional[str]
    ab_test: "McpCreateCampaignDraftBodyAbTest"
    #: A/B varyantları (ağırlıklar toplamı 100; en fazla bir is_control)
    variants: List["McpCreateCampaignDraftBodyVariantsItem"]
    template_id: str
    template_version: int
    delivery: "McpCreateCampaignDraftBodyDelivery"
    recurrence: Optional["McpCreateCampaignDraftBodyRecurrence"]
    send_at: Optional[str]


class McpCreateCampaignDraftBodyAbTest(TypedDict, total=False):
    """McpCreateCampaignDraftBodyAbTest şeması."""

    enabled: bool
    test_percentage: int
    winner: "McpCreateCampaignDraftBodyAbTestWinner"


class McpCreateCampaignDraftBodyAbTestWinner(TypedDict, total=False):
    """McpCreateCampaignDraftBodyAbTestWinner şeması."""

    #: Değerler: "manual", "auto".
    mode: str
    #: Değerler: "open_rate", "click_rate", "conversion_rate".
    metric: str
    evaluate_after_minutes: int


class McpCreateCampaignDraftBodyAudience(TypedDict, total=False):
    """McpCreateCampaignDraftBodyAudience şeması."""

    all: bool
    segments: List[str]
    exclude_segments: List[str]
    #: Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7).
    filters: "McpCreateCampaignDraftBodyAudienceFilters"
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]
    test_devices_only: bool


class McpCreateCampaignDraftBodyAudienceFilters(TypedDict, total=False):
    """Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7)."""

    all: List[Dict[str, Any]]
    any: List[Dict[str, Any]]
    none: List[Dict[str, Any]]


class McpCreateCampaignDraftBodyDelivery(TypedDict, total=False):
    """McpCreateCampaignDraftBodyDelivery şeması."""

    #: Değerler: "immediate", "per_user_timezone", "optimized".
    timezone_mode: str
    delivery_time_of_day: str
    throttle_per_minute: int
    ttl: int
    #: Değerler: 5, 10.
    priority: int
    collapse_id: str
    frequency_cap_exempt: bool
    quiet_hours_exempt: bool
    one_per_user: bool


class McpCreateCampaignDraftBodyRecurrence(TypedDict, total=False):
    """McpCreateCampaignDraftBodyRecurrence şeması."""

    cron: str
    until: Optional[str]
    timezone: str


class McpCreateCampaignDraftBodyVariantsItem(TypedDict, total=False):
    """McpCreateCampaignDraftBodyVariantsItem şeması."""

    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    content: Optional[Dict[str, Any]]
    is_control: bool


class McpCreateSegmentDraftBody(TypedDict, total=False):
    """McpCreateSegmentDraftBody şeması."""

    #: Zorunlu.
    name: str
    description: Optional[str]
    #: Zorunlu. Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7).
    definition: "McpCreateSegmentDraftBodyDefinition"
    is_dynamic: bool


class McpCreateSegmentDraftBodyDefinition(TypedDict, total=False):
    """Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7)."""

    all: List[Dict[str, Any]]
    any: List[Dict[str, Any]]
    none: List[Dict[str, Any]]


class Member(TypedDict, total=False):
    """Member şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    account_id: str
    #: Zorunlu.
    email: str
    #: Zorunlu.
    name: str
    #: Zorunlu. Değerler: "owner", "admin", "developer", "marketer", "analyst", "billing", "viewer", "composer".
    role: str
    #: Zorunlu.
    app_scopes: List[str]
    #: Zorunlu.
    accepted_at: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    last_login_at: Optional[str]


class MemberList(TypedDict, total=False):
    """MemberList şeması."""

    #: Zorunlu.
    data: List["Member"]


class Message(TypedDict, total=False):
    """Message şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu. Değerler: "campaign", "api", "journey", "test".
    source: str
    #: Zorunlu. Değerler: "queued", "processing", "completed", "cancelled", "failed".
    status: str
    #: Zorunlu.
    idempotency_key: Optional[str]
    #: Zorunlu.
    name: Optional[str]
    #: Zorunlu.
    content: Dict[str, Any]
    #: Zorunlu.
    target: Dict[str, Any]
    #: Zorunlu.
    options: Dict[str, Any]
    #: Zorunlu.
    labels: List[str]
    #: Zorunlu.
    category: Optional[str]
    #: Zorunlu.
    template_id: Optional[str]
    #: Zorunlu.
    campaign_id: Optional[str]
    #: Zorunlu.
    variants: Optional[List["MessageVariantsItem"]]
    #: Zorunlu.
    counts: "MessageCounts"
    #: Zorunlu.
    requested_by: "MessageRequestedBy"
    #: Zorunlu.
    error: Optional[str]
    #: Zorunlu.
    scheduled_for: Optional[str]
    #: Zorunlu.
    started_at: Optional[str]
    #: Zorunlu.
    completed_at: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class MessageCategory(TypedDict, total=False):
    """MessageCategory şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    key: str
    #: Zorunlu.
    name: Dict[str, str]
    #: Zorunlu.
    description: Dict[str, str]
    #: Zorunlu.
    channels: Optional[List[str]]
    #: Zorunlu.
    default_opted_in: bool
    #: Zorunlu.
    position: int
    #: Zorunlu.
    opted_out_users: int
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class MessageCategoryList(TypedDict, total=False):
    """MessageCategoryList şeması."""

    #: Zorunlu.
    data: List["MessageCategory"]


class MessageCounts(TypedDict, total=False):
    """MessageCounts şeması."""

    targeted: int
    suppressed: int
    sent: int
    delivered: int
    failed: int
    errored: int
    expired: int
    opened: int
    clicked: int
    converted: int
    bounced: int
    complained: int
    unsubscribed: int
    sms_segments: int


class MessageList(TypedDict, total=False):
    """MessageList şeması."""

    #: Zorunlu.
    data: List["Message"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class MessageRequestedBy(TypedDict, total=False):
    """MessageRequestedBy şeması."""

    #: Zorunlu. Değerler: "api_key", "account", "system".
    type: str
    id: str


MessagesReport = TypedDict(
    "MessagesReport",
    {
        # Zorunlu.
        "from": str,
        # Zorunlu.
        "to": str,
        # Zorunlu. Değerler: "day", "channel", "campaign".
        "group_by": str,
        # Zorunlu.
        "totals": "MessagesReportTotals",
        # Zorunlu.
        "previous": Optional["MessagesReportPrevious"],
        # Zorunlu.
        "rows": List["MessagesReportRowsItem"],
    },
    total=False,
)


class MessagesReportPrevious(TypedDict, total=False):
    """MessagesReportPrevious şeması."""

    #: Zorunlu.
    sent: int
    #: Zorunlu.
    delivered: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int
    #: Zorunlu.
    converted: int
    #: Zorunlu.
    delivery_rate: Optional[float]
    #: Zorunlu.
    open_rate: Optional[float]
    #: Zorunlu.
    click_rate: Optional[float]


class MessagesReportRowsItem(TypedDict, total=False):
    """MessagesReportRowsItem şeması."""

    #: Zorunlu.
    key: str
    #: Zorunlu.
    label: str
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    delivered: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int
    #: Zorunlu.
    converted: int


class MessagesReportTotals(TypedDict, total=False):
    """MessagesReportTotals şeması."""

    #: Zorunlu.
    sent: int
    #: Zorunlu.
    delivered: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int
    #: Zorunlu.
    converted: int
    #: Zorunlu.
    delivery_rate: Optional[float]
    #: Zorunlu.
    open_rate: Optional[float]
    #: Zorunlu.
    click_rate: Optional[float]


class MessageVariantsItem(TypedDict, total=False):
    """MessageVariantsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    #: Zorunlu.
    is_control: bool


class Ok(TypedDict, total=False):
    """Ok şeması."""

    #: Zorunlu.
    ok: bool


class Org(TypedDict, total=False):
    """Org şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    slug: str
    #: Zorunlu.
    plan_code: str
    #: Zorunlu. Değerler: "active", "suspended", "deleted".
    status: str
    #: Zorunlu.
    settings: "OrgSettings"
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    region: Optional[str]
    #: Zorunlu.
    managed_by_reseller: bool


class OrgSettings(TypedDict, total=False):
    """OrgSettings şeması."""

    mfaRequired: bool
    ipAllowlist: List[str]
    retentionDays: int
    sessionMaxHours: int
    auditStream: "OrgSettingsAuditStream"


class OrgSettingsAuditStream(TypedDict, total=False):
    """OrgSettingsAuditStream şeması."""

    s3: bool
    webhookAppId: Optional[str]


OverviewStats = TypedDict(
    "OverviewStats",
    {
        # Zorunlu. Değerler: "7d", "30d", "custom".
        "range": str,
        # Zorunlu.
        "from": str,
        # Zorunlu.
        "to": str,
        # Zorunlu.
        "kpis": "OverviewStatsKpis",
        # Zorunlu.
        "series": List["OverviewStatsSeriesItem"],
        # Zorunlu.
        "recent_messages": List["Message"],
        # Zorunlu.
        "recent_campaigns": List["OverviewStatsRecentCampaignsItem"],
        # Zorunlu.
        "top_errors": List["OverviewStatsTopErrorsItem"],
        # Zorunlu.
        "channels": List["OverviewStatsChannelsItem"],
    },
    total=False,
)


class OverviewStatsChannelsItem(TypedDict, total=False):
    """OverviewStatsChannelsItem şeması."""

    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu. Değerler: "apns", "fcm", "hms", "webpush", "smtp", "ses", "resend", "twilio", "netgsm", "meta_whatsapp", "google_rbm", "mock".
    provider: Optional[str]
    #: Zorunlu. Değerler: "unconfigured", "active", "invalid", "suspended".
    status: str
    #: Zorunlu.
    last_error: Optional[str]
    #: Zorunlu.
    active_subscriptions: int


class OverviewStatsKpis(TypedDict, total=False):
    """OverviewStatsKpis şeması."""

    #: Zorunlu.
    sent: int
    #: Zorunlu.
    delivered: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int
    #: Zorunlu.
    delivery_rate: Optional[float]
    #: Zorunlu.
    open_rate: Optional[float]
    #: Zorunlu.
    click_rate: Optional[float]
    #: Zorunlu.
    active_subscriptions: int
    #: Zorunlu.
    new_subscriptions: int
    #: Zorunlu.
    opt_outs: int


class OverviewStatsRecentCampaignsItem(TypedDict, total=False):
    """OverviewStatsRecentCampaignsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    type: str
    #: Zorunlu.
    status: str
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int
    #: Zorunlu.
    updated_at: str


class OverviewStatsSeriesItem(TypedDict, total=False):
    """OverviewStatsSeriesItem şeması."""

    #: Zorunlu.
    date: str
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    delivered: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    opened: int


class OverviewStatsTopErrorsItem(TypedDict, total=False):
    """OverviewStatsTopErrorsItem şeması."""

    #: Zorunlu.
    code: str
    #: Zorunlu.
    count: int


class PatchEventDefinitionDto(TypedDict, total=False):
    """PatchEventDefinitionDto şeması."""

    display_name: Optional[str]
    is_conversion: bool
    outcome_unique: bool
    outcome_unattributed: bool
    retention_days: Optional[int]


class PatchSubscriptionDto(TypedDict, total=False):
    """PatchSubscriptionDto şeması."""

    token: str
    device: "PatchSubscriptionDtoDevice"
    #: Değerler: "subscribed", "unsubscribed".
    status: str
    test_device: bool
    test_device_name: str


class PatchSubscriptionDtoDevice(TypedDict, total=False):
    """PatchSubscriptionDtoDevice şeması."""

    model: str
    os: str
    os_version: str
    app_version: Optional[str]
    sdk_version: str
    sdk_platform: str
    carrier: str
    locale: str
    timezone: str
    push_capable: bool
    #: Değerler: "sandbox", "production".
    push_environment: str


class PatchUserDto(TypedDict, total=False):
    """PatchUserDto şeması."""

    properties: Dict[str, Any]
    tags: Dict[str, Optional[str]]
    deltas: "PatchUserDtoDeltas"


class PatchUserDtoDeltas(TypedDict, total=False):
    """PatchUserDtoDeltas şeması."""

    session_count: int
    session_time: int
    purchases: List["PatchUserDtoDeltasPurchasesItem"]


class PatchUserDtoDeltasPurchasesItem(TypedDict, total=False):
    """PatchUserDtoDeltasPurchasesItem şeması."""

    #: Zorunlu.
    sku: str
    #: Zorunlu.
    amount: float
    iso: str
    count: int


ProvidersReport = TypedDict(
    "ProvidersReport",
    {
        # Zorunlu.
        "from": str,
        # Zorunlu.
        "to": str,
        # Zorunlu.
        "totals": "ProvidersReportTotals",
        # Zorunlu.
        "previous": Optional["ProvidersReportPrevious"],
        # Zorunlu.
        "rows": List["ProvidersReportRowsItem"],
    },
    total=False,
)


class ProvidersReportPrevious(TypedDict, total=False):
    """ProvidersReportPrevious şeması."""

    #: Zorunlu.
    sent: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    failure_rate: Optional[float]


class ProvidersReportRowsItem(TypedDict, total=False):
    """ProvidersReportRowsItem şeması."""

    #: Zorunlu.
    channel: str
    #: Zorunlu.
    provider: Optional[str]
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    failure_rate: Optional[float]
    #: Zorunlu.
    latency_p50_ms: Optional[float]
    #: Zorunlu.
    latency_p95_ms: Optional[float]
    #: Zorunlu.
    errors: List["ProvidersReportRowsItemErrorsItem"]


class ProvidersReportRowsItemErrorsItem(TypedDict, total=False):
    """ProvidersReportRowsItemErrorsItem şeması."""

    #: Zorunlu.
    code: str
    #: Zorunlu.
    count: int


class ProvidersReportTotals(TypedDict, total=False):
    """ProvidersReportTotals şeması."""

    #: Zorunlu.
    sent: int
    #: Zorunlu.
    failed: int
    #: Zorunlu.
    failure_rate: Optional[float]


class RenderPreview(TypedDict, total=False):
    """RenderPreview şeması."""

    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu.
    language: str
    #: Zorunlu.
    title: Optional[str]
    #: Zorunlu.
    subtitle: Optional[str]
    #: Zorunlu.
    body: Optional[str]
    #: Zorunlu.
    url: Optional[str]
    #: Zorunlu.
    image_url: Optional[str]
    #: Zorunlu.
    icon_url: Optional[str]
    #: Zorunlu.
    buttons: List["RenderPreviewButtonsItem"]
    #: Zorunlu.
    data: Dict[str, str]
    #: Zorunlu.
    warnings: List[str]
    email: Optional["RenderPreviewEmail"]
    sms: Optional["RenderPreviewSms"]


class RenderPreviewButtonsItem(TypedDict, total=False):
    """RenderPreviewButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    #: Zorunlu.
    url: Optional[str]


class RenderPreviewEmail(TypedDict, total=False):
    """RenderPreviewEmail şeması."""

    #: Zorunlu.
    subject: str
    #: Zorunlu.
    preheader: Optional[str]
    #: Zorunlu.
    html: str
    #: Zorunlu.
    text: str


class RenderPreviewSms(TypedDict, total=False):
    """RenderPreviewSms şeması."""

    #: Zorunlu.
    body: str
    #: Zorunlu. Değerler: "gsm7", "gsm7_tr", "ucs2".
    encoding: str
    #: Zorunlu.
    characters: int
    #: Zorunlu.
    segments: int
    #: Zorunlu.
    per_segment: int
    #: Zorunlu.
    non_gsm_characters: List[str]
    #: Zorunlu.
    turkish_characters: List[str]


class RenderTemplateDto(TypedDict, total=False):
    """RenderTemplateDto şeması."""

    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: str
    language: str
    user: "RenderTemplateDtoUser"
    custom_data: Dict[str, Any]
    content: "RenderTemplateDtoContent"
    version: int


class RenderTemplateDtoContent(TypedDict, total=False):
    """RenderTemplateDtoContent şeması."""

    headings: Dict[str, str]
    contents: Dict[str, str]
    subtitle: Dict[str, str]
    url: str
    app_url: str
    data: Dict[str, str]
    buttons: List["RenderTemplateDtoContentButtonsItem"]
    big_picture: str
    ios_attachments: Dict[str, str]
    ios_sound: str
    #: Değerler: "None", "SetTo", "Increase".
    ios_badge_type: str
    ios_badge_count: int
    #: Değerler: "passive", "active", "time-sensitive", "critical".
    ios_interruption_level: str
    ios_category: str
    android_channel_id: str
    android_group: str
    android_sound: str
    chrome_web_icon: str
    chrome_web_image: str
    chrome_web_badge: str
    web_push_topic: str
    content_available: bool
    mutable_content: bool
    custom_data: Dict[str, Any]
    email_subject: str
    email_body: str
    email_mjml: str
    email_preheader: str
    email_from_name: str
    email_from_address: str
    email_reply_to_address: str
    disable_email_click_tracking: bool
    sms_from: str
    disable_sms_link_shortening: bool
    add_to_inbox: bool
    inbox_ttl: int
    thread_id: str
    ios_relevance_score: float
    target_content_identifier: str
    small_icon: str
    large_icon: str
    android_accent_color: str
    #: Değerler: 1, 0, -1.
    android_visibility: int
    web_buttons: List["RenderTemplateDtoContentWebButtonsItem"]
    require_interaction: bool
    sms_media_urls: List[str]
    whatsapp_template: "RenderTemplateDtoContentWhatsappTemplate"
    whatsapp_media: "RenderTemplateDtoContentWhatsappMedia"
    whatsapp_interactive: "RenderTemplateDtoContentWhatsappInteractive"
    rcs_card: "RenderTemplateDtoContentRcsCard"
    rcs_suggestions: List[Any]
    rcs_content_sid: str
    rcs_content_variables: Dict[str, str]
    rcs_fallback_text: Dict[str, str]


class RenderTemplateDtoContentButtonsItem(TypedDict, total=False):
    """RenderTemplateDtoContentButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class RenderTemplateDtoContentRcsCard(TypedDict, total=False):
    """RenderTemplateDtoContentRcsCard şeması."""

    title: Dict[str, str]
    description: Dict[str, str]
    media_url: str
    #: Değerler: "SHORT", "MEDIUM", "TALL".
    media_height: str
    #: Değerler: "VERTICAL", "HORIZONTAL".
    orientation: str


class RenderTemplateDtoContentWebButtonsItem(TypedDict, total=False):
    """RenderTemplateDtoContentWebButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class RenderTemplateDtoContentWhatsappInteractive(TypedDict, total=False):
    """RenderTemplateDtoContentWhatsappInteractive şeması."""

    #: Zorunlu. Değerler: "button", "list".
    type: str
    header: str
    footer: str
    buttons: List["RenderTemplateDtoContentWhatsappInteractiveButtonsItem"]
    list: "RenderTemplateDtoContentWhatsappInteractiveList"


class RenderTemplateDtoContentWhatsappInteractiveButtonsItem(TypedDict, total=False):
    """RenderTemplateDtoContentWhatsappInteractiveButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str


class RenderTemplateDtoContentWhatsappInteractiveList(TypedDict, total=False):
    """RenderTemplateDtoContentWhatsappInteractiveList şeması."""

    #: Zorunlu.
    button: str
    #: Zorunlu.
    sections: List["RenderTemplateDtoContentWhatsappInteractiveListSectionsItem"]


class RenderTemplateDtoContentWhatsappInteractiveListSectionsItem(TypedDict, total=False):
    """RenderTemplateDtoContentWhatsappInteractiveListSectionsItem şeması."""

    title: str
    #: Zorunlu.
    rows: List["RenderTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem"]


class RenderTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem(TypedDict, total=False):
    """RenderTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str
    description: str


class RenderTemplateDtoContentWhatsappMedia(TypedDict, total=False):
    """RenderTemplateDtoContentWhatsappMedia şeması."""

    #: Zorunlu. Değerler: "image", "video", "document", "audio".
    type: str
    #: Zorunlu.
    url: str
    filename: str


class RenderTemplateDtoContentWhatsappTemplate(TypedDict, total=False):
    """RenderTemplateDtoContentWhatsappTemplate şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu.
    language: str
    header: Any
    body_params: List[str]
    button_params: List["RenderTemplateDtoContentWhatsappTemplateButtonParamsItem"]


class RenderTemplateDtoContentWhatsappTemplateButtonParamsItem(TypedDict, total=False):
    """RenderTemplateDtoContentWhatsappTemplateButtonParamsItem şeması."""

    #: Zorunlu.
    index: int
    #: Zorunlu. Değerler: "url", "quick_reply", "copy_code".
    sub_type: str
    #: Zorunlu.
    value: str


class RenderTemplateDtoUser(TypedDict, total=False):
    """RenderTemplateDtoUser şeması."""

    external_id: str
    tags: Dict[str, str]
    properties: Dict[str, Any]


class RetentionReport(TypedDict, total=False):
    """RetentionReport şeması."""

    #: Zorunlu.
    weeks: int
    #: Zorunlu.
    cohorts: List["RetentionReportCohortsItem"]
    #: Zorunlu.
    average: List[Optional[float]]


class RetentionReportCohortsItem(TypedDict, total=False):
    """RetentionReportCohortsItem şeması."""

    #: Zorunlu.
    week: str
    #: Zorunlu.
    users: int
    #: Zorunlu.
    retention: List[Optional[float]]


class ScheduleCampaignDto(TypedDict, total=False):
    """ScheduleCampaignDto şeması."""

    send_at: str
    recurrence: "ScheduleCampaignDtoRecurrence"


class ScheduleCampaignDtoRecurrence(TypedDict, total=False):
    """ScheduleCampaignDtoRecurrence şeması."""

    #: Zorunlu.
    cron: str
    until: Optional[str]
    timezone: str


class Segment(TypedDict, total=False):
    """Segment şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu.
    definition: Dict[str, Any]
    #: Zorunlu.
    is_dynamic: bool
    #: Zorunlu.
    estimated_count: Optional[int]
    #: Zorunlu.
    estimated_at: Optional[str]
    #: Zorunlu.
    created_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class SegmentCampaigns(TypedDict, total=False):
    """SegmentCampaigns şeması."""

    #: Zorunlu.
    data: List["SegmentCampaignsDataItem"]


class SegmentCampaignsDataItem(TypedDict, total=False):
    """SegmentCampaignsDataItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    status: str
    #: Zorunlu.
    type: str
    #: Zorunlu. Değerler: "include", "exclude".
    usage: str
    #: Zorunlu.
    created_at: str


class SegmentEstimate(TypedDict, total=False):
    """SegmentEstimate şeması."""

    #: Zorunlu.
    segment_id: Optional[str]
    #: Zorunlu.
    subscriptions: int
    #: Zorunlu.
    users: int
    #: Zorunlu.
    estimated_at: str
    #: Zorunlu.
    cached: bool
    #: Zorunlu.
    sampled: bool


class SegmentPage(TypedDict, total=False):
    """SegmentPage şeması."""

    #: Zorunlu.
    data: List["Segment"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class SegmentPreview(TypedDict, total=False):
    """SegmentPreview şeması."""

    #: Zorunlu.
    subscriptions: int
    #: Zorunlu.
    users: int
    #: Zorunlu.
    sampled: bool
    #: Zorunlu.
    sample: List["SegmentPreviewSampleItem"]


class SegmentPreviewSampleItem(TypedDict, total=False):
    """SegmentPreviewSampleItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu.
    tags: Dict[str, str]
    #: Zorunlu.
    last_active_at: str


class SegmentsCreateBody(TypedDict, total=False):
    """SegmentsCreateBody şeması."""

    #: Zorunlu.
    name: str
    description: Optional[str]
    #: Zorunlu. Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7).
    definition: "SegmentsCreateBodyDefinition"
    is_dynamic: bool


class SegmentsCreateBodyDefinition(TypedDict, total=False):
    """Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7)."""

    all: List[Dict[str, Any]]
    any: List[Dict[str, Any]]
    none: List[Dict[str, Any]]


class SegmentsPreviewBody(TypedDict, total=False):
    """SegmentsPreviewBody şeması."""

    #: Zorunlu. Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7).
    definition: "SegmentsPreviewBodyDefinition"
    limit: int


class SegmentsPreviewBodyDefinition(TypedDict, total=False):
    """Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7)."""

    all: List[Dict[str, Any]]
    any: List[Dict[str, Any]]
    none: List[Dict[str, Any]]


class SegmentsUpdateBody(TypedDict, total=False):
    """SegmentsUpdateBody şeması."""

    name: str
    description: Optional[str]
    #: Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7).
    definition: "SegmentsUpdateBodyDefinition"
    is_dynamic: bool


class SegmentsUpdateBodyDefinition(TypedDict, total=False):
    """Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7)."""

    all: List[Dict[str, Any]]
    any: List[Dict[str, Any]]
    none: List[Dict[str, Any]]


class SelectWinnerDto(TypedDict, total=False):
    """SelectWinnerDto şeması."""

    #: Zorunlu.
    variant_id: str


class SetOwnerDto(TypedDict, total=False):
    """SetOwnerDto şeması."""

    #: Zorunlu.
    external_id: str


class SetPreferencesDto(TypedDict, total=False):
    """SetPreferencesDto şeması."""

    #: Zorunlu.
    preferences: List["SetPreferencesDtoPreferencesItem"]


class SetPreferencesDtoPreferencesItem(TypedDict, total=False):
    """SetPreferencesDtoPreferencesItem şeması."""

    #: Zorunlu.
    category: str
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: Optional[str]
    #: Zorunlu.
    opted_in: bool


class SmsKeyword(TypedDict, total=False):
    """SmsKeyword şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    keyword: str
    #: Zorunlu. Değerler: "org", "app".
    scope: str
    #: Zorunlu.
    app_id: Optional[str]
    #: Zorunlu. Değerler: "sms", "whatsapp", "rcs".
    channels: List[str]
    #: Zorunlu.
    actions: Dict[str, Any]
    #: Zorunlu.
    enabled: bool
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class SmsKeywordList(TypedDict, total=False):
    """SmsKeywordList şeması."""

    #: Zorunlu.
    data: List["SmsKeyword"]
    #: Zorunlu.
    reserved: List[str]


class StartLiveActivityDto(TypedDict, total=False):
    """StartLiveActivityDto şeması."""

    activity_id: str
    attributes: Dict[str, Any]
    #: Zorunlu.
    target: "StartLiveActivityDtoTarget"
    #: Zorunlu.
    content_state: Dict[str, Any]
    alert: "StartLiveActivityDtoAlert"
    stale_date: int
    dismissal_date: int
    relevance_score: float
    #: Değerler: 5, 10.
    priority: int
    name: str


class StartLiveActivityDtoAlert(TypedDict, total=False):
    """StartLiveActivityDtoAlert şeması."""

    title: Dict[str, str]
    body: Dict[str, str]
    sound: str


class StartLiveActivityDtoTarget(TypedDict, total=False):
    """StartLiveActivityDtoTarget şeması."""

    include_external_ids: List[str]
    include_subscription_ids: List[str]
    included_segments: List[str]
    all: bool


class Subscription(TypedDict, total=False):
    """Subscription şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    user_id: Optional[str]
    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu.
    token: str
    #: Zorunlu. Değerler: "subscribed", "unsubscribed", "invalid", "pending".
    status: str
    #: Zorunlu. Değerler: "provider_rejected", "user_opt_out", "api", "uninstall".
    unsubscribe_reason: Optional[str]
    #: Zorunlu.
    device: "SubscriptionDevice"
    #: Zorunlu.
    test_device: bool
    #: Zorunlu.
    test_device_name: Optional[str]
    #: Zorunlu.
    last_active_at: str
    #: Zorunlu.
    last_sent_at: Optional[str]
    #: Zorunlu.
    last_delivered_at: Optional[str]
    #: Zorunlu.
    opted_in_at: Optional[str]
    #: Zorunlu.
    opt_in_source: Optional[str]
    #: Zorunlu.
    unsubscribed_at: Optional[str]
    #: Zorunlu.
    location: Optional["SubscriptionLocation"]
    #: Zorunlu.
    created_at: str


class SubscriptionDevice(TypedDict, total=False):
    """SubscriptionDevice şeması."""

    model: str
    os: str
    os_version: str
    app_version: Optional[str]
    sdk_version: str
    sdk_platform: str
    carrier: str
    locale: str
    timezone: str
    push_capable: bool
    #: Değerler: "sandbox", "production".
    push_environment: str


class SubscriptionLocation(TypedDict, total=False):
    """SubscriptionLocation şeması."""

    #: Zorunlu.
    lat: float
    #: Zorunlu.
    lng: float
    #: Zorunlu.
    accuracy_m: Optional[float]
    #: Zorunlu.
    geohash: Optional[str]
    #: Zorunlu.
    updated_at: Optional[str]
    #: Zorunlu.
    consent_at: Optional[str]


SubscriptionsReport = TypedDict(
    "SubscriptionsReport",
    {
        # Zorunlu.
        "from": str,
        # Zorunlu.
        "to": str,
        # Zorunlu.
        "totals": "SubscriptionsReportTotals",
        # Zorunlu.
        "previous": Optional["SubscriptionsReportPrevious"],
        # Zorunlu.
        "rows": List["SubscriptionsReportRowsItem"],
        # Zorunlu.
        "by_channel": List["SubscriptionsReportByChannelItem"],
    },
    total=False,
)


class SubscriptionsReportByChannelItem(TypedDict, total=False):
    """SubscriptionsReportByChannelItem şeması."""

    #: Zorunlu.
    channel: str
    #: Zorunlu.
    active: int
    #: Zorunlu.
    new: int
    #: Zorunlu.
    unsubscribed: int


class SubscriptionsReportPrevious(TypedDict, total=False):
    """SubscriptionsReportPrevious şeması."""

    #: Zorunlu.
    active: int
    #: Zorunlu.
    new: int
    #: Zorunlu.
    unsubscribed: int
    #: Zorunlu.
    opt_outs: int
    #: Zorunlu.
    net: int


class SubscriptionsReportRowsItem(TypedDict, total=False):
    """SubscriptionsReportRowsItem şeması."""

    #: Zorunlu.
    date: str
    #: Zorunlu.
    new: int
    #: Zorunlu.
    unsubscribed: int
    #: Zorunlu.
    opt_outs: int
    #: Zorunlu.
    net: int


class SubscriptionsReportTotals(TypedDict, total=False):
    """SubscriptionsReportTotals şeması."""

    #: Zorunlu.
    active: int
    #: Zorunlu.
    new: int
    #: Zorunlu.
    unsubscribed: int
    #: Zorunlu.
    opt_outs: int
    #: Zorunlu.
    net: int


class Suppression(TypedDict, total=False):
    """Suppression şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu. Değerler: "email", "sms", "whatsapp", "rcs".
    channel: str
    #: Zorunlu.
    value_masked: str
    #: Zorunlu. Değerler: "bounce", "complaint", "manual", "unsubscribe_link", "stop".
    reason: str
    #: Zorunlu.
    source: str
    #: Zorunlu.
    detail: Dict[str, Any]
    #: Zorunlu.
    expires_at: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class SuppressionPage(TypedDict, total=False):
    """SuppressionPage şeması."""

    #: Zorunlu.
    data: List["Suppression"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class Template(TypedDict, total=False):
    """Template şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: Optional[str]
    #: Zorunlu.
    current_version: int
    #: Zorunlu.
    tags: List[str]
    #: Zorunlu.
    content: Dict[str, Any]
    #: Zorunlu.
    created_by: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class TemplatePage(TypedDict, total=False):
    """TemplatePage şeması."""

    #: Zorunlu.
    data: List["Template"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class TemplateStats(TypedDict, total=False):
    """TemplateStats şeması."""

    #: Zorunlu.
    template_id: str
    #: Zorunlu.
    messages: int
    #: Zorunlu.
    campaigns: int
    #: Zorunlu.
    targeted: int
    #: Zorunlu.
    sent: int
    #: Zorunlu.
    delivered: int
    #: Zorunlu.
    opened: int
    #: Zorunlu.
    clicked: int
    #: Zorunlu.
    converted: int
    #: Zorunlu.
    open_rate: float
    #: Zorunlu.
    click_rate: float
    #: Zorunlu.
    conversion_rate: float
    #: Zorunlu.
    last_used_at: Optional[str]


class TemplateVersionList(TypedDict, total=False):
    """TemplateVersionList şeması."""

    #: Zorunlu.
    data: List["TemplateVersionListDataItem"]


class TemplateVersionListDataItem(TypedDict, total=False):
    """TemplateVersionListDataItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    version: int
    #: Zorunlu.
    content: Dict[str, Any]
    #: Zorunlu.
    created_by: Optional[str]
    #: Zorunlu.
    created_at: str


class TestDataFeedDto(TypedDict, total=False):
    """TestDataFeedDto şeması."""

    external_id: str
    user_id: str


class TriggerRunDto(TypedDict, total=False):
    """TriggerRunDto şeması."""

    external_id: str
    user_id: str
    alias: "TriggerRunDtoAlias"
    context: Dict[str, Any]


class TriggerRunDtoAlias(TypedDict, total=False):
    """TriggerRunDtoAlias şeması."""

    #: Zorunlu.
    label: str
    #: Zorunlu.
    value: str


class UpdateApiKeyDto(TypedDict, total=False):
    """UpdateApiKeyDto şeması."""

    name: str
    #: Değerler: "admin", "notifications:write", "users:read", "users:write", "events:write", "segments:read", "analytics:read", "mcp:write".
    scopes: List[str]
    ip_allowlist: List[str]
    expires_at: Optional[str]


class UpdateAppDto(TypedDict, total=False):
    """UpdateAppDto şeması."""

    name: str
    platform_flags: "UpdateAppDtoPlatformFlags"
    icon_url: Optional[str]
    default_language: str
    timezone: str
    settings: "UpdateAppDtoSettings"
    #: Değerler: "hmac", "jwt", "both".
    identity_verification_mode: str


class UpdateAppDtoPlatformFlags(TypedDict, total=False):
    """UpdateAppDtoPlatformFlags şeması."""

    ios: bool
    android: bool
    web: bool
    email: bool
    sms: bool


class UpdateAppDtoSettings(TypedDict, total=False):
    """UpdateAppDtoSettings şeması."""

    quietHours: Optional["UpdateAppDtoSettingsQuietHours"]
    frequencyCap: Optional["UpdateAppDtoSettingsFrequencyCap"]
    frequencyCaps: List["UpdateAppDtoSettingsFrequencyCapsItem"]
    inApp: "UpdateAppDtoSettingsInApp"
    androidChannels: List["UpdateAppDtoSettingsAndroidChannelsItem"]
    sms: "UpdateAppDtoSettingsSms"
    preferenceCenter: "UpdateAppDtoSettingsPreferenceCenter"
    defaultTtlSeconds: int
    identityVerificationRequired: bool
    allowedOrigins: List[str]
    campaignApprovalRequired: bool
    webPush: "UpdateAppDtoSettingsWebPush"
    onboarding: "UpdateAppDtoSettingsOnboarding"
    sdkSetup: Optional["UpdateAppDtoSettingsSdkSetup"]


class UpdateAppDtoSettingsAndroidChannelsItem(TypedDict, total=False):
    """UpdateAppDtoSettingsAndroidChannelsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    description: str
    #: Zorunlu. Değerler: "low", "default", "high", "urgent".
    importance: str
    sound: str
    vibration: bool
    group: str


class UpdateAppDtoSettingsFrequencyCap(TypedDict, total=False):
    """UpdateAppDtoSettingsFrequencyCap şeması."""

    #: Zorunlu.
    max: int
    #: Zorunlu.
    windowHours: int


class UpdateAppDtoSettingsFrequencyCapsItem(TypedDict, total=False):
    """UpdateAppDtoSettingsFrequencyCapsItem şeması."""

    #: Zorunlu.
    max: int
    #: Zorunlu.
    window: "UpdateAppDtoSettingsFrequencyCapsItemWindow"
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]


class UpdateAppDtoSettingsFrequencyCapsItemWindow(TypedDict, total=False):
    """UpdateAppDtoSettingsFrequencyCapsItemWindow şeması."""

    #: Zorunlu.
    value: int
    #: Zorunlu. Değerler: "minutes", "hours", "days", "weeks".
    unit: str


class UpdateAppDtoSettingsInApp(TypedDict, total=False):
    """UpdateAppDtoSettingsInApp şeması."""

    minIntervalSeconds: int


class UpdateAppDtoSettingsOnboarding(TypedDict, total=False):
    """UpdateAppDtoSettingsOnboarding şeması."""

    #: Zorunlu.
    step: int
    simulation: bool
    completed_at: Optional[str]
    version: int
    #: Değerler: "ios", "android", "huawei", "web".
    platforms: List[str]
    #: Değerler: "native", "flutter", "react-native", "unity", "capacitor", "cordova", "maui".
    framework: str
    #: Değerler: "code", "wordpress".
    web_integration: str


class UpdateAppDtoSettingsPreferenceCenter(TypedDict, total=False):
    """UpdateAppDtoSettingsPreferenceCenter şeması."""

    enabled: bool
    brandName: str
    logoUrl: str
    accentColor: str
    customUnsubscribeUrl: str
    texts: Dict[str, "UpdateAppDtoSettingsPreferenceCenterTextsValue"]


class UpdateAppDtoSettingsPreferenceCenterTextsValue(TypedDict, total=False):
    """UpdateAppDtoSettingsPreferenceCenterTextsValue şeması."""

    title: str
    description: str
    unsubscribeAll: str
    saved: str


class UpdateAppDtoSettingsQuietHours(TypedDict, total=False):
    """UpdateAppDtoSettingsQuietHours şeması."""

    #: Zorunlu.
    start: str
    #: Zorunlu.
    end: str
    #: Zorunlu. Değerler: "user", "app".
    timezoneMode: str


class UpdateAppDtoSettingsSdkSetup(TypedDict, total=False):
    """UpdateAppDtoSettingsSdkSetup şeması."""

    #: Zorunlu.
    version: int
    #: Zorunlu.
    platform: Optional[str]
    #: Zorunlu.
    step: str
    #: Zorunlu.
    furthest: str
    variant: Optional[str]
    detectedSubscriptionId: Optional[str]
    testMessageId: Optional[str]
    completedAt: Optional[str]


class UpdateAppDtoSettingsSms(TypedDict, total=False):
    """UpdateAppDtoSettingsSms şeması."""

    helpReply: str
    stopReply: str
    autoReply: bool


class UpdateAppDtoSettingsWebPush(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPush şeması."""

    serviceWorkerPath: str
    serviceWorkerScope: str
    prompt: "UpdateAppDtoSettingsWebPushPrompt"
    welcomeNotification: "UpdateAppDtoSettingsWebPushWelcomeNotification"
    clickBehavior: "UpdateAppDtoSettingsWebPushClickBehavior"
    customLink: "UpdateAppDtoSettingsWebPushCustomLink"
    promptBackoffDays: List[int]


class UpdateAppDtoSettingsWebPushClickBehavior(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushClickBehavior şeması."""

    #: Zorunlu. Değerler: "exact", "origin".
    match: str
    #: Zorunlu. Değerler: "navigate", "focus".
    action: str


class UpdateAppDtoSettingsWebPushCustomLink(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushCustomLink şeması."""

    #: Zorunlu.
    enabled: bool
    #: Zorunlu. Değerler: "button", "link".
    style: str
    #: Zorunlu. Değerler: "small", "medium", "large".
    size: str
    color: "UpdateAppDtoSettingsWebPushCustomLinkColor"
    texts: Dict[str, "UpdateAppDtoSettingsWebPushCustomLinkTextsValue"]
    unsubscribeEnabled: bool


class UpdateAppDtoSettingsWebPushCustomLinkColor(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushCustomLinkColor şeması."""

    button: str
    text: str


class UpdateAppDtoSettingsWebPushCustomLinkTextsValue(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushCustomLinkTextsValue şeması."""

    subscribe: str
    unsubscribe: str
    explanation: str


class UpdateAppDtoSettingsWebPushPrompt(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushPrompt şeması."""

    #: Zorunlu.
    enabled: bool
    #: Zorunlu. Değerler: "slidedown", "native".
    type: str
    #: Değerler: "push", "email", "sms", "email_sms".
    collect: str
    delaySeconds: int
    pageViews: int
    scrollPercent: int
    texts: Dict[str, "UpdateAppDtoSettingsWebPushPromptTextsValue"]
    categories: List["UpdateAppDtoSettingsWebPushPromptCategoriesItem"]
    accentColor: str


class UpdateAppDtoSettingsWebPushPromptCategoriesItem(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushPromptCategoriesItem şeması."""

    #: Zorunlu.
    tag: str
    #: Zorunlu.
    label: Dict[str, str]


class UpdateAppDtoSettingsWebPushPromptTextsValue(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushPromptTextsValue şeması."""

    title: str
    message: str
    accept: str
    cancel: str


class UpdateAppDtoSettingsWebPushWelcomeNotification(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushWelcomeNotification şeması."""

    #: Zorunlu.
    enabled: bool
    url: str
    texts: Dict[str, "UpdateAppDtoSettingsWebPushWelcomeNotificationTextsValue"]


class UpdateAppDtoSettingsWebPushWelcomeNotificationTextsValue(TypedDict, total=False):
    """UpdateAppDtoSettingsWebPushWelcomeNotificationTextsValue şeması."""

    title: str
    message: str


class UpdateCategoryDto(TypedDict, total=False):
    """UpdateCategoryDto şeması."""

    name: Dict[str, str]
    description: Dict[str, str]
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: Optional[List[str]]
    default_opted_in: bool
    position: int


class UpdateContentTableDto(TypedDict, total=False):
    """UpdateContentTableDto şeması."""

    description: Optional[str]


class UpdateDataFeedDto(TypedDict, total=False):
    """UpdateDataFeedDto şeması."""

    description: Optional[str]
    url_template: str
    #: Değerler: "GET", "POST".
    method: str
    body_template: Optional[str]
    headers: Dict[str, str]
    secret_headers: Optional[Dict[str, str]]
    cache_ttl_seconds: int
    timeout_ms: int
    enabled: bool


class UpdateInAppDto(TypedDict, total=False):
    """UpdateInAppDto şeması."""

    name: str
    triggers: List[Any]
    trigger_groups: List[List[Any]]
    variants: List["UpdateInAppDtoVariantsItem"]
    ab_test: "UpdateInAppDtoAbTest"
    display: "UpdateInAppDtoDisplay"
    audience: "UpdateInAppDtoAudience"
    frequency: "UpdateInAppDtoFrequency"
    journey_only: bool
    priority: int
    start_at: Optional[str]
    end_at: Optional[str]


class UpdateInAppDtoAbTest(TypedDict, total=False):
    """UpdateInAppDtoAbTest şeması."""

    winner: "UpdateInAppDtoAbTestWinner"


class UpdateInAppDtoAbTestWinner(TypedDict, total=False):
    """UpdateInAppDtoAbTestWinner şeması."""

    #: Zorunlu. Değerler: "manual", "auto".
    mode: str
    min_impressions: int
    confidence: float


class UpdateInAppDtoAudience(TypedDict, total=False):
    """UpdateInAppDtoAudience şeması."""

    included_segments: List[str]
    excluded_segments: List[str]


class UpdateInAppDtoDisplay(TypedDict, total=False):
    """UpdateInAppDtoDisplay şeması."""

    #: Zorunlu. Değerler: "modal", "banner_top", "banner_bottom", "fullscreen".
    layout: str
    background_color: str
    text_color: str
    dismissible: bool
    auto_dismiss_seconds: int
    #: Değerler: "blocks", "html".
    content_type: str
    html: Dict[str, str]
    html_height: int
    #: Zorunlu.
    blocks: List[Any]


class UpdateInAppDtoFrequency(TypedDict, total=False):
    """UpdateInAppDtoFrequency şeması."""

    max_impressions: int
    min_interval_seconds: int
    stop_after_interaction: bool


class UpdateInAppDtoVariantsItem(TypedDict, total=False):
    """UpdateInAppDtoVariantsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    weight_percent: int
    #: Zorunlu.
    display: "UpdateInAppDtoVariantsItemDisplay"


class UpdateInAppDtoVariantsItemDisplay(TypedDict, total=False):
    """UpdateInAppDtoVariantsItemDisplay şeması."""

    #: Zorunlu. Değerler: "modal", "banner_top", "banner_bottom", "fullscreen".
    layout: str
    background_color: str
    text_color: str
    dismissible: bool
    auto_dismiss_seconds: int
    #: Değerler: "blocks", "html".
    content_type: str
    html: Dict[str, str]
    html_height: int
    #: Zorunlu.
    blocks: List[Any]


class UpdateJourneyDto(TypedDict, total=False):
    """UpdateJourneyDto şeması."""

    name: str
    description: Optional[str]


class UpdateKeywordDto(TypedDict, total=False):
    """UpdateKeywordDto şeması."""

    keyword: str
    #: Değerler: "sms", "whatsapp", "rcs".
    channels: List[str]
    actions: "UpdateKeywordDtoActions"
    enabled: bool
    description: Optional[str]


class UpdateKeywordDtoActions(TypedDict, total=False):
    """UpdateKeywordDtoActions şeması."""

    add_tags: Dict[str, str]
    remove_tags: List[str]
    event: "UpdateKeywordDtoActionsEvent"
    reply: "UpdateKeywordDtoActionsReply"
    opt_in: bool


class UpdateKeywordDtoActionsEvent(TypedDict, total=False):
    """UpdateKeywordDtoActionsEvent şeması."""

    #: Zorunlu.
    name: str
    properties: Dict[str, str]


class UpdateKeywordDtoActionsReply(TypedDict, total=False):
    """UpdateKeywordDtoActionsReply şeması."""

    #: Zorunlu.
    text: str


class UpdateLiveActivityDto(TypedDict, total=False):
    """UpdateLiveActivityDto şeması."""

    #: Zorunlu.
    activity_id: str
    #: Zorunlu.
    content_state: Dict[str, Any]
    alert: "UpdateLiveActivityDtoAlert"
    stale_date: int
    dismissal_date: int
    relevance_score: float
    #: Değerler: 5, 10.
    priority: int
    name: str


class UpdateLiveActivityDtoAlert(TypedDict, total=False):
    """UpdateLiveActivityDtoAlert şeması."""

    title: Dict[str, str]
    body: Dict[str, str]
    sound: str


class UpdateLiveActivityTypeDto(TypedDict, total=False):
    """UpdateLiveActivityTypeDto şeması."""

    description: Optional[str]
    content_state_schema: "UpdateLiveActivityTypeDtoContentStateSchema"
    attributes_schema: "UpdateLiveActivityTypeDtoAttributesSchema"


class UpdateLiveActivityTypeDtoAttributesSchema(TypedDict, total=False):
    """UpdateLiveActivityTypeDtoAttributesSchema şeması."""

    #: Zorunlu. Değerler: "object".
    type: str
    #: Zorunlu.
    properties: Dict[str, "UpdateLiveActivityTypeDtoAttributesSchemaPropertiesValue"]
    required: List[str]


class UpdateLiveActivityTypeDtoAttributesSchemaPropertiesValue(TypedDict, total=False):
    """UpdateLiveActivityTypeDtoAttributesSchemaPropertiesValue şeması."""

    #: Zorunlu. Değerler: "string", "number", "integer", "boolean".
    type: str
    enum: List[Any]
    maxLength: int
    minimum: float
    maximum: float
    description: str


class UpdateLiveActivityTypeDtoContentStateSchema(TypedDict, total=False):
    """UpdateLiveActivityTypeDtoContentStateSchema şeması."""

    #: Zorunlu. Değerler: "object".
    type: str
    #: Zorunlu.
    properties: Dict[str, "UpdateLiveActivityTypeDtoContentStateSchemaPropertiesValue"]
    required: List[str]


class UpdateLiveActivityTypeDtoContentStateSchemaPropertiesValue(TypedDict, total=False):
    """UpdateLiveActivityTypeDtoContentStateSchemaPropertiesValue şeması."""

    #: Zorunlu. Değerler: "string", "number", "integer", "boolean".
    type: str
    enum: List[Any]
    maxLength: int
    minimum: float
    maximum: float
    description: str


class UpdateNodeDto(TypedDict, total=False):
    """UpdateNodeDto şeması."""

    data: Dict[str, Any]
    position: "UpdateNodeDtoPosition"


class UpdateNodeDtoPosition(TypedDict, total=False):
    """UpdateNodeDtoPosition şeması."""

    #: Zorunlu.
    x: float
    #: Zorunlu.
    y: float


class UpdateTemplateDto(TypedDict, total=False):
    """UpdateTemplateDto şeması."""

    name: str
    #: Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channel: Optional[str]
    tags: List[str]
    content: "UpdateTemplateDtoContent"


class UpdateTemplateDtoContent(TypedDict, total=False):
    """UpdateTemplateDtoContent şeması."""

    headings: Dict[str, str]
    contents: Dict[str, str]
    subtitle: Dict[str, str]
    url: str
    app_url: str
    data: Dict[str, str]
    buttons: List["UpdateTemplateDtoContentButtonsItem"]
    big_picture: str
    ios_attachments: Dict[str, str]
    ios_sound: str
    #: Değerler: "None", "SetTo", "Increase".
    ios_badge_type: str
    ios_badge_count: int
    #: Değerler: "passive", "active", "time-sensitive", "critical".
    ios_interruption_level: str
    ios_category: str
    android_channel_id: str
    android_group: str
    android_sound: str
    chrome_web_icon: str
    chrome_web_image: str
    chrome_web_badge: str
    web_push_topic: str
    content_available: bool
    mutable_content: bool
    custom_data: Dict[str, Any]
    email_subject: str
    email_body: str
    email_mjml: str
    email_preheader: str
    email_from_name: str
    email_from_address: str
    email_reply_to_address: str
    disable_email_click_tracking: bool
    sms_from: str
    disable_sms_link_shortening: bool
    add_to_inbox: bool
    inbox_ttl: int
    thread_id: str
    ios_relevance_score: float
    target_content_identifier: str
    small_icon: str
    large_icon: str
    android_accent_color: str
    #: Değerler: 1, 0, -1.
    android_visibility: int
    web_buttons: List["UpdateTemplateDtoContentWebButtonsItem"]
    require_interaction: bool
    sms_media_urls: List[str]
    whatsapp_template: "UpdateTemplateDtoContentWhatsappTemplate"
    whatsapp_media: "UpdateTemplateDtoContentWhatsappMedia"
    whatsapp_interactive: "UpdateTemplateDtoContentWhatsappInteractive"
    rcs_card: "UpdateTemplateDtoContentRcsCard"
    rcs_suggestions: List[Any]
    rcs_content_sid: str
    rcs_content_variables: Dict[str, str]
    rcs_fallback_text: Dict[str, str]


class UpdateTemplateDtoContentButtonsItem(TypedDict, total=False):
    """UpdateTemplateDtoContentButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class UpdateTemplateDtoContentRcsCard(TypedDict, total=False):
    """UpdateTemplateDtoContentRcsCard şeması."""

    title: Dict[str, str]
    description: Dict[str, str]
    media_url: str
    #: Değerler: "SHORT", "MEDIUM", "TALL".
    media_height: str
    #: Değerler: "VERTICAL", "HORIZONTAL".
    orientation: str


class UpdateTemplateDtoContentWebButtonsItem(TypedDict, total=False):
    """UpdateTemplateDtoContentWebButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class UpdateTemplateDtoContentWhatsappInteractive(TypedDict, total=False):
    """UpdateTemplateDtoContentWhatsappInteractive şeması."""

    #: Zorunlu. Değerler: "button", "list".
    type: str
    header: str
    footer: str
    buttons: List["UpdateTemplateDtoContentWhatsappInteractiveButtonsItem"]
    list: "UpdateTemplateDtoContentWhatsappInteractiveList"


class UpdateTemplateDtoContentWhatsappInteractiveButtonsItem(TypedDict, total=False):
    """UpdateTemplateDtoContentWhatsappInteractiveButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str


class UpdateTemplateDtoContentWhatsappInteractiveList(TypedDict, total=False):
    """UpdateTemplateDtoContentWhatsappInteractiveList şeması."""

    #: Zorunlu.
    button: str
    #: Zorunlu.
    sections: List["UpdateTemplateDtoContentWhatsappInteractiveListSectionsItem"]


class UpdateTemplateDtoContentWhatsappInteractiveListSectionsItem(TypedDict, total=False):
    """UpdateTemplateDtoContentWhatsappInteractiveListSectionsItem şeması."""

    title: str
    #: Zorunlu.
    rows: List["UpdateTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem"]


class UpdateTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem(TypedDict, total=False):
    """UpdateTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    title: str
    description: str


class UpdateTemplateDtoContentWhatsappMedia(TypedDict, total=False):
    """UpdateTemplateDtoContentWhatsappMedia şeması."""

    #: Zorunlu. Değerler: "image", "video", "document", "audio".
    type: str
    #: Zorunlu.
    url: str
    filename: str


class UpdateTemplateDtoContentWhatsappTemplate(TypedDict, total=False):
    """UpdateTemplateDtoContentWhatsappTemplate şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu.
    language: str
    header: Any
    body_params: List[str]
    button_params: List["UpdateTemplateDtoContentWhatsappTemplateButtonParamsItem"]


class UpdateTemplateDtoContentWhatsappTemplateButtonParamsItem(TypedDict, total=False):
    """UpdateTemplateDtoContentWhatsappTemplateButtonParamsItem şeması."""

    #: Zorunlu.
    index: int
    #: Zorunlu. Değerler: "url", "quick_reply", "copy_code".
    sub_type: str
    #: Zorunlu.
    value: str


class UpdateWarehouseExportDto(TypedDict, total=False):
    """UpdateWarehouseExportDto şeması."""

    name: str
    #: Değerler: "deliveries", "delivery_events", "events", "conversions", "users", "subscriptions".
    tables: List[str]
    #: Değerler: "hourly", "daily".
    schedule: str
    enabled: bool
    config: Dict[str, Any]
    credentials: Dict[str, Any]


class UpdateWarmupPlanDto(TypedDict, total=False):
    """UpdateWarmupPlanDto şeması."""

    name: str
    #: Değerler: "active", "paused".
    status: str
    daily_limits: List[int]
    provider_shares: Optional["UpdateWarmupPlanDtoProviderShares"]


class UpdateWarmupPlanDtoProviderShares(TypedDict, total=False):
    """UpdateWarmupPlanDtoProviderShares şeması."""

    #: Zorunlu.
    gmail: float
    #: Zorunlu.
    outlook: float
    #: Zorunlu.
    yahoo: float
    #: Zorunlu.
    other: float


class UpdateWebhookDto(TypedDict, total=False):
    """UpdateWebhookDto şeması."""

    url: str
    description: Optional[str]
    #: Değerler: "message.queued", "message.completed", "message.failed", "delivery.sent", "delivery.delivered", "delivery.failed", "delivery.opened", "delivery.clicked", "delivery.bounced", "delivery.complained", "delivery.unsubscribed", "in_app.impression", "in_app.clicked", "in_app.dismissed", "subscription.created", "subscription.unsubscribed", "subscription.invalidated", "user.created", "user.updated", "user.merged", "user.deleted", "event.received", "conversion.created", "campaign.scheduled", "campaign.started", "campaign.completed", "journey.entered", "journey.step_completed", "journey.completed", "journey.exited", "audit.created".
    events: List[str]
    event_filters: "UpdateWebhookDtoEventFilters"
    batch: bool
    headers: Optional[Dict[str, str]]
    #: Değerler: "active", "disabled".
    status: str
    body_template: Optional[str]
    #: Şablon çıktısının içerik türü (varsayılan application/json). Değerler: "application/json", "text/plain".
    body_content_type: str
    filters: Optional["UpdateWebhookDtoFilters"]


class UpdateWebhookDtoEventFilters(TypedDict, total=False):
    """UpdateWebhookDtoEventFilters şeması."""

    event_names: List[str]


class UpdateWebhookDtoFilters(TypedDict, total=False):
    """Olay filtresi: { match: all|any, conditions: [{ field, op, value? }] }."""

    #: Zorunlu. Değerler: "all", "any".
    match: str
    #: Zorunlu.
    conditions: List["UpdateWebhookDtoFiltersConditionsItem"]


class UpdateWebhookDtoFiltersConditionsItem(TypedDict, total=False):
    """UpdateWebhookDtoFiltersConditionsItem şeması."""

    #: Zorunlu.
    field: str
    #: Zorunlu. Değerler: "eq", "neq", "in", "not_in", "starts_with", "contains", "exists", "not_exists".
    op: str
    value: Any


class UpsertUserDto(TypedDict, total=False):
    """UpsertUserDto şeması."""

    identity: Any
    external_id: str
    properties: Dict[str, Any]
    tags: Dict[str, str]
    subscriptions: List["AddSubscriptionDto"]


class UsageReport(TypedDict, total=False):
    """UsageReport şeması."""

    #: Zorunlu.
    org_id: str
    #: Zorunlu.
    plan_code: str
    #: Zorunlu.
    period: "UsageReportPeriod"
    #: Zorunlu.
    metrics: List["UsageReportMetricsItem"]
    #: Zorunlu.
    apps: List["UsageReportAppsItem"]
    #: Zorunlu.
    daily: List["UsageReportDailyItem"]
    #: Zorunlu.
    trialing: bool
    #: Zorunlu.
    trial_ends_at: Optional[str]


class UsageReportAppsItem(TypedDict, total=False):
    """UsageReportAppsItem şeması."""

    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu.
    messages_sent: float
    #: Zorunlu.
    active_subscriptions: float
    #: Zorunlu.
    mau: float


class UsageReportDailyItem(TypedDict, total=False):
    """UsageReportDailyItem şeması."""

    #: Zorunlu.
    date: str
    #: Zorunlu.
    messages_sent: float
    #: Zorunlu.
    api_requests: float
    #: Zorunlu.
    events_ingested: float


class UsageReportMetricsItem(TypedDict, total=False):
    """UsageReportMetricsItem şeması."""

    #: Zorunlu.
    metric: str
    #: Zorunlu.
    used: float
    #: Zorunlu.
    limit: Optional[float]
    #: Zorunlu.
    percent: Optional[float]
    #: Zorunlu.
    hard: bool


class UsageReportPeriod(TypedDict, total=False):
    """UsageReportPeriod şeması."""

    #: Zorunlu.
    start: str
    #: Zorunlu.
    end: str


class User(TypedDict, total=False):
    """User şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu.
    properties: Dict[str, Any]
    #: Zorunlu.
    tags: Dict[str, str]
    #: Zorunlu.
    first_seen_at: str
    #: Zorunlu.
    last_active_at: str
    #: Zorunlu.
    session_count: int
    #: Zorunlu.
    usage_seconds: int
    #: Zorunlu.
    merged_into: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str
    #: Zorunlu.
    subscription_count: int
    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]


class UserDetail(TypedDict, total=False):
    """UserDetail şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu.
    properties: Dict[str, Any]
    #: Zorunlu.
    tags: Dict[str, str]
    #: Zorunlu.
    first_seen_at: str
    #: Zorunlu.
    last_active_at: str
    #: Zorunlu.
    session_count: int
    #: Zorunlu.
    usage_seconds: int
    #: Zorunlu.
    merged_into: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str
    #: Zorunlu.
    subscription_count: int
    #: Zorunlu. Değerler: "ios_push", "android_push", "hms_push", "web_push", "email", "sms", "whatsapp", "rcs".
    channels: List[str]
    #: Zorunlu.
    aliases: List["UserDetailAliasesItem"]
    #: Zorunlu.
    subscriptions: List["Subscription"]


class UserDetailAliasesItem(TypedDict, total=False):
    """UserDetailAliasesItem şeması."""

    #: Zorunlu.
    label: str
    #: Zorunlu.
    value: str


class UserExport(TypedDict, total=False):
    """UserExport şeması."""

    #: Zorunlu.
    exported_at: str
    #: Zorunlu.
    user: "UserDetail"
    #: Zorunlu.
    events: List["UserExportEventsItem"]


class UserExportEventsItem(TypedDict, total=False):
    """UserExportEventsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    user_id: Optional[str]
    #: Zorunlu.
    subscription_id: Optional[str]
    #: Zorunlu.
    name: str
    #: Zorunlu.
    properties: Dict[str, Any]
    #: Zorunlu.
    value: Optional[float]
    #: Zorunlu. Değerler: "sdk", "api", "system", "import".
    source: str
    #: Zorunlu.
    occurred_at: str


class UserIdentity(TypedDict, total=False):
    """UserIdentity şeması."""

    #: Zorunlu.
    identity: Dict[str, str]


class UserJourneyRuns(TypedDict, total=False):
    """UserJourneyRuns şeması."""

    #: Zorunlu.
    data: List["UserJourneyRunsDataItem"]


class UserJourneyRunsDataItem(TypedDict, total=False):
    """UserJourneyRunsDataItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    journey_id: str
    #: Zorunlu.
    version: int
    #: Zorunlu.
    user_id: str
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu. Değerler: "active", "waiting", "completed", "exited", "failed".
    status: str
    #: Zorunlu.
    current_node_id: Optional[str]
    #: Zorunlu.
    next_action_at: Optional[str]
    #: Zorunlu.
    entered_at: str
    #: Zorunlu.
    completed_at: Optional[str]
    #: Zorunlu.
    exit_reason: Optional[str]
    #: Zorunlu.
    goal_id: Optional[str]
    #: Zorunlu.
    goal_reached_at: Optional[str]
    #: Zorunlu.
    context: Dict[str, Any]
    #: Zorunlu.
    journey_name: str


class UserList(TypedDict, total=False):
    """UserList şeması."""

    #: Zorunlu.
    data: List["User"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class UserPreferences(TypedDict, total=False):
    """UserPreferences şeması."""

    #: Zorunlu.
    user_id: str
    #: Zorunlu.
    data: List["UserPreferencesDataItem"]
    #: Zorunlu.
    categories: List["MessageCategory"]


class UserPreferencesDataItem(TypedDict, total=False):
    """UserPreferencesDataItem şeması."""

    #: Zorunlu.
    category: str
    #: Zorunlu.
    channel: Optional[str]
    #: Zorunlu.
    opted_in: bool
    #: Zorunlu.
    explicit: bool
    #: Zorunlu.
    source: Optional[str]
    #: Zorunlu.
    updated_at: Optional[str]


class UsersSearchBody(TypedDict, total=False):
    """UsersSearchBody şeması."""

    #: Zorunlu. Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7).
    definition: "UsersSearchBodyDefinition"
    limit: int
    cursor: str


class UsersSearchBodyDefinition(TypedDict, total=False):
    """Filtre AST: all/any/none grupları ve { field, op, value } koşulları (docs/plan/05 §5.7)."""

    all: List[Dict[str, Any]]
    any: List[Dict[str, Any]]
    none: List[Dict[str, Any]]


class VerifyAddressDto(TypedDict, total=False):
    """VerifyAddressDto şeması."""

    #: Zorunlu.
    address: str


class WarehouseConnectionResult(TypedDict, total=False):
    """WarehouseConnectionResult şeması."""

    #: Zorunlu.
    ok: bool
    #: Zorunlu.
    detail: Optional[str]
    #: Zorunlu.
    error: Optional["WarehouseConnectionResultError"]


class WarehouseConnectionResultError(TypedDict, total=False):
    """WarehouseConnectionResultError şeması."""

    #: Zorunlu.
    code: str
    #: Zorunlu.
    message: str


class WarehouseExport(TypedDict, total=False):
    """WarehouseExport şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    name: str
    #: Zorunlu. Değerler: "bigquery", "snowflake", "s3_parquet".
    destination: str
    #: Zorunlu.
    config: Dict[str, Any]
    #: Zorunlu.
    credentials_hint: str
    #: Zorunlu. Değerler: "deliveries", "delivery_events", "events", "conversions", "users", "subscriptions".
    tables: List[str]
    #: Zorunlu. Değerler: "hourly", "daily".
    schedule: str
    #: Zorunlu.
    enabled: bool
    #: Zorunlu. Değerler: "active", "paused", "failing".
    status: str
    #: Zorunlu.
    consecutive_failures: int
    #: Zorunlu.
    last_error: Optional[str]
    #: Zorunlu.
    cursors: Dict[str, "WarehouseExportCursorsValue"]
    #: Zorunlu.
    schema_versions: Dict[str, int]
    #: Zorunlu.
    last_run_at: Optional[str]
    #: Zorunlu.
    last_success_at: Optional[str]
    #: Zorunlu.
    next_run_at: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class WarehouseExportCursorsValue(TypedDict, total=False):
    """WarehouseExportCursorsValue şeması."""

    #: Zorunlu.
    ts: str
    #: Zorunlu.
    id: str


class WarehouseExportList(TypedDict, total=False):
    """WarehouseExportList şeması."""

    #: Zorunlu.
    data: List["WarehouseExport"]


class WarehouseExportRun(TypedDict, total=False):
    """WarehouseExportRun şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    export_id: str
    #: Zorunlu. Değerler: "schedule", "manual".
    trigger: str
    #: Zorunlu. Değerler: "queued", "running", "succeeded", "failed".
    status: str
    #: Zorunlu.
    tables: Dict[str, "WarehouseExportRunTablesValue"]
    #: Zorunlu.
    row_count: int
    #: Zorunlu.
    attempt: int
    #: Zorunlu.
    error: Optional[str]
    #: Zorunlu.
    started_at: Optional[str]
    #: Zorunlu.
    finished_at: Optional[str]
    #: Zorunlu.
    duration_ms: Optional[int]
    #: Zorunlu.
    created_at: str


class WarehouseExportRunPage(TypedDict, total=False):
    """WarehouseExportRunPage şeması."""

    #: Zorunlu.
    data: List["WarehouseExportRun"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


WarehouseExportRunTablesValue = TypedDict(
    "WarehouseExportRunTablesValue",
    {
        # Zorunlu.
        "rows": int,
        # Zorunlu.
        "schema_version": int,
        # Zorunlu.
        "from": Optional["WarehouseExportRunTablesValueFrom"],
        # Zorunlu.
        "to": Optional["WarehouseExportRunTablesValueTo"],
        # Zorunlu.
        "objects": int,
    },
    total=False,
)


class WarehouseExportRunTablesValueFrom(TypedDict, total=False):
    """WarehouseExportRunTablesValueFrom şeması."""

    #: Zorunlu.
    ts: str
    #: Zorunlu.
    id: str


class WarehouseExportRunTablesValueTo(TypedDict, total=False):
    """WarehouseExportRunTablesValueTo şeması."""

    #: Zorunlu.
    ts: str
    #: Zorunlu.
    id: str


class WarehouseTables(TypedDict, total=False):
    """WarehouseTables şeması."""

    #: Zorunlu.
    data: List["WarehouseTablesDataItem"]


class WarehouseTablesDataItem(TypedDict, total=False):
    """WarehouseTablesDataItem şeması."""

    #: Zorunlu. Değerler: "deliveries", "delivery_events", "events", "conversions", "users", "subscriptions".
    name: str
    #: Zorunlu. Değerler: "incremental", "snapshot".
    mode: str
    #: Zorunlu.
    schema_version: int
    #: Zorunlu.
    cursor_column: Optional[str]
    #: Zorunlu.
    columns: List["WarehouseTablesDataItemColumnsItem"]


class WarehouseTablesDataItemColumnsItem(TypedDict, total=False):
    """WarehouseTablesDataItemColumnsItem şeması."""

    #: Zorunlu.
    name: str
    #: Zorunlu.
    type: str
    #: Zorunlu.
    nullable: bool


class Webhook(TypedDict, total=False):
    """Webhook şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    url: str
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu.
    events: List[str]
    #: Zorunlu.
    event_filters: "WebhookEventFilters"
    #: Zorunlu.
    batch: bool
    #: Zorunlu. Değerler: "active", "failing", "disabled".
    status: str
    #: Zorunlu.
    disabled_reason: Optional[str]
    #: Zorunlu.
    failure_count: int
    #: Zorunlu.
    failing_since: Optional[str]
    #: Zorunlu.
    last_success_at: Optional[str]
    #: Zorunlu.
    last_failure_at: Optional[str]
    #: Zorunlu.
    header_names: List[str]
    #: Zorunlu.
    previous_secret_expires_at: Optional[str]
    #: Zorunlu.
    body_template: Optional[str]
    #: Zorunlu. Değerler: "application/json", "text/plain".
    body_content_type: str
    #: Zorunlu.
    filters: Optional["WebhookFilters"]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str


class WebhookDeliveryDetail(TypedDict, total=False):
    """WebhookDeliveryDetail şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    endpoint_id: str
    #: Zorunlu.
    event_type: str
    #: Zorunlu.
    event_id: str
    #: Zorunlu.
    subject_id: Optional[str]
    #: Zorunlu.
    attempt: int
    #: Zorunlu. Değerler: "pending", "success", "failed", "dead".
    status: str
    #: Zorunlu.
    response_status: Optional[int]
    #: Zorunlu.
    response_body_excerpt: Optional[str]
    #: Zorunlu.
    error: Optional[str]
    #: Zorunlu.
    duration_ms: Optional[int]
    #: Zorunlu.
    next_retry_at: Optional[str]
    #: Zorunlu.
    delivered_at: Optional[str]
    #: Zorunlu.
    replay_of: Optional[str]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    payload: Dict[str, Any]


class WebhookDeliveryPage(TypedDict, total=False):
    """WebhookDeliveryPage şeması."""

    #: Zorunlu.
    data: List["WebhookDeliveryPageDataItem"]
    #: Zorunlu.
    next_cursor: Optional[str]
    #: Zorunlu.
    has_more: bool


class WebhookDeliveryPageDataItem(TypedDict, total=False):
    """WebhookDeliveryPageDataItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    endpoint_id: str
    #: Zorunlu.
    event_type: str
    #: Zorunlu.
    event_id: str
    #: Zorunlu.
    subject_id: Optional[str]
    #: Zorunlu.
    attempt: int
    #: Zorunlu. Değerler: "pending", "success", "failed", "dead".
    status: str
    #: Zorunlu.
    response_status: Optional[int]
    #: Zorunlu.
    response_body_excerpt: Optional[str]
    #: Zorunlu.
    error: Optional[str]
    #: Zorunlu.
    duration_ms: Optional[int]
    #: Zorunlu.
    next_retry_at: Optional[str]
    #: Zorunlu.
    delivered_at: Optional[str]
    #: Zorunlu.
    replay_of: Optional[str]
    #: Zorunlu.
    created_at: str


class WebhookEventFilters(TypedDict, total=False):
    """WebhookEventFilters şeması."""

    event_names: List[str]


class WebhookFilters(TypedDict, total=False):
    """WebhookFilters şeması."""

    #: Zorunlu. Değerler: "all", "any".
    match: str
    #: Zorunlu.
    conditions: List["WebhookFiltersConditionsItem"]


class WebhookFiltersConditionsItem(TypedDict, total=False):
    """WebhookFiltersConditionsItem şeması."""

    #: Zorunlu.
    field: str
    #: Zorunlu. Değerler: "eq", "neq", "in", "not_in", "starts_with", "contains", "exists", "not_exists".
    op: str
    value: Any


class WebhookList(TypedDict, total=False):
    """WebhookList şeması."""

    #: Zorunlu.
    data: List["Webhook"]


class WebhookPreviewDto(TypedDict, total=False):
    """WebhookPreviewDto şeması."""

    #: Zorunlu. Değerler: "message.queued", "message.completed", "message.failed", "delivery.sent", "delivery.delivered", "delivery.failed", "delivery.opened", "delivery.clicked", "delivery.bounced", "delivery.complained", "delivery.unsubscribed", "in_app.impression", "in_app.clicked", "in_app.dismissed", "subscription.created", "subscription.unsubscribed", "subscription.invalidated", "user.created", "user.updated", "user.merged", "user.deleted", "event.received", "conversion.created", "campaign.scheduled", "campaign.started", "campaign.completed", "journey.entered", "journey.step_completed", "journey.completed", "journey.exited", "audit.created", "webhook.test".
    event_type: str
    data: Dict[str, Any]
    body_template: Optional[str]
    #: Şablon çıktısının içerik türü (varsayılan application/json). Değerler: "application/json", "text/plain".
    body_content_type: str
    filters: Optional["WebhookPreviewDtoFilters"]
    batch: bool


class WebhookPreviewDtoFilters(TypedDict, total=False):
    """Olay filtresi: { match: all|any, conditions: [{ field, op, value? }] }."""

    #: Zorunlu. Değerler: "all", "any".
    match: str
    #: Zorunlu.
    conditions: List["WebhookPreviewDtoFiltersConditionsItem"]


class WebhookPreviewDtoFiltersConditionsItem(TypedDict, total=False):
    """WebhookPreviewDtoFiltersConditionsItem şeması."""

    #: Zorunlu.
    field: str
    #: Zorunlu. Değerler: "eq", "neq", "in", "not_in", "starts_with", "contains", "exists", "not_exists".
    op: str
    value: Any


class WebhookPreviewResult(TypedDict, total=False):
    """WebhookPreviewResult şeması."""

    #: Zorunlu.
    payload: Dict[str, Any]
    #: Zorunlu. Olay filtreden geçer mi (geçmezse gönderilmez).
    matched: bool
    #: Zorunlu.
    failed_conditions: List["WebhookPreviewResultFailedConditionsItem"]
    #: Zorunlu.
    body: Optional[str]
    #: Zorunlu.
    content_type: str
    #: Zorunlu.
    error: Optional["WebhookPreviewResultError"]


class WebhookPreviewResultError(TypedDict, total=False):
    """WebhookPreviewResultError şeması."""

    #: Zorunlu.
    code: str
    #: Zorunlu.
    message: str


class WebhookPreviewResultFailedConditionsItem(TypedDict, total=False):
    """WebhookPreviewResultFailedConditionsItem şeması."""

    #: Zorunlu.
    field: str
    #: Zorunlu.
    op: str
    value: Any


class WebhookWithSecret(TypedDict, total=False):
    """WebhookWithSecret şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    url: str
    #: Zorunlu.
    description: Optional[str]
    #: Zorunlu.
    events: List[str]
    #: Zorunlu.
    event_filters: "WebhookWithSecretEventFilters"
    #: Zorunlu.
    batch: bool
    #: Zorunlu. Değerler: "active", "failing", "disabled".
    status: str
    #: Zorunlu.
    disabled_reason: Optional[str]
    #: Zorunlu.
    failure_count: int
    #: Zorunlu.
    failing_since: Optional[str]
    #: Zorunlu.
    last_success_at: Optional[str]
    #: Zorunlu.
    last_failure_at: Optional[str]
    #: Zorunlu.
    header_names: List[str]
    #: Zorunlu.
    previous_secret_expires_at: Optional[str]
    #: Zorunlu.
    body_template: Optional[str]
    #: Zorunlu. Değerler: "application/json", "text/plain".
    body_content_type: str
    #: Zorunlu.
    filters: Optional["WebhookWithSecretFilters"]
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    updated_at: str
    #: Zorunlu. Yalnızca oluşturma ve rotasyon yanıtında bir kez döner.
    secret: str


class WebhookWithSecretEventFilters(TypedDict, total=False):
    """WebhookWithSecretEventFilters şeması."""

    event_names: List[str]


class WebhookWithSecretFilters(TypedDict, total=False):
    """WebhookWithSecretFilters şeması."""

    #: Zorunlu. Değerler: "all", "any".
    match: str
    #: Zorunlu.
    conditions: List["WebhookWithSecretFiltersConditionsItem"]


class WebhookWithSecretFiltersConditionsItem(TypedDict, total=False):
    """WebhookWithSecretFiltersConditionsItem şeması."""

    #: Zorunlu.
    field: str
    #: Zorunlu. Değerler: "eq", "neq", "in", "not_in", "starts_with", "contains", "exists", "not_exists".
    op: str
    value: Any


class WhatsAppTemplateList(TypedDict, total=False):
    """WhatsAppTemplateList şeması."""

    #: Zorunlu.
    data: List["WhatsAppTemplateListDataItem"]


class WhatsAppTemplateListDataItem(TypedDict, total=False):
    """WhatsAppTemplateListDataItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu.
    name: str
    #: Zorunlu.
    language: str
    #: Zorunlu.
    category: str
    #: Zorunlu.
    status: str
    #: Zorunlu.
    components: List[Dict[str, Any]]
    #: Zorunlu.
    body_params: int
    #: Zorunlu.
    rejected_reason: Optional[str]
    #: Zorunlu.
    quality_score: Optional[str]
    #: Zorunlu.
    synced_at: str


class WhatsAppTemplateSync(TypedDict, total=False):
    """WhatsAppTemplateSync şeması."""

    #: Zorunlu.
    total: int
    #: Zorunlu.
    removed: int
    #: Zorunlu.
    data: List["WhatsAppTemplateSyncDataItem"]


class WhatsAppTemplateSyncDataItem(TypedDict, total=False):
    """WhatsAppTemplateSyncDataItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    external_id: Optional[str]
    #: Zorunlu.
    name: str
    #: Zorunlu.
    language: str
    #: Zorunlu.
    category: str
    #: Zorunlu.
    status: str
    #: Zorunlu.
    components: List[Dict[str, Any]]
    #: Zorunlu.
    body_params: int
    #: Zorunlu.
    rejected_reason: Optional[str]
    #: Zorunlu.
    quality_score: Optional[str]
    #: Zorunlu.
    synced_at: str


class ZapierHook(TypedDict, total=False):
    """ZapierHook şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    event: str
    #: Zorunlu.
    event_name: Optional[str]
    #: Zorunlu.
    target_url: str
    #: Zorunlu.
    last_delivered_at: Optional[str]
    #: Zorunlu.
    failure_count: int
    #: Zorunlu.
    created_at: str


class ZapierMe(TypedDict, total=False):
    """ZapierMe şeması."""

    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    app_name: str
    #: Zorunlu.
    org_id: str
    #: Zorunlu.
    scopes: List[str]


class ZapierSamplesItem(TypedDict, total=False):
    """ZapierSamplesItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    type: str
    #: Zorunlu.
    created_at: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    data: Dict[str, Any]


class ZapierSubscribeDto(TypedDict, total=False):
    """ZapierSubscribeDto şeması."""

    #: Zorunlu.
    target_url: str
    #: Zorunlu. Değerler: "subscription.created", "subscription.unsubscribed", "event.received", "delivery.delivered", "delivery.opened", "delivery.clicked", "user.created", "user.updated", "conversion.created", "campaign.completed".
    event: str
    event_name: str


__all__ = [
    "AddAliasDto",
    "AddSubscriptionDto",
    "AddSubscriptionDtoDevice",
    "AddSubscriptionDtoOptIn",
    "ApiEventsDto",
    "ApiEventsDtoEventsItem",
    "ApiKey",
    "ApiKeyList",
    "App",
    "AppList",
    "AppPlatformFlags",
    "AppSettings",
    "AppSettingsAndroidChannelsItem",
    "AppSettingsFrequencyCap",
    "AppSettingsFrequencyCapsItem",
    "AppSettingsFrequencyCapsItemWindow",
    "AppSettingsInApp",
    "AppSettingsOnboarding",
    "AppSettingsPreferenceCenter",
    "AppSettingsPreferenceCenterTextsValue",
    "AppSettingsQuietHours",
    "AppSettingsSdkSetup",
    "AppSettingsSms",
    "AppSettingsWebPush",
    "AppSettingsWebPushClickBehavior",
    "AppSettingsWebPushCustomLink",
    "AppSettingsWebPushCustomLinkColor",
    "AppSettingsWebPushCustomLinkTextsValue",
    "AppSettingsWebPushPrompt",
    "AppSettingsWebPushPromptCategoriesItem",
    "AppSettingsWebPushPromptTextsValue",
    "AppSettingsWebPushWelcomeNotification",
    "AppSettingsWebPushWelcomeNotificationTextsValue",
    "AuditEntry",
    "AuditPage",
    "Campaign",
    "CampaignAbTest",
    "CampaignAbTestSignificance",
    "CampaignAbTestWinner",
    "CampaignApproval",
    "CampaignDelivery",
    "CampaignPage",
    "CampaignRecurrence",
    "CampaignsCreateBody",
    "CampaignsCreateBodyAbTest",
    "CampaignsCreateBodyAbTestWinner",
    "CampaignsCreateBodyAudience",
    "CampaignsCreateBodyAudienceFilters",
    "CampaignsCreateBodyDelivery",
    "CampaignsCreateBodyRecurrence",
    "CampaignsCreateBodyVariantsItem",
    "CampaignStats",
    "CampaignStats2",
    "CampaignStatsChannelsItem",
    "CampaignStatsErrorsItem",
    "CampaignStatsHourlyItem",
    "CampaignStatsRates",
    "CampaignsUpdateBody",
    "CampaignsUpdateBodyAbTest",
    "CampaignsUpdateBodyAbTestWinner",
    "CampaignsUpdateBodyAudience",
    "CampaignsUpdateBodyAudienceFilters",
    "CampaignsUpdateBodyDelivery",
    "CampaignsUpdateBodyRecurrence",
    "CampaignsUpdateBodyVariantsItem",
    "CampaignVariantsItem",
    "CampaignVariantStats",
    "CampaignVariantStatsAbTest",
    "CampaignVariantStatsAbTestSignificance",
    "CampaignVariantStatsAbTestWinner",
    "CampaignVariantStatsSignificance",
    "CampaignVariantStatsVariantsItem",
    "ChannelConfig",
    "ChannelConfigConfig",
    "ChannelConfigDnsCheck",
    "ChannelConfigDnsCheckDkim",
    "ChannelConfigDnsCheckDmarc",
    "ChannelConfigDnsCheckSpf",
    "ChannelList",
    "ChannelValidation",
    "ContentTable",
    "ContentTableList",
    "ContentTableRows",
    "Conversation",
    "ConversationMessagePage",
    "ConversationMessagePageDataItem",
    "ConversationPage",
    "ConversationReplyDto",
    "ConversationReplyDtoInteractive",
    "ConversationReplyDtoInteractiveButtonsItem",
    "ConversationReplyDtoInteractiveList",
    "ConversationReplyDtoInteractiveListSectionsItem",
    "ConversationReplyDtoInteractiveListSectionsItemRowsItem",
    "ConversationReplyDtoMedia",
    "ConversationReplyDtoTemplate",
    "ConversationReplyDtoTemplateButtonParamsItem",
    "ConversationReplyResult",
    "ConversationReplyResultConversationMessage",
    "ConversationWindow",
    "ConversionsReport",
    "ConversionsReportByCampaignItem",
    "ConversionsReportPrevious",
    "ConversionsReportRowsItem",
    "ConversionsReportTotals",
    "CopyTemplateDto",
    "CreateAppApiKeyDto",
    "CreateAppDto",
    "CreateAppDtoPlatformFlags",
    "CreateCategoryDto",
    "CreatedApiKey",
    "CreateDataFeedDto",
    "CreateExportDto",
    "CreateExportDtoFilters",
    "CreateIdentityKeyDto",
    "CreateInAppDto",
    "CreateInAppDtoAbTest",
    "CreateInAppDtoAbTestWinner",
    "CreateInAppDtoAudience",
    "CreateInAppDtoDisplay",
    "CreateInAppDtoFrequency",
    "CreateInAppDtoVariantsItem",
    "CreateInAppDtoVariantsItemDisplay",
    "CreateKeywordDto",
    "CreateKeywordDtoActions",
    "CreateKeywordDtoActionsEvent",
    "CreateKeywordDtoActionsReply",
    "CreateLiveActivityTypeDto",
    "CreateLiveActivityTypeDtoAttributesSchema",
    "CreateLiveActivityTypeDtoAttributesSchemaPropertiesValue",
    "CreateLiveActivityTypeDtoContentStateSchema",
    "CreateLiveActivityTypeDtoContentStateSchemaPropertiesValue",
    "CreateNotificationDto",
    "CreateNotificationDtoButtonsItem",
    "CreateNotificationDtoRcsCard",
    "CreateNotificationDtoTarget",
    "CreateNotificationDtoWebButtonsItem",
    "CreateNotificationDtoWhatsappInteractive",
    "CreateNotificationDtoWhatsappInteractiveButtonsItem",
    "CreateNotificationDtoWhatsappInteractiveList",
    "CreateNotificationDtoWhatsappInteractiveListSectionsItem",
    "CreateNotificationDtoWhatsappInteractiveListSectionsItemRowsItem",
    "CreateNotificationDtoWhatsappMedia",
    "CreateNotificationDtoWhatsappTemplate",
    "CreateNotificationDtoWhatsappTemplateButtonParamsItem",
    "CreateNotificationResult",
    "CreateSuppressionDto",
    "CreateTemplateDto",
    "CreateTemplateDtoContent",
    "CreateTemplateDtoContentButtonsItem",
    "CreateTemplateDtoContentRcsCard",
    "CreateTemplateDtoContentWebButtonsItem",
    "CreateTemplateDtoContentWhatsappInteractive",
    "CreateTemplateDtoContentWhatsappInteractiveButtonsItem",
    "CreateTemplateDtoContentWhatsappInteractiveList",
    "CreateTemplateDtoContentWhatsappInteractiveListSectionsItem",
    "CreateTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem",
    "CreateTemplateDtoContentWhatsappMedia",
    "CreateTemplateDtoContentWhatsappTemplate",
    "CreateTemplateDtoContentWhatsappTemplateButtonParamsItem",
    "CreateWarmupPlanDto",
    "CreateWarmupPlanDtoCurve",
    "CreateWarmupPlanDtoProviderShares",
    "CreateWebhookDto",
    "CreateWebhookDtoEventFilters",
    "CreateWebhookDtoFilters",
    "CreateWebhookDtoFiltersConditionsItem",
    "DataFeed",
    "DataFeedList",
    "DataFeedTestResult",
    "DataFeedTestResultUser",
    "DeliverabilitySettingsDto",
    "DeliverabilitySettingsDtoValidation",
    "DeliverabilitySettingsDtoVerifier",
    "Delivery",
    "DeliveryList",
    "EmailAddressCheck",
    "EmailDeliverabilitySettings",
    "EmailDeliverabilitySettingsValidation",
    "EmailDeliverabilitySettingsVerifier",
    "EmailWarmupPlan",
    "EmailWarmupPlanList",
    "EmailWarmupPlanToday",
    "EmailWarmupPlanTodayBucketsValue",
    "EmailWarmupUsage",
    "EmailWarmupUsageDataItem",
    "EndLiveActivityDto",
    "EndLiveActivityDtoAlert",
    "EngagementReport",
    "EngagementReportCellsItem",
    "EngagementReportPrevious",
    "EngagementReportRowsItem",
    "EngagementReportTotals",
    "EstimateAudienceDto",
    "EstimateAudienceDtoTarget",
    "EstimateAudienceResult",
    "EventDefinition",
    "EventDefinitionDetail",
    "EventDefinitionDetailDailyItem",
    "EventDefinitionDetailPropertiesItem",
    "EventDefinitionDetailPropertiesItemValuesItem",
    "EventDefinitionList",
    "EventsAccepted",
    "EventsReport",
    "EventsReportPrevious",
    "EventsReportRowsItem",
    "EventsReportTotals",
    "Export",
    "ExportFilters",
    "ExportList",
    "FunnelBodyDto",
    "FunnelBodyDtoStepsItem",
    "FunnelBodyDtoStepsItemWhere",
    "FunnelReport",
    "FunnelReportPrevious",
    "FunnelReportStepsItem",
    "IdentityKey",
    "IdentityKeyList",
    "Import",
    "ImportList",
    "ImportStats",
    "InAppMessage",
    "InAppMessageAbTest",
    "InAppMessageAbTestWinner",
    "InAppMessageAudience",
    "InAppMessageDisplay",
    "InAppMessageFrequency",
    "InAppMessagePage",
    "InAppMessageStats",
    "InAppMessageVariantSignificance",
    "InAppMessageVariantsItem",
    "InAppMessageVariantsItemDisplay",
    "InAppMessageVariantStatsItem",
    "InAppStatusDto",
    "InAppWinnerDto",
    "InboxItem",
    "InboxPage",
    "InboxReadAllResult",
    "IntegrationOk",
    "Journey",
    "JourneyDetail",
    "JourneyDetailEditing",
    "JourneyDetailIssuesItem",
    "JourneyDetailSummary",
    "JourneyPage",
    "JourneyPublishResult",
    "JourneyPublishResultIssuesItem",
    "JourneyRun",
    "JourneyRunDetail",
    "JourneyRunDetailStepsItem",
    "JourneyRunPage",
    "JourneysCreateBody",
    "JourneysCreateBodyGraph",
    "JourneysSaveDraftBody",
    "JourneysSaveDraftBodyGraph",
    "JourneyStats",
    "JourneyStatsGoalsItem",
    "JourneyStatsNodesItem",
    "JourneyStatsNodesItemVariantsItem",
    "JourneyStatsSummary",
    "JourneySummary",
    "JourneyTriggerResult",
    "JourneyVersionList",
    "JourneyVersionListDataItem",
    "LiveActivitySendResult",
    "LiveActivityTokenResult",
    "LiveActivityType",
    "LiveActivityTypeAttributesSchema",
    "LiveActivityTypeAttributesSchemaPropertiesValue",
    "LiveActivityTypeContentStateSchema",
    "LiveActivityTypeContentStateSchemaPropertiesValue",
    "LiveActivityTypeList",
    "McpCreateCampaignDraftBody",
    "McpCreateCampaignDraftBodyAbTest",
    "McpCreateCampaignDraftBodyAbTestWinner",
    "McpCreateCampaignDraftBodyAudience",
    "McpCreateCampaignDraftBodyAudienceFilters",
    "McpCreateCampaignDraftBodyDelivery",
    "McpCreateCampaignDraftBodyRecurrence",
    "McpCreateCampaignDraftBodyVariantsItem",
    "McpCreateSegmentDraftBody",
    "McpCreateSegmentDraftBodyDefinition",
    "Member",
    "MemberList",
    "Message",
    "MessageCategory",
    "MessageCategoryList",
    "MessageCounts",
    "MessageList",
    "MessageRequestedBy",
    "MessagesReport",
    "MessagesReportPrevious",
    "MessagesReportRowsItem",
    "MessagesReportTotals",
    "MessageVariantsItem",
    "Ok",
    "Org",
    "OrgSettings",
    "OrgSettingsAuditStream",
    "OverviewStats",
    "OverviewStatsChannelsItem",
    "OverviewStatsKpis",
    "OverviewStatsRecentCampaignsItem",
    "OverviewStatsSeriesItem",
    "OverviewStatsTopErrorsItem",
    "PatchEventDefinitionDto",
    "PatchSubscriptionDto",
    "PatchSubscriptionDtoDevice",
    "PatchUserDto",
    "PatchUserDtoDeltas",
    "PatchUserDtoDeltasPurchasesItem",
    "ProvidersReport",
    "ProvidersReportPrevious",
    "ProvidersReportRowsItem",
    "ProvidersReportRowsItemErrorsItem",
    "ProvidersReportTotals",
    "RenderPreview",
    "RenderPreviewButtonsItem",
    "RenderPreviewEmail",
    "RenderPreviewSms",
    "RenderTemplateDto",
    "RenderTemplateDtoContent",
    "RenderTemplateDtoContentButtonsItem",
    "RenderTemplateDtoContentRcsCard",
    "RenderTemplateDtoContentWebButtonsItem",
    "RenderTemplateDtoContentWhatsappInteractive",
    "RenderTemplateDtoContentWhatsappInteractiveButtonsItem",
    "RenderTemplateDtoContentWhatsappInteractiveList",
    "RenderTemplateDtoContentWhatsappInteractiveListSectionsItem",
    "RenderTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem",
    "RenderTemplateDtoContentWhatsappMedia",
    "RenderTemplateDtoContentWhatsappTemplate",
    "RenderTemplateDtoContentWhatsappTemplateButtonParamsItem",
    "RenderTemplateDtoUser",
    "RetentionReport",
    "RetentionReportCohortsItem",
    "ScheduleCampaignDto",
    "ScheduleCampaignDtoRecurrence",
    "Segment",
    "SegmentCampaigns",
    "SegmentCampaignsDataItem",
    "SegmentEstimate",
    "SegmentPage",
    "SegmentPreview",
    "SegmentPreviewSampleItem",
    "SegmentsCreateBody",
    "SegmentsCreateBodyDefinition",
    "SegmentsPreviewBody",
    "SegmentsPreviewBodyDefinition",
    "SegmentsUpdateBody",
    "SegmentsUpdateBodyDefinition",
    "SelectWinnerDto",
    "SetOwnerDto",
    "SetPreferencesDto",
    "SetPreferencesDtoPreferencesItem",
    "SmsKeyword",
    "SmsKeywordList",
    "StartLiveActivityDto",
    "StartLiveActivityDtoAlert",
    "StartLiveActivityDtoTarget",
    "Subscription",
    "SubscriptionDevice",
    "SubscriptionLocation",
    "SubscriptionsReport",
    "SubscriptionsReportByChannelItem",
    "SubscriptionsReportPrevious",
    "SubscriptionsReportRowsItem",
    "SubscriptionsReportTotals",
    "Suppression",
    "SuppressionPage",
    "Template",
    "TemplatePage",
    "TemplateStats",
    "TemplateVersionList",
    "TemplateVersionListDataItem",
    "TestDataFeedDto",
    "TriggerRunDto",
    "TriggerRunDtoAlias",
    "UpdateApiKeyDto",
    "UpdateAppDto",
    "UpdateAppDtoPlatformFlags",
    "UpdateAppDtoSettings",
    "UpdateAppDtoSettingsAndroidChannelsItem",
    "UpdateAppDtoSettingsFrequencyCap",
    "UpdateAppDtoSettingsFrequencyCapsItem",
    "UpdateAppDtoSettingsFrequencyCapsItemWindow",
    "UpdateAppDtoSettingsInApp",
    "UpdateAppDtoSettingsOnboarding",
    "UpdateAppDtoSettingsPreferenceCenter",
    "UpdateAppDtoSettingsPreferenceCenterTextsValue",
    "UpdateAppDtoSettingsQuietHours",
    "UpdateAppDtoSettingsSdkSetup",
    "UpdateAppDtoSettingsSms",
    "UpdateAppDtoSettingsWebPush",
    "UpdateAppDtoSettingsWebPushClickBehavior",
    "UpdateAppDtoSettingsWebPushCustomLink",
    "UpdateAppDtoSettingsWebPushCustomLinkColor",
    "UpdateAppDtoSettingsWebPushCustomLinkTextsValue",
    "UpdateAppDtoSettingsWebPushPrompt",
    "UpdateAppDtoSettingsWebPushPromptCategoriesItem",
    "UpdateAppDtoSettingsWebPushPromptTextsValue",
    "UpdateAppDtoSettingsWebPushWelcomeNotification",
    "UpdateAppDtoSettingsWebPushWelcomeNotificationTextsValue",
    "UpdateCategoryDto",
    "UpdateContentTableDto",
    "UpdateDataFeedDto",
    "UpdateInAppDto",
    "UpdateInAppDtoAbTest",
    "UpdateInAppDtoAbTestWinner",
    "UpdateInAppDtoAudience",
    "UpdateInAppDtoDisplay",
    "UpdateInAppDtoFrequency",
    "UpdateInAppDtoVariantsItem",
    "UpdateInAppDtoVariantsItemDisplay",
    "UpdateJourneyDto",
    "UpdateKeywordDto",
    "UpdateKeywordDtoActions",
    "UpdateKeywordDtoActionsEvent",
    "UpdateKeywordDtoActionsReply",
    "UpdateLiveActivityDto",
    "UpdateLiveActivityDtoAlert",
    "UpdateLiveActivityTypeDto",
    "UpdateLiveActivityTypeDtoAttributesSchema",
    "UpdateLiveActivityTypeDtoAttributesSchemaPropertiesValue",
    "UpdateLiveActivityTypeDtoContentStateSchema",
    "UpdateLiveActivityTypeDtoContentStateSchemaPropertiesValue",
    "UpdateNodeDto",
    "UpdateNodeDtoPosition",
    "UpdateTemplateDto",
    "UpdateTemplateDtoContent",
    "UpdateTemplateDtoContentButtonsItem",
    "UpdateTemplateDtoContentRcsCard",
    "UpdateTemplateDtoContentWebButtonsItem",
    "UpdateTemplateDtoContentWhatsappInteractive",
    "UpdateTemplateDtoContentWhatsappInteractiveButtonsItem",
    "UpdateTemplateDtoContentWhatsappInteractiveList",
    "UpdateTemplateDtoContentWhatsappInteractiveListSectionsItem",
    "UpdateTemplateDtoContentWhatsappInteractiveListSectionsItemRowsItem",
    "UpdateTemplateDtoContentWhatsappMedia",
    "UpdateTemplateDtoContentWhatsappTemplate",
    "UpdateTemplateDtoContentWhatsappTemplateButtonParamsItem",
    "UpdateWarehouseExportDto",
    "UpdateWarmupPlanDto",
    "UpdateWarmupPlanDtoProviderShares",
    "UpdateWebhookDto",
    "UpdateWebhookDtoEventFilters",
    "UpdateWebhookDtoFilters",
    "UpdateWebhookDtoFiltersConditionsItem",
    "UpsertUserDto",
    "UsageReport",
    "UsageReportAppsItem",
    "UsageReportDailyItem",
    "UsageReportMetricsItem",
    "UsageReportPeriod",
    "User",
    "UserDetail",
    "UserDetailAliasesItem",
    "UserExport",
    "UserExportEventsItem",
    "UserIdentity",
    "UserJourneyRuns",
    "UserJourneyRunsDataItem",
    "UserList",
    "UserPreferences",
    "UserPreferencesDataItem",
    "UsersSearchBody",
    "UsersSearchBodyDefinition",
    "VerifyAddressDto",
    "WarehouseConnectionResult",
    "WarehouseConnectionResultError",
    "WarehouseExport",
    "WarehouseExportCursorsValue",
    "WarehouseExportList",
    "WarehouseExportRun",
    "WarehouseExportRunPage",
    "WarehouseExportRunTablesValue",
    "WarehouseExportRunTablesValueFrom",
    "WarehouseExportRunTablesValueTo",
    "WarehouseTables",
    "WarehouseTablesDataItem",
    "WarehouseTablesDataItemColumnsItem",
    "Webhook",
    "WebhookDeliveryDetail",
    "WebhookDeliveryPage",
    "WebhookDeliveryPageDataItem",
    "WebhookEventFilters",
    "WebhookFilters",
    "WebhookFiltersConditionsItem",
    "WebhookList",
    "WebhookPreviewDto",
    "WebhookPreviewDtoFilters",
    "WebhookPreviewDtoFiltersConditionsItem",
    "WebhookPreviewResult",
    "WebhookPreviewResultError",
    "WebhookPreviewResultFailedConditionsItem",
    "WebhookWithSecret",
    "WebhookWithSecretEventFilters",
    "WebhookWithSecretFilters",
    "WebhookWithSecretFiltersConditionsItem",
    "WhatsAppTemplateList",
    "WhatsAppTemplateListDataItem",
    "WhatsAppTemplateSync",
    "WhatsAppTemplateSyncDataItem",
    "ZapierHook",
    "ZapierMe",
    "ZapierSamplesItem",
    "ZapierSubscribeDto",
]
