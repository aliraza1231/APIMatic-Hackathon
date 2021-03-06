# -*- coding: utf-8 -*-

"""
mixpanelexportapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mixpanelexportapi.decorators import lazy_property
from mixpanelexportapi.configuration import Configuration
from mixpanelexportapi.configuration import Environment
from mixpanelexportapi.http.auth.basic_auth import BasicAuth
from mixpanelexportapi.controllers.export_data_controller\
    import ExportDataController


class MixpanelexportapiClient(object):

    @lazy_property
    def export_data(self):
        return ExportDataController(self.config, self.auth_managers)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'],
                 environment=Environment.PRODUCTION,
                 basic_auth_user_name='TODO: Replace',
                 basic_auth_password='TODO: Replace', config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment,
                                         basic_auth_user_name=basic_auth_user_name,
                                         basic_auth_password=basic_auth_password)
        else:
            self.config = config
        self.initialize_auth_managers(self.config)

    def initialize_auth_managers(self, config):
        self.auth_managers = { key: None for key in ['global']}
        self.auth_managers['global'] = BasicAuth(config.basic_auth_user_name, config.basic_auth_password)
        return self.auth_managers
