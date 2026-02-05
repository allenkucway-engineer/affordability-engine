from validate import extract_income
from parse import parse_income
from logic import affordable_payment
from output import format_result


def run(user):
    """
    Orchestrator: moves data through the pipeline in order.
    """
    raw_income = extract_income(user)      # validation + extraction
    income = parse_income(raw_income)      # parsing
    payment = affordable_payment(income)   # business logic
    return format_result(payment)          # output formatting


if __name__ == "__main__":
    # Manual test / demo
    demo_user = {"income": "60000"}
    print(run(demo_user))
