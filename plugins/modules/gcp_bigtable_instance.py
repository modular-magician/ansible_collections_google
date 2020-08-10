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
module: gcp_bigtable_instance
description:
- A collection of Bigtable Tables and the resources that serve them. All tables in
  an instance are served from all Clusters in the instance.
short_description: Creates a GCP Instance
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
    - The unique name of the instance.
    required: false
    type: str
  display_name:
    description:
    - The descriptive name for this instance as it appears in UIs.
    - Can be changed at any time, but should be kept globally unique to avoid confusion.
    required: false
    type: str
  type:
    description:
    - The type of the instance. Defaults to `PRODUCTION`.
    - 'Some valid choices include: "TYPE_UNSPECIFIED", "PRODUCTION", "DEVELOPMENT"'
    required: false
    type: str
  labels:
    description:
    - Labels are a flexible and lightweight mechanism for organizing cloud resources
      into groups that reflect a customer's organizational needs and deployment strategies.
      They can be used to filter resources and aggregate metrics.
    required: false
    type: dict
  clusters:
    description:
    - An array of clusters. Maximum 4.
    elements: dict
    required: false
    type: list
    suboptions:
      name:
        description:
        - The unique name of the cluster.
        required: false
        type: str
      serve_nodes:
        description:
        - The number of nodes allocated to this cluster. More nodes enable higher
          throughput and more consistent performance.
        required: false
        type: int
      default_storage_type:
        description:
        - The type of storage used by this cluster to serve its parent instance's
          tables, unless explicitly overridden.
        - 'Some valid choices include: "STORAGE_TYPE_UNSPECIFIED", "SSD", "HDD"'
        required: false
        type: str
      location:
        description:
        - The location where this cluster's nodes and storage reside. For best performance,
          clients should be located as close as possible to this cluster. Currently
          only zones are supported, so values should be of the form `projects/<project>/locations/<zone>`.
        required: false
        type: str
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
'''

EXAMPLES = '''
- name: create a instance
  google.cloud.gcp_bigtable_instance:
    name: my-instance
    display_name: My Test Cluster
    clusters:
    - name: mycluster
      location: projects/test_project/locations/us-central1-a
      serve_nodes: 1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
state:
  description:
  - The current state of the instance.
  returned: success
  type: str
name:
  description:
  - The unique name of the instance.
  returned: success
  type: str
displayName:
  description:
  - The descriptive name for this instance as it appears in UIs.
  - Can be changed at any time, but should be kept globally unique to avoid confusion.
  returned: success
  type: str
type:
  description:
  - The type of the instance. Defaults to `PRODUCTION`.
  returned: success
  type: str
labels:
  description:
  - Labels are a flexible and lightweight mechanism for organizing cloud resources
    into groups that reflect a customer's organizational needs and deployment strategies.
    They can be used to filter resources and aggregate metrics.
  returned: success
  type: dict
clusters:
  description:
  - An array of clusters. Maximum 4.
  returned: success
  type: complex
  contains:
    name:
      description:
      - The unique name of the cluster.
      returned: success
      type: str
    serveNodes:
      description:
      - The number of nodes allocated to this cluster. More nodes enable higher throughput
        and more consistent performance.
      returned: success
      type: int
    defaultStorageType:
      description:
      - The type of storage used by this cluster to serve its parent instance's tables,
        unless explicitly overridden.
      returned: success
      type: str
    location:
      description:
      - The location where this cluster's nodes and storage reside. For best performance,
        clients should be located as close as possible to this cluster. Currently
        only zones are supported, so values should be of the form `projects/<project>/locations/<zone>`.
      returned: success
      type: str
    state:
      description:
      - The current state of the cluster.
      returned: success
      type: str
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
            name=dict(type='str'),
            display_name=dict(type='str'),
            type=dict(type='str'),
            labels=dict(type='dict'),
            clusters=dict(
                type='list',
                elements='dict',
                options=dict(name=dict(type='str'), serve_nodes=dict(type='int'), default_storage_type=dict(type='str'), location=dict(type='str')),
            ),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/bigtable']

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
    auth = GcpSession(module, 'bigtable')
    return wait_for_operation(module, auth.post(link, resource_to_create(module)))


def update(module, link):
    auth = GcpSession(module, 'bigtable')
    return return_if_object(module, auth.put(link, resource_to_request(module)))


def delete(module, link):
    auth = GcpSession(module, 'bigtable')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': module.params.get('name'),
        u'displayName': module.params.get('display_name'),
        u'type': module.params.get('type'),
        u'labels': module.params.get('labels'),
        u'clusters': InstanceClustersArray(module.params.get('clusters', []), module).to_request(),
    }
    request = encode_request(request, module)
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'bigtable')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://bigtableadmin.googleapis.com/v2/projects/{project}/instances/{name}".format(**module.params)


def collection(module):
    return "https://bigtableadmin.googleapis.com/v2/projects/{project}/instances".format(**module.params)


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
        u'state': response.get(u'state'),
        u'name': response.get(u'name'),
        u'displayName': response.get(u'displayName'),
        u'type': response.get(u'type'),
        u'labels': response.get(u'labels'),
        u'clusters': InstanceClustersArray(response.get(u'clusters', []), module).from_response(),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://bigtableadmin.googleapis.com/v2/operations/{module.params['clusters'][0]['location']}/{op_id}"
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
    op_uri = bigtable_async_url(module, {'op_id': op_id})
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


def resource_to_create(module):
    instance = resource_to_request(module)
    if 'name' in instance:
        del instance['name']

    clusters = []
    if 'clusters' in instance:
        clusters = instance['clusters']
        del instance['clusters']

    return {'instanceId': module.params['name'].split('/')[-1], 'instance': instance, 'clusters': clusters}


def encode_request(request, module):
    if 'name' in request:
        del request['name']

    if 'clusters' in request:
        request['clusters'] = convert_clusters_to_map(request['clusters'])
    return request


def decode_response(response, module):
    if 'name' in response:
        response['name'] = response['name'].split('/')[-1]

    if 'clusters' in response:
        response['clusters'] = convert_map_to_clusters(response['clusters'])
    return response


def convert_clusters_to_map(clusters):
    cmap = {}
    for cluster in clusters:
        cmap[cluster['name']] = cluster
        del cmap[cluster['name']]['name']
    return cmap


def convert_map_to_clusters(clusters):
    carray = []
    for key, cluster in clusters.items():
        cluster['name'] = key.split('/')[-1]
        carray.append(cluster)
    return carray


def bigtable_async_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    location_name = module.params['clusters'][0]['location'].split('/')[-1]

    url = 'https://bigtableadmin.googleapis.com/v2/operations/projects/%s' '/instances/%s/locations/%s/operations/{op_id}' % (
        module.params['project'],
        module.params['name'],
        location_name,
    )

    return url.format(**extra_data)


class InstanceClustersArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict(
            {
                u'name': item.get('name'),
                u'serveNodes': item.get('serve_nodes'),
                u'defaultStorageType': item.get('default_storage_type'),
                u'location': item.get('location'),
            }
        )

    def _response_from_item(self, item):
        return remove_nones_from_dict(
            {
                u'name': item.get(u'name'),
                u'serveNodes': item.get(u'serveNodes'),
                u'defaultStorageType': item.get(u'defaultStorageType'),
                u'location': item.get(u'location'),
            }
        )


if __name__ == '__main__':
    main()
