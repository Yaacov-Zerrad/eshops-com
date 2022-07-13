
import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "Aeo7slrixySBdhBZgzMUfLTdwD1ZQOaEuSCPW8Hxv8pRbouwIsgXdaNABmt_sKLypHcWPNf-pxQfa4-c"
        self.client_secret = "ENImt4jbUXrkIx94yyAdzFGGldjJcjbXD1xjrbSU_rT4uBeF9bxQSHqHvRG-Ytgf9oQwYpIlHJqW-Z0z"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)