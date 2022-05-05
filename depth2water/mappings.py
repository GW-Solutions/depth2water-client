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


class Mapping:
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
        'date_timezone': 'America/Vancouver'
    }
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


class GroundwaterMapping(Mapping):
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


class SurfaceWaterMapping(Mapping):
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


class ClimateMapping(Mapping):
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
