#!/bin/bash  
cci task run snowfakery --recipe OrgDataInit/lead.yml  --run-until-recipe-repeated 1 --org myTestSandbox --debug
# cci task run snowfakery --recipe OrgDataInit/account.yml 
cci task run snowfakery --recipe OrgDataInit/account.yml  --run-until-recipe-repeated 1  --org myTestSandbox --debug 

# Extrat All data
cci task run capture_sample_data --org myTestSandbox

# Delete All data 
cci task run delete_data -o objects Opportunity,Contact,Account,Lead,Product2,ContentDocument,Task --org myTestSandbox
# Load All data
cci task run load_sample_data --org myTestSandbox


