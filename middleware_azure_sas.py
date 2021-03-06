"""
Munki Middleware Azure SAS Proof of Concept

https://github.com/MaxXyzzy/Munki-Middleware-AzureSAS

by Max who doesn't know anything about Python (first timer!),
   or much about Munki, or much about Azure Storage :P

That said... It seems to work! Yay?


How To:
  1. Set the Azure Storage Container to Private.

  2. Create a Shared access token for the Container
     > Signing Method: Account Key.
     > Permissions: READ (nothing else)
     > Start/Expiry dates: Set appropriately for your needs.
     > Allowed Protocols: HTTPS Only.

  3. Put the generated Blob SAS token in AZURE_SAS below.

  4. Install the middleware_azure_sas.py file per the Munki docs:
     > https://github.com/munki/munki/wiki/Middleware

Example Blob SAS token / query string:
sp=r&st=2021-01-01T01:00:00Z&se=2025-01-01T01:00:00Z&spr=https&sv=2020-08-04&sr=c&sig=h16jMmeBR2LcGvgvZ8pGY1kGj16Wuv24CPKl6Wfj8xg%3D

"""

AZURE_SAS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def process_request_options(options):
    if 'blob.core' in options['url']:
        options['url'] = options['url'] + '?' + AZURE_SAS

    return options
