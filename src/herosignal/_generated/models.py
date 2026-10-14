# Bu dosya api/openapi.yaml'dan sdk/scripts/generate-server-sdks.mjs ile üretilmiştir; elle düzenlemeyin.
"""API şemalarının TypedDict karşılıkları (çalışma zamanında sade ``dict``)."""

from typing import Any, Dict, List, Optional, TypedDict


class AddAliasDto(TypedDict, total=False):
    """AddAliasDto şeması."""

    #: Zorunlu.
    identity: Dict[str, str]


class AddSubscriptionDto(TypedDict, total=False):
    """AddSubscriptionDto şeması."""

    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
    channel: str
    #: Zorunlu.
    token: str
    device: "AddSubscriptionDtoDevice"
    #: Değerler: "subscribed", "unsubscribed".
    status: str


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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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

    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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

    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
    channel: str
    #: Zorunlu. Değerler: "apns", "fcm", "webpush", "smtp", "ses", "resend", "twilio", "netgsm", "mock".
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
    #: Zorunlu. Değerler: "admin", "notifications:write", "users:read", "users:write", "events:write", "segments:read", "analytics:read".
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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
        # Değerler: "ios_push", "android_push", "web_push", "email", "sms".
        "channel": str,
        "segment_id": str,
    },
    total=False,
)


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
    #: Zorunlu.
    blocks: List[Any]


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


class CreateNotificationDtoTarget(TypedDict, total=False):
    """CreateNotificationDtoTarget şeması."""

    all: bool
    include_subscription_ids: List[str]
    include_external_ids: List[str]
    include_aliases: Dict[str, List[str]]
    included_segments: List[str]
    excluded_segments: List[str]
    filters: Any
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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

    #: Zorunlu. Değerler: "email", "sms".
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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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


class CreateTemplateDtoContentButtonsItem(TypedDict, total=False):
    """CreateTemplateDtoContentButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class CreateTemplateDtoContentWebButtonsItem(TypedDict, total=False):
    """CreateTemplateDtoContentWebButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class CreateWebhookDto(TypedDict, total=False):
    """CreateWebhookDto şeması."""

    #: Zorunlu.
    url: str
    description: Optional[str]
    #: Zorunlu. Değerler: "message.queued", "message.completed", "message.failed", "delivery.sent", "delivery.delivered", "delivery.failed", "delivery.opened", "delivery.clicked", "delivery.bounced", "delivery.complained", "delivery.unsubscribed", "in_app.impression", "in_app.clicked", "in_app.dismissed", "subscription.created", "subscription.unsubscribed", "subscription.invalidated", "user.created", "user.updated", "user.merged", "user.deleted", "event.received", "conversion.created", "campaign.scheduled", "campaign.started", "campaign.completed", "journey.entered", "journey.step_completed", "journey.completed", "journey.exited".
    events: List[str]
    event_filters: "CreateWebhookDtoEventFilters"
    batch: bool
    headers: Dict[str, str]


class CreateWebhookDtoEventFilters(TypedDict, total=False):
    """CreateWebhookDtoEventFilters şeması."""

    event_names: List[str]


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
    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
        # Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
    #: Zorunlu.
    blocks: List[Any]


class InAppMessageVariantSignificance(TypedDict, total=False):
    """InAppMessageVariantSignificance şeması."""

    #: Zorunlu.
    leader: Optional[str]
    #: Zorunlu.
    p_value: float
    #: Zorunlu.
    significant: bool


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


class OrgSettings(TypedDict, total=False):
    """OrgSettings şeması."""

    mfaRequired: bool
    ipAllowlist: List[str]
    retentionDays: int
    sessionMaxHours: int


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

    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
    channel: str
    #: Zorunlu. Değerler: "apns", "fcm", "webpush", "smtp", "ses", "resend", "twilio", "netgsm", "mock".
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

    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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

    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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


class RenderTemplateDtoContentButtonsItem(TypedDict, total=False):
    """RenderTemplateDtoContentButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class RenderTemplateDtoContentWebButtonsItem(TypedDict, total=False):
    """RenderTemplateDtoContentWebButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
    channel: Optional[str]
    #: Zorunlu.
    opted_in: bool


class Subscription(TypedDict, total=False):
    """Subscription şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    app_id: str
    #: Zorunlu.
    user_id: Optional[str]
    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
    unsubscribed_at: Optional[str]
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
    #: Zorunlu. Değerler: "email", "sms".
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
    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
    #: Değerler: "admin", "notifications:write", "users:read", "users:write", "events:write", "segments:read", "analytics:read".
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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
    channels: Optional[List[str]]
    default_opted_in: bool
    position: int


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
    #: Zorunlu.
    blocks: List[Any]


class UpdateJourneyDto(TypedDict, total=False):
    """UpdateJourneyDto şeması."""

    name: str
    description: Optional[str]


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
    #: Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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


class UpdateTemplateDtoContentButtonsItem(TypedDict, total=False):
    """UpdateTemplateDtoContentButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class UpdateTemplateDtoContentWebButtonsItem(TypedDict, total=False):
    """UpdateTemplateDtoContentWebButtonsItem şeması."""

    #: Zorunlu.
    id: str
    #: Zorunlu.
    text: str
    icon: str
    url: str


class UpdateWebhookDto(TypedDict, total=False):
    """UpdateWebhookDto şeması."""

    url: str
    description: Optional[str]
    #: Değerler: "message.queued", "message.completed", "message.failed", "delivery.sent", "delivery.delivered", "delivery.failed", "delivery.opened", "delivery.clicked", "delivery.bounced", "delivery.complained", "delivery.unsubscribed", "in_app.impression", "in_app.clicked", "in_app.dismissed", "subscription.created", "subscription.unsubscribed", "subscription.invalidated", "user.created", "user.updated", "user.merged", "user.deleted", "event.received", "conversion.created", "campaign.scheduled", "campaign.started", "campaign.completed", "journey.entered", "journey.step_completed", "journey.completed", "journey.exited".
    events: List[str]
    event_filters: "UpdateWebhookDtoEventFilters"
    batch: bool
    headers: Optional[Dict[str, str]]
    #: Değerler: "active", "disabled".
    status: str


class UpdateWebhookDtoEventFilters(TypedDict, total=False):
    """UpdateWebhookDtoEventFilters şeması."""

    event_names: List[str]


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
    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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
    #: Zorunlu. Değerler: "ios_push", "android_push", "web_push", "email", "sms".
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


class WebhookList(TypedDict, total=False):
    """WebhookList şeması."""

    #: Zorunlu.
    data: List["Webhook"]


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
    created_at: str
    #: Zorunlu.
    updated_at: str
    #: Zorunlu. Yalnızca oluşturma ve rotasyon yanıtında bir kez döner.
    secret: str


class WebhookWithSecretEventFilters(TypedDict, total=False):
    """WebhookWithSecretEventFilters şeması."""

    event_names: List[str]


__all__ = [
    "AddAliasDto",
    "AddSubscriptionDto",
    "AddSubscriptionDtoDevice",
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
    "CreateExportDto",
    "CreateExportDtoFilters",
    "CreateInAppDto",
    "CreateInAppDtoAbTest",
    "CreateInAppDtoAbTestWinner",
    "CreateInAppDtoAudience",
    "CreateInAppDtoDisplay",
    "CreateInAppDtoFrequency",
    "CreateInAppDtoVariantsItem",
    "CreateInAppDtoVariantsItemDisplay",
    "CreateNotificationDto",
    "CreateNotificationDtoButtonsItem",
    "CreateNotificationDtoTarget",
    "CreateNotificationDtoWebButtonsItem",
    "CreateNotificationResult",
    "CreateSuppressionDto",
    "CreateTemplateDto",
    "CreateTemplateDtoContent",
    "CreateTemplateDtoContentButtonsItem",
    "CreateTemplateDtoContentWebButtonsItem",
    "CreateWebhookDto",
    "CreateWebhookDtoEventFilters",
    "Delivery",
    "DeliveryList",
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
    "InAppMessageVariantsItem",
    "InAppMessageVariantsItemDisplay",
    "InAppMessageVariantSignificance",
    "InAppMessageVariantStatsItem",
    "InAppStatusDto",
    "InAppWinnerDto",
    "InboxItem",
    "InboxPage",
    "InboxReadAllResult",
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
    "RenderTemplateDtoContentWebButtonsItem",
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
    "Subscription",
    "SubscriptionDevice",
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
    "UpdateInAppDto",
    "UpdateInAppDtoAbTest",
    "UpdateInAppDtoAbTestWinner",
    "UpdateInAppDtoAudience",
    "UpdateInAppDtoDisplay",
    "UpdateInAppDtoFrequency",
    "UpdateInAppDtoVariantsItem",
    "UpdateInAppDtoVariantsItemDisplay",
    "UpdateJourneyDto",
    "UpdateNodeDto",
    "UpdateNodeDtoPosition",
    "UpdateTemplateDto",
    "UpdateTemplateDtoContent",
    "UpdateTemplateDtoContentButtonsItem",
    "UpdateTemplateDtoContentWebButtonsItem",
    "UpdateWebhookDto",
    "UpdateWebhookDtoEventFilters",
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
    "Webhook",
    "WebhookDeliveryDetail",
    "WebhookDeliveryPage",
    "WebhookDeliveryPageDataItem",
    "WebhookEventFilters",
    "WebhookList",
    "WebhookWithSecret",
    "WebhookWithSecretEventFilters",
]
