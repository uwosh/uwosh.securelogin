Introduction
============

Forces posting login credentials to SSL/HTTPS URL if the URL does not
match certain patterns, specifically for use at University of
Wisconsin Oshkosh, where our public URLs for Plone sites are like

    www.uwosh.edu/thissite

and our internal URLs are like

    plone3.webcluster.uwosh.edu:15082/sitefolder1/thissite 

and we want the internal URLs to allow non-SSL login but want all
public URLs to require SSL/HTTPS logins.  

For development, we want sites such as

    localhost:8080/thissite

to use the default non-SSL/HTTP login.
