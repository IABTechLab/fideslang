from fideslang.models import DataUse

DEFAULT_DATA_USES = [
    #############
    # Analytics #
    #############
    DataUse(
        fides_key="analytics",
        name="Analytics",
        description="Provides analytics for activities such as system and advertising performance reporting, insights and fraud detection.",
        parent_key=None,
    ),
    DataUse(
        fides_key="analytics.reporting",
        name="Analytics for Reporting",
        description="Provides analytics for general reporting such as system and advertising performance.",
        parent_key="analytics",
    ),
    DataUse(
        fides_key="analytics.reporting.ad_performance",
        name="Analytics for Advertising Performance",
        description="Provides analytics for reporting of advertising performance.",
        parent_key="analytics.reporting",
    ),
    DataUse(
        fides_key="analytics.reporting.content_performance",
        name="Analytics for Content Performance",
        description="Analytics for reporting on content performance.",
        parent_key="analytics.reporting",
    ),
    DataUse(
        fides_key="analytics.reporting.campaign_insights",
        name="Analytics for Insights",
        description="Provides analytics for reporting of campaign insights related to advertising and promotion activities.",
        parent_key="analytics.reporting",
    ),
    DataUse(
        fides_key="analytics.reporting.system",
        name="Analytics for System Activity",
        description="Provides analytics for reporting on system activity.",
        parent_key="analytics.reporting",
    ),
    DataUse(
        fides_key="analytics.reporting.system.performance",
        name="Analytics for System Performance",
        description="Provides analytics for reporting on system performance.",
        parent_key="analytics.reporting.system",
    ),
    ###########
    # Collect #
    ###########
    DataUse(
        fides_key="collect",
        name="Collect",
        description="Collects or stores data in order to use it for another purpose which has not yet been expressly defined.",
        parent_key=None,
    ),
    ##############
    # Employment #
    ##############
    DataUse(
        fides_key="employment",
        name="Employment",
        description="Processes data for the purpose of recruitment or employment and human resources (HR) related activities.",
        parent_key=None,
    ),
    DataUse(
        fides_key="employment.recruitment",
        name="Employment Recruitment",
        description="Processes data of prospective employees for the purpose of recruitment.",
        parent_key="employment",
    ),
    #############
    # Essential #
    #############
    DataUse(
        fides_key="essential",
        name="Essential",
        description="Operates the service or product, including legal obligations, support and basic system operations.",
        parent_key=None,
    ),
    DataUse(
        fides_key="essential.fraud_detection",
        name="Essential Fraud Detection",
        description="Detects possible fraud or misuse of the product, service, application or system.",
        parent_key="essential",
    ),
    DataUse(
        fides_key="essential.legal_obligation",
        name="Essential Legal Obligation",
        description="Provides service to meet a legal or compliance obligation such as consent management.",
        parent_key="essential",
    ),
    DataUse(
        fides_key="essential.service",
        name="Essential for Service",
        description="Provides the essential product, service, application or system, without which the product/service would not be possible.",
        parent_key="essential",
    ),
    DataUse(
        fides_key="essential.service.authentication",
        name="Essential Service Authentication",
        description="Authenticate users to the product, service, application or system.",
        parent_key="essential.service",
    ),
    DataUse(
        fides_key="essential.service.notifications",
        name="Essential Service Notifications",
        description="Sends notifications about the product, service, application or system.",
        parent_key="essential.service",
    ),
    DataUse(
        fides_key="essential.service.notifications.email",
        name="Essential Email Service Notifications",
        description="Sends email notifications about the product, service, application or system.",
        parent_key="essential.service.notifications",
    ),
    DataUse(
        fides_key="essential.service.notifications.sms",
        name="Essential SMS Service Notifications",
        description="Sends SMS notifications about the product, service, application or system.",
        parent_key="essential.service.notifications",
    ),
    DataUse(
        fides_key="essential.service.operations",
        name="Essential for Operations",
        description="Essential to ensure the operation of the product, service, application or system.",
        parent_key="essential.service",
    ),
    DataUse(
        fides_key="essential.service.operations.support",
        name="Essential for Operations Support",
        description="Provides support for the product, service, application or system.",
        parent_key="essential.service.operations",
    ),
    DataUse(
        fides_key="essential.service.operations.improve",
        name="Essential for Support Improvement",
        description="Essential to optimize and improve support for the product, service, application or system.",
        parent_key="essential.service.operations",
    ),
    DataUse(
        fides_key="essential.service.payment_processing",
        name="Essential for Payment Processing",
        description="Essential to processes payments for the product, service, application or system.",
        parent_key="essential.service",
    ),
    DataUse(
        fides_key="essential.service.security",
        name="Essential for Security",
        description="Essential to provide security for the product, service, application or system",
        parent_key="essential.service",
    ),
    DataUse(
        fides_key="essential.service.upgrades",
        name="Essential for Service Upgrades",
        description="Provides timely system upgrade information options.",
        parent_key="essential.service",
    ),
    # Finance
    DataUse(
        fides_key="finance",
        name="Finance",
        description="Enables finance and accounting activities such as audits and tax reporting.",
        parent_key=None,
    ),
    ##############
    # Functional #
    ##############
    DataUse(
        fides_key="functional",
        name="Functional",
        description="Used for specific, necessary, and legitimate purposes",
        parent_key=None,
    ),
    DataUse(
        fides_key="functional.storage",
        name="Local Data Storage",
        description="Stores or accesses information from the device as needed when using a product, service, application, or system",
        parent_key="functional",
    ),
    DataUse(
        fides_key="functional.service",
        name="Service",
        description="Functions relating to provided services, products, applications or systems.",
        parent_key="functional",
    ),
    DataUse(
        fides_key="functional.service.improve",
        name="Improve Service",
        description="Improves the specific product, service, application or system.",
        parent_key="functional.service",
    ),
    #############
    # Marketing #
    #############
    DataUse(
        fides_key="marketing",
        name="Marketing",
        description="Enables marketing, promotion, advertising and sales activities for the product, service, application or system.",
        parent_key=None,
    ),
    #########################
    # marketing.advertising #
    #########################
    DataUse(
        fides_key="marketing.advertising",
        name="Advertising, Marketing or Promotion",
        description="Advertises or promotes the product, service, application or system and associated services.",
        parent_key="marketing",
    ),
    DataUse(
        fides_key="marketing.advertising.first_party",
        name="First Party Advertising",
        description="Serves advertisements based on first party data collected or derived about the user.",
        parent_key="marketing.advertising",
    ),
    DataUse(
        fides_key="marketing.advertising.first_party.contextual",
        name="First Party Contextual Advertising",
        description="Serves advertisements based on current content being viewed by the user of the system or service.",
        parent_key="marketing.advertising.first_party",
    ),
    DataUse(
        fides_key="marketing.advertising.first_party.targeted",
        name="First Party Personalized Advertising",
        description="Targets advertisements based on data collected or derived about the user from use of the system.",
        parent_key="marketing.advertising.first_party",
    ),
    DataUse(
        fides_key="marketing.advertising.frequency_capping",
        name="Frequency Capping",
        description="Restricts the number of times a specific advertisement is shown to an individual.",
        parent_key="marketing.advertising",
    ),
    DataUse(
        fides_key="marketing.advertising.negative_targeting",
        name="Negative Targeting",
        description="Enforces rules used to ensure a certain audience or group is not targeted by advertising.",
        parent_key="marketing.advertising",
    ),
    DataUse(
        fides_key="marketing.advertising.profiling",
        name="Profiling for Advertising",
        description="Creates audience profiles for the purpose of targeted advertising",
        parent_key="marketing.advertising",
    ),
    DataUse(
        fides_key="marketing.advertising.serving",
        name="Essential for Serving Ads",
        description="Essential to the delivery of advertising and content.",
        parent_key="marketing.advertising",
    ),
    DataUse(
        fides_key="marketing.advertising.third_party",
        name="Third Party Advertising",
        description="Serves advertisements based on data within the system or joined with data provided by 3rd parties.",
        parent_key="marketing.advertising",
    ),
    DataUse(
        fides_key="marketing.advertising.third_party.targeted",
        name="Third Party Targeted Advertising",
        description="Targets advertisements based on data within the system or joined with data provided by 3rd parties.",
        parent_key="marketing.advertising.third_party",
    ),
    ############################
    # marketing.communications #
    ############################
    DataUse(
        fides_key="marketing.communications",
        name="Marketing Communications",
        description="Uses combined channels to message and market to a customer, user or prospect.",
        parent_key="marketing",
    ),
    DataUse(
        fides_key="marketing.communications.email",
        name="Marketing Email Communications",
        description="Sends email marketing communications.",
        parent_key="marketing.communications",
    ),
    DataUse(
        fides_key="marketing.communications.sms",
        name="Marketing SMS Communications",
        description="Sends SMS marketing communications.",
        parent_key="marketing.communications",
    ),
    ##############
    # Operations #
    ##############
    DataUse(
        fides_key="operations",
        name="Operations",
        description="Supports business processes necessary to the organization's operation.",
        parent_key=None,
    ),
    ###############
    # Personalize #
    ###############
    DataUse(
        fides_key="personalize",
        name="Personalize",
        description="Personalizes the product, service, application or system.",
        parent_key=None,
    ),
    DataUse(
        fides_key="personalize.content",
        name="Content Personalization",
        description="Personalizes the content of the product, service, application or system.",
        parent_key="personalize",
    ),
    DataUse(
        fides_key="personalize.profiling",
        name="Personalized Profiling",
        description="Creates profiles for the purpose of serving content.",
        parent_key="personalize",
    ),
    DataUse(
        fides_key="personalize.system",
        name="System Personalization",
        description="Personalizes the system.",
        parent_key="personalize",
    ),
    #########
    # Sales #
    #########
    DataUse(
        fides_key="sales",
        name="Sales",
        description="Supports sales activities such as communications and outreach.",
        parent_key=None,
    ),
    #######################
    # Third-Party Sharing #
    #######################
    DataUse(
        fides_key="third_party_sharing",
        name="Third Party Sharing",
        description="Transfers data to third parties outside of the system or service's scope.",
        parent_key=None,
    ),
    DataUse(
        fides_key="third_party_sharing.legal_obligation",
        name="Sharing for Legal Obligation",
        description="Shares data for legal obligations, including contracts, applicable laws or regulations.",
        parent_key="third_party_sharing",
    ),
    ###################
    # Train AI System #
    ###################
    DataUse(
        fides_key="train_ai_system",
        name="Train AI System",
        description="Trains an AI system or data model for machine learning.",
        parent_key=None,
    ),
]

for category in DEFAULT_DATA_USES:
    category.is_default = True
