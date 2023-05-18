import requests

from config.settings import settings
from core.consul import CONSUL_CLIENTS, Consul
from enums.service_api import RouteType


class ConsulService:
    client: Consul

    """
    Consul's microservice invocation tool
    Use it to discover services on consul, and use a common name to discover services,
    and use a restful interface for remote calls to microservices, but we should constrain it,
    so we should apply uniform interface constraints.
    """

    def __init__(self, consul_host=None, consul_port=None):
        """
        TODO: Should poll check, is currently fixed.
        :param consul_host:
        :param consul_port:
        """
        self.client = CONSUL_CLIENTS[0]

    def call_service_method(self, service_name: str, config: RouteType) -> object:
        """
        Microservice interface invocation
        :param service_name:
        :param config:
        :return:
        """
        service = self.client.find_server(service_name)
        url = f"http://{service.address}:{service.port}{settings.API_V1_STR}"
        api_uri = ""
        # copy
        params_dict = config.params.copy()

        # 验证是否是RestFul传参
        if params_dict.get("_is"):
            del params_dict["_is"]
        else:
            api_uri = config.api.format(**params_dict)
        full_url = url + api_uri
        response = requests.request(method=config.method, url=full_url)
        if response.status_code != 200:
            raise Exception(f"Failed to call method '{config.api}' on service '{service_name}'")
        else:
            return response.json()


ConsulServiceUtil = ConsulService()
