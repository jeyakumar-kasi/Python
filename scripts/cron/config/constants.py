import time
import string
from zoneinfo import ZoneInfo
from datetime import datetime
from enum import StrEnum, UNIQUE, verify
from config import settings
from enum import Enum


def get_current_epoch_time():
    return int(time.time() * 1000)


def get_current_date_time():
    return datetime.now().replace(tzinfo=ZoneInfo('Asia/Kolkata'))


class Constants:
    SALARIED_CBILL = 600
    SEP_SENP_CBILL = 575
    NTC_CIBIL = 300
    ASSIGNEE_ROLE = 'Assignee'
    ASSIGNOR_ROLE = 'Assignor'
    SECTION_LIST = [
        'Applicant/Co-applicant',
        'loan-details',
        'document',
        'co-applicant',
        'guarantor',
        'property',
        'references',
        'bank-details',
        'technical',
    ]
    REJECT_REASONS = [
        'CNI- Loan no longer required',
        'CNI-Loan already processed elsewhere',
        'CNI-Interest Rate- Better offer from outside',
        'CNI-Interest Rate-Too high to afford',
        'CNI-Both Interest Rate and Sanctioned Amount-Better offer from outside',
        'CNI-Concerns with the Repayment Period',
        'CNI-Concerns around processing and other charges',
        'CNI-High Insurance Amount',
        'Duplicate Application',
        'CIBIL Negative/Poor RTR',
        'Income Eligibility Not Met',
        'Dedupe Reject',
        'PD Negative Reject',
        'RCU Negative',
        'Legal Negative',
        'Technical Negative',
        'Suspicious Transaction',
        'Fraudlent Transaction',
        'Incomplete Documents',
        'Fraudlent Documentation',
        'Loan Eligibility not meeting Requirement',
        'Underwriting Model Output Red - Applicant - High Probablity of Default',
        'Underwriting Model Output Red - Coapplicant - Overall High Probablity of Default',
        'Underwriting Model Output Amber - Rejected during Underwriting review',
        'Hunter Response is Negative',
        'Collateral ineligible for funding',
        'Others',
    ]
    TOKEN_EXPIRED = 'Token Expired'
    INVALID_TOKEN = 'Invalid Token'
    TEST_BASE_URL = 'http://testserver'
    TEST_ANYIO_BACKEND = 'asyncio'
    DEFAULT_NO_OF_RETRIES = 3
    NOVEL_EXCEL_FRAUD_SHEET_NAME = 'Fraud Indicators'
    BUREAU_CHECK_WAIVER_SCORE_LIMIT = 750
    ADD_CO_APPLICANT_LIMIT = 1
    ADD_GUARANTOR_LIMIT = 1

    if settings.ENV_NAME == 'DEV':
        FROM_PRAGATI_NEW_LEAD_KAFKA_TOPIC = 'pragati_ilos_lead_data'
        ASSIGNMENT_LEAD_KAFKA_TOPIC = 'local_ilos_lead_assignment'
        GROUP_FROM_PRAGATI_NEW_LEAD_KAFKA_TOPIC = 'grp_pragati_ilos_lead_data'
        EMAIL_NOTIFICATION_TOPIC = 'email_notification'
        SMS_NOTIFICATION_TOPIC = 'sms_notification'
        # GROUP_EMAIL_NOTIFICATION_TOPIC = 'grp_local_email_topic'
        # GROUP_NOTIFICATION_TOPIC = 'grp_local_sms_topic'
        # PRAGATI_PUSH_NOTIFICATION_TOPIC = 'pragati_push_notification_topic'
        # GROUP_PRAGATI_PUSH_NOTIFICATION_TOPIC = 'grp_local_pragati_push_notification_topic'
        PRAGATI_QUERY_NOTIFICATION_TOPIC = 'pragati_query_notification_topic'
        PDF_GENERATION_TOPIC = 'local_ilos_form_pdf_generation_topic'
        FLEXCUBE_DEDUPE_TOPIC = 'local_ilos_flexcube_dedupe_topic'
        FLEXCUBE_COMMUNICATION_TOPIC = 'local_ilos_flexcube_communication_topic'
        GROUP_PDF_GENERATION_TOPIC = 'grp_local_ilos_form_pdf_generation_topic'
        GROUP_FLEXCUBE_DEDUPE_TOPIC = 'grp_local_ilos_flexcube_dedupe_topic'
        GROUP_FLEXCUBE_COMMUNICATION_TOPIC = 'grp_local_ilos_flexcube_communication_topic'
        GROUP_LEAD_ASSIGNMENT_TOPIC = 'grp_local_ilos_lead_assignment'
        TO_PRAGATI_LEAD_UPDATE_TOPIC = 'to_pragati_lead_update_topic'
        FROM_PRAGATI_LEAD_UPDATE_TOPIC = 'from_pragati_lead_update_topic'
        GROUP_FROM_PRAGATI_LEAD_UPDATE_TOPIC = 'grp_from_pragati_lead_update_topic'
        FROM_CORE_ESIGN_CALLBACK_TOPIC = 'core_esign_callback_topic'
        GROUP_FROM_CORE_ESIGN_CALLBACK_TOPIC = 'grp_core_esign_callback_topic'
        UNDERWRITING_TO_IPA_TOPIC = 'underwriting_to_ipa_topic'
        UNDERWRITING_GENERIC_TOPIC = 'underwriting_generic_topic'
        NOVEL_CALLBACK_TOPIC = 'novel_callback_topic'
        NOVEL_CALLBACK_GROUP = 'grp_novel_callback_topic'
        BRANCH_MASTER_ACCESS_TOKEN = "Q3ViZUFQSQ=="
        BRANCH_MASTER_VENDOR = "Test"
        BRANCH_MASTER_API_TYPE = "BranchAPI"
        FROM_ILOS_TO_VERIFICATION_TOPIC = 'local_ilos_to_verification'
        FROM_ILOS_TO_VERIFICATION_GROUP = 'grp_ilos_to_verification'
        FROM_VERIFICATION_TO_ILOS_TOPIC = 'local_verification_to_ilos'
        FROM_VERIFICATION_TO_ILOS_GROUP = 'grp_verification_to_ilos'
        PD_CONSUMER = 'pd_consumer'
        DMS_BUCKET_BASE_URL = 'https://capriglobal-dev.s3.ap-south-1.amazonaws.com'
        TECHNICAL_VERIFICATION_TOPIC = 'local_technical_verification_topic'
        TECHNICAL_VERIFICATION_TOPIC_GROUP = 'grp_local_technical_verification_topic'

    elif settings.ENV_NAME == 'UAT':
        DMS_BUCKET_BASE_URL = 'https://pragati-uat-bucket.s3.ap-south-1.amazonaws.com'
        FROM_PRAGATI_NEW_LEAD_KAFKA_TOPIC = 'uat_pragati_ilos_lead_data'
        ASSIGNMENT_LEAD_KAFKA_TOPIC = 'uat_ilos_lead_assignment'
        GROUP_FROM_PRAGATI_NEW_LEAD_KAFKA_TOPIC = 'grp_uat_pragati_ilos_lead_data'
        EMAIL_NOTIFICATION_TOPIC = 'email_notification'
        SMS_NOTIFICATION_TOPIC = 'sms_notification'
        # GROUP_EMAIL_NOTIFICATION_TOPIC = 'grp_local_email_topic'
        # GROUP_NOTIFICATION_TOPIC = 'grp_local_sms_topic'
        # PRAGATI_PUSH_NOTIFICATION_TOPIC = 'uat_pragati_push_notification_topic'
        # GROUP_PRAGATI_PUSH_NOTIFICATION_TOPIC = 'grp_uat_pragati_push_notification_topic'
        PRAGATI_QUERY_NOTIFICATION_TOPIC = 'uat_pragati_query_notification_topic'
        PDF_GENERATION_TOPIC = 'uat_ilos_form_pdf_generation_topic'
        FLEXCUBE_DEDUPE_TOPIC = 'uat_ilos_flexcube_dedupe_topic'
        FLEXCUBE_COMMUNICATION_TOPIC = 'uat_ilos_flexcube_communication_topic'
        GROUP_PDF_GENERATION_TOPIC = 'grp_uat_ilos_form_pdf_generation_topic'
        GROUP_FLEXCUBE_DEDUPE_TOPIC = 'grp_uat_ilos_flexcube_dedupe_topic'
        GROUP_FLEXCUBE_COMMUNICATION_TOPIC = 'grp_uat_ilos_flexcube_communication_topic'
        GROUP_LEAD_ASSIGNMENT_TOPIC = 'uat_grp_ilos_lead_assignment'
        TO_PRAGATI_LEAD_UPDATE_TOPIC = 'uat_to_pragati_lead_update_topic'
        FROM_PRAGATI_LEAD_UPDATE_TOPIC = 'uat_from_pragati_lead_update_topic'
        GROUP_FROM_PRAGATI_LEAD_UPDATE_TOPIC = 'grp_uat_FROM_PRAGATI_LEAD_UPDATE_TOPIC'
        FROM_CORE_ESIGN_CALLBACK_TOPIC = 'core_esign_callback_topic'
        GROUP_FROM_CORE_ESIGN_CALLBACK_TOPIC = 'grp_uat_core_esign_callback_topic'
        UNDERWRITING_TO_IPA_TOPIC = 'uat_underwriting_to_ipa_topic'
        UNDERWRITING_GENERIC_TOPIC = 'uat_underwriting_generic_topic'
        NOVEL_CALLBACK_TOPIC = 'novel_callback_topic'
        NOVEL_CALLBACK_GROUP = 'grp_uat_novel_callback_topic'
        BRANCH_MASTER_ACCESS_TOKEN = "Q3ViZUFQSQ=="
        BRANCH_MASTER_VENDOR = "Test"
        BRANCH_MASTER_API_TYPE = "BranchAPI"
        FROM_ILOS_TO_VERIFICATION_TOPIC = 'uat_ilos_to_verification'
        FROM_ILOS_TO_VERIFICATION_GROUP = 'grp_uat_ilos_to_verification'
        FROM_VERIFICATION_TO_ILOS_TOPIC = 'uat_verification_to_ilos'
        FROM_VERIFICATION_TO_ILOS_GROUP = 'grp_uat_verification_to_ilos'
        TECHNICAL_VERIFICATION_TOPIC = 'uat_technical_verification_topic'
        TECHNICAL_VERIFICATION_TOPIC_GROUP = 'grp_uat_technical_verification_topic'

    else:
        DMS_BUCKET_BASE_URL = ''
        FROM_PRAGATI_NEW_LEAD_KAFKA_TOPIC = 'prod_pragati_ilos_lead_data'
        ASSIGNMENT_LEAD_KAFKA_TOPIC = 'prod_ilos_lead_assignment'
        GROUP_FROM_PRAGATI_NEW_LEAD_KAFKA_TOPIC = 'grp_prod_pragati_ilos_lead_data'
        EMAIL_NOTIFICATION_TOPIC = 'email_notification'
        SMS_NOTIFICATION_TOPIC = 'sms_notification'
        # GROUP_EMAIL_NOTIFICATION_TOPIC = 'grp_local_email_topic'
        # GROUP_NOTIFICATION_TOPIC = 'grp_local_sms_topic'
        # PRAGATI_PUSH_NOTIFICATION_TOPIC = 'pragati_push_notification_topic'
        # GROUP_PRAGATI_PUSH_NOTIFICATION_TOPIC = 'grp_local_pragati_push_notification_topic'
        PRAGATI_QUERY_NOTIFICATION_TOPIC = 'pragati_query_notification_topic'
        PDF_GENERATION_TOPIC = 'prod_ilos_form_pdf_generation_topic'
        FLEXCUBE_DEDUPE_TOPIC = 'prod_ilos_flexcube_dedupe_topic'
        FLEXCUBE_COMMUNICATION_TOPIC = 'prod_ilos_flexcube_communication_topic'
        GROUP_PDF_GENERATION_TOPIC = 'prod_ilos_form_pdf_generation_topic'
        GROUP_FLEXCUBE_DEDUPE_TOPIC = 'grp_prod_ilos_flexcube_dedupe_topic'
        GROUP_FLEXCUBE_COMMUNICATION_TOPIC = 'grp_prod_ilos_flexcube_communication_topic'
        GROUP_LEAD_ASSIGNMENT_TOPIC = 'prod_local_ilos_lead_assignment'
        TO_PRAGATI_LEAD_UPDATE_TOPIC = 'to_pragati_lead_update_topic'
        FROM_PRAGATI_LEAD_UPDATE_TOPIC = 'prod_from_pragati_lead_update_topic'
        GROUP_FROM_PRAGATI_LEAD_UPDATE_TOPIC = 'grp_prod_FROM_PRAGATI_LEAD_UPDATE_TOPIC'
        FROM_CORE_ESIGN_CALLBACK_TOPIC = 'core_esign_callback_topic'
        GROUP_FROM_CORE_ESIGN_CALLBACK_TOPIC = 'grp_core_esign_callback_topic'
        UNDERWRITING_TO_IPA_TOPIC = 'underwriting_to_ipa_topic'
        UNDERWRITING_GENERIC_TOPIC = 'underwriting_generic_topic'
        NOVEL_CALLBACK_TOPIC = 'novel_callback_topic'
        NOVEL_CALLBACK_GROUP = 'grp_novel_callback_topic'
        BRANCH_MASTER_ACCESS_TOKEN = "Q3ViZUFQSQ=="
        BRANCH_MASTER_VENDOR = "Test"
        BRANCH_MASTER_API_TYPE = "BranchAPI"
        FROM_ILOS_TO_VERIFICATION_TOPIC = 'prod_ilos_to_verification'
        FROM_ILOS_TO_VERIFICATION_GROUP = 'grp_prod_ilos_to_verification'
        FROM_VERIFICATION_TO_ILOS_TOPIC = 'prod_verification_to_ilos'
        FROM_VERIFICATION_TO_ILOS_GROUP = 'grp_prod_verification_to_ilos'
        TECHNICAL_VERIFICATION_TOPIC = 'prod_technical_verification_topic'
        TECHNICAL_VERIFICATION_TOPIC_GROUP = 'grp_prod_technical_verification_topic'


@verify(UNIQUE)
class CPUStatusEnum(StrEnum):
    OPEN = 'OPEN'
    PENDING = 'PENDING'
    SUBMITTED = 'SUBMITTED'
    SENT_TO_CUSTOMER_REVIEW = 'SENT_TO_CUSTOMER_REVIEW'
    CUSTOMER_REVIEW_DONE = 'CUSTOMER_REVIEW_DONE'
    REPLIED_BY_RM = 'REPLIED_BY_RM'


@verify(UNIQUE)
class LeadStatusEnum(StrEnum):
    OPEN = 'SUBMITTED_TO_CPU'
    CPA_ASSIGNED = 'IN_PROGRESS_AT_CPU'
    QUERY_RAISED = 'QUERY_RAISED_TO_SALES'
    REJECTED = 'REJECTED'
    PENDING_FOR_DDE = 'PENDING_FOR_DDE'
    CREDIT_RECOMMENDATION = 'CREDIT_RECOMMENDATION'
    PD_REJECT = 'PD_REJECT'
    ELIGIBILITY_NORMS = 'ELIGIBILITY_NORMS'
    CREDIT_DECISIONED = 'CREDIT_DECISIONED'
    COMMERCIAL_APPROVAL = 'COMMERCIAL_APPROVAL'
    SANCTIONED = 'SANCTIONED'


@verify(UNIQUE)
class LeadSubStatusEnum(StrEnum):
    OPEN = 'SUBMITTED_TO_CPU'
    CPA_ASSIGNED = 'IN_PROGRESS_AT_CPU'
    QUERY_RAISED = 'QUERY_RAISED_TO_SALES'
    REJECTED = 'REJECTED'
    PENDING_FOR_DDE = 'PENDING_FOR_DDE'
    MOVED_TO_REJECTION_POOL = 'MOVED_TO_REJECTION_POOL'
    INCOME_PROOF = 'INCOME_PROOF'
    OBLIGATION_ANALYSIS = 'OBLIGATION_ANALYSIS'
    PD_INITIATED = 'PD_INITIATED'
    PD_COMPLETED = 'PD_COMPLETED'
    TECHNICAL_INITIATED = 'TECHNICAL_INITIATED'
    TECHNICAL_COMPLETED = 'TECHNICAL_COMPLETED'
    FI_INITIATED = 'FI_INITIATED'
    FI_COMPLETED = 'FI_COMPLETED'
    LEGAL_INITIATED = 'LEGAL_INITIATED'
    LEGAL_COMPLETED = 'LEGAL_COMPLETED'
    RCU_INITIATED = 'RCU_INITIATED'
    RCU_COMPLETED = 'RCU_COMPLETED'
    ELIGIBILITY_NORMS = 'ELIGIBILITY_NORMS'
    CREDIT_DECISIONED = 'CREDIT_DECISIONED'
    COMMERCIAL_APPROVAL = 'COMMERCIAL_APPROVAL'
    SANCTIONED = 'SANCTIONED'
    ASSIGNED_TO_UNDERWRITER = "ASSIGNED_TO_UNDERWRITER"
    DEDUPE_PENDING = "DEDUPE_PENDING"


class RoleEnum:
    CPA = 'CPA'
    COM = 'COM'
    UNDERWRITER = 'UNDERWRITER'
    CP = 'CP'
    QC = 'QC'
    TL = 'TEAM LEAD'
    HUNTERSPOC = 'HUNTERSPOC'
    TECHNICAL_VALUATOR = 'TEI'
    TECHNICAL_COORDINATOR = 'TC'
    TECHNICAL_VENDOR = 'TVALEXT'
    TECHNICAL_VETTING = 'TVET'
    TECHNICAL_APPROVER = 'TA'
    LC = 'LC'
    LV = 'LV'
    LM = 'LM'
    LA = 'LA'
    OPS = 'OPS'


class TechnicalLoanAmount:
    LIMIT_1 = 5000000
    LIMIT_2 = 7500000

class PermissionEnum:
    RAISE_QUERY_SECTION = 'raisequery'


class KafkaStatusEnum:
    FAILED = 'FAILED'
    PULLED = 'PULLED'
    PUSHED = 'PUSHED'
    SUCCESS = 'SUCCESS'
    RETRY = 'RETRY'


class KafkaActions:
    BRE_CHECK = 'BRE_CHECK'
    KAFKA_EMAIL = 'kafka_email'
    KAFKA_CONSUMER = 'KAFKA_CONSUMER'
    LV_FORM_SUBMIT = 'LV_FORM_SUBMIT'


class InputActionEnum(StrEnum):
    UPDATE = 'update'
    DELETE = 'delete'


@verify(UNIQUE)
class RateTypeEnum(StrEnum):
    FIXED = 'FIXED'
    SEMI_FIXED = 'SEMI-FIXED'
    FLOATING = 'FLOATING'


class NotificationType:
    SMS = 'SMS'
    EMAIL = 'EMAIL'


class NotificationMessageType:
    STANDARD = 'STANDARD'


class NovelStatus:
    PROCESSED = 'Processed'
    DOWNLOADED = 'Downloaded'
    INPROGRESS = 'In Progress'
    DELETED = 'Deleted'
    REJECTED = 'Rejected'
    SUBMITTED = 'Submitted'


class NotificationEnum:
    SMS_PDF_GENERATION = '''Dear {rm_name},\n\n\nApplication form has been generated by CPU user {cpu_user} for {application_id}. Please contact the primary applicant to check the application form and get it validated via OTP. CAPRI GLOBAL'''
    EMAIL_SUBJECT_ESIGN_RM = '''Esign sms sent for application id {application_id}'''
    EMAIL_CONTENT_ESIGN_RM = '''Dear {rm_name},\n\nApplication form {short_link} has been generated for application id - {application_id}. Please contact the primary applicant to check the application form and get it validated via OTP. \n\nRegards,\nCapri Loans\n\n'''
    SMS_APPLICATION_SUBMIT = 'Dear {customer_name},\n\n\nApplication no {application_id} has been submitted to Credit by CPU user {cpa_email} for further processing. CAPRI GLOBAL'
    SMS_QUERY_RAISED = '''Hi {rm_name},\n\nSome additional information are required to process the loan application number {application_id} further. Please provide the information by clicking on the following link {form_link}.\n\nRegards,\nCapri Loans'''
    EMAIL_SUBJECT_QUERY_RAISED = 'Query raised for {application_id}'
    EMAIL_CONTENT_QUERY_RAISED = '''Dear {rm_bm_name},\n\nSome additional information are required to process the loan application number {application_id} further. Please provide the information by clicking on the following link {form_link}\n\nRegards,\nCapri Loans\n\n'''
    NOTIFY_RM_BM_EMAIL_CONTENT_QUERY_RAISED = '''Dear {rm_bm_name},\n\nPlease note that Application No {application_id} sourced by you has been reviewed by the Credit Processing Team and queries have been submitted for your review and action. The queries can be viewed under Open Queries Tab of your Pragati App.\n\nRequest you to please respond to the queries at the earliest so that the file can be processed further.\n\n'''
    EMAIL_SUBJECT_REJECT_LEAD = 'Application rejected - {application_id}'
    EMAIL_CONTENT_REJECT_LEAD = '''Dear {rm_bm_name},\n\nThe lead {application_id} submitted to CPU has been rejected by CPA/COM after validations.\n\n'''
    EMAIL_SUBJECT_REJECT_OLDER_LEADS = 'Application rejected - {application_id}'
    EMAIL_CONTENT_REJECT_OLDER_LEADS = (
        '''Dear {rm_bm_name},\n\nThe lead {application_id} submitted to CPU has been expired.\n\n'''
    )
    EMAIL_SUBJECT_PDF_GENERATION = 'Application form for {application_id}'
    EMAIL_CONTENT_PDF_GENERATION = '''Dear {rm_bm_name},\n\nApplication form has been generated by CPU user {cpa_email}.\n\nPlease contact the Applicant to check the application form and get it approved via OTP.\n\n'''
    EMAIL_SUBJECT_LEAD_ASSIGNMENT = 'Application assigned - {application_id}'
    EMAIL_CONTENT_LEAD_ASSIGNMENT = (
        '''Dear {rm_name},\n\nThe Application no {application_id} has been assigned to you by {assignor_email}\n\n'''
    )
    EMAIL_SUBJECT_NEW_RM_ASSIGNMENT = 'Application reassigned to new RM for - {application_id}'
    EMAIL_CONTENT_NEW_RM_ASSIGNMENT = (
        'Dear {cpa_name},\n\nThe Application no {application_id} has been re-assigned to new RM {rm_name}\n\n'
    )
    EMAIL_SUBJECT_CPA_REASSIGNMENT = 'Application assigned - {application_id}'
    EMAIL_CONTENT_CPA_REASSIGNMENT = (
        'Dear {cpa_name},\n\nThe Application no {application_id} has been assigned to you by {assignor_email}\n\n'
    )
    EMAIL_SUBJECT_COMPLETE_LEAD = 'Application submitted to Credit - {application_id}'
    EMAIL_CONTENT_COMPLETE_LEAD = '''Dear {rm_bm_name},\n\nApplication has been submitted to Credit by CPU user {cpa_email}.\n\nPlease find the application form verified by customer attached for your reference.\n{application_form}\n\nRegards,\nCapri Loans\n\n'''
    SMS_E_SIGN = '''Dear Customer, Application form pdf has been generated for your application - {application_id} Please click on the {link} to see your submitted application data, OTP for verifying the data is {otp}'''

    EMAIL_SUBJECT_CPA_REASSIGNMENT_UPDATE_TO_RM = 'Application no {application_id} Reassigned To New CPA.'
    EMAIL_CONTENT_CPA_REASSIGNMENT_UPDATE_TO_RM = (
        'Dear {rm_name},\n\nThe Application no {application_id} has been re-assigned to CPU user {assignee_email}\n\n'
    )
    EMAIL_SUBJECT_RM_REPLY_ON_QUERY = 'Query reply for {application_id}'
    EMAIL_CONTENT_RM_REPLY_ON_QUERY = '''Dear {cpa_name},\n\nRM {rm_bm_name} has responded on the query raised for application number {application_id}.\n\nRegards,\nCapri Loans\n\n'''
    EMAIL_SUBJECT_RCU_CREDIT_STATUS = 'Approval Required for application id {application_id}'
    EMAIL_CONTENT_RCU_CREDIT_STATUS = (
        'Dear {recipient_name}, Please find the respective status for the application no {application_id}.\n\n Credit Status: {credit_status} \n RCU Status: {rcu_status} \n\n Please share the final status for the application approval.\n Thanks'
    )

    EMAIL_SUBJECT_RCU_STATUS_RECEIVED_NOTIFICATION = 'A new RCU Status has been recieved for application id {application_id}'
    EMAIL_CONTENT_RCU_STATUS_NOTIFIER = (
        'Dear Branch Credit Manager, Please find the respective rcu status for the application no {application_id}.\n\n RCU Status: {rcu_status} \n\n Please share the final status for the application approval.\n Thanks'
    )
    EMAIL_SUBJECT_LV_ASSIGNMENT = (
        'The Application no {application_id} has been assigned to you by {assignor_email}\n\n'
    )
    EMAIL_CONTENT_LV_ASSIGNMENT = (
        '''Dear {lv_email},\n\nThe Application no {application_id} has been assigned to you by {assignor_email}\n\n'''
    )
    EMAIL_SUBJECT_LV_ASSIGNMENT_NOTIFICATION_TO_LM = (
        'The Application no {application_id} has been assigned to {lv_email} by {assignor_email}\n\n'
    )
    EMAIL_CONTENT_LV_ASSIGNMENT_NOTIFICATION_TO_LM = (
        '''Dear {lm_email},\n\nThe Application no {application_id} has been assigned to {lv_email} by {lv_email}\n\n'''
    )



LoanType = {'home loan': 'CGHFL', 'home equity': 'CGHFL', 'msme tl': 'CGCL'}


EPOCH_24H_TIME_INTERVAL = 86399000
AMOUNT_LIMIT_FOR_GST = 2500000  # Loan Amount In Lakhs (INR)
EPOCH_30_DAYS_TIME_INTERVAL = 86400000 * 30
INVALID_RETRIGGER_COUNT = 3


class CIBIL_CONSTANTS:
    NAMES_INDEX = 'N01'
    IDS_INDEX = 'I01'
    IDS_TYPE = 'PAN'
    TELEPHONE_INDEX = 'T01'
    TELEPHONE_TYPE = 'MOBILE'
    ENQUIRY_ENRICHED = 'Y'
    ADDRESS_INDEX = 'A01'
    ADDRESS_CATEGORY = 'PERMANENT'
    ENQUIRY_ACCOUNTS_INDEX = 'I01'
    ENQUIRY_PURPOSE = {'msme tl': 'Housing Loan', 'home loan': 'Housing Loan', 'home equity': 'Property Loan'}


class CIBIL_INDIVIDUAL_CONSTANTS(CIBIL_CONSTANTS):
    pass


class CIBIL_ORGANIZATION_CONSTANTS(CIBIL_CONSTANTS):
    CMR_FLAG = '1'
    CONTACT_PREFIX = '91'
    ENQUIRY_TYPE = 'New loan'
    TYPE_OF_ENTITY = {
        'private limited company': 'Private Limited',
        'public limited company': 'Public Limited',
        'sole proprietorship': 'Proprietorship',
        'partnership': 'Partnership',
        'llp': 'Partnership',
        'trust': 'Trust',
        'societies': 'Co-operative Society',
    }
    CLASS_OF_ACTIVITY = {'X': 'x'}
    PERMANENT = 'PERMANENT'


CUSTOMER_EDUCATION_MAP = {
    "illiterate": "0",
    "below matriculation": "1",
    "matriculation": "2",
    "intermediate": "3",
    "graduate": "4",
    "undergraduate": "5",
    "post graduate or master degree": "6",
    "professional course or certification": "7",
}

CUSTOMER_SEX_MAP = {"male": "M", "female": "F", "others": "T"}
CUSTOMER_MARITAL_STATUS_MAP = {
    "NONE": 0,
    "SINGLE": 1,
    "UNMARRIED": 1,
    "MARRIED": 2,
    "DIVORCED": 3,
    "WIDOWED": 4,
    "SEPARATED": 5,
    "OTHERS": 6,
}

PROFESSION_CODE_MAPPING = {
    "accountant (cost/chartered)": 1,
    "agriculturist": 2,
    "architect": 3,
    "artisan and craftsman": 4,
    "artist": 5,
    "author/writer": 6,
    "banker": 7,
    "businessman": 8,
    "business executive": 9,
    "civil servant/govt servant": 10,
    "consultant": 11,
    "contractor": 12,
    "defence personnel": 13,
    "director": 14,
    "doctor": 15,
    "engineer": 16,
    "ex-servicemen": 17,
    "executive director": 18,
    "financial broker": 19,
    "govt servant": 20,
    "house wife": 21,
    "industrialist": 22,
    "journalist": 23,
    "lawyer/solicitor": 24,
    "legislator": 25,
    "magistrate": 26,
    "managing director": 27,
    "migrant labourer": 28,
    "nurse": 29,
    "others": 30,
    "pensioner": 31,
    "pharmacist": 32,
    "street vendors": 33,
    "real estate services": 34,
    "street hawkers": 35,
    "self help groups": 38,
    "self employed": 39,
    "service": 40,
    "student": 41,
    "staff - officer": 42,
    "staff - clerical": 43,
    "sub staff/pte": 44,
    "teacher": 45,
    "trader": 46,
    "transport operator": 47,
    "unemployed": 48,
    "professor": 49,
    "asst. professor": 50,
    "child care taker ": 58,
    "home tutions": 59,
    "pmi-acp": 65,
    "it consultant": 68,
    "teacher": 77,
    "new profession": 80,
    "miscellaneous": 99,
    "chartered accountants ": 51,
    "karta  ": 52,
    "others": 53,
    "partner ": 54,
    "promoter  ": 55,
    "proprietor ": 56,
    "senior lawyer ": 57,
    "shareholder  ": 60,
    "tax consultants ": 61,
    "trustee ": 62,
}

BUSINESS_CODE_MAPPING = {
    "government": 101,
    "private company": 102,
    "cash": 103,
    "professionalconsultants": 104,
    "hospitalclinicdoctor": 105,
    "advertisement": 106,
    "agents": 107,
    "agriculture": 108,
    "brickkiln": 109,
    "builder": 110,
    "building material suppliers": 111,
    "daily wage worker": 112,
    "dairymilk trading": 113,
    "diamondgemsstones": 114,
    "distributorswholesalers": 115,
    "driver": 116,
    "eateryfast food": 117,
    "electricelectronic items": 118,
    "electricianplumber repairing": 119,
    "fabricatorsfurniture": 120,
    "fancy storecosmetic items": 121,
    "fertilizerpesticides": 122,
    "flour mill": 123,
    "fmcg goods": 124,
    "fmcg goods": 125,
    "food grain": 126,
    "footwear bags": 127,
    "fruit and vegetable": 128,
    "garment shop cloth stores textile": 129,
    "hair saloons": 130,
    "hardwareauto parts ": 131,
    "hotelsrestaurantscatering business ": 132,
    "installation work": 133,
    "ironwork": 134,
    "jewellerygoldsmithsilver": 135,
    "job work": 136,
    "kitchen items": 137,
    "laundrydrycleaner": 138,
    "light mandap flower decorator dj band": 139,
    "mason": 140,
    "medical stores": 141,
    "mines  stone crusher": 142,
    "mobile  computer salesaccessories": 143,
    "other manufacturer": 144,
    "other retail trader": 145,
    "other services": 146,
    "photo copiercyber cafprinting  desig": 147,
    "photo studioevent management": 148,
    "plastic itemspaper items": 149,
    "provision stores general storesstation": 150,
    "purohit  astrologer": 151,
    "rental income from propertygoods": 152,
    "repairing work": 153,
    "schoolstuition centerscolleges": 154,
    "scrap business": 155,
    "sculpturehandicraft mfg": 156,
    "service sectorlabour contractor": 158,
    "service sectorpaint contractor": 159,
    "sweetssaiverybakery": 160,
    "tailorstitchingembroidery": 161,
    "tea stall": 162,
    "tours and travels": 163,
    "transportersearthmover hiring": 164,
    "water supplier": 165,
    "workshops automechweldingservice cent": 166,
    "mining and quarrying inc coal": 167,
    "sugar": 168,
    "edible oils and vanaspati": 169,
    "tea": 170,
    "others": 171,
    "beverages and tobacco": 172,
    "cotton textiles": 173,
    "jute textiles": 174,
    "man made textiles": 175,
    "other textiles": 176,
    "leather and leather products": 177,
    "wood and wood products": 178,
    "paper and paper products": 179,
    "petroleum, coal products and nuclear fuels": 180,
    "fertiliser": 181,
    "drug and pharmaceuticals": 182,
    "petro chemicals": 183,
    "rubber, plastic and their products": 184,
    "glass and glassware": 185,
    "cement and cement product": 186,
    "iron and steel": 187,
    "other metal and metal product": 188,
    "electronics": 189,
    "vehicles, vehicle parts and transport equi": 190,
    "gems and jewellery": 191,
    "construction": 192,
    "power": 193,
    "telecommunications": 194,
    "roads": 195,
    "other infrastructure": 196,
    "other industries": 197,
    "fleet owner": 198,
    "commission agent": 199,
    "software development": 200,
    "repair and maintenance": 201,
    "tourism": 202,
    "hotels": 203,
    "bars and restuarants ": 204,
    "coffee outlet": 205,
    "guest house": 206,
    "comission agents": 207,
    "clearing agents": 208,
    "crane operators": 209,
    "doctors": 210,
    "chartered accounts": 211,
    "architects": 212,
    "brokers": 213,
    "hair saloon ": 214,
    "spa ": 215,
    "tw service centre": 216,
    "four wheeler service centre": 217,
    "three wheeler service centre": 218,
    "civil contractors": 219,
    "automobile leasing": 220,
    "leasing of earthmoving machine": 221,
    "wholesale trade": 222,
    "retail trade": 223,
    "school": 224,
    "college": 225,
    "any other educational institute": 226,
}

INDIVIDUAL_CUSTOMER_CATEGORY_MAPPING = {
    "sep": {
        "gross turnover method": "GTM",
        "emi equalizer": "SEQ",
        "cash profit method (cpm)": "CPI",
        "no income proof - cash profit method (nip-cpm)": "ID2",
        "banking surrogate (bs)": "SUR",
        "category a": "SAA",
        "category b": "SAB",
        "category c": "SAC",
        "no income proof (nip)": "ID1",
        "cash salary": "ID3",
    },
    "senp": {
        "gross turnover method": "GTM",
        "emi equalizer": "SEQ",
        "cash profit method (cpm)": "CPI",
        "no income proof - cash profit method (nip-cpm)": "ID2",
        "banking surrogate (bs)": "SUR",
        "category a": "SAA",
        "category b": "SAB",
        "category c": "SAC",
        "no income proof (nip)": "ID1",
        "cash salary": "ID3",
    },
    "salaried": {
        "gross turnover method": "GTM",
        "emi equalizer": "SEQ",
        "cash profit method (cpm)": "CPI",
        "no income proof - cash profit method (nip-cpm)": None,
        "banking surrogate (bs)": "SUR",
        "category a": "SAA",
        "category b": "SAB",
        "category c": "SAC",
        "no income proof (nip)": None,
        "cash salary": "ID3",
    },
}

ORG_CUSTOMER_CATEGORY_MAPPING = {
    "gross turnover method": "C4 ",
    "emi equalizer": None,
    "cash profit method (cpm)": "CPC",
    "no income proof - cash profit method (nip-cpm)": None,
    "banking surrogate (bs)": "C2 ",
    "category a, b, c ": None,
    "no income proof (nip)": None,
    "cash salary": None,
}

class CommunicationConstants:
    COMM_BUCKET_NAME = 'uat-analytics-team-reporting'
    COMM_OBJECTS_PREFIX = 'communication_module_files'
    COMM_SMS_MODE = 'sms'
    COMM_EMAIL_MODE = 'email'
    CGCL_LOB = 'CGCL'
    CGHFL_LOB = 'CGHFL'
    CGCL_SOURCE = 'induscgcl'
    CGHFL_SOURCE = 'induscghfl'
    GENERIC_SOURCE = 'cbp'

class FlexcubeConstants:
    ENTITY_NAME = "flexcube_service"
    CHANNEL = "API"
    INDIA = 'IN'
    INDIA_FULL = 'INDIA'
    INDIAN = "IN"
    PHONE = "0"
    LANGUAGE = "ENG"
    CUSTOMER = "C"
    BANK_CODE = 999

    # service codes
    SERVICE_CODE_CUSTOMER_CREATE = 214
    SERVICE_CODE_CUSTOMER_DEDUPE = 277
    SERVICE_CODE_CUSTOMER_MODIFICATION = 179
    SERVICE_CODE_LOAN_ACCOUNT_OPENING = 216
    SERVICE_CODE_COLLATERAL_CREATE = "A105"
    SERVICE_CODE_COLLATERAL_LINKAGE = 270
    SERVICE_CODE_CUSTOMER_360 = 913
    SERVICE_CODE_IMD_UPDATE = "A112"
    SERVICE_CODE_CUSTOMER_ACCOUNT_RELATION = 267
    SERVICE_CODE_XFACE_CUSTOMER_ADDITIONAL_INFO = 938
    SERVICE_CODE_IRS_ADD_CRR_DETERMINATION_CRITERIA = 937
    CUSTOMER_MODIFICATION = 503
    SERVICE_CODE_CUSTOMER_ADDITIONAL_CBR = 509

    SERVICE_CODE_PAYMENT_MANDATE = "A102"
    SERVICE_CODE_PAYMENT_REGISTER = "A107"
    SERVICE_CODE_DOCUMENT_ADDITION = 940

    SERVICE_CODE_LOAN_INSTALLMENT_PAYMENT_INQUIRY = 195

    SERVICE_CODE_LOAN_INSTALLMENT_PAYMENT_INQUIRY = 195
    SERVICE_CODE_LOAN_HOST_DISBURSEMENT_DETAILS = 941	
    SERVICE_CODE_LOAN_ACCOUNT_DISB_DEDUCTION_DETAILS_INQUIRY = 286

    DEFAULT_BANKCODE = 999
    DEFAULT_TRANSACTION_BRANCH = 99999
    DEFAULT_USER_ID = "SYSTELLER"
    DEFAULT_USER_EMAIL = "SYSTELLER"
    MIS_CODE = 0
    LOAN_ACCOUNT_DATE_BASIS = 1
    LOAN_REBATE_APPLICABLE = "N"
    LOAN_ADDITIONAL_INTEREST_VARIANCE = 0
    LOAN_COD_AGGREMENT_NUMBER = 12
    LOAN_REPAYMENT_MODE = 3
    COLLATERAL_ASSET_CLASS = 1
    COLLATERAL_TYPE_CHARGE = 1
    COLLATERAL_TYPE_PROPERTY = 0
    FLOATING_COLLATERAL = "N"
    DEFAULT_COUNTRY = "INDIA"
    COLLATERAL_PRIORITY = 0
    COLLATERAL_IMPACT_OF_RATE_CHANGE = "I"
    COLLATERAL_PRIMARY_OR_SECONDARY = "P"
    IMD_INSTRUMENT_MODE = "RP"
    IMD_SERVICE_CHARGE_CODE = 2012
    IMD_SERVICE_CHARGE_AMOUNT = 1000
    IMD_TRANSACTION_CCY = 104  # currency mappping needed if we want to support multiple currencies current is INR
    PAYMENT_MANDATE_EXTERNAL_TASK_CODE = "PMX02"
    PAYMENT_MANDATE_ACTION = "A"
    PAYMENT_TYPE = "1"  # 1 is for ACH means Automatic Clearing house
    PAYMENT_MANDATE_TYPE = "2"  # 2 is for DR (Debut MAndate)
    PAYMENT_MANDATE_PROVIDER_ID_CODE = "121"  # it is for YES BANK which is provided by NPCI
    PAYMENT_MANDATE_UTILITY_PROVIDER = "BANK"
    PAYMENT_MANDATE_SPONSOR_BANK_IFSC = "IFSC12354"
    PAYMENT_MANDATE_SPONSOR_BANK_MICR = "12323565"
    PAYMENT_MANDATE_DEST_ACCOUNT_NUMBER = (
        "50000000351422"  # DEST account is Beneficiary account where disbursement will credited
    )
    PAYMENT_MANDATE_DEST_BANK_NAME = "HDFC BANK LTD"
    PAYMENT_MANDATE_DEST_BRANCH_ADDRESS = "NOIDA"
    PAYMENT_MANDATE_DEST_IFSC = "HDFC0000088"
    PAYMENT_MANDATE_DEST_MICR = "110240014"
    PAYMENT_MANDATE_FREQUENCY = "0"
    PAYMENT_MANDATE_DEBIT_TYPE = "2"  # corresponds to Maximum Amount
    # TODO:  4 is for cancelled, but this is not much significant now, when this gets fixed on fc side, need to update this
    PAYMENT_MANDATE_STATUS = "4"
    PAYMENT_MANDATE_COD_REASON = 0
    PAYMENT_MANDATE_PARTNER_BANK_CODE = 1020  # 9009 is also possible value here
    PAYMENT_MANDATE_IDENTIFIER = "E"  # corresponds to e mandate

    CUSTOMER_ACCT_REL_FLG_TXN_TYPE = "A"
    TEST_APPLICATION_ID = ["100060", "900194"]  #

    PAYMENT_REGISTER_SERIAL_NO = 1
    PAYMENT_REGISTER_EXTERNAL_TASK_CODE = "LNX04"
    PAYMENT_PARTNER_BANK_CODE = 1020
    PAYMENT_REGISTER_MODE = 2  # TODO: what to pass
    PAYMENT_REGISTER_DISB_NUMBER_FIRST_DISB = 1
    PAYMENT_REGISTER_DISB_NUMBER_SECOND_DISB = 2
    DOCUMENT_CHECK = 3
    DOCUMENT_SOURCE = 2
    DOCUMENT_STATUS_MODE = 1
    NO = "N"
    YES = "Y"
    MSME = "msme tl"

class EntityType(str, Enum):
    INDIVIDUAL = 'individual'
    ORGANIZATION = 'organization'


@verify(UNIQUE)
class CustomerType(StrEnum):
    APPLICANT = 'applicant'
    CO_APPLICANT = 'co_applicant'
    GUARANTOR = 'guarantor'


@verify(UNIQUE)
class QueryType(StrEnum):
    CHANGE = 'change'
    ADD_COAPPLICANT = 'add_coapplicant'
    ADD_GUARANTOR = 'add_guarantor'
    TECHNICAL = 'verification$technical'

    @classmethod
    def values(cls):
        return list(cls._value2member_map_.keys())

class BREColorEnum:
    GREEN = 'GREEN'
    LIGHT_GREEN = 'LIGHT GREEN'
    DARK_GREEN = 'DARK GREEN'
    AMBER = 'AMBER'
    RED = 'RED'
    LIGHT_RED = 'LIGHT RED'
    DARK_RED = 'DARK RED'


class UnderwritingStageEnum:
    REJECTED = 'REJECTED'
    REJECT_SUCCESS = 'REJECT_SUCCESS'
    CO_APPLICANT_PROPERTY_OWNER_FAILED = 'CO_APPLICANT_PROPERTY_OWNER_FAILED'
    FAMILY_CHECK_NEEDED = 'FAMILY_CHECK_NEEDED'
    PROPERTY_CHECK_PROCEED_FAIL = 'PROPERTY_CHECK_PROCEED_FAIL'
    QUERY_RAISED_ADD_CO_APPLICANT = 'QUERY_RAISED_ADD_CO_APPLICANT'
    NO_CO_APPLICANT_AVAILABLE = 'NO_CO_APPLICANT_AVAILABLE'
    CO_APPLICANT_ADDED = 'CO_APPLICANT_ADDED'
    FAMILY_CHECK_ACCEPT = 'FAMILY_CHECK_ACCEPT'
    FIT_TO_PROCEED = 'FIT_TO_PROCEED'
    CPU_PROCESS_COMPLETED = 'CPU_PROCESS_COMPLETED'
    RAISED_REQUEST_FOR_DEVIATION = "RAISED_REQUEST_FOR_DEVIATION"
    APPROVED_IN_DEVIATION = "APPROVED_IN_DEVIATION"
    REJECTED_IN_DEVIATION = "REJECTED_IN_DEVIATION"
    FAMILY_CHECK_SKIPPED = "FAMILY_CHECK_SKIPPED"
    APPLICATION_GENERATED = "APPLICATION_GENERATED_BY_UNDERWRITER"
    UNDERWRITING_DONE = "UNDERWRITING_DONE"
    QUERY_RAISED_ADD_GUARANTOR = 'QUERY_RAISED_ADD_GUARANTOR'
    NO_GUARANTOR_AVAILABLE = 'NO_GUARANTOR_AVAILABLE'
    GUARANTOR_ADDED = 'GUARANTOR_ADDED'
    ENTITY_TYPE_ORGANIZATION = "ENTITY_TYPE_ORGANIZATION"
    

class RCUStageEnum:
    CREDIT_STATUS_PROCEED = 'proceed'
    CREDIT_STATUS_REJECT = 'rejected'
    RCU_STATUS_POSITIVE = 'Positive'
    RCU_STATUS_NEGATIVE = 'Negative'
    RCU_STATUS_REFER_TO_CREDIT = 'Refer to credit'
    RCU_STATUS_HARD_NEGATIVE = 'Hard Negative'
    RAISED_REQUEST_FOR_DEVIATION = "RAISED_REQUEST_FOR_DEVIATION"


class BreConstants:
    CARPET_AREA = '1800'
    ASSET_DEVELOPMENT_STATUS = 'DEVELOPING'
    ASSET_DISTANCE_FROM_BRANCH = '5.0'
    DEDUPE = 'N'
    TOTAL_EXPENSES = 0
    BEW = "BEW"
    SENIP = "SENIP"
    BRANCH_CODE = "SUR"
    BORROWER_TYPE = "SELF_EMP"


class BorrowerTypeEnum:
    SALARIED = "salaried"
    SEP = "sep"
    SENP = "senp"


class DeviationEnum:
    PRODUCT = "LOS_Deviation"
    FEE_ROUND_CONDITION = "Application Fees Refund"
    COMPANY_TYPE = "CGCL"


class DeviationConditionsEnum(Enum):
    DPD_UPTO_30_DEDUPE_SUBMIT = "Negative CIBIL/CRIF Report (Up to 30 days) DPD in last 12 months)"
    DPD_MORE_THAN_30_DEDUPE_SUBMIT = "Negative CIBIL/ CRIF Report (> 30 days DPD in last 12 months)"


HunterGenderMapping = {'others': '0', 'male': '1', 'female': '2', 'unknown': '3'}


HunterSpocStatus = ['suspect', 'clear', 'declined']


HunterMaritalStatusMapping = {
    'married': '0',
    'civil_partnership': '0',
    'living_with_partner': '3',
    'single': '4',
    'separated': '5',
    'divorced': '6',
    'widowed': '7',
    'na': '99',
    'unmarried': '4',
}


HunterQualificationTypeMapping = {
    'engineer': '1',
    'below_metric': '2',
    'diploma': '3',
    'doctorate': '4',
    'degree': '5',
    'hsc': '6',
    'it_tech_diploma': '7',
    'illiterate': '8',
    'matric': '9',
    'post_graduate': '10',
    'professional': '11',
    'under_graduate': '12',
    'graduation': '12',
    'other': '13',
}


HunterProductMapping = {'Home Equity': '1', 'MSME TL': '2', 'Home Loan': '3'}

SUCCESS_COLOURS = (BREColorEnum.GREEN, BREColorEnum.LIGHT_GREEN, BREColorEnum.DARK_GREEN, BREColorEnum.AMBER)


FAILURE_COLOURS = (BREColorEnum.RED, BREColorEnum.LIGHT_RED, BREColorEnum.DARK_RED)


class UnderwritingMessageEnum:
    MESSAGE_ONE = "The application has been rejected during underwriting model run"
    MESSAGE_TWO = "The application under Application no. {application_number} submitted by {primary_applicant_name} is fit to proceed."
    MESSAGE_THREE = "The application has been rejected during underwriting model owing to {co_applicant_details}{guarantor_details} not clearing the underwriting criteria"
    MESSAGE_FOUR = "The sole co-applicant {co_applicant_details}{guarantor_details} of Application {application_number} has not cleared the underwriting check. Please indicate if another co-applicant is available to be added or not."
    # MESSAGE_FIVE = "A non-financial co-applicant has been removed during underwriting model run. Should this application proceed further?"
    MESSAGE_SIX = "{co_applicant_details}{guarantor_details} has not cleared the underwriting check and will be removed from the file. Please indicate if any other co-applicant can be added before the application moves forward."
    MESSAGE_SEVEN = "The application has been successfully rejected"
    MESSAGE_EIGHT = "A co-applicant/guarantor has been removed during underwriting model run. Should this application proceed further?"
    MESSAGE_NINE = "Co-applicant has been successfully added. Awaiting CPU process to complete"
    MESSAGE_TEN = "Requested for deviation approval"
    MESSAGE_ELEVEN = "Request has been approved"
    MESSAGE_TWELVE = "Request has been rejected"
    MESSAGE_THIRTEEN = "Query has been successfully raised to add a new co-applicant"
    MESSAGE_FOURTEEN = "{co_applicant_details}{guarantor_details} who is also a property owner has failed the underwriting check. Either remove the property from the loan property details or ask the co-applicant to transfer ownership to other co-applicants or applicant"
    MESSAGE_FIFTEEN = "Application generated"
    MESSAGE_SIXTEEN = "Query has been successfully raised to add a new guarantor"
    MESSAGE_SEVENTEEN = "Guarantor has been successfully added. Awaiting CPU process to complete"
    MESSAGE_EIGHTEEN = "No co-applicant available."


class UnderwritingSubMessageEnum:
    SUB_MESSAGE_ONE = "Please fulfill the above conditions to proceed"
    SUB_MESSAGE_TWO = "CPU process is yet to complete. Please wait"


pragati_state_to_cibil_state_mapping = {
    "bihar": "Bihar",
    "sikkim": "Sikkim",
    "arunachal pradesh": "Arunachal Pradesh",
    "nagaland": "Nagaland",
    "nanipur": "Manipur",
    "mizoram": "Mizoram",
    "tripura": "Tripura",
    "meghlaya": "Meghalaya",
    "assam": "Assam",
    "west bengal": "West Bengal",
    "jharkhand": "Jharkhand",
    "odisha": "Orissa",
    "chattisgarh": "Chhattisgarh",
    "madhya pradesh": "Madhya Pradesh",
    "gujarat": "Gujarat",
    "dadra nagar haveli and daman diu": "Daman & Diu",
    "dadra nagar haveli and daman diu": "Dadra & Nagar Haveli",
    "maharashtra": "Maharashtra",
    "andhra pradesh": "Andhra Pradesh",
    "karnataka": "Karnataka",
    "goa": "Goa",
    "lakshwadeep": "Lakshadweep",
    "kerala": "Kerala",
    "tamil nadu": "Tamil Nadu",
    "pondicherry": "Pondicherry",
    "andaman and nicobar island": "Andaman & Nicobar Islands",
    "telangana": "Telangana",
    "jammu and kashmir": "Jammu & Kashmir",
    "himachal pradesh": "Himachal Pradesh",
    "punjab": "Punjab",
    "uttarakhand": "Uttaranchal",
    "haryana": "Haryana",
    "delhi": "Delhi",
    "rajasthan": "Rajasthan",
    "uttar pradesh": "Uttar Pradesh",
}


@verify(UNIQUE)
class AddressType(StrEnum):
    RESIDENCE = 'resident'
    BUSINESS = 'business'


@verify(UNIQUE)
class FiType(StrEnum):
    REFER_BRANCH = 'REFER_BRANCH'
    ASSIGN_VENDOR = 'ASSIGN_VENDOR'


@verify(UNIQUE)
class VendorStatusEnum(StrEnum):
    PENDING = 'INITIATED'
    POSITIVE = 'POSITIVE'
    NEGATIVE = 'NEGATIVE'
    REFER_TO_CREDIT = 'REFER_TO_CREDIT'
    FI_WAIVED = 'FI_WAIVED'


class PosidexConstants:
    SUCCESS_RESP_CODE = "200"
    SUCCESS_STATUS_INFO = "C"
    DEV_ENV = "DEV"
    DEFALUT_FLEXCUBE_ID = 605428

# TODO: sample mapping can get changed as development proceed
product_code_mapping = {
    'affordable housing loan prime senp': {'product_code': 505, 'rate_code': 300, 'schedule_code': 3000},
    'home loan high yield semi fixed': {'product_code': 520, 'rate_code': 300, 'schedule_code': 3000},
    'home loan high yield variable': {'product_code': 510, 'rate_code': 300, 'schedule_code': 3000},
    'home loan variable': {'product_code': 503, 'rate_code': 300, 'schedule_code': 3000},
    'home loan semi fixed': {'product_code': 512, 'rate_code': 300, 'schedule_code': 3000},
    'home loan sahaj variable': {'product_code': 515, 'rate_code': 300, 'schedule_code': 3000},
    'home loan sahaj semi fixed': {'product_code': 513, 'rate_code': 300, 'schedule_code': 3000},
    'home equity sahaj semi fixed': {'product_code': 502, 'rate_code': 300, 'schedule_code': 3000},
    'home equity sahaj variable': {'product_code': 514, 'rate_code': 300, 'schedule_code': 3000},
    'home equity assignment': {'product_code': 506, 'rate_code': 300, 'schedule_code': 3000},
    'home equity high yield semi fixed': {'product_code': 501, 'rate_code': 300, 'schedule_code': 3000},
    'home equity high yield variable': {'product_code': 521, 'rate_code': 300, 'schedule_code': 3000},
    'home equity semi fixed': {'product_code': 201, 'rate_code': 200, 'schedule_code': 1001},
    'home equity variable': {'product_code': 201, 'rate_code': 200, 'schedule_code': 1001},
    'msme tl semi fixed': {'product_code': 509, 'rate_code': 300, 'schedule_code': 3000},
    'msme tl floating': {'product_code': 518, 'rate_code': 300, 'schedule_code': 3000},
    'msme tl sahaj semi fixed': {'product_code': 517, 'rate_code': 300, 'schedule_code': 3000},
    'msme tl sahaj floating': {'product_code': 516, 'rate_code': 300, 'schedule_code': 3000},
}

# TODO : update the below list with updated mapping once special characters get removed and length
# get reduced to 40 chars

loan_purpose_mapping = {
    'purchase of raw material or enhancement of stock': 'Purchase of Raw material',
    'furnishing of security deposit or earnest money toward business': 'Furnishing of security deposit',
}

collateral_code_mapping = {
    "commercial-joint-partly self occupied mix use": 322,
    "commercial-joint-rented": 323,
    "commercial-joint-self occupied": 324,
    "commercial-joint-vacant": 325,
    "commercial-single-partly self occupied mix use": 326,
    "commercial-single-rented": 327,
    "commercial-single-self occupied": 328,
    "commercial-single-vacant": 329,
    "industrial-joint-partly self occupied mix use": 416,
    "industrial-joint-rented": 417,
    "industrial-joint-self occupied": 418,
    "industrial-joint-vacant": 419,
    "industrial-single-partly self occupied mix use": 420,
    "industrial-single-rented": 421,
    "industrial-single-self occupied": 422,
    "industrial-single-vacant": 423,
    "residential-joint-partly self occupied mix use": 213,
    "residential-joint-rented": 214,
    "residential-joint-self occupied": 215,
    "residential-joint-vacant": 216,
    "residential-single-partly self occupied mix use": 217,
    "residential-single-rented": 218,
    "residential-single-self occupied": 219,
    "residential-single-vacant": 220,
    "semi residential-joint-partly self occupied mix use": 601,
    "semi residential-joint-rented": 602,
    "semi residential-joint-self occupied": 603,
    "semi residential-joint-vacant": 604,
    "semi residential-single-partly self occupied mix use": 605,
    "semi residential-single-rented": 606,
    "semi residential-single-self occupied": 607,
    "semi residential-single-vacant": 608,
}

imd_mode_mapping = {
    "dd" : "C", # no mapping for dd , i guess cash will work, need to confirm
    "qr-paytm" : "C", # no mapping for paytm qr
    "paytm": "C", # no mapping for paytm
    "qr-razorpay": "RP",
    "razorpay": "RP",
}

mandate_type_mapping = {
    "savings bank account cheque": "10",
    "current account cheque": "11",
    "bankers cheque": "12",
    "cash credit account cheque": "13",
    "at Par current account cheques": "29",
    "at par cash credit account cheques": "30",
    "savings bank at par cheque": "31",
}

TEST_FLEXCUBE_RESPONSE_WITH_DPD = {
    "postingDate": "20231113",
    "transactionStatus": {
        "FCYHangeHandlingApplied": False,
        "errorCode": "0",
        "extendedReply": {},
        "externalReferenceNo": "njfdvddkghffkddfd",
        "isOverriden": False,
        "isServiceChargeApplied": False,
        "replyCode": 0,
        "spReturnValue": 0,
    },
    "customerResponse": {
        "xfaceCustomerBasicInquiryDTO": {
            "aadhrNoUpdDate": "20230927",
            "ageOfCustRel": "",
            "bankShortName": "Sendhwa-SIB Tower-MP",
            "birthDate": "19840106",
            "categoryType": "Salaried",
            "combWithdrawBal": 0,
            "custCrr": "10100",
            "customerAddress": {
                "city": "KOLHAPUR",
                "country": "IN",
                "line1": "Uttur",
                "line2": "Main road",
                "state": "MAHARASHTRA",
                "zip": "416502",
            },
            "customerFullName": "MAYA EKNATH INJAL",
            "customerId": 830651,
            "customerName": {
                "firstName": "MAYA",
                "formattedFullName": "MAYA#EKNATH#INJAL",
                "fullName": "MAYA EKNATH INJAL",
                "lastName": "INJAL",
                "midName": "EKNATH",
                "prefix": "Mrs",
                "shortName": "MAYA",
            },
            "homeBranch": "10005",
            "icType": "I",
            "icTypeDesc": "ID Card",
            "incomeTaxNumber": "ADPPI3871F",
            "isImageAvailable": False,
            "isSignatureAvailable": False,
            "mobileNumber": "8983608200",
            "nationalIdentificationCode": "8983608200",
            "npaStatus": "Normal",
            "officerID": "Vaultsysv10005",
            "sex": {"enumValue": "F", "mutable": False, "value": "F"},
        }
    },
    "xfaceCustomerAccountDetailsDTO": {
        "accountDetails": [
            {
                "DPD": "31",
                "RPABalance": 0,
                "accountCrr": "100",
                "accountId": "30100005368998  ",
                "accountStatus": "8",
                "acyAmount": 180000,
                "amountDisbursedToday": 0,
                "amountPaidToday": 0,
                "amtGoal": 0,
                "amtInstal": 0,
                "amtLien": 0,
                "amtPrincipalBalance": 180000,
                "availableBalance": 180000,
                "balPrincipal": 0,
                "balUncollecInt": 0,
                "balUncollecPrinc": 0,
                "balanceBook": 180000,
                "billAmount": 0,
                "branchCode": "10005",
                "branchName": "Sendhwa-SIB Tower-MP",
                "classification": "NORMAL",
                "cntCollAuc": "0",
                "cntCollLien": "0",
                "cntCollSpurious": "0",
                "codDepNo": 0,
                "compoundingInterestArrears": 0,
                "contractedInterestAmount": 6953.42,
                "contractedRateOfInterest": 30,
                "currencyCode": 104,
                "currencyShortName": "INR",
                "currentStatus": "8",
                "currentStatusDescription": "ACCOUNT OPEN REGULAR",
                "customerRelationship": "SOW",
                "datAcctOpen": "20230927",
                "datMaturity": "20240327",
                "disbursementAmount": 180000,
                "disbursementDate": "2023-09-27 00:00:00",
                "divertingInterestArrears": 0,
                "feeArrears": 0,
                "flagSpurious": "Normal",
                "flgLegal": "N",
                "flgTdLinkage": "N  ",
                "flgTellerAccess": "",
                "futureDatedAmount": 0,
                "futureInterest": 0,
                "iban": "IN43109930100005368",
                "installmentArrears": 0,
                "interestArrears": 0,
                "interestDue": "0",
                "interestFromCurrentDateTillNextEMI": 0,
                "interestOnArrears": 0,
                "lcyAmount": 180000,
                "loanApplicationNumber": "GL234351434",
                "minAmountDue": 0,
                "moduleCode": "L",
                "monthsSinceActive": 0,
                "nextDueDate": "20240327",
                "nextInstallmentDue": 206891.26,
                "nonAccountedArrears": 0,
                "npaStatus": "Normal",
                "originalBalance": 186632,
                "otherArrears": 0,
                "penaltyArrears": 0,
                "penaltyInterestAccured": 0,
                "pmiArrears": 0,
                "premiumArrears": 0,
                "principalArrears": 0,
                "productCode": 301,
                "productName": "301-Gold Loan Standard",
                "ratInt": 30,
                "reason": "          ",
                "rebateInterestAmount": 5330.96,
                "rebateRateOfInterest": 7,
                "reserveAmount": 0,
                "safeDepositBoxId": 0,
                "suspendedInterestOnArrears": 0,
                "suspendedPenaltyArrears": 0,
                "suspenededPMIArrears": 0,
                "tenure": "0 Months 0 Days 0 Years ",
                "totalAcyAmount": 180000,
                "totalBalBook": 180000,
                "totalBalUncollecInt": 0,
                "totalBalUncollecPrinc": 0,
                "totalLcyAmount": 180000,
                "totalOutstandings": 180000,
                "totalOutstandingsForForeClosure": 186953.42,
                "unbilledAdditionalPenaltyInterest": 0,
                "unbilledPenaltyArrears": 0,
                "unbilledPrincipalBalance": 180000,
                "unbilledServiceCharge": 0,
                "unclearFunds": 0,
                "unclearedFunds": 0,
                "uncollectedArrears": 0,
                "version": 10,
            }
        ],
        "corporateAccountDTO": [],
        "externalAccountDTO": [],
        "isCustomerSchemeAvailable": False,
    },
}

HUNTER_STATE_MAPPING = {
    "maharashtra": "MAH",
    "rajasthan": "RAJ",
    "gujarat": "GUJ",
    "madhya pradesh": "MP",
    "punjab": "PUN",
    "haryana": "HAR",
    "karnataka": "KAR",
    "uttar pradesh": "UP",
    "tamil nadu": "TN",
    "delhi": "NCR",
    "ghaziabad": "NCR",
    "faridabad": "NCR",
    "noida": "NCR",
    "greater noida": "NCR",
}


@verify(UNIQUE)
class FIStatusEnum(StrEnum):
    IN_PROGRESS = 'IN_PROGRESS'
    SUBMITTED = 'SUBMITTED'


role_to_status_filter_mapping = {
    #     "QC": [
    #         {
    #     	"stage_name": "SUBMITTED_TO_CPU",
    #     	"display_name": "SUBMITTED TO CPU",
    #     	"sub_stage": [{
    #     	               "sub_stage_name":"SUBMITTED_TO_CPU",
    #     	               "display_name":"SUBMITTED TO CPU",
    #     	               "filters":[]
    #     	 }]
    #     },
    #     {
    #     	"stage_name": "IN_PROGRESS_AT_CPU",
    #     	"display_name": "IN PROGRESS AT CPU",
    #     	"sub_stage": [{
    #     	  "sub_stage_name": "IN_PROGRESS_AT_CPU",
    #     	  "sub_stage_display_name" : "IN PROGRESS AT CPU",
    #     	  "filters": [{
    #     	               "filter_name": "OPEN",
    #     	               "display_name": "OPEN",
    #     	               "sub_filters":[]
    #     	      },{
    #     	          	"filter_name": "PENDING",
    #     	               "display_name": "PENDING",
    #     	               "sub_filters":["REPLIED_BY_RM","CUSTOMER_REVIEW_DONE","ALL_PENDING"]
    #     	      },{
    #     	              "filter_name":"SUBMITTED",
    #     	              "display_name":"SUBMITTED",
    #     	              "sub_filters":[]
    #     	      }]
    #     	}]
    #     }
    #     ],
    # "Team Lead":[
    #     {
    #     	"stage_name": "SUBMITTED_TO_CPU",
    #     	"display_name": "SUBMITTED TO CPU",
    #     	"sub_stage": [{
    #     	               "sub_stage_name":"SUBMITTED_TO_CPU",
    #     	               "display_name":"SUBMITTED TO CPU",
    #     	               "filters":[]
    #     	 }]
    #     },
    #     {
    #     	"stage_name": "IN_PROGRESS_AT_CPU",
    #     	"display_name": "IN PROGRESS AT CPU",
    #     	"sub_stage": [{
    #     	  "sub_stage_name": "IN_PROGRESS_AT_CPU",
    #     	  "sub_stage_display_name" : "IN PROGRESS AT CPU",
    #     	  "filters": [{
    #     	               "filter_name": "OPEN",
    #     	               "display_name": "OPEN",
    #     	               "sub_filters":[]
    #     	      },{
    #     	          	"filter_name": "PENDING",
    #     	               "display_name": "PENDING",
    #     	               "sub_filters":[]
    #     	      },{
    #     	              "filter_name":"SUBMITTED",
    #     	              "display_name":"SUBMITTED",
    #     	              "sub_filters":[]
    #     	      }]
    #     	}]
    #     }
    #     ],
    "Credit Processor": [
        {
            "stage_name": "CREDIT_RECOMMENDATION",
            "display_name": "CREDIT RECOMMENDATION",
            "sub_stage": [
                {"sub_stage_name": "INCOME_PROOF", "display_name": "INCOME PROOF", "filters": []},
                {"sub_stage_name": "OBLIGATION_ANALYSIS", "display_name": "OBLIGATION ANALYSIS", "filters": []},
                {"sub_stage_name": "UNDERWRITING", "display_name": "UNDERWRITING", "filters": []},
                {"sub_stage_name": "FI", "display_name": "FI", "filters": []},
            ],
        },
        {
            "stage_name": "PENDING_FOR_DDE",
            "display_name": "PENDING FOR DDE",
            "sub_stage": [{"sub_stage_name": "PENDING_FOR_DDE", "display_name": "PEDNDING FOR DDE", "filters": []}],
        },
    ],
    "Underwriter": [
        {
            "stage_name": "PENDING_FOR_DDE",
            "display_name": "PENDING FOR DDE",
            "sub_stage": [{"sub_stage_name": "PENDING_FOR_DDE", "display_name": "PEDNDING FOR DDE", "filters": []}],
        }
    ],
    "FI_Vendor": [
        {
            "stage_name": "FI",
            "display_name": "FI",
            "sub_stage": [
                {"sub_stage_name": "FI_INITIATED", "display_name": "", "filters": []},
                {"sub_stage_name": "FI_COMPLETED", "display_name": "", "filters": []},
            ],
        }
    ],
}


RCU_STATUS = ['Positive', 'Refer to Credit', 'Negative', 'Hard Negative']

HUNTER_LOAN_PURPOSE_MAPPING = {
    'home loan': '0',
    'Home Equity': '0',
    'msme tl': '1'
}

class RelatedAddressEnum(StrEnum):
    AADHAR = 'Aadhar'
    CURRENT = 'Current'
    CURRENT_OF_APPLICANT = 'Current Address of Primary Applicant'
    NONE = 'None'


class ReasonForWaiverEnum(StrEnum):
    REASON1 = 'R1'
    REASON2 = 'R2'
    ALREADY_EXISTS = 'Already Exists'
    AUTO = 'auto'


class PreSanctionEnum(StrEnum):
    NOVEL_REPORT = 'NOVEL_REPORT'


ZONAL_CREDIT_MANAGER = 'Zonal Credit Manager'
AREA_CREDIT_MANAGER = 'Area Credit Manager'
RISK_HEAD = {
    'name': 'Bhavesh Prajapati',
    'email': 'Bhavesh.prajapati@caprihomeloans.com'
}

BRE_GENERATE_TOKEN_CREDENTIALS = {
    "username": "ILOS",
    "password": "i10$@c@pR1"
}

class OpType(StrEnum):
    ADD_CO_APPLICANT = 'add_coapplicant'
    ADD_GUARANTOR = 'add_guarantor'


class OpStatus(StrEnum):
    SUBMITTED = 'SUBMITTED'
    RM_CANCELLED = 'RM CANCELLED'


class PropertyTechnicalStatus(StrEnum):
    REFERRED_BRANCH = "REFERRED_BRANCH"
    ASSIGNED_EVALUATOR = "ASSIGNED_EVALUATOR"
    VALUATION_REPORT_SUBMIT = "VALUATION_REPORT_SUBMIT"
    RETRIGGER_EVALUATION = "RETRIGGER_EVALUATION"
    REPORT_SUBMITTED = "REPORT_SUBMITTED"
    REPORT_UPDATED = "REPORT_UPDATED"
    SEND_BACK = "SEND_BACK"
    FINAL_VALUATION_SUBMIT = "FINAL_VALUATION_SUBMIT"


class TechnicalStage(StrEnum):
    VALUATION = "TECHNICAL_VALUATION"
    VETTING = "TECHNICAL_VETTING"
    TECH_APPROVAL = "TECHNICAL_APPROVAL"
    CREDIT_APPROVAL = "CREDIT_APPROVAL"
    RELOOK_POOL = "RELOOK_POOL"
    COMPLETED = "COMPLETED"


class TechnicalConstants:
    MIN_LOAN_LIMIT = 2500000
    TECHNICAL_1 = "TECHNICAL_1"
    TECHNICAL_2 = "TECHNICAL_2"
    RELOOK_POOL_OFFSET_DAYS = 30
    YES = "Y"
    NO = "N"
    APPROVAL_TECHNICAL_LOAN_AMOUNT = 5000000
    MIN_TECHNICAL_REQUIRED_UNDER_50_LAKH = 1
    MIN_TECHNICAL_REQUIRED_ABOVE_50_LAKH = 2


    RETRIGGER = "RETRIGGER"
    RE_ASSIGN_TIME_LIMIT = 24 * 60 * 60 * 1000

    TECHNICAL_REPORTS_FOLDER_NAME = 'upload_docs/technical_reports/'
    REPORT_UPLOAD_RETRY_COUNT = 5

    @classmethod
    def get_discard_limit(cls, loan_amount):
        return 1 if loan_amount <= cls.MIN_LOAN_LIMIT else 2


class LegalStageEnum(StrEnum):
    ON_HOLD = 'ON_HOLD'
    NEGATIVE = 'NEGATIVE'
    REJECTED = 'REJECTED'
    ASSIGNED_TO_LC = 'ASSIGNED_TO_LC'
    SUBMIT_BY_LC = 'SUBMIT_BY_LC'
    VENDOR_REPORT_SUBMIT = 'VENDOR_REPORT_SUBMIT'
    ASSIGNED_TO_LM = "ASSIGNED_TO_LM"
    RECOMMENDED_TO_LA = "RECOMMENDED_TO_LA"
    ASSIGNED_TO_CREDIT = "ASSIGNED_TO_CREDIT"
    SUBMITTED_BY_CREDIT = "SUBMITTED_BY_CREDIT"
    HOLD_DOC_PENDING = 'HOLD_DOC_PENDING'
    QUERY_NOT_RESOLVED = 'QUERY_NOT_RESOLVED'

    
class ProductTypeEnum(StrEnum):
    CGCL = 'CGCL'
    CGHFL = 'CGHFL'
    
    
class ReportStatusEnum(StrEnum):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    
    
class CRONIntervalType:
    DAILY = 'days'
    HOURLY = 'hours'
    MINUTELY = 'minutes'
    SECONDLY = 'seconds'
    MONTHLY = 'months'


class CRONConfig:
    UPDATED_BY_PREFIX = 'CRON_'
    HOLD_DOC_EXPIRE_DAYS = 7
    HOLD_DOC_REJECT_DAYS = 45

    # Trigger Configurations
    HOLD_DOC_TRIGGER = {'interval': 5, 'interval_type': CRONIntervalType.MINUTELY} # Every 5 mins
    

PRODUCT_TYPES = {
    ProductTypeEnum.CGCL.value: 'Capri Global Capital Ltd',
    ProductTypeEnum.CGHFL.value: 'Capri Global Housing Finance Limited'  
}

loan_amount_constraints = {
    'msme tl':{
        'min':200000,
        'max':15000000,
    },
    'home loan':{
        'min':200000,
        'max':15000000,
    },
    'home equity':{
        'min':200000,
        'max':10000000,
    }
}

loan_tenure_constraints_in_months = {
    'msme tl':{
        'min':12,
        'max':180
    },
    'home equity':{
        'min':12,
        'max':180
    },
    'home loan':{
        'min':12,
        'max':380
    }
}

DISCRETE_CHECK_RESULT = 'discreet_check_result'


RCU_CREDIT_STATUS_DEVIATION_MATRIX = {
    'proceed': {
        'Positive': None,
        'Refer to credit': 'Area Credit Manager',
        'Negative': 'Zonal Credit Manager',
        'Hard Negative': 'risk head'
    },
    'reject': {
        'Positive': None,
        'Refer to credit': None,
        'Negative': None,
        'Hard Negative': None
    }
}


ZONAL_CREDIT_MANAGER = 'Zonal Credit Manager'
AREA_CREDIT_MANAGER = 'Area Credit Manager'
RISK_HEAD = {
    'name': 'Bhavesh Prajapati',
    'email': 'Bhavesh.prajapati@caprihomeloans.com'
}

BRE_GENERATE_TOKEN_CREDENTIALS = {
    "username": "ILOS",
    "password": "i10$@c@pR1"
}

LEGAL_MANAGER = 'Legal Manager'


class SectionName(StrEnum):
    UNDERWRITING ='under-writing'
    CREDIT_UNDERWRITING ='credit-underwriting'
    LEGAL = 'legal'
    

# TODO 
department_mapping_dict = {
    'technical_ur': 'Technical (PV) - UR',
    'credit_ur': 'Credit - UR',
    'sales_ur': 'Sales - UR',
    'operations_ur': 'Operations - UR',
    'legal_ur': 'Legal - UR'
}


class IncomeProgramConstant:
    SALARIED_INCOME_PROGRAM = ("category_a", "category_b", "category_c", "cash")
    NIP_INCOME_PROGRAM = "nip"
    NIP_CPM_INCOME_PROGRAM = "nip_cpm"
    BANKING_SURROGATE = "banking_surrogate"
    GROSS_TURNOVER = "gross_turnover"


class PDEnum(StrEnum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    PENDING = "PENDING"
    REJECT = "REJECT"
    PENDING_FOR_REVIEW = "PENDING_FOR_REVIEW"
    QUERY_RAISED = "QUERY_RAISED"

class ModeOfRepayment(StrEnum):
    ECS = 'ECS'
    ACH = 'ACH'
    NACH = 'NACH'

class RepaymentFrequency(StrEnum):
    MONTHLY = 'Monthly'
    QUATERLY = 'Quaterly'
    YEARLY = 'Yearly'

class RiskCategory(StrEnum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class RoiType(StrEnum):
    FIXED = 'Fixed'
    FLOATING = 'Floating'
    VARIABLE = 'Variable'

class ModeOfDisbursement(StrEnum):
    CHEQUE = 'Cheque'
    ONLING = 'Online'

class Gender(StrEnum):
    MALE = 'male'
    FEMALE = 'female'

class LoanElegibilityProduct(StrEnum):
    ROI = 'ILOS_Loan_Eligibility_CGHFL_ROI'
    TENURE = 'ILOS_Loan_Eligibility_CGHFL_Tenure'


class PropertyLegalStatusEnum:
    VENDOR_SUBMITTED = 'VENDOR_SUBMITTED'
    VENDOR_ALLOCATED = 'VENDOR_ALLOCATED'
    REFERRED_TO_OTHER_BRANCH = 'REFERRED_TO_OTHER_BRANCH'
    SEND_BACK_BY_LM = 'SEND_BACK_BY_LM'


class LegalApprovalStatus(str, Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    RECOMMEND = "RECOMMEND"
    SUBMIT = "SUBMIT"


LegalHierarchyOrder = [
    "LEGAL MANAGER",
    "AREA LEGAL MANAGER",
    "REGIONAL LEGAL MANAGER",
    "ZONAL LEGAL MANAGER",
    "NATIONAL LEGAL MANAGER"
]


class Amount(int, Enum):
    TWENTY_FIVE_LAKHS = 2500000
    FIFTY_LAKHS = 5000000
    SEVENTY_FIVE_LAKHS = 7500000
    ONE_CRORE = 10000000
