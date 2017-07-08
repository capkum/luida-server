from api.accounts.models import Accounts


def get_account_by_email(email):
    return Accounts.query.filter_by(email=email).first_or_404()
