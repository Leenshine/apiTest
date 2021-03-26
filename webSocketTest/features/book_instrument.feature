Feature: book.{instrument_name}.{depth}
  Publishes order book changes for an instrument (e.g. BTC_USDT) based on price level depth


  Scenario Outline: Verify book.{instrument_name}.{depth}
    Given User send request with "<instrument_name>" and "<depth>"
    Then check the "<method>" is expected
    Then check the "<instrument_name>" is correct
    Then check the "<subscription>" is expected subscription
    Then check the "<depth>" is expected depth

    Examples:
      |instrument_name|depth|method|subscription|
      |ETH_CRO        |150  |subscribe|book.ETH_CRO.150|
      |BTC_USDT       |10   |subscribe|book.BTC_USDT.10|




  Scenario Outline: Verify book.{instrument_name}.{depth} invalid
    Given User send request with "<instrument_name>" and "<depth>"
    Then verify the invalid response message

    Examples:
      |instrument_name|depth|
      |ETH_CRO        |1  |
      |ETH_CRO_invalid|150|


