import consul
from consul import Check

from _types.service import Service
from config.settings import settings

# 集群节点
CONSUL_NODES = [{ "host": "127.0.0.1", "port": 8500 }]
# clients
CONSUL_CLIENTS = []


class Consul:
    """
    ServiceRegistration

    Considering cluster service registration a separate registration method is added to consul
    and a unified handler function is also added.

    """

    client: consul.Consul

    def __init__(self, host: str, port: int):
        self.client = consul.Consul(host=host, port=port)

    def register_service(self, config: Service):
        service_definition = dict(config)
        service_definition["service_id"] = config.name
        check = Check.http(
            f"http://{config.address}:{config.port}{settings.API_V1_STR}/health", "10s", "10s", deregister="1m"
        )
        service_definition["check"] = check
        self.client.agent.service.register(**service_definition)
        print(f"register success ! -------> {config.name}")

    def deregister_service(self, name: str):
        self.client.agent.service.deregister(name)
        print(f"deregister success ! ------> {name}")

    def find_server(self, name) -> Service:
        """
        Access to healthy services
        :param name:
        :return:
        """
        index, data = self.client.health.service(name)
        service = data[0]["Service"] if len(data) > 0 else None
        if service is not None:
            config = {
                "name": name,
                "host": service["Address"],
                "port": int(service["Port"]),
                "tags": service["Tags"]
            }
            return Service(**config)
        else:
            raise Exception(f"consul did not register a {name} service.")


for node in CONSUL_NODES:
    CONSUL_CLIENTS.append(Consul(node["host"], node["port"]))


def registerAll(config: Service):
    """
    Register with all nodes
    :param config:
    :return:
    """
    for client in CONSUL_CLIENTS:
        client.register_service(config)


def deregisterAll(server_name: str):
    for client in CONSUL_CLIENTS:
        client.deregister_service(server_name)


def findServerAll(server_name: str):
    services: list[Service] = []
    for client in CONSUL_CLIENTS:
        server = client.find_server(server_name)
        if server:
            services.append(server)
    return services
