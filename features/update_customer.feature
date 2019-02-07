Feature: Update the customer based on id
  As a service I want to the update customer details.

  Scenario: Updating existing customer
    Given customer "Nicole Forsgren" with ID "12345" exists
    When I update customer "12345" surname to "Jones"
    When I fetch customer "12345"
    Then I should see customer "Nicole Jones"
