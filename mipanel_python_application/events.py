from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class CommonsEvents(ExtendedEnum):
    TransformViaAPI = "TransformViaAPI"
    TransformViaWeb = "TransformViaWeb"
    Transform_Failed = "Transform_Failed"


class PortalEvents(ExtendedEnum):
    PortalPublishingCompleteFailure = "PortalPublishingCompleteFailure"
    PortalPublishingSuccess = "PortalPublishingSuccess"
    EmbeddableDevPortalPreviewed = "EmbeddableDevPortalPreviewed"
    OnPremPortalGeneration = "OnPremPortalGeneration"
    OnPremPortalGenerationFailure = "OnPremPortalGenerationFailure"


class CodeGenEvents(ExtendedEnum):
    SDKGenerated_API = "SDKGenerated_API"
    SDKGenerated_WEBSITE = "SDKGenerated_WEBSITE"
    SDKGenerated_WIDGET = "SDKGenerated_WIDGET"
    Failed_SDKGenerated_API = "Failed: SDKGenerated_API"
    Failed_SDKGenerated_WEBSITE = "Failed: SDKGenerated_WEBSITE"
    Failed_SDKGenerated_WIDGET = "Failed: SDKGenerated_WIDGET"


class CGaaSEvents(ExtendedEnum):
    TransformViaAPI = "TransformViaAPI"
    Failed_SDKGenerated_API = "Failed: SDKGenerated_API"
    SDKGenerated_API = "SDKGenerated_API"
    SignUp = "SignUp"
    Transform_Failed = "Transform_Failed"
    OnPremPortalGeneration = "OnPremPortalGeneration"
    OnPremPortalGenerationFailure = "OnPremPortalGenerationFailure"



