import re
import json

with open('raw.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Extract all prices
prices = re.findall(r'\d[\d ]*,\d{2}', text)

# 2. Find all product names
products_matches = re.findall(r'\d+\.\s*(.*?)\s*\d+[, ]\d{2}', text)

# 3. Calculate total amount
total = sum(prices)

# 4. Extract date and time
datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})', text)
date_time = datetime_match.group(1) if datetime_match else ''

# 5. Find payment method
payment_match = re.search(r'Банковская карта|Наличными', text)
payment_method = payment_match.group(0) if payment_match else 'Unknown'

# 6. Create structured output
receipt_data = {
    'products': [{'name': name, 'price': price} for name, price in zip(products_matches, prices)],
    'total_calculated': total,
    'date_time': date_time,
    'payment_method': payment_method
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=4))