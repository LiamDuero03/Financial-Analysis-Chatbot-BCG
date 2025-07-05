# chatbot.py

from data_extraction import get_latest_value, get_latest_yoy_change

def simple_chatbot(user_query: str) -> str:
    user_query = user_query.lower()

    # Extract company name - a simple approach; improve as needed
    companies = ['tesla', 'microsoft', 'apple']
    company = None
    for comp in companies:
        if comp in user_query:
            company = comp
            break
    if not company:
        company = 'tesla'  # default company if none found

    if "total revenue" in user_query:
        return f"The total revenue for {company.title()} is {get_latest_value(company, 'Total Revenue')}."
    
    elif "net income changed" in user_query or "net income change" in user_query:
        return f"The net income for {company.title()} has {get_latest_yoy_change(company, 'Net Income')}."
    
    elif "total assets" in user_query:
        return f"The total assets for {company.title()} are {get_latest_value(company, 'Total Assets')}."
    
    elif "cash flow" in user_query or "operating activities" in user_query:
        return f"The cash flow from operating activities for {company.title()} is {get_latest_value(company, 'Cash Flow from Operating Activities')}."
    
    elif "liabilities changed" in user_query or "liabilities change" in user_query:
        return f"The total liabilities for {company.title()} have {get_latest_yoy_change(company, 'Total Liabilities')}."
    
    else:
        return "Sorry, I can only provide information on predefined financial queries."

