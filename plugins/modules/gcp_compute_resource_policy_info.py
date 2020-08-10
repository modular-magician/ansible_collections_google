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
module: gcp_compute_resource_policy_info
description:
- Gather info for GCP ResourcePolicy
short_description: Gather info for GCP ResourcePolicy
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  filters:
    description:
    - A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters).
    - Each additional filter in the list will act be added as an AND condition (filter1
      and filter2) .
    type: list
    elements: str
  region:
    description:
    - Region where resource policy resides.
    required: true
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
notes:
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
- name: get info on a resource policy
  gcp_compute_resource_policy_info:
    region: us-central1
    filters:
    - name = test_object
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    name:
      description:
      - The name of the resource, provided by the client when initially creating the
        resource. The resource name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match the
        regular expression `[a-z]([-a-z0-9]*[a-z0-9])`? which means the first character
        must be a lowercase letter, and all following characters must be a dash, lowercase
        letter, or digit, except the last character, which cannot be a dash.
      returned: success
      type: str
    snapshotSchedulePolicy:
      description:
      - Policy for creating snapshots of persistent disks.
      returned: success
      type: complex
      contains:
        schedule:
          description:
          - Contains one of an `hourlySchedule`, `dailySchedule`, or `weeklySchedule`.
          returned: success
          type: complex
          contains:
            hourlySchedule:
              description:
              - The policy will execute every nth hour starting at the specified time.
              returned: success
              type: complex
              contains:
                hoursInCycle:
                  description:
                  - The number of hours between snapshots.
                  returned: success
                  type: int
                startTime:
                  description:
                  - Time within the window to start the operations.
                  - 'It must be in an hourly format "HH:MM", where HH : [00-23] and
                    MM : [00] GMT.'
                  - 'eg: 21:00 .'
                  returned: success
                  type: str
            dailySchedule:
              description:
              - The policy will execute every nth day at the specified time.
              returned: success
              type: complex
              contains:
                daysInCycle:
                  description:
                  - The number of days between snapshots.
                  returned: success
                  type: int
                startTime:
                  description:
                  - This must be in UTC format that resolves to one of 00:00, 04:00,
                    08:00, 12:00, 16:00, or 20:00. For example, both 13:00-5 and 08:00
                    are valid.
                  returned: success
                  type: str
            weeklySchedule:
              description:
              - Allows specifying a snapshot time for each day of the week.
              returned: success
              type: complex
              contains:
                dayOfWeeks:
                  description:
                  - May contain up to seven (one for each day of the week) snapshot
                    times.
                  returned: success
                  type: complex
                  contains:
                    startTime:
                      description:
                      - Time within the window to start the operations.
                      - 'It must be in format "HH:MM", where HH : [00-23] and MM :
                        [00-00] GMT.'
                      returned: success
                      type: str
                    day:
                      description:
                      - The day of the week to create the snapshot. e.g. MONDAY .
                      returned: success
                      type: str
        retentionPolicy:
          description:
          - Retention policy applied to snapshots created by this resource policy.
          returned: success
          type: complex
          contains:
            maxRetentionDays:
              description:
              - Maximum age of the snapshot that is allowed to be kept.
              returned: success
              type: int
            onSourceDiskDelete:
              description:
              - Specifies the behavior to apply to scheduled snapshots when the source
                disk is deleted.
              returned: success
              type: str
        snapshotProperties:
          description:
          - Properties with which the snapshots are created, such as labels.
          returned: success
          type: complex
          contains:
            labels:
              description:
              - A set of key-value pairs.
              returned: success
              type: dict
            storageLocations:
              description:
              - Cloud Storage bucket location to store the auto snapshot (regional
                or multi-regional) .
              returned: success
              type: list
            guestFlush:
              description:
              - Whether to perform a 'guest aware' snapshot.
              returned: success
              type: bool
    groupPlacementPolicy:
      description:
      - Policy for creating snapshots of persistent disks.
      returned: success
      type: complex
      contains:
        vmCount:
          description:
          - Number of vms in this placement group.
          returned: success
          type: int
        availabilityDomainCount:
          description:
          - The number of availability domains instances will be spread across. If
            two instances are in different availability domain, they will not be put
            in the same low latency network .
          returned: success
          type: int
        collocation:
          description:
          - Collocation specifies whether to place VMs inside the same availability
            domain on the same low-latency network.
          - Specify `COLLOCATED` to enable collocation. Can only be specified with
            `vm_count`. If compute instances are created with a COLLOCATED policy,
            then exactly `vm_count` instances must be created at the same time with
            the resource policy attached.
          returned: success
          type: str
    region:
      description:
      - Region where resource policy resides.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################
from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str'), region=dict(required=True, type='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/resourcePolicies".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    return auth.list(link, return_if_object, array_name='items', params={'filter': query})


def query_options(filters):
    if not filters:
        return ''

    if len(filters) == 1:
        return filters[0]
    else:
        queries = []
        for f in filters:
            # For multiple queries, all queries should have ()
            if f[0] != '(' and f[-1] != ')':
                queries.append("(%s)" % ''.join(f))
            else:
                queries.append(f)

        return ' '.join(queries)


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
