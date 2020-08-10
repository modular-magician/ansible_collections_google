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
module: gcp_compute_instance_template_info
description:
- Gather info for GCP InstanceTemplate
short_description: Gather info for GCP InstanceTemplate
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
- name: get info on an instance template
  gcp_compute_instance_template_info:
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
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    description:
      description:
      - An optional description of this resource. Provide this property when you create
        the resource.
      returned: success
      type: str
    id:
      description:
      - The unique identifier for the resource. This identifier is defined by the
        server.
      returned: success
      type: int
    name:
      description:
      - Name of the resource. The name is 1-63 characters long and complies with RFC1035.
      returned: success
      type: str
    properties:
      description:
      - The instance properties for this instance template.
      returned: success
      type: complex
      contains:
        canIpForward:
          description:
          - Enables instances created based on this template to send packets with
            source IP addresses other than their own and receive packets with destination
            IP addresses other than their own. If these instances will be used as
            an IP gateway or it will be set as the next-hop in a Route resource, specify
            true. If unsure, leave this set to false.
          returned: success
          type: bool
        description:
          description:
          - An optional text description for the instances that are created from this
            instance template.
          returned: success
          type: str
        disks:
          description:
          - An array of disks that are associated with the instances that are created
            from this template.
          returned: success
          type: complex
          contains:
            licenses:
              description:
              - Any applicable license URI.
              returned: success
              type: list
            autoDelete:
              description:
              - Specifies whether the disk will be auto-deleted when the instance
                is deleted (but not when the disk is detached from the instance).
              - 'Tip: Disks should be set to autoDelete=true so that leftover disks
                are not left behind on machine deletion.'
              returned: success
              type: bool
            boot:
              description:
              - Indicates that this is a boot disk. The virtual machine will use the
                first partition of the disk for its root filesystem.
              returned: success
              type: bool
            deviceName:
              description:
              - Specifies a unique device name of your choice that is reflected into
                the /dev/disk/by-id/google-* tree of a Linux operating system running
                within the instance. This name can be used to reference the device
                for mounting, resizing, and so on, from within the instance.
              returned: success
              type: str
            diskEncryptionKey:
              description:
              - Encrypts or decrypts a disk using a customer-supplied encryption key.
              returned: success
              type: complex
              contains:
                rawKey:
                  description:
                  - Specifies a 256-bit customer-supplied encryption key, encoded
                    in RFC 4648 base64 to either encrypt or decrypt this resource.
                  returned: success
                  type: str
                rsaEncryptedKey:
                  description:
                  - Specifies an RFC 4648 base64 encoded, RSA-wrapped 2048-bit customer-supplied
                    encryption key to either encrypt or decrypt this resource.
                  returned: success
                  type: str
                sha256:
                  description:
                  - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied
                    encryption key that protects this resource.
                  returned: success
                  type: str
            index:
              description:
              - Assigns a zero-based index to this disk, where 0 is reserved for the
                boot disk. For example, if you have many disks attached to an instance,
                each disk would have a unique index number. If not specified, the
                server will choose an appropriate value.
              returned: success
              type: int
            initializeParams:
              description:
              - Specifies the parameters for a new disk that will be created alongside
                the new instance. Use initialization parameters to create boot disks
                or local SSDs attached to the new instance.
              returned: success
              type: complex
              contains:
                diskName:
                  description:
                  - Specifies the disk name. If not specified, the default is to use
                    the name of the instance.
                  returned: success
                  type: str
                diskSizeGb:
                  description:
                  - Specifies the size of the disk in base-2 GB.
                  returned: success
                  type: int
                diskType:
                  description:
                  - Reference to a disk type.
                  - Specifies the disk type to use to create the instance.
                  - If not specified, the default is pd-standard.
                  returned: success
                  type: str
                sourceImage:
                  description:
                  - The source image to create this disk. When creating a new instance,
                    one of initializeParams.sourceImage or disks.source is required.
                    To create a disk with one of the public operating system images,
                    specify the image by its family name.
                  returned: success
                  type: str
                sourceImageEncryptionKey:
                  description:
                  - The customer-supplied encryption key of the source image. Required
                    if the source image is protected by a customer-supplied encryption
                    key.
                  - Instance templates do not store customer-supplied encryption keys,
                    so you cannot create disks for instances in a managed instance
                    group if the source images are encrypted with your own keys.
                  returned: success
                  type: complex
                  contains:
                    rawKey:
                      description:
                      - Specifies a 256-bit customer-supplied encryption key, encoded
                        in RFC 4648 base64 to either encrypt or decrypt this resource.
                      returned: success
                      type: str
                    sha256:
                      description:
                      - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied
                        encryption key that protects this resource.
                      returned: success
                      type: str
            interface:
              description:
              - Specifies the disk interface to use for attaching this disk, which
                is either SCSI or NVME. The default is SCSI.
              - Persistent disks must always use SCSI and the request will fail if
                you attempt to attach a persistent disk in any other format than SCSI.
              returned: success
              type: str
            mode:
              description:
              - The mode in which to attach this disk, either READ_WRITE or READ_ONLY.
                If not specified, the default is to attach the disk in READ_WRITE
                mode.
              returned: success
              type: str
            source:
              description:
              - Reference to a disk. When creating a new instance, one of initializeParams.sourceImage
                or disks.source is required.
              - If desired, you can also attach existing non-root persistent disks
                using this property. This field is only applicable for persistent
                disks.
              - Note that for InstanceTemplate, specify the disk name, not the URL
                for the disk.
              returned: success
              type: dict
            type:
              description:
              - Specifies the type of the disk, either SCRATCH or PERSISTENT. If not
                specified, the default is PERSISTENT.
              returned: success
              type: str
        labels:
          description:
          - Labels to apply to this address. A list of key->value pairs.
          returned: success
          type: dict
        machineType:
          description:
          - The machine type to use in the VM instance template.
          returned: success
          type: str
        minCpuPlatform:
          description:
          - Specifies a minimum CPU platform for the VM instance. Applicable values
            are the friendly names of CPU platforms .
          returned: success
          type: str
        metadata:
          description:
          - The metadata key/value pairs to assign to instances that are created from
            this template. These pairs can consist of custom metadata or predefined
            keys.
          returned: success
          type: dict
        guestAccelerators:
          description:
          - List of the type and count of accelerator cards attached to the instance
            .
          returned: success
          type: complex
          contains:
            acceleratorCount:
              description:
              - The number of the guest accelerator cards exposed to this instance.
              returned: success
              type: int
            acceleratorType:
              description:
              - Full or partial URL of the accelerator type resource to expose to
                this instance.
              returned: success
              type: str
        networkInterfaces:
          description:
          - An array of configurations for this interface. This specifies how this
            interface is configured to interact with other network services, such
            as connecting to the internet. Only one network interface is supported
            per instance.
          returned: success
          type: complex
          contains:
            accessConfigs:
              description:
              - An array of configurations for this interface. Currently, only one
                access config, ONE_TO_ONE_NAT, is supported. If there are no accessConfigs
                specified, then this instance will have no external internet access.
              returned: success
              type: complex
              contains:
                name:
                  description:
                  - The name of this access configuration. The default and recommended
                    name is External NAT but you can use any arbitrary string you
                    would like. For example, My external IP or Network Access.
                  returned: success
                  type: str
                natIP:
                  description:
                  - Reference to an address.
                  - An external IP address associated with this instance.
                  - Specify an unused static external IP address available to the
                    project or leave this field undefined to use an IP from a shared
                    ephemeral IP address pool. If you specify a static external IP
                    address, it must live in the same region as the zone of the instance.
                  returned: success
                  type: dict
                type:
                  description:
                  - The type of configuration. The default and only option is ONE_TO_ONE_NAT.
                  returned: success
                  type: str
                setPublicPtr:
                  description:
                  - Specifies whether a public DNS PTR record should be created to
                    map the external IP address of the instance to a DNS domain name.
                  returned: success
                  type: bool
                publicPtrDomainName:
                  description:
                  - The DNS domain name for the public PTR record. You can set this
                    field only if the setPublicPtr field is enabled.
                  returned: success
                  type: str
                networkTier:
                  description:
                  - This signifies the networking tier used for configuring this access
                    configuration. If an AccessConfig is specified without a valid
                    external IP address, an ephemeral IP will be created with this
                    networkTier. If an AccessConfig with a valid external IP address
                    is specified, it must match that of the networkTier associated
                    with the Address resource owning that IP.
                  returned: success
                  type: str
            aliasIpRanges:
              description:
              - An array of alias IP ranges for this network interface. Can only be
                specified for network interfaces on subnet-mode networks.
              returned: success
              type: complex
              contains:
                ipCidrRange:
                  description:
                  - The IP CIDR range represented by this alias IP range.
                  - This IP CIDR range must belong to the specified subnetwork and
                    cannot contain IP addresses reserved by system or used by other
                    network interfaces. This range may be a single IP address (e.g.
                    10.2.3.4), a netmask (e.g. /24) or a CIDR format string (e.g.
                    10.1.2.0/24).
                  returned: success
                  type: str
                subnetworkRangeName:
                  description:
                  - Optional subnetwork secondary range name specifying the secondary
                    range from which to allocate the IP CIDR range for this alias
                    IP range. If left unspecified, the primary range of the subnetwork
                    will be used.
                  returned: success
                  type: str
            name:
              description:
              - The name of the network interface, generated by the server. For network
                devices, these are eth0, eth1, etc .
              returned: success
              type: str
            network:
              description:
              - Specifies the title of an existing network. When creating an instance,
                if neither the network nor the subnetwork is specified, the default
                network global/networks/default is used; if the network is not specified
                but the subnetwork is specified, the network is inferred.
              returned: success
              type: dict
            networkIP:
              description:
              - An IPv4 internal network address to assign to the instance for this
                network interface. If not specified by the user, an unused internal
                IP is assigned by the system.
              returned: success
              type: str
            subnetwork:
              description:
              - Reference to a VPC network.
              - If the network resource is in legacy mode, do not provide this property.
                If the network is in auto subnet mode, providing the subnetwork is
                optional. If the network is in custom subnet mode, then this field
                should be specified.
              returned: success
              type: dict
        scheduling:
          description:
          - Sets the scheduling options for this instance.
          returned: success
          type: complex
          contains:
            automaticRestart:
              description:
              - Specifies whether the instance should be automatically restarted if
                it is terminated by Compute Engine (not terminated by a user).
              - You can only set the automatic restart option for standard instances.
                Preemptible instances cannot be automatically restarted.
              returned: success
              type: bool
            onHostMaintenance:
              description:
              - Defines the maintenance behavior for this instance. For standard instances,
                the default behavior is MIGRATE. For preemptible instances, the default
                and only possible behavior is TERMINATE.
              - For more information, see Setting Instance Scheduling Options.
              returned: success
              type: str
            preemptible:
              description:
              - Defines whether the instance is preemptible. This can only be set
                during instance creation, it cannot be set or changed after the instance
                has been created.
              returned: success
              type: bool
        serviceAccounts:
          description:
          - A list of service accounts, with their specified scopes, authorized for
            this instance. Only one service account per VM instance is supported.
          returned: success
          type: complex
          contains:
            email:
              description:
              - Email address of the service account.
              returned: success
              type: str
            scopes:
              description:
              - The list of scopes to be made available for this service account.
              returned: success
              type: list
        tags:
          description:
          - A list of tags to apply to this instance. Tags are used to identify valid
            sources or targets for network firewalls and are specified by the client
            during instance creation. The tags can be later modified by the setTags
            method. Each tag within the list must comply with RFC1035.
          returned: success
          type: complex
          contains:
            fingerprint:
              description:
              - Specifies a fingerprint for this request, which is essentially a hash
                of the metadata's contents and used for optimistic locking.
              - The fingerprint is initially generated by Compute Engine and changes
                after every request to modify or update metadata. You must always
                provide an up-to-date fingerprint hash in order to update or change
                metadata.
              returned: success
              type: str
            items:
              description:
              - An array of tags. Each tag must be 1-63 characters long, and comply
                with RFC1035.
              returned: success
              type: list
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
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/instanceTemplates".format(**module.params)


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
