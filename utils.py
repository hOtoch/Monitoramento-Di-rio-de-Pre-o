def format_price_text(price_text):
    price_formated = price_text.replace('.','').replace(',','.')
    
    price_formated = ''.join([c for c in price_formated if c.isdigit() or c == '.'])
    
    return float(price_formated)
    