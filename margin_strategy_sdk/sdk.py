from enum import Enum
from typing import Dict, List


class Candle:
    """
    Data representing a single candle of variable length (check min_time and max_time).
    """

    def __init__(self) -> None:
        # Price of the first trade in the candle.
        self.in_value = None
        # Highest traded price in the candle.
        self.max = None
        # Time of the latest trade in the candle or closing time of the candle.
        self.max_time = None
        # Lowest traded price in the candle.
        self.min = None
        # Start time of the candle.
        self.min_time = None
        # Price of the last trade in the candle.
        self.out_value = None
        # Number of trades included in the candle.
        self.trade_number = None
        # Volume traded within the candle.
        self.volume = None
        # Value weighted average price of the candle.
        self.vwap = None


class ExitReason(Enum):
    """
    The reason for an exit call.
    """
    # The strategy has to be aborted due to unexpected circumstances.
    ABORT = 0
    # The strategy has to be stopped because of an error.
    ERROR = 1
    # The strategy finished successfully.
    FINISHED_SUCCESSFULLY = 2



class FundsEntry:
    """
    An entry in the funds map.
    """

    def __init__(self) -> None:
        # The available amount for a currency.
        self.available = None
        # The reserved amount for a currency.
        self.reserved = None
        # Total amount of a currency in the account.
        self.total_for_currency = None


class OrderBookEntry:
    """
    An entry of an order book.
    """

    def __init__(self) -> None:
        # Amount of the order book entry.
        self.amount = None
        # Price of the order book entry.
        self.price = None


class OrderBook:
    """
    An order book containing a list of order book entries for each ask and bid side.
    """

    def __init__(self) -> None:
        # List of asks ordered by price in ascending order.
        self.asks = None
        # List of bids ordered by price in descending order.
        self.bids = None


class Order:
    """
    An order owned by the user.
    """

    def __init__(self) -> None:
        # Overall amount of the order.
        self.amount = None
        # True if the order is a buy order.
        self.buy = None
        # Id of the order.
        self.id = None
        # Price of the order.
        self.price = None
        # Amount that has been filled already.
        self.received_amount = None
        # Amount that has not been filled yet.
        self.remaining_amount = None
        # Timestamp of the order.
        self.timestamp = None


class OrderUpdate:
    """
    Update for a strategy order.
    """

    class Status(Enum):
        """
        Update status defining what happened to the order since the last update.
        """
        # The order was filled.
        FILLED = 0
        # The order was adapted by the user (this means the order id changes).
        ADAPTED = 1
        # The order was canceled by the user.
        CANCELED = 2
        # The order did not change.
        NO_CHANGE = 3
        # The order reappeared after disappearing.
        REAPPEARED = 4
        # The order could not be found anymore. It could become filled after this or reappear.
        DISAPPEARED = 5
        # A change to the order occured.
        OTHER_CHANGE = 6
        # The order got partially filled.
        PARTIALLY_FILLED = 7
        # The order was adapted by the user and got filled.
        ADAPTED_AND_FILLED = 8

    ADAPTED = Status.ADAPTED
    ADAPTED_AND_FILLED = Status.ADAPTED_AND_FILLED
    CANCELED = Status.CANCELED
    DISAPPEARED = Status.DISAPPEARED
    FILLED = Status.FILLED
    NO_CHANGE = Status.NO_CHANGE
    OTHER_CHANGE = Status.OTHER_CHANGE
    PARTIALLY_FILLED = Status.PARTIALLY_FILLED
    REAPPEARED = Status.REAPPEARED

    def __init__(self) -> None:
        # Original order previous to this update.
        self.original_order = None
        # Trades that belong to the order, if any exist so far.
        self.resulting_trades = None
        # Update status defining what happened to the order since the last update.
        self.status = None
        # Time of the change.
        self.timestamp = None
        # Newly updated order.
        self.updated_order = None


class PrivateTrade:
    """
    A trade owned by the user.
    """

    def __init__(self) -> None:
        # Amount of the trade.
        self.amount = None
        # True, if the trade was a buy.
        self.buy = None
        # Id of the trade.
        self.id = None
        # Id of the order that the trade belongs to.
        self.order_id = None
        # Price at which the trade was executed.
        self.price = None
        # Timestamp of the trade.
        self.timestamp = None


class PublicTrade:
    """
    Trade done on the currency pair by someone on the exchange.
    """

    def __init__(self) -> None:
        # Amount of the trade.
        self.amount = None
        # True, if the trade was a buy.
        self.buy = None
        # Id of the trade.
        self.id = None
        # Price at which the trade was executed.
        self.price = None
        # Time when the trade was executed in the exchange.
        self.timestamp = None


class RoundingType(Enum):
    """
    Defines the rounding operation that is going to be used.
    """
    # Rounds the value up.
    CEIL = 0
    # Rounds the value down.
    FLOOR = 1
    # Rounds the value to the closest rounded value.
    ROUND = 2



class Ticker:
    """
    Ticker data.
    """

    def __init__(self) -> None:
        # Price of the currency pair one day ago.
        self.last_day_price = None
        # Last traded price of the currency pair.
        self.last_price = None
        # Timestamp of the ticker data.
        self.timestamp = None


class StrategyConfig:
    """
    Configuration of the strategy. This contains for example the data updates that the strategy needs. The configuration will determine which functions on the strategy are called, when there is new data or changes to strategy orders.
    """

    class DataSubscriptionType(Enum):
        """
        The type of subscriptions that the strategy needs to receive.
        """
        # Receive the latest order book updates.
        ORDER_BOOK = 0
        # Receive the latest public trade history updates.
        PUBLIC_TRADE_HISTORY = 1
        # Receive the latest ticker.
        TICKER = 2
        # Receive the latest changes to your relevant funds.
        FUNDS = 3

    FUNDS = DataSubscriptionType.FUNDS
    ORDER_BOOK = DataSubscriptionType.ORDER_BOOK
    PUBLIC_TRADE_HISTORY = DataSubscriptionType.PUBLIC_TRADE_HISTORY
    TICKER = DataSubscriptionType.TICKER

    def __init__(self) -> None:
        # This set should contain all the data types that are required by the strategy, as only the specified ones will be updated.
        self.required_data_updates = None


class TradingCapabilityManager:
    """
    Accessor for trading capability information. Used to get minimum and maximum amounts and prices for order placing, round amounts and prices correctly and validate orders before placing them.
    """

    def get_due_buy_total(self, amount: float, price: float) -> float:
        """
        Returns the total that is going to be extracted from the funds when placing a buy order at the given amount and price.
        """
        return None

    def get_max_buy_amount(self, price: float) -> float:
        """
        Returns the maximally possible buy amount that can be placed at a given price.
        """
        return None

    def get_max_sell_amount(self, price: float) -> float:
        """
        Returns the maximally possible sell amount that can be placed at a given price.
        """
        return None

    def get_min_buy_amount(self, price: float) -> float:
        """
        Returns the minimally possible buy amount that can be placed at a given price.
        """
        return None

    def get_min_sell_amount(self, price: float) -> float:
        """
        Returns the maximally possible sell amount that can be placed at a given price.
        """
        return None

    def get_minimal_amount_change(self, reference_amount: float) -> float:
        """
        Get the minimal amount change that is possible to use on the exchange around the reference amount value.
        """
        return None

    def get_minimal_price_change(self, reference_price: float) -> float:
        """
        Get the minimal price change that is possible to use on the exchange around the reference price value.
        """
        return None

    def get_sell_amount_to_receive_total(self, target_total: float, price: float, rounding_type: RoundingType) -> float:
        """
        Returns the amount that needs to be placed in a sell order at the given price to receive the target total.
        """
        return None

    def get_sell_total_to_receive(self, amount: float, price: float) -> float:
        """
        Returns the total that is going to be added to the funds when a sell order at the given amount and price goes through.
        """
        return None

    def is_order_valid(self, buy: bool, amount: float, price: float) -> bool:
        """
        Checks whether the order consisting of buy/sell side, price and amount could be placed as it is. If this returns false, you need to adapt the rounding of the amount or price or check that the amount is in the range of min/max amount for the selected side.
        """
        return None

    def round_amount(self, unrounded_amount: float, rounding_type: RoundingType) -> float:
        """
        Rounds an amount of an order, trade etc. to the correct number of decimals.
        """
        return None

    def round_price(self, unrounded_price: float, rounding_type: RoundingType) -> float:
        """
        Rounds an price of an order, trade etc. to the correct number of decimals.
        """
        return None


class StrategyBase:
    """
    Base class of any user created strategies. Implement the required functions to make the strategy functional.
    """

    def cancel_order(self, order_id: int) -> None:
        """
        Use this function to cancel an order. Make sure to use the order_id of an actually open order and not the order_placing_id returned by the place_order function.
        """
        return None

    def exit(self, reason: ExitReason, message: str = '') -> None:
        """
        Use this function to end the strategy. This can be done after the strategy finishes successfully, has to be aborted or after an error occured.
        """
        return None

    def get_buffered_completed_trades(self) -> List[PrivateTrade]:
        """
        Use this function to instantly get the list of your completed trades associated to this strategy.
        """
        return None

    def get_buffered_funds(self) -> Dict[str, FundsEntry]:
        """
        Use this function to instantly get your available funds.
        """
        return None

    def get_buffered_open_orders(self) -> List[Order]:
        """
        Use this function to instantly get the list of your open orders associated to this strategy.
        """
        return None

    def get_buffered_order_book(self) -> OrderBook:
        """
        Use this function to instantly get the last available order book.
        """
        return None

    def get_buffered_recent_candles(self, candle_size_in_minutes: int, number_of_candles: int = 50) -> List[Candle]:
        """
        Use this function to instantly get a list of the most recent candles. The argument candle_size_in_minutes has to be given.
        """
        return None

    def get_buffered_recent_trades(self) -> List[PublicTrade]:
        """
        Use this function to instantly get a list of the most recent public trades.
        """
        return None

    def get_buffered_ticker(self) -> Ticker:
        """
        Use this function to instantly get the last ticker values.
        """
        return None

    def get_currency_pair(self) -> str:
        """
        Use this function to get the active currency pair.
        """
        return None

    def get_first_currency(self) -> str:
        """
        Use this function to get the base currency.
        """
        return None

    def get_second_currency(self) -> str:
        """
        Use this function to get the quote currency.
        """
        return None

    def get_strategy_config(self) -> StrategyConfig:
        """
        This function will be called to determine the requirements of the strategy.
        """
        return None

    def get_trading_capability_manager(self) -> TradingCapabilityManager:
        """
        Use this function to get the trading capability manager. This can be used to get minimum and maximum amounts and prices for order placing, round amounts and prices correctly and validate orders you intend to place.
        """
        return None

    def init(self) -> None:
        """
        This functions is called to initialize the strategy before extracting the configuration and before it can be started.
        """
        return None

    def on_cancel_order_error_string(self, order_id: int, error_message: str) -> None:
        """
        This function is called when an order has could not be canceled correctly.
        """
        return None

    def on_cancel_order_success(self, order_id: int, canceled_order: Order) -> None:
        """
        This function is called after an order has been canceled successfully.
        """
        return None

    def on_new_funds(self, funds: Dict[str, FundsEntry]) -> None:
        """
        This function is called when the funds have changed.
        """
        return None

    def on_new_order_book(self, order_book: OrderBook) -> None:
        """
        This function is called when a new order book is available.
        """
        return None

    def on_new_public_trades(self, trades: List[PublicTrade]) -> None:
        """
        This function is called when new public trades are available.
        """
        return None

    def on_new_ticker(self, ticker: Ticker) -> None:
        """
        This function is called when a new ticker is available.
        """
        return None

    def on_order_update(self, update: OrderUpdate) -> None:
        """
        This functions is called when an order has changed.
        """
        return None

    def on_place_order_error_string(self, order_placing_id: int, error_message: str) -> None:
        """
        This function is called when an order has could not be placed correctly. You can identify the order using the order_placing_id which is returned by the place_order function.
        """
        return None

    def on_place_order_success(self, order_placing_id: int, order: Order) -> None:
        """
        This function is called after an order has been placed successfully. You can identify the order using the order_placing_id which is returned by the place_order function.
        """
        return None

    def place_limit_order(self, buy: bool, amount: float, price: float) -> int:
        """
        Use this function to place an order. The return value is the order placing id. Either on_place_order_success or on_place_order_error_string will be called with the order placing id, when the the placing action is done.
        """
        return None

    def restore_strategy_state(self, strategy_state: Dict[str, str]) -> None:
        """
        This function will be called to restore the strategy to a previous state.
        """
        return None

    def save_strategy_state(self) -> Dict[str, str]:
        """
        This function should return all the information that needs to be saved to restore the strategy at a later time. It will be called regularly.
        """
        return None

    def set_status(self, status_string: str) -> None:
        """
        Use this function to set the strategy status displayed in the strategy window.
        """
        return None

    def start(self) -> None:
        """
        This function is called to start the strategy. Afterwards the strategy will also receive data updates.
        """
        return None

    def stop(self) -> None:
        """
        This function is called to stop the strategy. Make sure everything is stopped and cleaned up here before the function returns.
        """
        return None

    def suspend(self) -> None:
        """
        This function is called to suspend the strategy. Afterwards the state of the strategy will be saved for later use, but other than that the strategy should then be inactive. Make sure to stop any running threads etc. before the function returns.
        """
        return None

    def unsuspend(self) -> None:
        """
        This function is called to unsuspend the strategy to pick up its action. This can happen after a manual suspend or network outage or after the restart of margin.
        """
        return None


class LogLevel(Enum):
    """
    Level of logging
    """
    # Debug logging level
    DEBUG = 0
    # Info logging level
    INFO = 1
    # Important logging level
    IMPORTANT = 2
    # Warning logging level
    WARNING = 3
    # Error logging level
    ERROR = 4
    # Critical error logging level
    CRITICAL = 5



def write_log(level: LogLevel, message: str) -> None:
    """
    Use this function to write to the bot log.
    """
    return None


