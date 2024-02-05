## Installed software

![Static Badge](https://img.shields.io/badge/python-3.11.2-black?logo=Python&labelColor=EEDC9A) ![Static Badge](https://img.shields.io/badge/jenkins--lts-2.426.3-black?logo=Jenkins&labelColor=EEDC9A) ![Static Badge](https://img.shields.io/badge/pytest-8.0.0-black?logo=pytest&labelColor=EEDC9A) ![Static Badge](https://img.shields.io/badge/ngrok-3.5.0-black?logo=ngrok&labelColor=EEDC9A)


## PROBLEM STATEMENT
The objective of the repository is to implement basic math utility functions in Python <code><img width="12" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>, accompanied by test cases that can be tested using pytest <code><img width="12" src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" alt="pytest" title="pytest"/></code>. Additionally, Jenkins <code><img width="12" src="https://user-images.githubusercontent.com/25181517/179090274-733373ef-3b59-4f28-9ecb-244bea700932.png" alt="Jenkins" title="Jenkins"/></code> integration will be set up for automated testing. 

## Python
[MathUtils.py](/MathUtils.py) contains basic mathematical functions such as addition, subtraction, multiplication and division.
[tests_data.py](/tests_data.py) stores test cases for different functions.

## Pytest
[test_math_utils.py](/test_math_utils.py) contains test cases for those mathematical operations with setup and teardown methods.

## Jenkins Pipeline
- Downloaded **jenkins-lts** using ```brew install jenkins-lts``` and setting up configuration details for the admin.
- Created a pipeline in jenkins which polls this github repository using webhook and sends an email notification to the receipient with build logs.
- Intialized two stages: **build** to compile python files and **test** to run test cases and generates an xml report inside the workspace.
- Pipeline script can be found in this [Jenkinsfile](/Jenkinsfile)
- Tunneled localhost with Ngrok to create a proxy address for using a webhook in GitHub and to automate the pipeline when new commits happen.

### Pipeline Overview

<img width="1458" alt="Screenshot 2024-02-05 at 3 32 59 PM" src="https://github.com/VigneshPugalenthi/unit-testing-with-jenkins/assets/46440651/0157ced0-8d26-428b-8894-f8129a5124bd">





