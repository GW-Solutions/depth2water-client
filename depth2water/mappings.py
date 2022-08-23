def get_groundwater_mapping(mapping=None):
    if mapping:
        return GroundwaterMapping().get_mapping(mapping)
    return GroundwaterMapping().mapping


def get_surface_water_mapping(mapping=None):
    if mapping:
        return SurfaceWaterMapping().get_mapping(mapping)
    return SurfaceWaterMapping().mapping


def get_climate_mapping(mapping=None):
    if mapping:
        return ClimateMapping().get_mapping(mapping)
    return ClimateMapping().mapping


def get_station_mapping(mapping=None):
    if mapping:
        return StationMapping().get_mapping(mapping)
    return StationMapping().mapping


def get_groundwater_station_mapping(mapping=None):
    if mapping:
        return GroundwaterStationMapping().get_mapping(mapping)
    return GroundwaterStationMapping().mapping


def get_surface_water_station_mapping(mapping=None):
    if mapping:
        return SurfaceWaterStationMapping().get_mapping(mapping)
    return SurfaceWaterStationMapping().mapping


def get_climate_station_mapping(mapping=None):
    if mapping:
        return ClimateStationMapping().get_mapping(mapping)
    return ClimateStationMapping().mapping


class Mapping:
    _BASE_MAPPING = {}
    _MAPPING = {}

    @property
    def mapping(self):
        new_mapping = dict(self._BASE_MAPPING)
        new_mapping.update(self._MAPPING)
        return new_mapping

    def get_mapping(self, mapping):
        new_mapping = self.mapping
        new_mapping.update(mapping)
        return new_mapping


class StationMapping(Mapping):
    _BASE_MAPPING = {
        'accuracy_elevation': '',
        'accuracy_location': '',
        'aquifer_number': '',
        'easting_m': '',
        'ground_elevation_m': '',
        'latitude': '',
        'location_name': '',
        'longitude': '',
        'monitoring_status': 'ACTIVE',
        'monitoring_type': '',
        'northing_m': '',
        'prov_terr_state_lc': '',
        'pump_depth_m': '',
        'sounder_pipe_m': '',
        'station_id': '',
        'client_id': '',
        'top_of_casing_m': '',
        'well_aquifer_type': '',
        'well_depth_m': '',
        'well_id_plate': '',
        'well_tag_number': '',
        'zone': '',
        'zone_meta': '',
        'waterbody_type': '',
        'waterbody_name': '',
        'watershed_name': '',
        'watershed_area': '',
        'climate_id': '',
        'wmo_id': '',
        'tc_id': '',
        'measurement_frequency': '',
        'aquifer_description': '',
        'data_interpretation': '',
        'owner': ''
    }


class GroundwaterStationMapping(StationMapping):
    _MAPPING = {
        'monitoring_type': 'GROUNDWATER'
    }



class SurfaceWaterStationMapping(StationMapping):
    _MAPPING = {
        'monitoring_type': 'SURFACE_WATER'
    }


class ClimateStationMapping(StationMapping):
    _MAPPING = {
        'monitoring_type': 'CLIMATE'
    }


class TimeSeriesMapping(Mapping):
    _BASE_MAPPING = {
        'logger': '',
        'station': '',
        'barometric_pressure_units': '',
        'first_row': 2,
        'header_row': 1,
        'excel_sheet': '',
        'approval_level': '',
        'comments': '',
        'date': '',
        'datetime': '',
        'grade_code': '',
        'station_id': '',
        'station_in_filename': False,
        'measurement_type': '',
        'owner': '',
        'time': '',
        'file_type': '',
        'date_date_format': '',
        'time_date_format': '',
        'datetime_date_format': '',
        'datetime_timezone': 'America/Vancouver',
        'date_timezone': 'America/Vancouver',
        'published': ''
    }


class GroundwaterMapping(TimeSeriesMapping):
    _MAPPING = {
        'monitoring_type': 'GROUNDWATER',
        'compensation_station': '',
        'barometric_pressure_m': '',
        'conductivity_us_cm': '',
        'depth_to_water_m': '',
        'depth_to_water_manual': '',
        'depth_to_water_manual_units': '',
        'depth_to_water_manual_time': '',
        'depth_to_water_manual_timezone': '',
        'logger_depth_manual': '',
        'logger_depth_manual_units': '',
        'logger_depth_manual_time': '',
        'logger_depth_manual_timezone': '',
        'manual_measurement_comments': '',
        'depth_to_water_mtoc': '',
        'ground_elevation_m': '',
        'ground_water_elevation_m': '',
        'temperature_c': '',
        'water_level_compensated_m': '',
        'water_level_non_compensated_m': '',
        'data_quality_type': ''
    }


class SurfaceWaterMapping(TimeSeriesMapping):
    _MAPPING = {
        'monitoring_type': 'SURFACE_WATER',
        'barometric_pressure_units': '',
        'barometric_pressure_m': '',
        'surface_water_elevation_m': '',
        'temperature_c': '',
        'water_level_staff_gauge_calibrated': '',
        'water_level_non_compensated_m': '',
        'water_level_compensated_m': '',
        'water_flow_calibrated_mps': ''
    }


class ClimateMapping(TimeSeriesMapping):
    _MAPPING = {
        'monitoring_type': 'CLIMATE',
        'temperature_c': '',
        'temp_flag': '',
        'dew_point_temperature_c': '',
        'dew_point_temperature_flag': '',
        'relative_humidity': '',
        'relative_humidity_flag': '',
        'wind_direction_tens_degrees': '',
        'wind_direction_flag': '',
        'wind_speed_kmh': '',
        'wind_speed_flag': '',
        'visibility_km': '',
        'visibility_flag': '',
        'station_atmospheric_pressure_m': '',
        'station_atmospheric_pressure_flag': '',
        'humidex': '',
        'humidex_flag': '',
        'wind_chill': '',
        'wind_chill_flag': '',
        'weather': '',
        'max_temperature_c': '',
        'max_temp_flag': '',
        'min_temperature_c': '',
        'min_temperature_flag': '',
        'mean_temperature_c': '',
        'mean_temperature_flag': '',
        'heat_degree_days_c': '',
        'heat_degree_days_flag': '',
        'cool_degree_days_c': '',
        'cool_degree_days_flag': '',
        'total_rain_mm': '',
        'total_rain_flag': '',
        'total_snow_cm': '',
        'total_snow_flag': '',
        'total_precipitation_mm': '',
        'total_precipitation_flag': '',
        'snow_on_ground_cm': '',
        'snow_on_ground_flag': '',
        'direction_max_gust_tens_degree': '',
        'direction_max_gust_flag': '',
        'speed_max_gust_kmh': '',
        'speed_max_gust_flag': ''
    }
