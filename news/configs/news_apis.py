from django.conf import settings

IS_CONFIGURED = False

if not IS_CONFIGURED:
    EventRegistryKey = settings.EVENT_REGISTRY_KEY
    IS_CONFIGURED = True
