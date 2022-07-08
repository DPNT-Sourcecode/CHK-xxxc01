

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    
    # First validate that we have A, B, C or D
    allowed_skus = "ABCD"  # List of allowed SKUs

    total = 0  # Start with 0 total

    pricing_list = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15 
    }

    discounts = {
        "A" : {
            "items": 0,
            "deal": 3, 
            "discount": -20
        }, # For every 3 save £20
        "B": {
            "items": 0,
            "deal": 2,
            "discount": -15
        }  # For every 2 save £15
    }

    # If SKUs is empty or not a string reject with -1
    if skus == "" or isinstance(skus, str) is False:
        return -1
    
    for sku in skus:  # Iterate SKUs

        if sku not in allowed_skus:  # Check in allowed SKUs
            return -1  # If contains foreign SKUs reject with -1

        else:  # Valid SKU
            if sku in discounts:  # This is a discounted SKU save for later
                discounts[sku]["items"] += 1

            total += pricing_list[sku]  # Keep track of totals


    # Now let's adjust for discounts by examining the discounts
    for _,v in discounts.items():
        if v["items"] % v["deal"] == 0:
            discount = (v["items"] / v["deal"]) * v["discount"]
            print(discount)
            total += discount

    return total

    

    








