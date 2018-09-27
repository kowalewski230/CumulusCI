
list_metadata_start_envelope = (
    '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n  <soap:Header>\n    <SessionHeader xmlns="http://soap.sforce.com/2006/04/metadata">\n      <sessionId>###SESSION_ID###</sessionId>\n    </SessionHeader>\n  </soap:Header>\n  <soap:Body>\n    <listMetadata xmlns="http://soap.sforce.com/2006/04/metadata">\n      <queries>\n        <type>CustomObject</type>\n      </queries>\n      <asOfVersion>{api_version}</asOfVersion>\n    </listMetadata>\n  </soap:Body>\n</soap:Envelope>'
)

retrieve_packaged_start_envelope = (
    '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n  <soap:Header>\n    <SessionHeader xmlns="http://soap.sforce.com/2006/04/metadata">\n      <sessionId>###SESSION_ID###</sessionId>\n    </SessionHeader>\n  </soap:Header>\n  <soap:Body>\n    <retrieve xmlns="http://soap.sforce.com/2006/04/metadata">\n      <retrieveRequest>\n        <apiVersion>{api_version}</apiVersion>\n        <packageNames>{package_name}</packageNames>\n      </retrieveRequest>\n    </retrieve>\n  </soap:Body>\n</soap:Envelope>'
)

retrieve_unpackaged_start_envelope = (
    '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n  <soap:Header>\n    <SessionHeader xmlns="http://soap.sforce.com/2006/04/metadata">\n      <sessionId>###SESSION_ID###</sessionId>\n    </SessionHeader>\n  </soap:Header>\n  <soap:Body>\n    <retrieve xmlns="http://soap.sforce.com/2006/04/metadata">\n      <retrieveRequest>\n        <apiVersion>{api_version}</apiVersion>\n        <unpackaged>\n          <version>41.0</version> \n        </unpackaged>\n      </retrieveRequest>\n    </retrieve>\n  </soap:Body>\n</soap:Envelope>'
)


result_envelope = (
    '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n  <soap:Header>\n    <SessionHeader xmlns="http://soap.sforce.com/2006/04/metadata">\n      <sessionId>###SESSION_ID###</sessionId>\n    </SessionHeader>\n  </soap:Header>\n  <soap:Body>\n    <checkRetrieveStatus xmlns="http://soap.sforce.com/2006/04/metadata">\n      <asyncProcessId>{process_id}</asyncProcessId>\n    </checkRetrieveStatus>\n  </soap:Body>\n</soap:Envelope>'
)

deploy_result = (
    '<?xml version="1.0" encoding="utf-8"?>\n<testing>\n  <status>{status}</status>\n{extra}</testing>'
)
deploy_result_failure = (
    '<?xml version="1.0" encoding="utf-8"?>\n<result>\n  <status>Failed</status>\n  <details>\n    {details}\n  </details>\n</result>'
)

list_metadata_result = (
    '<?xml version="1.0" encoding="utf-8"?>\n<result><fullName>Test__c</fullName></result>'
)

retrieve_result = (
    '<?xml version="1.0" encoding="utf-8"?>\n<testing>\n  <zipFile>{zip}</zipFile>\n{extra}</testing>'
)

status_envelope = (
    '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n  <soap:Header>\n    <SessionHeader xmlns="http://soap.sforce.com/2006/04/metadata">\n      <sessionId>###SESSION_ID###</sessionId>\n    </SessionHeader>\n  </soap:Header>\n  <soap:Body>\n    <checkStatus xmlns="http://soap.sforce.com/2006/04/metadata">\n      <asyncProcessId>{process_id}</asyncProcessId>\n    </checkStatus>\n  </soap:Body>\n</soap:Envelope>'
)

deploy_status_envelope = (
    '<?xml version="1.0" encoding="utf-8"?>\n<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n  <soap:Header>\n    <SessionHeader xmlns="http://soap.sforce.com/2006/04/metadata">\n      <sessionId>###SESSION_ID###</sessionId>\n    </SessionHeader>\n  </soap:Header>\n  <soap:Body>\n    <checkDeployStatus xmlns="http://soap.sforce.com/2006/04/metadata">\n      <asyncProcessId>{process_id}</asyncProcessId>\n      <includeDetails>true</includeDetails>\n    </checkDeployStatus>\n  </soap:Body>\n</soap:Envelope>'
)
