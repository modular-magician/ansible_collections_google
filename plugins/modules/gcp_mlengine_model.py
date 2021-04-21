#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_mlengine_model
description:
- Represents a machine learning solution.
- A model can have multiple versions, each of which is a deployed, trained model ready
  to receive prediction requests. The model itself is just a container.
short_description: Creates a GCP Model
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  name:
    description:
    - The name specified for the model.
    required: true
    type: str
  description:
    description:
    - The description specified for the model when it was created.
    required: false
    type: str
  default_version:
    description:
    - The default version of the model. This version will be used to handle prediction
      requests that do not specify a version.
    required: false
    type: dict
    suboptions:
      name:
        description:
        - The name specified for the version when it was created.
        required: true
        type: str
  regions:
    description:
    - The list of regions where the model is going to be deployed.
    - Currently only one region per model is supported .
    elements: str
    required: false
    type: list
  online_prediction_logging:
    description:
    - If true, online prediction access logs are sent to StackDriver Logging.
    required: false
    type: bool
  online_prediction_console_logging:
    description:
    - If true, online prediction nodes send stderr and stdout streams to Stackdriver
      Logging.
    required: false
    type: bool
  labels:
    description:
    - One or more labels that you can add, to organize your models.
    required: false
    type: dict
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/ai-platform/prediction/docs/reference/rest/v1/projects.models)'
- 'Official Documentation: U(https://cloud.google.com/ai-platform/prediction/docs/deploying-models)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a model
  google.cloud.gcp_mlengine_model:
    name: "{{ resource_name | replace('-', '_') }}"
    description: My model
    regions:
    - us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - The name specified for the model.
  returned: success
  type: str
description:
  description:
  - The description specified for the model when it was created.
  returned: success
  type: str
defaultVersion:
  description:
  - The default version of the model. This version will be used to handle prediction
    requests that do not specify a version.
  returned: success
  type: complex
  contains:
    name:
      description:
      - The name specified for the version when it was created.
      returned: success
      type: str
regions:
  description:
  - The list of regions where the model is going to be deployed.
  - Currently only one region per model is supported .
  returned: success
  type: list
onlinePredictionLogging:
  description:
  - If true, online prediction access logs are sent to StackDriver Logging.
  returned: success
  type: bool
onlinePredictionConsoleLogging:
  description:
  - If true, online prediction nodes send stderr and stdout streams to Stackdriver
    Logging.
  returned: success
  type: bool
labels:
  description:
  - One or more labels that you can add, to organize your models.
  returned: success
  type: dict
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import (
    navigate_hash,
    GcpSession,
    GcpModule,
    GcpRequest,
    remove_nones_from_dict,
    replace_resource_dict,
)
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            description=dict(type='str'),
            default_version=dict(type='dict', options=dict(name=dict(required=True, type='str'))),
            regions=dict(type='list', elements='str'),
            online_prediction_logging=dict(type='bool'),
            online_prediction_console_logging=dict(type='bool'),
            labels=dict(type='dict'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'mlengine')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    delete(module, self_link(module))
    create(module, collection(module))


def delete(module, link):
    auth = GcpSession(module, 'mlengine')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'defaultVersion': ModelDefaultversion(module.params.get('default_version', {}), module).to_request(),
        u'regions': module.params.get('regions'),
        u'onlinePredictionLogging': module.params.get('online_prediction_logging'),
        u'onlinePredictionConsoleLogging': module.params.get('online_prediction_console_logging'),
        u'labels': module.params.get('labels'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'mlengine')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://ml.googleapis.com/v1/projects/{project}/models/{name}".format(**module.params)


def collection(module):
    return "https://ml.googleapis.com/v1/projects/{project}/models".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    result = decode_response(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)
    request = decode_response(request, module)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'name': response.get(u'name'),
        u'description': response.get(u'description'),
        u'defaultVersion': ModelDefaultversion(response.get(u'defaultVersion', {}), module).from_response(),
        u'regions': response.get(u'regions'),
        u'onlinePredictionLogging': response.get(u'onlinePredictionLogging'),
        u'onlinePredictionConsoleLogging': response.get(u'onlinePredictionConsoleLogging'),
        u'labels': response.get(u'labels'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://ml.googleapis.com/v1/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response)
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['done'])
    wait_done = wait_for_completion(status, op_result, module)
    raise_if_errors(wait_done, ['error'], module)
    return navigate_hash(wait_done, ['response'])


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while not status:
        raise_if_errors(op_result, ['error'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, False)
        status = navigate_hash(op_result, ['done'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


# Short names are given (and expected) by the API
# but are returned as full names.
def decode_response(response, module):
    if 'name' in response and 'metadata' not in response:
        response['name'] = response['name'].split('/')[-1]
    return response


class ModelDefaultversion(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'name': self.request.get('name')})

    def from_response(self):
        return remove_nones_from_dict({u'name': self.request.get(u'name')})


if __name__ == '__main__':
    main()
