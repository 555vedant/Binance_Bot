import random
import logging

class MockBinanceClient:

    def futures_create_order(self, **params):

        logging.info(f"API REQUEST | {params}")

        order_id = random.randint(100000, 999999)

        response = {
            "orderId": order_id,
            "symbol": params["symbol"],
            "side": params["side"],
            "type": params["type"],
            "status": "FILLED" if params["type"] == "MARKET" else "NEW",
            "executedQty": params["quantity"],
            "avgPrice": params.get("price", "65000")
        }

        logging.info(f"API RESPONSE | {response}")

        return response


def get_client():
    return MockBinanceClient()