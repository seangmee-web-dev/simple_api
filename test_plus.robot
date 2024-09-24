*** Settings ***
Library    RequestsLibrary


*** Test Cases ***
Test Calculate Numbers 6 and 5 (ฺBefore Using Keywords)

    ${resp}=     GET    http://127.0.0.1:8000/plus/6/5

    # Verify the status code is 200 (OK)
    Should Be Equal    ${resp.status_code}    ${200}

    # Get the response content as a JSON object
    ${json_resp}=    Set Variable  ${resp.json()}

    # Verify the response of plus operation
    Should Be Equal    ${json_resp['result']}    ${11}

Test Calculate Numbers 8 and 8 (ฺBefore Using Keywords)

    ${resp}=     GET    http://127.0.0.1:8000/plus/8/8

    # Verify the status code is 200 (OK)
    Should Be Equal    ${resp.status_code}    ${200}

    # Get the response content as a JSON object
    ${json_resp}=    Set Variable  ${resp.json()}

    # Verify the response of plus operation
    Should Be Equal    ${json_resp['result']}    ${16}
