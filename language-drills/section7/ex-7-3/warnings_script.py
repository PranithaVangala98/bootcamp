import warnings

def deprecated_func():
    warnings.warn("old_function() is deprecated and will be removed in a future version.", 
                  category=DeprecationWarning)

deprecated_func()
