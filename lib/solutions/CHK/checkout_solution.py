

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    
    # First validate that we have A, B, C or D
    allowed_skus = "ABCD"  # List of allowed SKUs
    
    sku_string_is_valid = True  # Assume valid 

    total = 0

    # If SKUs is empty or not a string reject with -1
    if skus == "" or isinstance(skus, str) is False:
        return -1
    
    for sku in skus:  # Iterate SKUs
        if sku not in allowed_skus:  # Check in allowed SKUs
            sku_string_is_valid = False
        # else:
        #     if 

    if sku_string_is_valid == False:  # If contains foreign SKUs reject with -1
        return -1

    else:
        return True

    

    




