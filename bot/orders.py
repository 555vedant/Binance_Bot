import logging

def place_order(client, symbol, side, order_type, quantity, price=None):

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    try:
        response = client.futures_create_order(**params)
        return response
    except Exception as e:
        logging.error(f"ORDER ERROR | {e}")
        raise