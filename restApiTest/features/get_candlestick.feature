Feature: Get Candlestick
  Retrieves candlesticks (k-line data history) over a given period for an instrument (e.g. BTC_USDT)

  Scenario Outline: Verify public/get-candlestick
    Given User send request with "<instrument_name>" and "<interval>"
    Then check the "<response_status>" is expected
    Then check the "<response_code>" is correct
    Then check the "<response_method>" is expected method
    Then check the instrument name in result is correct
    Then check the interval in result is correct
    Then verify the k-line data is correct at the "<specified_time>"

    Examples:
      |instrument_name|interval|response_status|response_code|response_method|specified_time|
      |ETH_CRO        |7D      |200            |0            |public/get-candlestick|2020-06-25 08:00:00|


  Scenario Outline: Verify public/get-candlestick with invalid instrument
    Given User send request with "<instrument_name>" and "<interval>"
    Then check the response is invalid

    Examples:
      |instrument_name|interval|
      |ETH_CRO_invalid|7D      |
      |      111      |7D      |



  Scenario Outline: Verify public/get-candlestick with invalid interval
    Given User send request with "<instrument_name>" and "<interval>"
    Then check the response is invalid interval

    Examples:
      |instrument_name|interval|
      |ETH_CRO         |7H     |
      |ETH_CRO         |35m    |
      |ETH_CRO         |3242424|

