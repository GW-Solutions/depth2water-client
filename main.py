# Example script using depth2water client
# Below are all required imports
import logging
from dateutil.parser import parser
from depth2water import *

# Client fully supports logging
logging.basicConfig(level=logging.DEBUG)

USERNAME = "gwadmin"
PASSWORD = "kowe#0485"
CLIENT_ID = "ZcaJhSvmWMdJnw93JKSuCecOczCIfZYCnMAUKzfE"
CLIENT_SECRET = "YsqWyesEJ4m7V7dBg0hpKRzjjEj9WRAVWs43LGj9cRp6ir4crmC5Uoi7gvwN7NZYRsfZ6SQXqq9h6H31Y63l8uV29kKyGQpiP7JMle7ftZMJ4xcXxpRNu4Rs3V9yY6sZ"
TEST_USER_ID = 24  # will use admin account to create data for a different user in this example


if __name__ == '__main__':

    # Create depth2water client
    client = create_client(USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, host='localhost:8000', scheme='http')
    print(client._user_id)
    # station = client.get_station_by_station_id('1095')
    # print(station)
    from datetime import datetime
    from dateutil.parser import parse
    # start_date = str(parse("2021-01-01T00:00:00-08:00"))
    # end_date = str(parse("2021-12-31T23:59:59-08:00"))
    # resp = client.bulk_delete_groundwater_data("VOW03")
    # resp = client.bulk_update_groundwater_data("VOW04", {'data_quality_type': 'PUMPING_EFFECT'})
    # print(resp)
    # data = client.get_groundwater_data(station_id='VOW01')
    # data2 = client.get_groundwater_data(station_id='VOW01', page=2)
    # data3 = client.get_groundwater_data(url=data2['next'])
    # result = data3['results'][0]
    # print('got_data', result)
    # # result['logger'] = ''
    # result['compensation_manual_measurement'] = ''
    # result['logger_depth_m'] = 5000
    # client.update_groundwater_data(result['id'], result)
    # resp = client.delete_groundwater_data(result['id'])
    # print(resp)
    # print(get_station_mapping())
    # print(get_groundwater_station_mapping())
    # print(get_surface_water_station_mapping())
    # print(get_climate_station_mapping())
    #
    # # Get appropriate base mapping. Contains all required mappings for API serializers.
    surface_water_mapping = get_surface_water_mapping()

    # Add in your file specific mappings
    # surface_water_mapping["date"] = "Date"
    # surface_water_mapping["time"] = "Level"
    # surface_water_mapping["water_level_compensated_m"] = "level"
    # surface_water_mapping["station_id"] = "Station_ID"
    # # Currently using admin account, create for specific user
    # surface_water_mapping["owner"] = TEST_USER_ID

    # Alternatively, you can pass the mappings directly to the get_* func
    file_mappings = {
        "date": "Date", "water_level_compensated_m": "level", "published": "pub_status", "station_id": "STATION_NUMBER", "owner": 1}
    surface_water_mapping = get_surface_water_mapping(file_mappings)
    #
    # climate_mapping = get_climate_station_mapping({"station_id": "NOT_OWNED", "latitude": 49, "longitude": -120})
    # new_station = client.create_station(climate_mapping)
    # print("NEW", resp)
    # !NOTE! Mapping assumes that header_row = 1 and first_row = 2.
    # If they don't, please update the mapping dicts.

    # !NOTE! Uploader uses default Pacific time zone. Update if needed.

    client.post_csv_file("/home/davebshow/Downloads/08MA002_2023-05-10.csv", surface_water_mapping)
    
    # station = client.get_station_by_station_id('TESTPOSTCLIMATE')
    # # Remember responses are raw Requests JSON now
    # station_resource_uri = station['results'][0]['url']
    print(station)
    file_mappings = {
        'station_id': 'station_name',
        'station': "",
        'max_temperature_c': 'max_temp',
        'max_temp_flag': 'max_temp_flag',
        'min_temperature_c': 'min_temp',
        'min_temperature_flag': 'min_temp_flag',
        'mean_temperature_c': 'mean_temp',
        'mean_temperature_flag': 'mean_temp_flag',
        'heat_degree_days_c': 'heat_deg_days',
        'heat_degree_days_flag': 'heat_deg_days_flag',
        'cool_degree_days_c': 'cool_deg_days',
        'cool_degree_days_flag': 'cool_deg_days_flag',
        'total_rain_mm': 'total_rain',
        'total_rain_flag': 'total_rain_flag',
        'total_snow_cm': 'total_snow',
        'total_snow_flag': 'total_snow_flag',
        'total_precipitation_mm': 'total_precip',
        'total_precipitation_flag': 'total_precip_flag',
        'snow_on_ground_cm': 'snow_on_grnd',
        'snow_on_ground_flag': 'snow_on_grnd_flag',
        'direction_max_gust_tens_degree': 'dir_of_max_gust',
        'direction_max_gust_flag': 'dir_of_max_gust_flag',
        'speed_max_gust_kmh': 'spd_of_max_gust',
        'speed_max_gust_flag': 'spd_of_max_gust_flag',
        'owner': 24,
        'comments': '',
        'datetime': 'datetime'
    }
    # client.post_csv_file("/home/davebshow/Downloads/1032_2022-08-02.csv", get_climate_mapping(file_mappings))
