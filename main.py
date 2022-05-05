# Example script using depth2water client
# Below are all required imports
import logging
from depth2water import create_client, get_groundwater_mapping, get_surface_water_mapping, get_climate_mapping

# Client fully supports logging
logging.basicConfig(level=logging.DEBUG)

USERNAME = "admin"
PASSWORD = "adminpass"
CLIENT_ID = "xxxCLIENTxxx"
CLIENT_SECRET = "xxxxxSECRETxxxxx"
TEST_USER_ID = 24  # will use admin account to create data for a different user in this example


if __name__ == '__main__':

    # Create depth2water client
    client = create_client(USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, host='localhost:8000', scheme='http')

    # Get appropriate base mapping. Contains all required mappings for API serializers.
    surface_water_mapping = get_surface_water_mapping()

    # Add in your file specific mappings
    surface_water_mapping["date"] = "Date"
    surface_water_mapping["time"] = "Level"
    surface_water_mapping["water_level_compensated_m"] = "level"
    surface_water_mapping["station_id"] = "Station_ID"
    # Currently using admin account, create for specific user
    surface_water_mapping["owner"] = TEST_USER_ID

    # Alternatively, you can pass the mappings directly to the get_* func
    file_mappings = {
        "date": "Date", "time": "Time", "water_level_compensated_m": "level", "station_id": "Station_ID", "owner": 24}
    surface_water_mapping = get_surface_water_mapping(file_mappings)

    # !NOTE! Mapping assumes that header_row = 1 and first_row = 2.
    # If they don't, please update the mapping dicts.

    # !NOTE! Uploader uses default Pacific time zone. Update if needed.

    client.post_csv_file("depth2water/data/test_csv_post.csv", surface_water_mapping)
