from collections import OrderedDict
from typing import Dict, Set, Type

from oaas.client_definition import ClientDefinition
from oaas.client_provider import ClientMiddleware
from oaas.server_provider import ServerMiddleware
from oaas.service_definition import ServiceDefinition

clients: Dict[Type, ClientDefinition] = OrderedDict()
services: Dict[ServiceDefinition, bool] = OrderedDict()

servers_middleware: Set[ServerMiddleware] = set()
clients_middleware: Set[ClientMiddleware] = set()
