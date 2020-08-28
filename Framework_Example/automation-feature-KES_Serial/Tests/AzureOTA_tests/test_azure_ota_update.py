import pytest

from Lib.AZURE.AzureOTAupdate import AzureOTAupdate

#pytest -s test_azure_ota_update.py --device_id test-m01-010209009BE118BC54440139

@pytest.mark.TM_414
def test_azure_ota(device_id):
    azure = AzureOTAupdate("valik_ota_test1", device_id)
    assert azure.check_desired_twin()           # Desire twin check
    assert azure.check_reported_twin()          # Reported twin check
    azure.roll_back_azure_config()


