Feature: book.{instrument_name}.{depth}
  Publishes order book changes for an instrument (e.g. BTC_USDT) based on price level depth


  Scenario Outline: Verify book.{instrument_name}.{depth}
    Given User send request with "<instrument_name>" and "<depth>"
#    Then check the "<method>" is expected
#    Then check the "<response_code>" is correct
#    Then check the "<response_method>" is expected method
#    Then check the instrument name in result is correct
#    Then check the interval in result is correct
#    Then verify the k-line data is correct at the "<specified_time>"

    Examples:
      |instrument_name|depth|method|response_code|response_method|specified_time|
      |ETH_CRO        |10   |subscribe|0            |public/get-candlestick|2020-06-25 08:00:00|
#      |ETH_CRO        |7D      |200         |0            |public/get-candlestick|2020-06-25 08:00:00|