

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    
    # First validate that we have A, B, C or D
    allowed_skus = "ABCD"
    if all(sku in allowed_skus for sku in skus) is not True:
        return -1
