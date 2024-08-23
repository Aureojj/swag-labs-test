# SWAG-LABS-TEST

## Overview
This repository contains a test project for validating the success flow of the website Sauce Demo using the username `standard_user`. The project utilizes **Behavior-Driven Development (BDD)** for scenario specification, **Pytest-bdd** for test execution, and **Selenium** for interacting with the website's interface. The **Page Object pattern** is used as a strategy for organizing test code.

## Architecture
The project follows a simple and organized architecture:

- **features/**: Contains feature files written in Gherkin syntax, which define the test scenarios.
- **pages/**: Holds page object classes, which encapsulate the website's pages and provide methods for interacting with them.
- **utils/**: Contains utility files, which provides fixtures and setup/teardown functions for tests.
- **pyproject.toml**: I'm using Poetry to organise the project's dependencies, including Pytest, Pytest-bdd, Selenium and other necessary libraries.
- **tests/**: Contains test files that execute the test scenarios defined in the feature files.

## Technologies Used
### Behavior-Driven Development (BDD)
BDD is a software development process that encourages collaboration between developers, testers, and non-technical stakeholders. It allows us to define test scenarios in a natural language, making it easier to understand and maintain.

### Pytest
Pytest is a popular testing framework for Python that provides a lot of flexibility and customization options. It's used to execute the test scenarios defined in the feature files.

### Selenium
Selenium is an automation tool that allows us to interact with web browsers programmatically. It's used to simulate user interactions with the website, such as clicking buttons and filling out forms.

### Page Object Pattern
The Page Object pattern is a design pattern that helps to organize test code by encapsulating the website's pages into separate classes. This makes it easier to maintain and update tests as the website changes.

### Allure Report
Is a popular open source tool for visualizing the results of a test run. It can be added to your testing workflow with little to zero configuration. It produces reports that can be opened anywhere and can be read by anyone, no deep technical knowledge required.

### Python Black
Is code formatter that checks Python code for errors, warnings, and best practices. It helps to maintain code quality and consistency throughout the project.

## Github Actions
GitHub Actions is an automation tool that lets you create customised workflows for compiling, testing and deploying your code directly from GitHub. It helps automate repetitive tasks, improve development efficiency and ensure project consistency and quality.

## Getting Started
To get started with this project, follow these steps:

This is necessary to run: Python ^3.10, Poetry, Docker.

1. Clone the repository: `git clone https://github.com/Aureojj/SWAG-LABS-TEST.git`
2. Install poetry: `pip install poetry`
3. Install dependencies:`poetry install` 
4. Run the container server to execute test inside: `docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest`
5. Run the tests: `poetry run pytest`

## Access the report

1. Run the Allure generate: `allure generate`
2. Run the Allure Server: `allure server`


#### Explore the feature files and page object classes to understand how the tests are organized and executed.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
