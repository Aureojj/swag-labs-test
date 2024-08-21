# SWAG-LABS-TEST

## Overview
This repository contains a test project for validating the success flow of the website Sauce Demo using the username `standard_user`. The project utilizes **Behavior-Driven Development (BDD)** for scenario specification, **Pytest** for test execution, and **Selenium** for interacting with the website's interface. The **Page Object pattern** is used as a strategy for organizing test code.

## Architecture
The project follows a simple and organized architecture:

- **features/**: Contains feature files written in Gherkin syntax, which define the test scenarios.
- **pages/**: Holds page object classes, which encapsulate the website's pages and provide methods for interacting with them.
- **utils/**: Contains utility files, which provides fixtures and setup/teardown functions for tests.
- **requirements.txt**: Lists the project's dependencies, including Pytest, Selenium, and other required libraries.
- **test_files.py**: Contains test functions that execute the test scenarios defined in the feature files.

## Technologies Used
### Behavior-Driven Development (BDD)
BDD is a software development process that encourages collaboration between developers, testers, and non-technical stakeholders. It allows us to define test scenarios in a natural language, making it easier to understand and maintain.

### Pytest
Pytest is a popular testing framework for Python that provides a lot of flexibility and customization options. It's used to execute the test scenarios defined in the feature files.

### Selenium
Selenium is an automation tool that allows us to interact with web browsers programmatically. It's used to simulate user interactions with the website, such as clicking buttons and filling out forms.

### Page Object Pattern
The Page Object pattern is a design pattern that helps to organize test code by encapsulating the website's pages into separate classes. This makes it easier to maintain and update tests as the website changes.

### Black
Black is code formatter that checks Python code for errors, warnings, and best practices. It helps to maintain code quality and consistency throughout the project.

## Getting Started
To get started with this project, follow these steps:

This is necessary to run: Python 3 and Chrome.

1. Clone the repository: `git clone https://github.com/Aureojj/SWAG-LABS-TEST.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the tests: `pytest`
4. Run the Black: `black .`
5. Explore the feature files and page object classes to understand how the tests are organized and executed.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
