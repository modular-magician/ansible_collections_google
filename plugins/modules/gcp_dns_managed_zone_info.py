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
module: gcp_dns_managed_zone_info
description:
- Gather info for GCP ManagedZone
short_description: Gather info for GCP ManagedZone
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  dns_name:
    description:
    - Restricts the list to return only zones with this domain name.
    type: list
    elements: str
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
- name: get info on a managed zone
  gcp_dns_managed_zone_info:
    dns_name: test.somewild2.example.com.
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
    description:
      description:
      - A mutable string of at most 1024 characters associated with this resource
        for the user's convenience. Has no effect on the managed zone's function.
      returned: success
      type: str
    dnsName:
      description:
      - The DNS name of this managed zone, for instance "example.com.".
      returned: success
      type: str
    dnssecConfig:
      description:
      - DNSSEC configuration.
      returned: success
      type: complex
      contains:
        kind:
          description:
          - Identifies what kind of resource this is.
          returned: success
          type: str
        nonExistence:
          description:
          - Specifies the mechanism used to provide authenticated denial-of-existence
            responses.
          - non_existence can only be updated when the state is `off`.
          returned: success
          type: str
        state:
          description:
          - Specifies whether DNSSEC is enabled, and what mode it is in.
          returned: success
          type: str
        defaultKeySpecs:
          description:
          - Specifies parameters that will be used for generating initial DnsKeys
            for this ManagedZone. If you provide a spec for keySigning or zoneSigning,
            you must also provide one for the other.
          - default_key_specs can only be updated when the state is `off`.
          returned: success
          type: complex
          contains:
            algorithm:
              description:
              - String mnemonic specifying the DNSSEC algorithm of this key.
              returned: success
              type: str
            keyLength:
              description:
              - Length of the keys in bits.
              returned: success
              type: int
            keyType:
              description:
              - Specifies whether this is a key signing key (KSK) or a zone signing
                key (ZSK). Key signing keys have the Secure Entry Point flag set and,
                when active, will only be used to sign resource record sets of type
                DNSKEY. Zone signing keys do not have the Secure Entry Point flag
                set and will be used to sign all other types of resource record sets.
              returned: success
              type: str
            kind:
              description:
              - Identifies what kind of resource this is.
              returned: success
              type: str
    id:
      description:
      - Unique identifier for the resource; defined by the server.
      returned: success
      type: int
    name:
      description:
      - User assigned name for this resource.
      - Must be unique within the project.
      returned: success
      type: str
    nameServers:
      description:
      - Delegate your managed_zone to these virtual name servers; defined by the server
        .
      returned: success
      type: list
    nameServerSet:
      description:
      - Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet
        is a set of DNS name servers that all host the same ManagedZones. Most users
        will leave this field unset.
      returned: success
      type: str
    creationTime:
      description:
      - The time that this resource was created on the server.
      - This is in RFC3339 text format.
      returned: success
      type: str
    labels:
      description:
      - A set of key/value label pairs to assign to this ManagedZone.
      returned: success
      type: dict
    visibility:
      description:
      - 'The zone''s visibility: public zones are exposed to the Internet, while private
        zones are visible only to Virtual Private Cloud resources.'
      returned: success
      type: str
    privateVisibilityConfig:
      description:
      - For privately visible zones, the set of Virtual Private Cloud resources that
        the zone is visible from.
      returned: success
      type: complex
      contains:
        networks:
          description:
          - The list of VPC networks that can see this zone.
          returned: success
          type: complex
          contains:
            networkUrl:
              description:
              - The fully qualified URL of the VPC network to bind to.
              - This should be formatted like `U(https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`)
                .
              returned: success
              type: str
    forwardingConfig:
      description:
      - The presence for this field indicates that outbound forwarding is enabled
        for this zone. The value of this field contains the set of destinations to
        forward to.
      returned: success
      type: complex
      contains:
        targetNameServers:
          description:
          - List of target name servers to forward to. Cloud DNS will select the best
            available name server if more than one target is given.
          returned: success
          type: complex
          contains:
            ipv4Address:
              description:
              - IPv4 address of a target name server.
              returned: success
              type: str
            forwardingPath:
              description:
              - Forwarding path for this TargetNameServer. If unset or `default` Cloud
                DNS will make forwarding decision based on address ranges, i.e. RFC1918
                addresses go to the VPC, Non-RFC1918 addresses go to the Internet.
                When set to `private`, Cloud DNS will always send queries through
                VPC for this target .
              returned: success
              type: str
    peeringConfig:
      description:
      - The presence of this field indicates that DNS Peering is enabled for this
        zone. The value of this field contains the network to peer with.
      returned: success
      type: complex
      contains:
        targetNetwork:
          description:
          - The network with which to peer.
          returned: success
          type: complex
          contains:
            networkUrl:
              description:
              - The fully qualified URL of the VPC network to forward queries to.
              - This should be formatted like `U(https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`)
                .
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
    module = GcpModule(argument_spec=dict(dns_name=dict(type='list', elements='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/ndev.clouddns.readwrite']

    return_value = {'resources': fetch_list(module, collection(module), module.params['dns_name'])}
    module.exit_json(**return_value)


def collection(module):
    return "https://dns.googleapis.com/dns/v1/projects/{project}/managedZones".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'dns')
    return auth.list(link, return_if_object, array_name='managedZones', params={'dnsName': query})


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
