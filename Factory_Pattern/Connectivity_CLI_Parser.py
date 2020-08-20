# class CLI_Parser(object):
#     pass


class CLIParser():
    def specific_parser(self, input, format):
        parser = self._get_parser(format)
        return parser(input)

    def _get_parser(self, format):
        if format == "ayla_profiles_count":
            return self.connectivity_ayla_profiles_counter
        elif format == "ayla_profiles_list":
            return self.connectivity_list_ayla_profiles
        elif format == "software_platform_status":
            return self.software_platform_status
        else:
            raise NotImplementedError

    def connectivity_ayla_profiles_counter(self, input):
        counter = 1
        return counter

    def connectivity_list_ayla_profiles(self, input):
        wifi_profiles = None
        return wifi_profiles

    def software_platform_status(self, input):
        status = 'Standby'
        return status

counter = CLIParser().specific_parser("input string", "ayla_profiles_count")
print(counter)