# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your Application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.33
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yapily.api_client import ApiClient


class ApplicationUsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_user_using_post(self, new_application_user, **kwargs):  # noqa: E501
        """Add an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_user_using_post(new_application_user, async=True)
        >>> result = thread.get()

        :param async bool
        :param NewApplicationUser new_application_user: newApplicationUser (required)
        :return: ApplicationUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_user_using_post_with_http_info(new_application_user, **kwargs)  # noqa: E501
        else:
            (data) = self.add_user_using_post_with_http_info(new_application_user, **kwargs)  # noqa: E501
            return data

    def add_user_using_post_with_http_info(self, new_application_user, **kwargs):  # noqa: E501
        """Add an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_user_using_post_with_http_info(new_application_user, async=True)
        >>> result = thread.get()

        :param async bool
        :param NewApplicationUser new_application_user: newApplicationUser (required)
        :return: ApplicationUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['new_application_user']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'new_application_user' is set
        if ('new_application_user' not in params or
                params['new_application_user'] is None):
            raise ValueError("Missing the required parameter `new_application_user` when calling `add_user_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_application_user' in params:
            body_params = params['new_application_user']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationUser',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user_using_delete(self, user_uuid, **kwargs):  # noqa: E501
        """Delete an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_using_delete(user_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_uuid: userUuid (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_user_using_delete_with_http_info(user_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_using_delete_with_http_info(user_uuid, **kwargs)  # noqa: E501
            return data

    def delete_user_using_delete_with_http_info(self, user_uuid, **kwargs):  # noqa: E501
        """Delete an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_using_delete_with_http_info(user_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_uuid: userUuid (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if ('user_uuid' not in params or
                params['user_uuid'] is None):
            raise ValueError("Missing the required parameter `user_uuid` when calling `delete_user_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in params:
            path_params['userUuid'] = params['user_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{userUuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_using_get(self, user_uuid, **kwargs):  # noqa: E501
        """Get an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_using_get(user_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_uuid: userUuid (required)
        :return: ApplicationUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_using_get_with_http_info(user_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_using_get_with_http_info(user_uuid, **kwargs)  # noqa: E501
            return data

    def get_user_using_get_with_http_info(self, user_uuid, **kwargs):  # noqa: E501
        """Get an application user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_using_get_with_http_info(user_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_uuid: userUuid (required)
        :return: ApplicationUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if ('user_uuid' not in params or
                params['user_uuid'] is None):
            raise ValueError("Missing the required parameter `user_uuid` when calling `get_user_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in params:
            path_params['userUuid'] = params['user_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{userUuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationUser',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users_using_get(self, **kwargs):  # noqa: E501
        """Get application users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_users_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[ApplicationUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_users_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_users_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_users_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get application users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_users_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[ApplicationUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ApplicationUser]',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
