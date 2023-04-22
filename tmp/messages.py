

class ROR:

    def __init__(self):
        # mobile
        self.mobile_acquisition_status = 'User Mobile Exists with Another Partner Under Attribution Period'
        self.mobile_acquisition_date_and_same_partner_cooloff = 'User Mobile Exists With Same Partner Within Attribution\Cooloff Period'
        self.mobile_user_profile_rejected = 'User Profile Rejected Within Attribution Period'
        self.mobile_user_registration = 'User Profile Registered Within Attribution Period'
        self.mobile_user_profile_approved = 'User Profile Approved Within Attribution Period'
        self.mobile_user_loan_exist = 'User Already Taken First Loan'
        self.mobile_user_mobile_history = 'Mobile Used Earlier With Another User'
        #email
        self.email_acquisition_status = 'User Email Exists with Another Partner Under Attribution Period'
        self.email_acquisition_date_and_same_partner_cooloff = 'User Email Exists with Same Partner Within Attribution\Cooloff Period'
        self.email_user_profile_rejected = 'User Profile Rejected Within Attribution Period'
        self.email_user_registration = 'User Profile Registered Within Attribution Period'
        self.email_user_profile_approved = 'User Profile Approved Within Attribution Period'
        self.email_user_loan_exist = 'User Already Taken First Loan'
        #mobileEmail
        self.mobileEmail_acquisition_status = 'User Mobile\Email Exists with Another Partner Under Attribution Period'
        self.mobileEmail_acquisition_date_and_same_partner_cooloff = 'User Mobile\Email Exists with Same Partner Within Attribution\Cooloff Period'
        self.mobileEmail_user_profile_rejected = 'User Profile Rejected Within Attribution Period'
        self.mobileEmail_user_registration = 'User Profile Registered Within Attribution Period'
        self.mobileEmail_user_profile_approved = 'User Profile Approved Within Attribution Period'
        self.mobileEmail_user_loan_exist = 'User Already Taken First Loan'
        #reactivation
        self.reactivation_reactivation_eligible = 'Partner Is Not Eligible For Reactivation'
        self.reactivation_no_loan = 'User Is Not Eligible For Reactivation, No Loan Taken Previously'
        self.reactivation_open_loan = 'User Has an Open Loan'
        self.reactivation_loan_closed_date = 'Reactivation Criteria Breached (135 Days)'
        self.reactivation_negative_credit = 'User Has a Negative Credit Limit'
        self.reactivation_reactivated = 'Lead Already Exisit With Some Another Partner Under Reactivation'
        self.reactivation_reactivation_cooloff = 'Reactivation Not Allowed in Cooloff Period'
        self.reactivation_reactivation_date = 'Reactivation Not Allowed in Attribution Period'

