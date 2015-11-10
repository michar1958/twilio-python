# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import deserialize
from twilio import values
from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page


class PhoneNumberList(ListResource):

    def __init__(self, version, trunk_sid):
        """
        Initialize the PhoneNumberList
        
        :param Version version: Version that contains the resource
        :param trunk_sid: The trunk_sid
        
        :returns: PhoneNumberList
        :rtype: PhoneNumberList
        """
        super(PhoneNumberList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
        }
        self._uri = '/Trunks/{trunk_sid}/PhoneNumbers'.format(**self._solution)

    def create(self, phone_number_sid):
        """
        Create a new PhoneNumberInstance
        
        :param unicode phone_number_sid: The phone_number_sid
        
        :returns: Newly created PhoneNumberInstance
        :rtype: PhoneNumberInstance
        """
        data = values.of({
            'PhoneNumberSid': phone_number_sid,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return PhoneNumberInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams PhoneNumberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        page = self.page(
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def read(self, limit=None, page_size=None):
        """
        Reads PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of PhoneNumberInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return PhoneNumberPage(
            self._version,
            response,
            trunk_sid=self._solution['trunk_sid'],
        )

    def get(self, sid):
        """
        Constructs a PhoneNumberContext
        
        :param sid: The sid
        
        :returns: PhoneNumberContext
        :rtype: PhoneNumberContext
        """
        return PhoneNumberContext(
            self._version,
            trunk_sid=self._solution['trunk_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a PhoneNumberContext
        
        :param sid: The sid
        
        :returns: PhoneNumberContext
        :rtype: PhoneNumberContext
        """
        return PhoneNumberContext(
            self._version,
            trunk_sid=self._solution['trunk_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.PhoneNumberList>'


class PhoneNumberPage(Page):

    def __init__(self, version, response, trunk_sid):
        """
        Initialize the PhoneNumberPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param trunk_sid: The trunk_sid
        
        :returns: PhoneNumberPage
        :rtype: PhoneNumberPage
        """
        super(PhoneNumberPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance
        
        :param dict payload: Payload response from the API
        
        :returns: PhoneNumberInstance
        :rtype: PhoneNumberInstance
        """
        return PhoneNumberInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.PhoneNumberPage>'


class PhoneNumberContext(InstanceContext):

    def __init__(self, version, trunk_sid, sid):
        """
        Initialize the PhoneNumberContext
        
        :param Version version: Version that contains the resource
        :param trunk_sid: The trunk_sid
        :param sid: The sid
        
        :returns: PhoneNumberContext
        :rtype: PhoneNumberContext
        """
        super(PhoneNumberContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
            'sid': sid,
        }
        self._uri = '/Trunks/{trunk_sid}/PhoneNumbers/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a PhoneNumberInstance
        
        :returns: Fetched PhoneNumberInstance
        :rtype: PhoneNumberInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return PhoneNumberInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the PhoneNumberInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.PhoneNumberContext {}>'.format(context)


class PhoneNumberInstance(InstanceResource):

    def __init__(self, version, payload, trunk_sid, sid=None):
        """
        Initialize the PhoneNumberInstance
        
        :returns: PhoneNumberInstance
        :rtype: PhoneNumberInstance
        """
        super(PhoneNumberInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'address_requirements': payload['address_requirements'],
            'api_version': payload['api_version'],
            'beta': payload['beta'],
            'capabilities': payload['capabilities'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'links': payload['links'],
            'phone_number': payload['phone_number'],
            'sid': payload['sid'],
            'sms_application_sid': payload['sms_application_sid'],
            'sms_fallback_method': payload['sms_fallback_method'],
            'sms_fallback_url': payload['sms_fallback_url'],
            'sms_method': payload['sms_method'],
            'sms_url': payload['sms_url'],
            'status_callback': payload['status_callback'],
            'status_callback_method': payload['status_callback_method'],
            'trunk_sid': payload['trunk_sid'],
            'url': payload['url'],
            'voice_application_sid': payload['voice_application_sid'],
            'voice_caller_id_lookup': payload['voice_caller_id_lookup'],
            'voice_fallback_method': payload['voice_fallback_method'],
            'voice_fallback_url': payload['voice_fallback_url'],
            'voice_method': payload['voice_method'],
            'voice_url': payload['voice_url'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'trunk_sid': trunk_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                trunk_sid=self._solution['trunk_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def address_requirements(self):
        """
        :returns: The address_requirements
        :rtype: phone_number.address_requirement
        """
        return self._properties['address_requirements']

    @property
    def api_version(self):
        """
        :returns: The api_version
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def beta(self):
        """
        :returns: The beta
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def capabilities(self):
        """
        :returns: The capabilities
        :rtype: unicode
        """
        return self._properties['capabilities']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def phone_number(self):
        """
        :returns: The phone_number
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def sms_application_sid(self):
        """
        :returns: The sms_application_sid
        :rtype: unicode
        """
        return self._properties['sms_application_sid']

    @property
    def sms_fallback_method(self):
        """
        :returns: The sms_fallback_method
        :rtype: unicode
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: The sms_fallback_url
        :rtype: unicode
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: The sms_method
        :rtype: unicode
        """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """
        :returns: The sms_url
        :rtype: unicode
        """
        return self._properties['sms_url']

    @property
    def status_callback(self):
        """
        :returns: The status_callback
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The status_callback_method
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def trunk_sid(self):
        """
        :returns: The trunk_sid
        :rtype: unicode
        """
        return self._properties['trunk_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def voice_application_sid(self):
        """
        :returns: The voice_application_sid
        :rtype: unicode
        """
        return self._properties['voice_application_sid']

    @property
    def voice_caller_id_lookup(self):
        """
        :returns: The voice_caller_id_lookup
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']

    @property
    def voice_fallback_method(self):
        """
        :returns: The voice_fallback_method
        :rtype: unicode
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: The voice_fallback_url
        :rtype: unicode
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: The voice_method
        :rtype: unicode
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: The voice_url
        :rtype: unicode
        """
        return self._properties['voice_url']

    def fetch(self):
        """
        Fetch a PhoneNumberInstance
        
        :returns: Fetched PhoneNumberInstance
        :rtype: PhoneNumberInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the PhoneNumberInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.PhoneNumberInstance {}>'.format(context)