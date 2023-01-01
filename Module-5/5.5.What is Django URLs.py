"""

Q1 : What is Django URLs ? make program to create django urls ?

ANS : 

==> Django runs through each URL pattern, in order, and stops at the first one that 
    matches the requested URL, matching against path_info . 
    
==> Once one of the URL patterns matches, Django imports and calls the given view,
    which is a Python function.
    
==> A request in Django first comes to urls.py and then goes to the matching function in views.py. 

==> Python functions in views.py take the web request from urls.py and give the web response to templates. 

==> It may go to the data access layer in models.py as per the queryset.     

"""