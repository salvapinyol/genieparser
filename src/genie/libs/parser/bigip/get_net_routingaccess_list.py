# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/routing/access-list' resources
# =============================================


class NetRoutingAccesslistSchema(MetaParser):

    schema = {}


class NetRoutingAccesslist(NetRoutingAccesslistSchema):
    """ To F5 resource for /mgmt/tm/net/routing/access-list
    """

    cli_command = "/mgmt/tm/net/routing/access-list"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
