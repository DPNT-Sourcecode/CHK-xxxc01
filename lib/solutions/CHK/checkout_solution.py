

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    
    # First validate that we have A, B, C or D
    allowed_skus = "ABCD"  # List of allowed SKUs
    
    sku_string_is_valid = True  # Assume valid 
    
    for sku in skus:  # Iterate SKUs
        if sku not in allowed_skus:  # Check in allowed SKUs
            sku_string_is_valid = False

    if sku_string_is_valid == False:  # If contains foreign SKUs reject with -1
        return -1

    



