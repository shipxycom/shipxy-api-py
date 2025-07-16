from typing import List

from pydantic import BaseModel


class SearchShipResult(BaseModel):
    match_type: int
    mmsi: int
    imo: int
    call_sign: str
    ship_name: str
    data_source: int
    last_time: str
    last_time_utc: int


class SearchShipResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: List[SearchShipResult]


class ShipPosition(BaseModel):
    mmsi: int
    imo: int
    call_sign: str
    ship_name: str
    ship_cnname: str = ''  # 有些结果可能没有此字段
    data_source: int
    ship_type: int
    length: float
    width: float
    left: float
    trail: float
    draught: float
    dest: str
    destcode: str
    eta: str
    eta_utc: int = 0  # 有些接口可能没有此字段
    navistat: int
    lat: float
    lng: float
    sog: float
    cog: float
    hdg: float
    rot: float
    last_time: str
    last_time_utc: int


class SingleShipResponse(BaseModel):
    status: int
    msg: str
    data: ShipPosition


class ManyShipResponse(BaseModel):
    status: int
    msg: str
    data: list[ShipPosition]


class FleetShipResponse(BaseModel):
    status: int
    msg: str
    data: list[ShipPosition]


class SurRoundingShipResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[ShipPosition]


class AreaShipData(BaseModel):
    total: int
    scode: int
    continue_: int = 0  # 'continue'为Python关键字，改为continue_
    ship_list: list[ShipPosition]

    # class Config:
    #     fields = {'continue_': 'continue'}


class AreaShipResponse(BaseModel):
    status: int
    msg: str
    data: AreaShipData


class ShipRegistryData(BaseModel):
    mmsi: int
    registry: str


class ShipRegistryResponse(BaseModel):
    status: int
    msg: str
    data: ShipRegistryData


class EngineInfo(BaseModel):
    designer: str
    powerKW: int


class ShipParticularData(BaseModel):
    mmsi: int
    imo: int
    call_sign: str
    ship_name: str
    length: float
    mould_width: float
    flag_country_code: str
    flag_country: str
    build_country: str
    build_date: str
    class_name: str
    pandi_club: str
    ship_type: str
    ship_type_level5_subgroup: str
    ship_type_group: str
    ship_status: str
    gross_tonnage: float
    net_tonnage: float
    deadweight: float
    teu: int
    speed_max: float
    speed_service: float
    draught: float
    port_of_registry: str
    group_code: str
    group_company: str
    group_country_code: str
    group_country: str
    shipmanager_code: str
    shipmanager_company: str
    shipmanager_country_code: str
    shipManager_country: str
    operator_code: str
    operator_company: str
    operator_country_code: str
    operator_country: str
    doc_code: str
    doc_company: str
    doc_country_code: str
    doc_country: str
    registered_code: str
    registered_owner: str
    registered_country_code: str
    registered_country: str
    technical_code: str
    technical_manager: str
    technical_country_code: str
    technical_country: str
    builder_code: str
    builder_company: str
    builder_country_code: str
    builder_country: str
    update_time: str
    main_engine_list: list[EngineInfo]
    aux_engine_list: list[EngineInfo]


class SearchShipParticularResponse(BaseModel):
    status: int
    msg: str
    data: list[ShipParticularData]


class PortData(BaseModel):
    port_code: str
    port_name: str
    port_cnname: str
    port_time_zone: str
    port_country_name: str
    port_country_cnname: str
    port_country_code: str


class SearchPortResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[PortData]


class BerthShipData(BaseModel):
    mmsi: int
    imo: int
    call_sign: str
    ship_name: str
    ship_type: int
    length: float
    width: float
    left: float
    trail: float
    draught: float
    arrival_time: str
    arrival_time_utc: int
    stay_time: float
    navistat: int = 0  # 有些数据可能没有该字段


class GetBerthShipsResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[BerthShipData]


class AnchorShipData(BaseModel):
    mmsi: int
    imo: int
    call_sign: str
    ship_name: str
    ship_type: int
    length: float
    width: float
    left: float
    trail: float
    draught: float
    arrival_time: str
    arrival_time_utc: int
    stay_time: float
    navistat: int = 0  # 有些数据可能没有该字段


class GetAnchorShipsResponse(BaseModel):
    status: int
    msg: str
    total: int = 0
    data: list[AnchorShipData] = []


class ETAShipData(BaseModel):
    mmsi: int
    ship_name: str
    imo: int
    dwt: float
    ship_type: str
    length: float
    width: float
    draught: float
    preport_cnname: str
    last_time: str
    last_time_utc: int
    eta: str
    eta_utc: int
    dest: str
    ship_flag: str = ""
    registry: str = ""


class GetETAShipsResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[ETAShipData]


class ShipTrackPoint(BaseModel):
    data_source: int
    utc: int
    lng: float
    lat: float
    sog: float
    cog: float


class GetShipTrackResponse(BaseModel):
    status: int
    msg: str
    data: list[ShipTrackPoint]


class ApproachShipInfo(BaseModel):
    mmsi: int
    imo: int
    call_sign: str
    ship_name: str
    ship_type: int


class ApproachEventInfo(BaseModel):
    approach_zone: int
    lat: float
    lng: float
    port_code: str
    position: str
    approach_time: str
    approach_time_utc: int
    separation_time: str
    separation_time_utc: int
    duration: float
    sog: float


class ApproachDataItem(BaseModel):
    approach_ship: ApproachShipInfo
    approach_event: ApproachEventInfo


class ShipApproachData(BaseModel):
    ship_data: ApproachShipInfo
    approach_data: list[ApproachDataItem]


class SearchShipApproachResponse(BaseModel):
    status: int
    msg: str
    data: ShipApproachData


class PortOfCallData(BaseModel):
    ship_name: str
    call_sign: str
    imo: int
    mmsi: int
    ship_type: int
    port_cnname: str
    port_name: str
    port_time_zone: str
    port_code: str
    terminal_name: str
    berth_name: str
    port_country_cnname: str
    port_country_name: str
    port_country_code: str
    arrival_anchorage: str = ""
    ata: str = ""
    atb: str = ""
    atd: str = ""
    arrival_draught: float = 0.0
    departure_draught: float = 0.0
    stay_time: float = 0.0
    stay_terminal_time: float = 0.0


class GetPortOfCallByShipResponse(BaseModel):
    status: int
    msg: str
    data: list[PortOfCallData]


class PortOfCallByShipPortData(BaseModel):
    ship_name: str
    call_sign: str
    imo: int
    mmsi: int
    ship_type: str
    port_cnname: str
    port_name: str
    port_time_zone: str
    port_code: str
    terminal_name: str
    berth_name: str
    port_country_cnname: str
    port_country_name: str
    port_country_code: str
    arriveanchorage: str = ""
    ata: str = ""
    atb: str = ""
    atd: str = ""
    arrival_draught: float = 0.0
    departure_draught: float = 0.0
    stay_time: float = 0.0
    stay_terminal_time: float = 0.0


class GetPortOfCallByShipPortResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[PortOfCallByShipPortData]


class PortInfo(BaseModel):
    port_code: str = ""
    port_name: str = ""
    port_cnname: str = ""
    port_time_zone: str = ""
    port_country_name: str = ""
    port_country_cnname: str = ""
    port_country_code: str = ""
    arrive_anchorage: str = ""
    ata: str = ""
    atb: str = ""
    atd: str = ""
    # currentport 可能有 country_en、country_code、arriveanchorage
    country_en: str = ""
    country_code: str = ""
    arriveanchorage: str = ""


class ShipStatusData(BaseModel):
    ship_name: str
    call_sign: str
    imo: int
    mmsi: int
    ship_type: str
    current_sea_area: str = ""
    sea_area_code: str = ""
    current_city: str = ""
    current_city_code: str = ""
    lng: float = 0.0
    lat: float = 0.0
    previousport: PortInfo = None
    currentport: PortInfo = None


class GetShipStatusResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[ShipStatusData]


class PortCallPortInfo(BaseModel):
    port_code: str = ""
    port_cnname: str = ""
    port_name: str = ""
    port_time_zone: str = ""
    terminal_name: str = ""
    berth_name: str = ""
    arrival_anchorage: str = ""
    ata: str = ""
    atb: str = ""
    atd: str = ""
    arrival_draught: float = 0.0
    departure_draught: float = 0.0
    stay_time: float = 0.0
    stay_terminal_time: float = 0.0


class PortOfCallByPortData(BaseModel):
    imo: int
    mmsi: int
    ship_type: str
    ship_name: str
    call_sign: str
    currentport: PortCallPortInfo = None
    previousport: PortCallPortInfo = None
    nextport: PortCallPortInfo = None


class GetPortOfCallByPortResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[PortOfCallByPortData]


class RoutePoint(BaseModel):
    lng: float
    lat: float


class PlanRouteByPointData(BaseModel):
    distance: float
    route: list[RoutePoint]


class PlanRouteByPointResponse(BaseModel):
    status: int
    msg: str
    data: PlanRouteByPointData


class PlanRouteByPortData(BaseModel):
    distance: float
    route: list[RoutePoint]


class PlanRouteByPortResponse(BaseModel):
    status: int
    msg: str
    data: PlanRouteByPortData


class SingleETAShipInfo(BaseModel):
    mmsi: int
    imo: int
    ship_name: str
    call_sign: str
    ship_type: int


class SingleETALocationInfo(BaseModel):
    lng: float
    lat: float
    speed: float = 0.0
    sog: float = 0.0
    sea_area: str = ""
    sea_area_code: int = None


class SingleETAPortInfo(BaseModel):
    port_code: str = ""
    port_cnname: str = ""
    port_name: str = ""
    time_zone: int = 0
    port_country_code: str = ""
    port_country_name: str = ""
    port_country_cnname: str = ""
    ata: float = 0.0
    atb: float = 0.0
    atd: float = 0.0


class SingleETANextPortInfo(BaseModel):
    port_code: str = ""
    port_cnname: str = ""
    port_name: str = ""
    time_zone: int = 0
    port_country_code: str = ""
    port_country_name: str = ""
    port_country_cnname: str = ""
    sailed_distance: float = 0.0
    sailed_time: float = 0.0
    ais_speed: float = 0.0
    speed: float = 0.0
    eta: str = ""
    eta_utc: int = 0
    remaining_distance: float = 0.0
    distance: float = 0.0


class GetSingleETAPreciseData(BaseModel):
    ship: SingleETAShipInfo
    location: SingleETALocationInfo
    preport: SingleETAPortInfo
    nextport: SingleETANextPortInfo


class GetSingleETAPreciseResponse(BaseModel):
    status: int
    msg: str
    data: GetSingleETAPreciseData


class WeatherData(BaseModel):
    weather_type: int
    sea_area: str
    publish_time: str
    center_lat: float
    center_lng: float
    forecastaging: str
    meteorological: str
    winddirection: str
    windpower: str
    waveheight: str = None
    visibility: float


class GetWeatherResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[WeatherData]


class TyphoonListItem(BaseModel):
    typhoon_id: int
    typhoon_code: int
    typhoon_cncode: str
    typhoon_cnname: str
    typhoon_name: str
    current_year: int
    dataMark: str


class GetAllTyphoonResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[TyphoonListItem]


class TyphoonDetailItem(BaseModel):
    typhoon_id: int
    typhoon_time: int
    forecast: str
    fhour: str
    lat: float
    lng: float
    grade: int
    mspeed: float
    pressure: float
    kspeed: float
    direction: str
    radius7: float
    radius10: float
    radius7_s: float
    radius10_s: float
    radius12_s: float


class GetSingleTyphoonResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[TyphoonDetailItem]


class TideStationInfo(BaseModel):
    port_code: int
    port_cnname: str
    port_name: str
    port_country_cnname: str
    port_country_name: str
    lat: float
    lng: float
    port_time_zone: str
    datumn: str
    tide_type: str


class GetTidesResponse(BaseModel):
    status: int
    msg: str
    total: int
    data: list[TideStationInfo]


class TideOverviewItem(BaseModel):
    tide_date: str
    tide_time1: str
    tide_time2: str
    tide_time3: str
    tide_time4: str
    tide_height1: float
    tide_height2: float
    tide_height3: float
    tide_height4: float
    tide_lowhigh1: str
    tide_lowhigh2: str
    tide_lowhigh3: str
    tide_lowhigh4: str


class TideDetailItem(BaseModel):
    tide_date: str
    h0: float = 0.0
    h1: float = 0.0
    h2: float = 0.0
    h3: float = 0.0
    h4: float = 0.0
    h5: float = 0.0
    h6: float = 0.0
    h7: float = 0.0
    h8: float = 0.0
    h9: float = 0.0
    h10: float = 0.0
    h11: float = 0.0
    h12: float = 0.0
    h13: float = 0.0
    h14: float = 0.0
    h15: float = 0.0
    h16: float = 0.0
    h17: float = 0.0
    h18: float = 0.0
    h19: float = 0.0
    h20: float = 0.0
    h21: float = 0.0
    h22: float = 0.0
    h23: float = 0.0


class GetTideDataData(BaseModel):
    overview: list[TideOverviewItem]
    detail: list[TideDetailItem]


class GetTideDataResponse(BaseModel):
    status: int
    msg: str
    data: GetTideDataData


class GetWeatherByPointData(BaseModel):
    bm500: float
    humidity: float
    oceandir: float
    oceanspeed: float
    pressure: float
    swelldir: float
    swellheight: float
    swellperiod: float
    temperature: float
    visibility: float
    waveheight: float
    winddir: float
    windspeed: float
    publish_time: str
    lng: float
    lat: float


class GetWeatherByPointResponse(BaseModel):
    status: float
    msg: str
    data: GetWeatherByPointData


class GetNavWarningData(BaseModel):
    warning_type: int = 0
    source: str = ''
    title: str = ''
    range_type: int = 0
    range_points: str = ''
    radius: float = 0
    pub_time: str = ''
    expire_time: str = ''
    content: str = ''


class GetNavWarningResponse(BaseModel):
    status: float
    msg: str
    total: int
    data: List[GetNavWarningData]
