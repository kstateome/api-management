K-State API Mangager
====================


Installation
============
Installing from source

pip install git+ssh://git@github.com/kstateome/api-management.git


What Tools are Included
=======================

The API Manager keeps track of API keys and tracks of the usage.  Each call can be logged easily.



Usage
=====

Method Helpers::

	key_exists(dictionary) - Checks for a key.  Returns true if key exists or false is not
	
			dictionary is {'key': key}
	
	key_check(dictionary) - Makes sure key is correct.  If key is valid returns True
	
Example::


	attrs = self.flatten_dict(request.PUT)
	key_dict = {'key': request.GET.get('key')}
	        if key_exists(key_dict) == False:
	            return key_required_error()
	        if key_check(key_dict):
	            try:
	                audience = Audience.objects.active().get(pk=audience_id)
	            except Audience.DoesNotExist:
	                return rc.NOT_FOUND
	            audience.name = attrs['name']
	            audience.save()
	            log_use(request.GET.get('key'), 'Audience', audience.id, 'updated')
	            return audience
	        else:
	            return key_incorrect_error()
	            

Logging Helper

	log_use(key, object being manipulated as string, id of object, action as string)
	
	
Example

	log_use(request.GET.get('key'), 'Audience', audience.id, 'updated')