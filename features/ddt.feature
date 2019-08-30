@ddt
  Feature: Check DDT
  Scenario Outline: Open practiceselenium.com website and fill multiple values
    When I open practiceselenium website
    And I fill "<firstname>" "<lastname>" "<sex>" "<yrs>" "<date_stopped>"
    And I fill "<tea>" "<excited_about>" "<continent>" and "<selenium_commands>"
    And I hit submit button
    Then I go back to Welcome page and verify title
  Examples:
  |firstname| lastname|sex|yrs|date_stopped|tea|excited_about|continent|selenium_commands|
  |Pradeep  |kumar    |Male|2|1/1/2000|Red Tea|Break|Europe|Navigation Commands|
  |Greg  |Mont    |Male|1|1/1/2001|Black Tea|Harmless Addiction|Asia|Browser Commands|
  |Rex  |Morg    |Male|3|3/1/2010|oolong tea|Harmless Addiction|USA|Wait Commands|
  |Captain  |Cook    |Male|5|5/2/2010|Red Tea|Harmless Addiction|USA|Switch Commands|
  |Michele  |Bing    |Female|5|5/2/2011|Black Tea|Harmless Addiction|USA|Switch Commands|