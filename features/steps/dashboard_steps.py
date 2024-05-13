"""
This module contains the step definitions for the dashboard.feature file.
"""

import time
import random
from behave import given, when, then
from selenium.webdriver.common.by import By


# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa


HTTP_201_CREATED = 201
HTTP_200_OK = 200
HTTP_204_NO_CONTENT = 204


def select_random_client(context):
    """Select a random client from the dropdown"""
    context.numero_client = random.randint(2, 10)
    try:
        # Find the selectbox element by its container's class or another identifier
        dropdown_container = context.driver.find_element(By.CLASS_NAME, "stSelectbox")

        # Click to open the dropdown
        dropdown_container.click()

        # Select an option using an xpath that matches the option label
        option = context.driver.find_element(
            By.XPATH, f'//div[text()="{context.numero_client}"]'
        )
        option.click()

        print("Dropdown selection works correctly.")

        time.sleep(5)

        # Further interactions or validations can follow here
    except Exception as error:  # pylint: disable=broad-except
        print(f"Error testing dropdown: {error}")


@given("I visit the homepage")
def step_impl(context):
    context.driver.get(context.base_url)


@when("I click on select a specific numero_client")
def step_impl(context):
    select_random_client(context)


@then("I have the dashboard displayed for the right client")
def step_impl(context):
    try:
        # Locate all Markdown elements
        markdown_elements = context.driver.find_elements(By.CLASS_NAME, "stMarkdown")

        if len(markdown_elements) > 1:
            # Access the second Markdown element by index
            second_markdown = markdown_elements[1]

            # Retrieve and print its inner text
            second_markdown_text = second_markdown.text
            print("Second Markdown content:", second_markdown_text)
        else:
            print("Less than two Markdown elements found.")

    except Exception as error:  # pylint: disable=broad-except
        print(f"Error fetching Markdown elements: {error}")

    assert f"Currently selected client: {context.numero_client}" == second_markdown_text


@given("I am in the dashboard for a specific client")
def step_impl(context):
    context.driver.get(context.base_url)
    select_random_client(context)


@when('I click on "{analysis_name}"')
def step_impl(context, analysis_name):
    try:
        # Find the selectbox element by its container's class or another identifier
        dropdown_container = context.driver.find_element(By.CLASS_NAME, "stSelectbox")

        # Click to open the dropdown
        dropdown_container.click()

        # Select an option using an xpath that matches the option label
        option = context.driver.find_element(
            By.XPATH, f'//div[text()="{analysis_name}"]'
        )
        option.click()

        print("Dropdown selection works correctly.")

        time.sleep(5)

        # Further interactions or validations can follow here
    except Exception as error:  # pylint: disable=broad-except
        print(f"Error testing dropdown: {error}")


@then('I have the markdown "{analysis_name}"')
def step_impl(context, analysis_name):
    try:
        # Locate all Markdown elements
        markdown_elements = context.driver.find_elements(By.CLASS_NAME, "stMarkdown")

        if len(markdown_elements) > 1:
            # Access the second Markdown element by index
            third_markdown = markdown_elements[2]

            # Retrieve and print its inner text
            third_markdown_text = third_markdown.text
            print("Third Markdown content:", third_markdown_text)
        else:
            print("Less than two Markdown elements found.")

    except Exception as error:  # pylint: disable=broad-except
        print(f"Error fetching Markdown elements: {error}")

    assert analysis_name == third_markdown_text


@then('I have a metric for "{sub_analysis_name}"')
def step_impl(context, sub_analysis_name):
    try:
        # Locate all Markdown elements
        markdown_elements = context.driver.find_elements(
            By.CLASS_NAME, "element-container"
        )

        if len(markdown_elements) >= 1:
            # Access the second Markdown element by index
            last_metric = markdown_elements[-2]

            # Retrieve and print its inner text
            last_metric_text = last_metric.text
            print("Last Metric content:", last_metric_text)
        else:
            print("No Metric found")

    except Exception as error:  # pylint: disable=broad-except
        print(f"Error fetching Metric Label elements: {error}")

    assert sub_analysis_name in last_metric_text
