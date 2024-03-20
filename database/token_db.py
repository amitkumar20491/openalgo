from database.master_contract_db import SymToken  # Import here to avoid circular imports
from cachetools import TTLCache

# Define a cache for the tokens with a max size and a 60-second TTL
token_cache = TTLCache(maxsize=1024, ttl=60)

def get_token(symbol, exchange):
    """
    Retrieves a token for a given symbol and exchange, utilizing a cache to improve performance.
    """
    cache_key = f"{symbol}-{exchange}"
    # Attempt to retrieve from cache
    if cache_key in token_cache:
        return token_cache[cache_key]
    else:
        # Query database if not in cache
        token = get_token_dbquery(symbol, exchange)
        # Cache the result for future requests
        if token is not None:
            token_cache[cache_key] = token
        return token

def get_token_dbquery(symbol, exchange):
    """
    Queries the database for a token by symbol and exchange.
    """
    
    try:
        sym_token = SymToken.query.filter_by(symbol=symbol, exchange=exchange).first()
        if sym_token:
            return sym_token.token
        else:
            return None
    except Exception as e:
        print(f"Error while querying the database: {e}")
        return None
    


def get_symbol(token, exchange):
    """
    Retrieves a symbol for a given token and exchange, utilizing a cache to improve performance.
    """
    cache_key = f"{token}-{exchange}"
    # Attempt to retrieve from cache
    if cache_key in token_cache:
        return token_cache[cache_key]
    else:
        # Query database if not in cache
        symbol = get_symbol_dbquery(token, exchange)
        # Cache the result for future requests
        if symbol is not None:
            token_cache[cache_key] = symbol
        return symbol

def get_symbol_dbquery(token, exchange):
    """
    Queries the database for a symbol by token and exchange.
    """
    try:
        sym_token = SymToken.query.filter_by(token=token, exchange=exchange).first()
        if sym_token:
            return sym_token.symbol
        else:
            return None
    except Exception as e:
        print(f"Error while querying the database: {e}")
        return None


def get_oa_symbol(symbol, exchange):
    """
    Retrieves a symbol for a given token and exchange, utilizing a cache to improve performance.
    """
    cache_key = f"oa{symbol}-{exchange}"
    # Attempt to retrieve from cache
    if cache_key in token_cache:
        return token_cache[cache_key]
    else:
        # Query database if not in cache
        oasymbol = get_oa_symbol_dbquery(symbol, exchange)
        # Cache the result for future requests
        if oasymbol is not None:
            token_cache[cache_key] = oasymbol
        return oasymbol

def get_oa_symbol_dbquery(symbol, exchange):
    """
    Queries the database for a symbol by token and exchange.
    """
    try:
        sym_token = SymToken.query.filter_by(brsymbol=symbol, exchange=exchange).first()
        if sym_token:
            return sym_token.symbol
        else:
            return None
    except Exception as e:
        print(f"Error while querying the database: {e}")
        return None
