

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    
    # First validate that we have A, B, C or D
    allowed_skus = "ABCD"  # List of allowed SKUs
    
    sku_string_is_valid = True  # Assume valid 

    total = 0  # Start with 0 total

    pricing_list = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15 
    }

    discounts = [
        ("A", 3, -20), # For every 3 save £20
        ("B", 2, -15)  # For every 2 save £15
    ]

    deals_memory = []  # Hold any deals in here to check for later

    # If SKUs is empty or not a string reject with -1
    if skus == "" or isinstance(skus, str) is False:
        return -1
    
    for sku in skus:  # Iterate SKUs
        if sku not in allowed_skus:  # Check in allowed SKUs
            return -1  # If contains foreign SKUs reject with -1
        else: # Valid SKU
            


    return total

    

    

