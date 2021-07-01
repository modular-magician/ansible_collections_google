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
module: gcp_cloudtasks_queue_info
description:
- Gather info for GCP Queue
short_description: Gather info for GCP Queue
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  location:
    description:
    - The location of the queue.
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
- for authentication, you can set service_account_file using the C(GCP_SERVICE_ACCOUNT_FILE)
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
- name: get info on a queue
  gcp_cloudtasks_queue_info:
    location: us-central1
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
      - The queue name.
      returned: success
      type: str
    appEngineRoutingOverride:
      description:
      - Overrides for task-level appEngineRouting. These settings apply only to App
        Engine tasks in this queue .
      returned: success
      type: complex
      contains:
        service:
          description:
          - App service.
          - By default, the task is sent to the service which is the default service
            when the task is attempted.
          returned: success
          type: str
        version:
          description:
          - App version.
          - By default, the task is sent to the version which is the default version
            when the task is attempted.
          returned: success
          type: str
        instance:
          description:
          - App instance.
          - By default, the task is sent to an instance which is available when the
            task is attempted.
          returned: success
          type: str
        host:
          description:
          - The host that the task is sent to.
          returned: success
          type: str
    rateLimits:
      description:
      - Rate limits for task dispatches.
      - 'The queue''s actual dispatch rate is the result of: * Number of tasks in
        the queue * User-specified throttling: rateLimits, retryConfig, and the queue''s
        state.'
      - "* System throttling due to 429 (Too Many Requests) or 503 (Service Unavailable)
        responses from the worker, high error rates, or to smooth sudden large traffic
        spikes."
      returned: success
      type: complex
      contains:
        maxDispatchesPerSecond:
          description:
          - The maximum rate at which tasks are dispatched from this queue.
          - If unspecified when the queue is created, Cloud Tasks will pick the default.
          returned: success
          type: str
        maxConcurrentDispatches:
          description:
          - The maximum number of concurrent tasks that Cloud Tasks allows to be dispatched
            for this queue. After this threshold has been reached, Cloud Tasks stops
            dispatching tasks until the number of concurrent requests decreases.
          returned: success
          type: int
        maxBurstSize:
          description:
          - The max burst size.
          - Max burst size limits how fast tasks in queue are processed when many
            tasks are in the queue and the rate is high. This field allows the queue
            to have a high rate so processing starts shortly after a task is enqueued,
            but still limits resource usage when many tasks are enqueued in a short
            period of time.
          returned: success
          type: int
    retryConfig:
      description:
      - Settings that determine the retry behavior.
      returned: success
      type: complex
      contains:
        maxAttempts:
          description:
          - Number of attempts per task.
          - Cloud Tasks will attempt the task maxAttempts times (that is, if the first
            attempt fails, then there will be maxAttempts - 1 retries). Must be >=
            -1.
          - If unspecified when the queue is created, Cloud Tasks will pick the default.
          - "-1 indicates unlimited attempts."
          returned: success
          type: int
        maxRetryDuration:
          description:
          - If positive, maxRetryDuration specifies the time limit for retrying a
            failed task, measured from when the task was first attempted. Once maxRetryDuration
            time has passed and the task has been attempted maxAttempts times, no
            further attempts will be made and the task will be deleted.
          - If zero, then the task age is unlimited.
          returned: success
          type: str
        minBackoff:
          description:
          - A task will be scheduled for retry between minBackoff and maxBackoff duration
            after it fails, if the queue's RetryConfig specifies that the task should
            be retried.
          returned: success
          type: str
        maxBackoff:
          description:
          - A task will be scheduled for retry between minBackoff and maxBackoff duration
            after it fails, if the queue's RetryConfig specifies that the task should
            be retried.
          returned: success
          type: str
        maxDoublings:
          description:
          - The time between retries will double maxDoublings times.
          - A task's retry interval starts at minBackoff, then doubles maxDoublings
            times, then increases linearly, and finally retries retries at intervals
            of maxBackoff up to maxAttempts times.
          returned: success
          type: int
        purgeTime:
          description:
          - The last time this queue was purged.
          returned: success
          type: str
    stackdriverLoggingConfig:
      description:
      - Configuration options for writing logs to Stackdriver Logging.
      returned: success
      type: complex
      contains:
        samplingRatio:
          description:
          - Specifies the fraction of operations to write to Stackdriver Logging.
          - This field may contain any value between 0.0 and 1.0, inclusive. 0.0 is
            the default and means that no operations are logged.
          returned: success
          type: str
    status:
      description:
      - The current state of the queue.
      returned: success
      type: str
    location:
      description:
      - The location of the queue.
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
    module = GcpModule(argument_spec=dict(location=dict(required=True, type='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    return_value = {'resources': fetch_list(module, collection(module))}
    module.exit_json(**return_value)


def collection(module):
    return "https://cloudtasks.googleapis.com/v2/projects/{project}/locations/{location}/queues".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'cloudtasks')
    return auth.list(link, return_if_object, array_name='queues')


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
