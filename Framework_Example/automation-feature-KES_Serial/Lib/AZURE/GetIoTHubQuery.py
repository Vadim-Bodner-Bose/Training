from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import QuerySpecification
from Config.Azure_Config import IOTHUB_CONNECTION_STR

class GetIoTHubQuery:

    def __init__(self):
        # Create IoTHubRegistryManager
        self.iothub_registry_manager = IoTHubRegistryManager(IOTHUB_CONNECTION_STR)

    def get_query_result(self, query):
        try:
            query_specification = QuerySpecification(query=query)

            # Get all device twins using query
            query_result = self.iothub_registry_manager.query_iot_hub(query_specification)

            q_list = []
            for q in query_result.items:
                dict_iter = iter(q.additional_properties.values())
                q_list.append(next(dict_iter))

            return q_list

        except Exception as ex:
            print("Select statement returns empty dict.")