# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    OpenAPI spec version: 0.0.160
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from yapily.api_client import ApiClient


class ConsentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_consent_using_post(self, user_uuid, create_consent_access_token, **kwargs):  # noqa: E501
        """Post consent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_consent_using_post(user_uuid, create_consent_access_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_uuid: userUuid (required)
        :param CreateConsentAccessToken create_consent_access_token: createConsentAccessToken (required)
        :return: Consent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_consent_using_post_with_http_info(user_uuid, create_consent_access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.add_consent_using_post_with_http_info(user_uuid, create_consent_access_token, **kwargs)  # noqa: E501
            return data

    def add_consent_using_post_with_http_info(self, user_uuid, create_consent_access_token, **kwargs):  # noqa: E501
        """Post consent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_consent_using_post_with_http_info(user_uuid, create_consent_access_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_uuid: userUuid (required)
        :param CreateConsentAccessToken create_consent_access_token: createConsentAccessToken (required)
        :return: Consent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uuid', 'create_consent_access_token']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_consent_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if ('user_uuid' not in params or
                params['user_uuid'] is None):
            raise ValueError("Missing the required parameter `user_uuid` when calling `add_consent_using_post`")  # noqa: E501
        # verify the required parameter 'create_consent_access_token' is set
        if ('create_consent_access_token' not in params or
                params['create_consent_access_token'] is None):
            raise ValueError("Missing the required parameter `create_consent_access_token` when calling `add_consent_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in params:
            path_params['userUuid'] = params['user_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_consent_access_token' in params:
            body_params = params['create_consent_access_token']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{userUuid}/consents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Consent',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_consent_with_code_using_post(self, consent_by_auth_code, **kwargs):  # noqa: E501
        """Post auth-code and auth-state  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_consent_with_code_using_post(consent_by_auth_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param ConsentAuthCodeRequest consent_by_auth_code: consentByAuthCode (required)
        :return: Consent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_consent_with_code_using_post_with_http_info(consent_by_auth_code, **kwargs)  # noqa: E501
        else:
            (data) = self.create_consent_with_code_using_post_with_http_info(consent_by_auth_code, **kwargs)  # noqa: E501
            return data

    def create_consent_with_code_using_post_with_http_info(self, consent_by_auth_code, **kwargs):  # noqa: E501
        """Post auth-code and auth-state  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_consent_with_code_using_post_with_http_info(consent_by_auth_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param ConsentAuthCodeRequest consent_by_auth_code: consentByAuthCode (required)
        :return: Consent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_by_auth_code']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_consent_with_code_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent_by_auth_code' is set
        if ('consent_by_auth_code' not in params or
                params['consent_by_auth_code'] is None):
            raise ValueError("Missing the required parameter `consent_by_auth_code` when calling `create_consent_with_code_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'consent_by_auth_code' in params:
            body_params = params['consent_by_auth_code']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consent-auth-code', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Consent',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_using_delete(self, consent_id, **kwargs):  # noqa: E501
        """Delete consent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_using_delete(consent_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent_id: consentId (required)
        :param bool force_delete: forceDelete
        :return: ApiResponseOfConsentDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_using_delete_with_http_info(consent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_using_delete_with_http_info(consent_id, **kwargs)  # noqa: E501
            return data

    def delete_using_delete_with_http_info(self, consent_id, **kwargs):  # noqa: E501
        """Delete consent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_using_delete_with_http_info(consent_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent_id: consentId (required)
        :param bool force_delete: forceDelete
        :return: ApiResponseOfConsentDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_id', 'force_delete']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent_id' is set
        if ('consent_id' not in params or
                params['consent_id'] is None):
            raise ValueError("Missing the required parameter `consent_id` when calling `delete_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in params:
            path_params['consentId'] = params['consent_id']  # noqa: E501

        query_params = []
        if 'force_delete' in params:
            query_params.append(('forceDelete', params['force_delete']))  # noqa: E501

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
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consents/{consentId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfConsentDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_consent_by_id_using_get(self, consent_id, **kwargs):  # noqa: E501
        """Get consent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_consent_by_id_using_get(consent_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent_id: consentId (required)
        :return: ApiResponseOfConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_consent_by_id_using_get_with_http_info(consent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_consent_by_id_using_get_with_http_info(consent_id, **kwargs)  # noqa: E501
            return data

    def get_consent_by_id_using_get_with_http_info(self, consent_id, **kwargs):  # noqa: E501
        """Get consent  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_consent_by_id_using_get_with_http_info(consent_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str consent_id: consentId (required)
        :return: ApiResponseOfConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consent_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent_id' is set
        if ('consent_id' not in params or
                params['consent_id'] is None):
            raise ValueError("Missing the required parameter `consent_id` when calling `get_consent_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in params:
            path_params['consentId'] = params['consent_id']  # noqa: E501

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
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consents/{consentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOfConsent',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_consent_by_single_access_consent_using_post(self, one_time_token, **kwargs):  # noqa: E501
        """Post one time token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_consent_by_single_access_consent_using_post(one_time_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param OneTimeTokenRequest one_time_token: oneTimeToken (required)
        :return: Consent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_consent_by_single_access_consent_using_post_with_http_info(one_time_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_consent_by_single_access_consent_using_post_with_http_info(one_time_token, **kwargs)  # noqa: E501
            return data

    def get_consent_by_single_access_consent_using_post_with_http_info(self, one_time_token, **kwargs):  # noqa: E501
        """Post one time token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_consent_by_single_access_consent_using_post_with_http_info(one_time_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param OneTimeTokenRequest one_time_token: oneTimeToken (required)
        :return: Consent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['one_time_token']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consent_by_single_access_consent_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'one_time_token' is set
        if ('one_time_token' not in params or
                params['one_time_token'] is None):
            raise ValueError("Missing the required parameter `one_time_token` when calling `get_consent_by_single_access_consent_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'one_time_token' in params:
            body_params = params['one_time_token']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consent-one-time-token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Consent',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_consents_using_get(self, **kwargs):  # noqa: E501
        """Get consents sorted by creation date  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_consents_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] filter_application_user_id: Filter consents by your application user Id (applicationUserId)
        :param list[str] filter_user_uuid: Filter consents by Yapily user Id (userUuid)
        :param list[str] filter_institution: Use this parameter to filter consent by institution, using the Yapily institution Id
        :param list[str] filter_status: Use this parameter to filter consent by status
        :param str _from: Use this parameter to filter consents created after the date specified
        :param str before: Use this parameter to filter consents created before the date specified
        :param int limit: Use this parameter to limit consent results, max limit is 20
        :param int offset: Use this parameter to specify the offset of the results
        :return: ApiListResponseOfConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_consents_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_consents_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_consents_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get consents sorted by creation date  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_consents_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] filter_application_user_id: Filter consents by your application user Id (applicationUserId)
        :param list[str] filter_user_uuid: Filter consents by Yapily user Id (userUuid)
        :param list[str] filter_institution: Use this parameter to filter consent by institution, using the Yapily institution Id
        :param list[str] filter_status: Use this parameter to filter consent by status
        :param str _from: Use this parameter to filter consents created after the date specified
        :param str before: Use this parameter to filter consents created before the date specified
        :param int limit: Use this parameter to limit consent results, max limit is 20
        :param int offset: Use this parameter to specify the offset of the results
        :return: ApiListResponseOfConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_application_user_id', 'filter_user_uuid', 'filter_institution', 'filter_status', '_from', 'before', 'limit', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consents_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_application_user_id' in params:
            query_params.append(('filter[applicationUserId]', params['filter_application_user_id']))  # noqa: E501
            collection_formats['filter[applicationUserId]'] = 'multi'  # noqa: E501
        if 'filter_user_uuid' in params:
            query_params.append(('filter[userUuid]', params['filter_user_uuid']))  # noqa: E501
            collection_formats['filter[userUuid]'] = 'multi'  # noqa: E501
        if 'filter_institution' in params:
            query_params.append(('filter[institution]', params['filter_institution']))  # noqa: E501
            collection_formats['filter[institution]'] = 'multi'  # noqa: E501
        if 'filter_status' in params:
            query_params.append(('filter[status]', params['filter_status']))  # noqa: E501
            collection_formats['filter[status]'] = 'multi'  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/consents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListResponseOfConsent',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_consents_using_get(self, user_uuid, **kwargs):  # noqa: E501
        """Get latest user consents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_consents_using_get(user_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_uuid: userUuid (required)
        :param str filter_institution: Use this parameter to filter consent by institution, using the Yapily institution Id. This replaces the deprecated `institutionId` query param.
        :param int limit: Use this parameter to limit consent results, max limit is 20
        :return: list[Consent]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_consents_using_get_with_http_info(user_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_consents_using_get_with_http_info(user_uuid, **kwargs)  # noqa: E501
            return data

    def get_user_consents_using_get_with_http_info(self, user_uuid, **kwargs):  # noqa: E501
        """Get latest user consents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_consents_using_get_with_http_info(user_uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_uuid: userUuid (required)
        :param str filter_institution: Use this parameter to filter consent by institution, using the Yapily institution Id. This replaces the deprecated `institutionId` query param.
        :param int limit: Use this parameter to limit consent results, max limit is 20
        :return: list[Consent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uuid', 'filter_institution', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_consents_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if ('user_uuid' not in params or
                params['user_uuid'] is None):
            raise ValueError("Missing the required parameter `user_uuid` when calling `get_user_consents_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in params:
            path_params['userUuid'] = params['user_uuid']  # noqa: E501

        query_params = []
        if 'filter_institution' in params:
            query_params.append(('filter[institution]', params['filter_institution']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = ['basicAuth', 'tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users/{userUuid}/consents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Consent]',  # noqa: E501
            auth_settings=auth_settings,
            asyncRequest=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
