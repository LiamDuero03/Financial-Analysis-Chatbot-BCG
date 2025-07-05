# 📊 Financial Analysis Chatbot

This chatbot was developed as part of the **BCG Virtual Experience Program on Forage**.  
It simulates how generative AI can be applied to financial analysis, allowing users to query company financial data through natural language.

---

## 🧠 Project Overview

The **Financial Analysis Chatbot** uses a simple rule-based NLP approach to understand user queries about financial metrics and respond using the latest available data.

### Users can ask about:
- Total Revenue  
- Net Income Change  
- Total Assets  
- Cash Flow from Operating Activities  
- Total Liabilities Change  

If no company is mentioned, it defaults to Tesla.

---

## 💼 Companies Analyzed
- **Apple**
- **Microsoft**
- **Tesla**

The data includes:
- Revenue
- Net income
- Assets
- Liabilities
- Cash flow
- Year-over-year percentage changes

---

## ⚙️ How It Works

The chatbot pipeline includes:
- A `main.py` CLI interface
- A `chatbot.py` module to handle logic
- A `data_extraction.py` module to query the data from a preprocessed DataFrame

---

## 🚀 Getting Started

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/financial-chatbot.git
cd financial-chatbot
