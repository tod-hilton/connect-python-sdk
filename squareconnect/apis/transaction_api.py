# coding: utf-8

"""
Copyright 2016 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TransactionApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def capture_transaction(self, authorization, location_id, transaction_id, **kwargs):
        """
        CaptureTransaction
        Captures a transaction that was created with the **Charge** endpoint with a `delay_capture` value of `true`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.capture_transaction(authorization, location_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str location_id:  (required)
        :param str transaction_id:  (required)
        :return: CaptureTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'location_id', 'transaction_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method capture_transaction" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `capture_transaction`")
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `capture_transaction`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `capture_transaction`")


        resource_path = '/v2/locations/{location_id}/transactions/{transaction_id}/capture'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']
        if 'transaction_id' in params:
            path_params['transaction_id'] = params['transaction_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CaptureTransactionResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def charge(self, authorization, location_id, body, **kwargs):
        """
        Charge
        Charges a card represented by a token.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.charge(authorization, location_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str location_id: The ID of the location to associate the transaction with. (required)
        :param ChargeRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: ChargeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'location_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method charge" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `charge`")
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `charge`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `charge`")


        resource_path = '/v2/locations/{location_id}/transactions'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ChargeResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def list_transactions(self, authorization, location_id, **kwargs):
        """
        ListTransactions
        Lists transactions for a particular location.  When making a request to this endpoint, your request body **must** include either the `cursor` parameter, or it must include both `begin_time` and `end_time` with an optional `sort_order`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_transactions(authorization, location_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str location_id: The ID of the location to list transactions for. (required)
        :param str begin_time: The beginning of the requested reporting period, in RFC 3339 format.
        :param str end_time: The end of the requested reporting period, in RFC 3339 format.
        :param str sort_order: The order in which results are listed in the response (`ASC` for chronological, `DESC` for reverse-chronological).
        :param str cursor: A pagination cursor to retrieve the next set of results for your original query to the endpoint.
        :return: ListTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'location_id', 'begin_time', 'end_time', 'sort_order', 'cursor']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_transactions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `list_transactions`")
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `list_transactions`")


        resource_path = '/v2/locations/{location_id}/transactions'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']

        query_params = {}
        if 'begin_time' in params and params['begin_time'] is not None:
            query_params['begin_time'] = params['begin_time']
        if 'end_time' in params and params['end_time'] is not None:
            query_params['end_time'] = params['end_time']
        if 'sort_order' in params and params['sort_order'] is not None:
            query_params['sort_order'] = params['sort_order']
        if 'cursor' in params and params['cursor'] is not None:
            query_params['cursor'] = params['cursor']

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ListTransactionsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def retrieve_transaction(self, authorization, location_id, transaction_id, **kwargs):
        """
        RetrieveTransaction
        Retrieves details for a single transaction.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.retrieve_transaction(authorization, location_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str location_id:  (required)
        :param str transaction_id:  (required)
        :return: RetrieveTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'location_id', 'transaction_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_transaction" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `retrieve_transaction`")
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `retrieve_transaction`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `retrieve_transaction`")


        resource_path = '/v2/locations/{location_id}/transactions/{transaction_id}'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']
        if 'transaction_id' in params:
            path_params['transaction_id'] = params['transaction_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RetrieveTransactionResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def void_transaction(self, authorization, location_id, transaction_id, **kwargs):
        """
        VoidTransaction
        Cancels a transaction that was created with the **Charge** endpoint with a `delay_capture` value of `true`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_transaction(authorization, location_id, transaction_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: The value to provide in the Authorization header of your request. This value should follow the format `Bearer YOUR_ACCESS_TOKEN_HERE`. (required)
        :param str location_id:  (required)
        :param str transaction_id:  (required)
        :return: VoidTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'location_id', 'transaction_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method void_transaction" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `void_transaction`")
        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `void_transaction`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params) or (params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `void_transaction`")


        resource_path = '/v2/locations/{location_id}/transactions/{transaction_id}/void'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']
        if 'transaction_id' in params:
            path_params['transaction_id'] = params['transaction_id']

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = "Bearer {}".format(params['authorization'])

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='VoidTransactionResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        
