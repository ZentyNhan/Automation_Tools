import os
import re

import claraVR
from testproject.para_fsi.GLib import *
FaultsDict = {}

FaultID = GetFaultList()

################## AliveCounter ##################
FaultsDict['FAULT_GW_170_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_170_ALC'] = {
	'FaultName' : 'FAULT_GW_170_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_170',
	'Signal' : 'EPS_RollingCounter_170',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_170_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_EPS', 'code':'0xD92882'}
}

FaultsDict['FAULT_GW_17E_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_17E_ALC'] = {
	'FaultName' : 'FAULT_GW_17E_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_17E',
	'Signal' : 'EPS_RollingCounter_17E',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_17E_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_EPS', 'code':'0xD92882'}
}

FaultsDict['FAULT_GW_180_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_180_ALC'] = {
	'FaultName' : 'FAULT_GW_180_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_RollingCounter',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_180_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_SAS', 'code':'0xD92282'}
}

FaultsDict['FAULT_GW_184_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_184_ALC'] = {
	'FaultName' : 'FAULT_GW_184_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_184',
	'Signal' : 'EMS_RollingCounter_184',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_184_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_EMS', 'code':'0xD92082'}
}

FaultsDict['FAULT_GW_187_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_187_ALC'] = {
	'FaultName' : 'FAULT_GW_187_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_187',
	'Signal' : 'ESP_RollingCounter_187',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_187_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_ESP', 'code':'0xD92182'}
}

FaultsDict['FAULT_GW_188_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_188_ALC'] = {
	'FaultName' : 'FAULT_GW_188_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_188',
	'Signal' : 'TCU_RollingCounter_188',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_188_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_TCU', 'code':'0xD92382'}
}

FaultsDict['FAULT_GW_196_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_196_ALC'] = {
	'FaultName' : 'FAULT_GW_196_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_196',
	'Signal' : 'EMS_RollingCounter_196',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_196_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_EMS', 'code':'0xD92082'}
}

FaultsDict['FAULT_GW_197_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_197_ALC'] = {
	'FaultName' : 'FAULT_GW_197_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_197',
	'Signal' : 'ESP_RollingCounter_197',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_197_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_EPB', 'code':'0xD92982'}
}

FaultsDict['FAULT_GW_1A6_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_1A6_ALC'] = {
	'FaultName' : 'FAULT_GW_1A6_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A6',
	'Signal' : 'EMS_RollingCounter_1A6',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_1A6_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_EMS', 'code':'0xD92082'}
}

FaultsDict['FAULT_GW_1A8_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_1A8_ALC'] = {
	'FaultName' : 'FAULT_GW_1A8_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A8',
	'Signal' : 'TCU_RollingCounter_1A8',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_1A8_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_TCU', 'code':'0xD92382'}
}

FaultsDict['FAULT_GW_206_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_206_ALC'] = {
	'FaultName' : 'FAULT_GW_206_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_206',
	'Signal' : 'ESP_RollingCounter_206',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_206_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_ESP', 'code':'0xD92182'}
}

FaultsDict['FAULT_GW_208_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_208_ALC'] = {
	'FaultName' : 'FAULT_GW_208_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : 'ESP_RollingCounter_208',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_208_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_ESP', 'code':'0xD92182'}
}

FaultsDict['FAULT_GW_24F_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_24F_ALC'] = {
	'FaultName' : 'FAULT_GW_24F_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_24F',
	'Signal' : 'EPS_RollingCounter_24F',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_24F_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_EPS', 'code':'0xD92882'}
}

FaultsDict['FAULT_GW_258_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_258_ALC'] = {
	'FaultName' : 'FAULT_GW_258_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_258',
	'Signal' : 'ESP_RollingCounter_258',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_258_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_ESP', 'code':'0xD92182'}
}

FaultsDict['FAULT_GW_26A_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_26A_ALC'] = {
	'FaultName' : 'FAULT_GW_26A_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_26A',
	'Signal' : 'EMS_RollingCounter_26A',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_26A_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_EMS', 'code':'0xD92082'}
}

FaultsDict['FAULT_GW_277_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_277_ALC'] = {
	'FaultName' : 'FAULT_GW_277_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_RollingCounter_277',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_277_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_ESP', 'code':'0xD92182'}
}

FaultsDict['FAULT_GW_278_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_278_ALC'] = {
	'FaultName' : 'FAULT_GW_278_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_278',
	'Signal' : 'ESP_RollingCounter_278',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_278_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_ESP', 'code':'0xD92182'}
}

FaultsDict['FAULT_GW_28C_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_28C_ALC'] = {
	'FaultName' : 'FAULT_GW_28C_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_28C',
	'Signal' : 'GW_MFS_RollingCounter_28C',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_28C_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_GW_MFS', 'code':'0xD92782'}
}

FaultsDict['FAULT_GW_2DE_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_2DE_ALC'] = {
	'FaultName' : 'FAULT_GW_2DE_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_2DE',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_2DE_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_IP', 'code':'0xD92B82'}
}


FaultsDict['FAULT_GW_356_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_356_ALC'] = {
	'FaultName' : 'FAULT_GW_356_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_356',
	'Signal' : 'IMS_RollingCounter_356',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_356_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_IMS', 'code':'0xD92582'}
}

FaultsDict['FAULT_GW_360_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_360_ALC'] = {
	'FaultName' : 'FAULT_GW_360_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_360',
	'Signal' : 'IMS_RollingCounter_360',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_360_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_IMS', 'code':'0xD92582'}
}

FaultsDict['FAULT_GW_3AF_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3AF_ALC'] = {
	'FaultName' : 'FAULT_GW_3AF_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3AF',
	'Signal' : 'HU_RollingCounter_3AF',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3AF_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_HU', 'code':'0xD92682'}
}

FaultsDict['FAULT_GW_3B8_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3B8_ALC'] = {
	'FaultName' : 'FAULT_GW_3B8_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3B8',
	'Signal' : 'HU_RollingCounter_3B8',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3B8_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_HU', 'code':'0xD92682'}
}

FaultsDict['FAULT_GW_3BB_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3BB_ALC'] = {
	'FaultName' : 'FAULT_GW_3BB_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3BB',
	'Signal' : 'HU_RollingCounter_3BB',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3BB_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_HU', 'code':'0xD92682'}
}

FaultsDict['FAULT_GW_3C2_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3C2_ALC'] = {
	'FaultName' : 'FAULT_GW_3C2_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3C2',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3C2_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_HU', 'code':'0xD92682'}
}

FaultsDict['FAULT_GW_3C7_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3C7_ALC'] = {
	'FaultName' : 'FAULT_GW_3C7_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3C7',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3C7_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_HU', 'code':'0xD92682'}
}

FaultsDict['FAULT_GW_50_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_50_ALC'] = {
	'FaultName' : 'FAULT_GW_50_ALC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_50',
	'Signal' : 'SRS_RollingCounter_id050',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_50_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ROLLING_COUNTER_SRS', 'code':'0xD92482'}
}

FaultsDict['FAULT_PRI_VFC_LineInfo_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_LineInfo_ALC'] = {
	'FaultName' : 'FAULT_PRI_VFC_LineInfo_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_LineHeader',
	'Signal' : 'VFC_Line01_AliveCtr',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_LineInfo_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_LineInfo_E2E', 'code':'0xD97108'}
}

FaultsDict['FAULT_PRI_VFC_ObjectInfo_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_ObjectInfo_ALC'] = {
	'FaultName' : 'FAULT_PRI_VFC_ObjectInfo_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_ObjectHdr',
	'Signal' : 'VFC_ObjHdr_AliveCtr',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_ObjectInfo_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_ObjectInfo_E2E', 'code':'0xD97008'}
}

FaultsDict['FAULT_PRI_VFC_SensorState_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_SensorState_ALC'] = {
	'FaultName' : 'FAULT_PRI_VFC_SensorState_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_SensorState',
	'Signal' : 'VFC_SensorState_AliveCtr',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_SensorState_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_SensorState_E2E', 'code':'0xD96808'}
}


FaultsDict['FAULT_PRI_VFC_TSR_ASL_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_TSR_ASL_ALC'] = {
	'FaultName' : 'FAULT_PRI_VFC_TSR_ASL_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_TSR_ASL',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_TSR_ASL_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_TSR_ASL_E2E', 'code':'0xD96908'}
}

FaultsDict['FAULT_VFC_0x89_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x89_ALC'] = {
	'FaultName' : 'FAULT_VFC_0x89_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x89',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x89_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

FaultsDict['FAULT_VFC_0x91_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x91_ALC'] = {
	'FaultName' : 'FAULT_VFC_0x91_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x91',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x91_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

FaultsDict['FAULT_VFC_0x92_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x92_ALC'] = {
	'FaultName' : 'FAULT_VFC_0x92_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x92',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x92_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

FaultsDict['FAULT_VFC_0x93_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x93_ALC'] = {
	'FaultName' : 'FAULT_VFC_0x93_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x93',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x93_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

FaultsDict['FAULT_VFC_0x94_ALC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x94_ALC'] = {
	'FaultName' : 'FAULT_VFC_0x94_ALC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'ALV',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x94',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x94_ALC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

################## Checksum ##################
FaultsDict['FAULT_GW_170_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_170_CRC'] = {
	'FaultName' : 'FAULT_GW_170_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_170',
	'Signal' : 'EPS_CRCCheck_170',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_170_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_EPS', 'code':'0xD94783'}
}

FaultsDict['FAULT_GW_17E_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_17E_CRC'] = {
	'FaultName' : 'FAULT_GW_17E_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_17E',
	'Signal' : 'EPS_CRCCheck_17E',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_17E_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_EPS', 'code':'0xD94783'}
}

FaultsDict['FAULT_GW_180_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_180_CRC'] = {
	'FaultName' : 'FAULT_GW_180_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_CRCCheck',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_180_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_SAS', 'code':'0xD94283'}
}

FaultsDict['FAULT_GW_184_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_184_CRC'] = {
	'FaultName' : 'FAULT_GW_184_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_184',
	'Signal' : 'EMS_CRCCheck_184',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_184_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_EMS', 'code':'0xD94083'}
}

FaultsDict['FAULT_GW_187_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_187_CRC'] = {
	'FaultName' : 'FAULT_GW_187_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_187',
	'Signal' : 'ESP_CRCCheck_187',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_187_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_ESP', 'code':'0xD94183'}
}

FaultsDict['FAULT_GW_188_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_188_CRC'] = {
	'FaultName' : 'FAULT_GW_188_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_188',
	'Signal' : 'TCU_CRCCheck_188',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_188_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_TCU', 'code':'0xD94383'}
}

FaultsDict['FAULT_GW_196_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_196_CRC'] = {
	'FaultName' : 'FAULT_GW_196_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_196',
	'Signal' : 'EMS_CRCCheck_196',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_196_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_EMS', 'code':'0xD94083'}
}

FaultsDict['FAULT_GW_197_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_197_CRC'] = {
	'FaultName' : 'FAULT_GW_197_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_197',
	'Signal' : 'ESP_CRCCheck_197',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_197_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_EPB', 'code':'0xD94883'}
}

FaultsDict['FAULT_GW_1A6_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_1A6_CRC'] = {
	'FaultName' : 'FAULT_GW_1A6_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A6',
	'Signal' : 'EMS_CRCCheck_1A6',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_1A6_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_EMS', 'code':'0xD94083'}
}

FaultsDict['FAULT_GW_1A8_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_1A8_CRC'] = {
	'FaultName' : 'FAULT_GW_1A8_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A8',
	'Signal' : 'TCU_CRCCheck_1A8',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_1A8_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_TCU', 'code':'0xD94383'}
}

FaultsDict['FAULT_GW_206_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_206_CRC'] = {
	'FaultName' : 'FAULT_GW_206_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_206',
	'Signal' : 'ESP_CRCCheck_206',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_206_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_ESP', 'code':'0xD94183'}
}

FaultsDict['FAULT_GW_208_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_208_CRC'] = {
	'FaultName' : 'FAULT_GW_208_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : 'ESP_CRCCheck_208',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_208_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_ESP', 'code':'0xD94183'}
}

FaultsDict['FAULT_GW_24F_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_24F_CRC'] = {
	'FaultName' : 'FAULT_GW_24F_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_24F',
	'Signal' : 'EPS_CRCCheck_24F',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_24F_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_EPS', 'code':'0xD94783'}
}

FaultsDict['FAULT_GW_258_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_258_CRC'] = {
	'FaultName' : 'FAULT_GW_258_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_258',
	'Signal' : 'ESP_CRCCheck_258',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_258_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_ESP', 'code':'0xD94183'}
}

FaultsDict['FAULT_GW_26A_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_26A_CRC'] = {
	'FaultName' : 'FAULT_GW_26A_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_26A',
	'Signal' : 'EMS_CRCCheck_26A',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_26A_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_EMS', 'code':'0xD94083'}
}

FaultsDict['FAULT_GW_277_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_277_CRC'] = {
	'FaultName' : 'FAULT_GW_277_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_CRCCheck_277',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_277_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_ESP', 'code':'0xD94183'}
}

FaultsDict['FAULT_GW_278_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_278_CRC'] = {
	'FaultName' : 'FAULT_GW_278_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_278',
	'Signal' : 'ESP_CRCCheck_278',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_278_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_ESP', 'code':'0xD94183'}
}

FaultsDict['FAULT_GW_28C_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_28C_CRC'] = {
	'FaultName' : 'FAULT_GW_28C_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_28C',
	'Signal' : 'GW_MFS_CRCCheck_28C',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_28C_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_GW_MFS', 'code':'0xD94683'}
}

FaultsDict['FAULT_GW_2DE_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_2DE_CRC'] = {
	'FaultName' : 'FAULT_GW_2DE_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_2DE',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_2DE_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_IP', 'code':'0xD94A83'}
}


FaultsDict['FAULT_GW_356_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_356_CRC'] = {
	'FaultName' : 'FAULT_GW_356_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_356',
	'Signal' : 'IMS_CRCCheck_356',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_356_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_IMS', 'code':'0xD94483'}
}

FaultsDict['FAULT_GW_360_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_360_CRC'] = {
	'FaultName' : 'FAULT_GW_360_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_360',
	'Signal' : 'IMS_CRCCheck_360',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_360_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_IMS', 'code':'0xD94483'}
}

FaultsDict['FAULT_GW_3AF_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3AF_CRC'] = {
	'FaultName' : 'FAULT_GW_3AF_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3AF',
	'Signal' : 'HU_CRCCheck_3AF',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3AF_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_HU', 'code':'0xD94583'}
}

FaultsDict['FAULT_GW_3B8_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3B8_CRC'] = {
	'FaultName' : 'FAULT_GW_3B8_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3B8',
	'Signal' : 'HU_CRCCheck_3B8',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3B8_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_HU', 'code':'0xD94583'}
}

FaultsDict['FAULT_GW_3BB_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3BB_CRC'] = {
	'FaultName' : 'FAULT_GW_3BB_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3BB',
	'Signal' : 'HU_CRCCheck_3BB',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3BB_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_HU', 'code':'0xD94583'}
}

FaultsDict['FAULT_GW_3C2_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3C2_CRC'] = {
	'FaultName' : 'FAULT_GW_3C2_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3C2',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3C2_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_HU', 'code':'0xD94583'}
}

FaultsDict['FAULT_GW_3C7_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3C7_CRC'] = {
	'FaultName' : 'FAULT_GW_3C7_CRC',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3C7',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3C7_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_CRCCHECK_HU', 'code':'0xD94583'}
}

FaultsDict['FAULT_PRI_VFC_LineInfo_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_LineInfo_CRC'] = {
	'FaultName' : 'FAULT_PRI_VFC_LineInfo_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_LineHeader',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_LineInfo_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_LineInfo_E2E', 'code':'0xD97108'}
}

FaultsDict['FAULT_PRI_VFC_ObjectInfo_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_ObjectInfo_CRC'] = {
	'FaultName' : 'FAULT_PRI_VFC_ObjectInfo_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_ObjectHdr',
	'Signal' : 'VFC_ObjHdr_CRC',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_ObjectInfo_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_ObjectInfo_E2E', 'code':'0xD97008'}
}

FaultsDict['FAULT_PRI_VFC_SensorState_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_SensorState_CRC'] = {
	'FaultName' : 'FAULT_PRI_VFC_SensorState_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_SensorState',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_SensorState_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_SensorState_E2E', 'code':'0xD96808'}
}

FaultsDict['FAULT_PRI_VFC_TSR_ASL_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_TSR_ASL_CRC'] = {
	'FaultName' : 'FAULT_PRI_VFC_TSR_ASL_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_TSR_ASL',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_TSR_ASL_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_TSR_ASL_E2E', 'code':'0xD96908'}
}

FaultsDict['FAULT_VFC_0x89_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x89_CRC'] = {
	'FaultName' : 'FAULT_VFC_0x89_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x89',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x89_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

FaultsDict['FAULT_VFC_0x91_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x91_CRC'] = {
	'FaultName' : 'FAULT_VFC_0x91_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x91',
	'Signal' : 'VFC_0x91_CRC',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x91_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

FaultsDict['FAULT_VFC_0x92_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x92_CRC'] = {
	'FaultName' : 'FAULT_VFC_0x92_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x92',
	'Signal' : 'VFC_0x92_CRC',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x92_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

FaultsDict['FAULT_VFC_0x93_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x93_CRC'] = {
	'FaultName' : 'FAULT_VFC_0x93_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x93',
	'Signal' : 'VFC_0x93_CRC',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x93_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

FaultsDict['FAULT_VFC_0x94_CRC'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x94_CRC'] = {
	'FaultName' : 'FAULT_VFC_0x94_CRC',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'CRC',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x94',
	'Signal' : 'VFC_0x94_CRC',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x94_CRC'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_E2E', 'code':'0xD96C08'}
}

################## DataLengthCheck ##################
################## Timeout ##################
FaultsDict['FAULT_ACC_1BA_Rx_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_1BA_Rx_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_1BA_Rx_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_1BA',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_1BA_Rx_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_ACC_244_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_244_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_244_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_244',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_244_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_ACC_307_Rx_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_307_Rx_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_307_Rx_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_307',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_307_Rx_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_ACC_312_Rx_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_312_Rx_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_312_Rx_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_312',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_312_Rx_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_ACC_31A_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_31A_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_31A_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_31A',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_31A_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_ACC_36F_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_36F_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_36F_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_36F',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_36F_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_ACC_378_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_378_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_378_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_378',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_378_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_ACC_382_Rx_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_382_Rx_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_382_Rx_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_382',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_382_Rx_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_ACC_693_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_ACC_693_TIMEOUT'] = {
	'FaultName' : 'FAULT_ACC_693_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'ACC_693',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ACC_693_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TX_TO_ACC_MESSAGE', 'code':'0xD91087'}
}

FaultsDict['FAULT_GW_170_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_170_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_170_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_170',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_170_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_EPS', 'code':'0xD90987'}
}

FaultsDict['FAULT_GW_17E_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_17E_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_17E_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_17E',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_17E_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_EPS', 'code':'0xD90987'}
}

FaultsDict['FAULT_GW_180_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_180_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_180_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_180',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_180_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_SAS', 'code':'0xD90D87'}
}

FaultsDict['FAULT_GW_184_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_184_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_184_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_184',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_184_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_EMS', 'code':'0xD90087'}
}

FaultsDict['FAULT_GW_187_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_187_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_187_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_187',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_187_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_ESP', 'code':'0xD90687'}
}

FaultsDict['FAULT_GW_188_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_188_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_188_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_188',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_188_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_TCU', 'code':'0xD90F87'}
}

FaultsDict['FAULT_GW_196_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_196_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_196_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_196',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_196_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_EMS', 'code':'0xD90087'}
}

FaultsDict['FAULT_GW_197_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_197_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_197_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_197',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_197_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b10001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_EPB', 'code':'0xD90587'}
}

FaultsDict['FAULT_GW_1A6_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_1A6_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_1A6_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A6',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_1A6_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_EMS', 'code':'0xD90087'}
}

FaultsDict['FAULT_GW_1A8_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_1A8_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_1A8_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A8',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_1A8_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_TCU', 'code':'0xD90F87'}
}

FaultsDict['FAULT_GW_206_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_206_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_206_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_206',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_206_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_ESP', 'code':'0xD90687'}
}

FaultsDict['FAULT_GW_208_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_208_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_208_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_208_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_ESP', 'code':'0xD90687'}
}

FaultsDict['FAULT_GW_24F_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_24F_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_24F_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_24F',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_24F_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_EPS', 'code':'0xD90987'}
}

FaultsDict['FAULT_GW_258_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_258_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_258_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_258',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_258_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_ESP', 'code':'0xD90687'}
}

FaultsDict['FAULT_GW_26A_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_26A_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_26A_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_26A',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_26A_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_EMS', 'code':'0xD90087'}
}

FaultsDict['FAULT_GW_277_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_277_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_277_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_277_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_ESP', 'code':'0xD90687'}
}

FaultsDict['FAULT_GW_278_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_278_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_278_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_278',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_278_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_ESP', 'code':'0xD90687'}
}

FaultsDict['FAULT_GW_28B_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_28B_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_28B_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_28B',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_28B_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_BCM', 'code':'0xD90A87'}
}

FaultsDict['FAULT_GW_28C_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_28C_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_28C_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_28C',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_28C_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000,
	'EHT' : 15,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_GW_MFS', 'code':'0xD90C87'}
}

FaultsDict['FAULT_GW_2DE_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_2DE_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_2DE_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_2DE',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_2DE_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_IP', 'code':'0xD90487'}
}


FaultsDict['FAULT_GW_356_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_356_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_356_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_356',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_356_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_IMS', 'code':'0xD90787'}
}

FaultsDict['FAULT_GW_360_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_360_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_360_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_360',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_360_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_IMS', 'code':'0xD90787'}
}

FaultsDict['FAULT_GW_387_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_387_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_387_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_387',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_387_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_BCM', 'code':'0xD90A87'}
}

FaultsDict['FAULT_GW_3AF_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3AF_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_3AF_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3AF',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3AF_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_HU', 'code':'0xD90887'}
}

FaultsDict['FAULT_GW_3B8_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3B8_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_3B8_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3B8',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3B8_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_HU', 'code':'0xD90887'}
}

FaultsDict['FAULT_GW_3BB_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3BB_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_3BB_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3BB',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3BB_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_HU', 'code':'0xD90887'}
}

FaultsDict['FAULT_GW_3C2_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3C2_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_3C2_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3C2',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3C2_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_HU', 'code':'0xD90887'}
}

FaultsDict['FAULT_GW_3C7_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3C7_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_3C7_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3C7',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3C7_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_HU', 'code':'0xD90887'}
}
FaultsDict['FAULT_GW_3FD_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_3FD_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_3FD_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_3FD',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_3FD_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 1000.0,
	'EHT' : 15.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_BCM', 'code':'0xD90A87'}
}

FaultsDict['FAULT_GW_50_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_GW_50_TIMEOUT'] = {
	'FaultName' : 'FAULT_GW_50_TIMEOUT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_2',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_50',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_GW_50_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 2500,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TIMEOUT_SRS', 'code':'0xD90E87'}
}


FaultsDict['FAULT_PRI_VFC_SensorState_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_SensorState_TIMEOUT'] = {
	'FaultName' : 'FAULT_PRI_VFC_SensorState_TIMEOUT',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_SensorState',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_SensorState_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 4,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_SensorState_TIMEOUT', 'code':'0xD96487'}
}

FaultsDict['FAULT_PRI_VFC_TSR_ASL_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_TSR_ASL_TIMEOUT'] = {
	'FaultName' : 'FAULT_PRI_VFC_TSR_ASL_TIMEOUT',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_TSR_ASL',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_TSR_ASL_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 4,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_TSR_ASL_TIMEOUT', 'code':'0xD96587'}
}

FaultsDict['FAULT_VFC_0x89_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x89_TIMEOUT'] = {
	'FaultName' : 'FAULT_VFC_0x89_TIMEOUT',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x89',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x89_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 50,
	'EHT' : 0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_TIMEOUT', 'code':'0xD96C87'}
}

FaultsDict['FAULT_VFC_0x91_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x91_TIMEOUT'] = {
	'FaultName' : 'FAULT_VFC_0x91_TIMEOUT',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x91',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x91_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500,
	'EHT' : 0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_TIMEOUT', 'code':'0xD96C87'}
}

FaultsDict['FAULT_VFC_0x92_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x92_TIMEOUT'] = {
	'FaultName' : 'FAULT_VFC_0x92_TIMEOUT',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x92',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x92_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500,
	'EHT' : 0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_TIMEOUT', 'code':'0xD96C87'}
}

FaultsDict['FAULT_VFC_0x93_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x93_TIMEOUT'] = {
	'FaultName' : 'FAULT_VFC_0x93_TIMEOUT',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x93',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x93_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_TIMEOUT', 'code':'0xD96C87'}
}

FaultsDict['FAULT_VFC_0x94_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_0x94_TIMEOUT'] = {
	'FaultName' : 'FAULT_VFC_0x94_TIMEOUT',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x94',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_0x94_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 100,
	'EHT' : 0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_TIMEOUT', 'code':'0xD96C87'}
}

FaultsDict['FAULT_VFC_LateralInformation_1_TIMEOUT'] = dict(FaultsDict)
FaultsDict['FAULT_VFC_LateralInformation_1_TIMEOUT'] = {
	'FaultName' : 'FAULT_VFC_LateralInformation_1_TIMEOUT',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'TO',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x96',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VFC_LateralInformation_1_TIMEOUT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFCLateralCntrl_TIMEOUT', 'code':'0xD96C87'}
}

################## Signal ##################
FaultsDict['FAULT_AT_Trans_FAIL'] = dict(FaultsDict)
FaultsDict['FAULT_AT_Trans_FAIL'] = {
	'FaultName' : 'FAULT_AT_Trans_FAIL',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A8',
	'Signal' : 'TCU_TransFailureStatus',
	'Value' : [2, 3],
	'FaultID' : FaultID['FAULT_AT_Trans_FAIL'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_Trans_FAIL', 'code':'0xA12181'}
}

FaultsDict['FAULT_AccPedalPosition_ERROR'] = dict(FaultsDict)
FaultsDict['FAULT_AccPedalPosition_ERROR'] = {
	'FaultName' : 'FAULT_AccPedalPosition_ERROR',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_196',
	'Signal' : 'EMS_AccpedelError',
	'Value' : 0x01,
	'FaultID' : FaultID['FAULT_AccPedalPosition_ERROR'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_AccPedal_ERROR', 'code':'0xA10277'}
}

FaultsDict['FAULT_AccPedalPosition_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_AccPedalPosition_INVALID'] = {
	'FaultName' : 'FAULT_AccPedalPosition_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_196',
	'Signal' : 'EMS_RealAccPedal',
	'Value' : {'raw':0xFF},
	'FaultID' : FaultID['FAULT_AccPedalPosition_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_AccPedalPosition_INVALID', 'code':'0xA13A81'}
}

FaultsDict['FAULT_BCM_FRONTWIPERSTATUS_FAILURE'] = dict(FaultsDict)
FaultsDict['FAULT_BCM_FRONTWIPERSTATUS_FAILURE'] = {
	'FaultName' : 'FAULT_BCM_FRONTWIPERSTATUS_FAILURE',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_387',
	'Signal' : 'BCM_FrontWiperStatus',
	'Value' : 3,
	'FaultID' : FaultID['FAULT_BCM_FRONTWIPERSTATUS_FAILURE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_FrontWiperStatus_ERR', 'code':'0xA13E08'}
}

FaultsDict['FAULT_DiagInfo_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_DiagInfo_INVALID'] = {
	'FaultName' : 'FAULT_DiagInfo_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_28C',
	'Signal' : 'GW_MFS_DiagInfoSW_28C',
	'Value' : [1, 2, 3],
	'FaultID' : FaultID['FAULT_DiagInfo_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_DiagInfo_ERROR', 'code':'0xA17081'}
}

FaultsDict['FAULT_DriverBuckleSwitchStatus_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_DriverBuckleSwitchStatus_INVALID'] = {
	'FaultName' : 'FAULT_DriverBuckleSwitchStatus_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_50',
	'Signal' : 'SRS_DriverBuckleSwitchStatus',
	'Value' : [2, 3],
	'FaultID' : FaultID['FAULT_DriverBuckleSwitchStatus_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_SRS_DriverBuckleSwitchStatus', 'code':'0xA13581'}
}

FaultsDict['FAULT_EMS_BrakePedalStatus'] = dict(FaultsDict)
FaultsDict['FAULT_EMS_BrakePedalStatus'] = {
	'FaultName' : 'FAULT_EMS_BrakePedalStatus',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_196',
	'Signal' : 'EMS_BrakePedalStatus',
	'Value' : [2, 3],
	'FaultID' : FaultID['FAULT_EMS_BrakePedalStatus'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_BrakePedal_ERROR', 'code':'0xA10181'}
}

FaultsDict['FAULT_EMS_TorqFailure_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_EMS_TorqFailure_INVALID'] = {
	'FaultName' : 'FAULT_EMS_TorqFailure_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_184',
	'Signal' : 'EMS_TorqFailure',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_EMS_TorqFailure_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_Torq_FAIL', 'code':'0xA10381'}
}

FaultsDict['FAULT_EPB_FAIL'] = dict(FaultsDict)
FaultsDict['FAULT_EPB_FAIL'] = {
	'FaultName' : 'FAULT_EPB_FAIL',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_197',
	'Signal' : 'EPB_Status',
	'Value' : 3,
	'FaultID' : FaultID['FAULT_EPB_FAIL'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10001, 'irr': 0b0},
	'DTC' : {'name':'DTC_EPB_FAIL', 'code':'0xA10681'}
}

FaultsDict['FAULT_EPB_FAIL_2'] = dict(FaultsDict)
FaultsDict['FAULT_EPB_FAIL_2'] = {
	'FaultName' : 'FAULT_EPB_FAIL_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_197',
	'Signal' : 'EPB_FailStatus',
	'Value' : [1, 2, 3],
	'FaultID' : FaultID['FAULT_EPB_FAIL'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10001, 'irr': 0b0},
	'DTC' : {'name':'DTC_EPB_FAIL', 'code':'0xA10681'}
}

FaultsDict['FAULT_EPB_SwitchPosition_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_EPB_SwitchPosition_INVALID'] = {
	'FaultName' : 'FAULT_EPB_SwitchPosition_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_197',
	'Signal' : 'EPB_SwitchPositionValid',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_EPB_SwitchPosition_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10001, 'irr': 0b0},
	'DTC' : {'name':'DTC_EPB_SwitchPosition_INVALID', 'code':'0xA10581'}
}

FaultsDict['FAULT_EPB_SwitchPosition_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_EPB_SwitchPosition_INVALID_2'] = {
	'FaultName' : 'FAULT_EPB_SwitchPosition_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_197',
	'Signal' : 'EPB_SwitchPosition',
	'Value' : 3,
	'FaultID' : FaultID['FAULT_EPB_SwitchPosition_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10001, 'irr': 0b0},
	'DTC' : {'name':'DTC_EPB_SwitchPosition_INVALID', 'code':'0xA10581'}
}

FaultsDict['FAULT_EPS_SteerAgSnsrCalSts_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_EPS_SteerAgSnsrCalSts_INVALID'] = {
	'FaultName' : 'FAULT_EPS_SteerAgSnsrCalSts_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_Calibrated',
	'Value' : 0x01,
	'FaultID' : FaultID['FAULT_EPS_SteerAgSnsrCalSts_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_SASCalibrated_FAIL', 'code':'0xA10754'}
}

FaultsDict['FAULT_EPS_SteeringAngleSpeed_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_EPS_SteeringAngleSpeed_INVALID'] = {
	'FaultName' : 'FAULT_EPS_SteeringAngleSpeed_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_SteeringAngleSpeed',
	'Value' : {'raw':0xFF},
	'FaultID' : FaultID['FAULT_EPS_SteeringAngleSpeed_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_SteeringAngleSpeed_ERROR', 'code':'0xA12881'}
}

FaultsDict['FAULT_EPS_SteeringAngleSpeed_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_EPS_SteeringAngleSpeed_INVALID_2'] = {
	'FaultName' : 'FAULT_EPS_SteeringAngleSpeed_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : 'cloneFault',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_SASFailure',
	'Value' : 0x01,
	'FaultID' : FaultID['FAULT_EPS_SteeringAngleSpeed_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_SteeringAngleSpeed_ERROR', 'code':'0xA12881'}
}

FaultsDict['FAULT_ESP_ABS_FAILURE'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_ABS_FAILURE'] = {
	'FaultName' : 'FAULT_ESP_ABS_FAILURE',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_187',
	'Signal' : 'ESP_ABSFailStatus',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_ESP_ABS_FAILURE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ABS_FAIL', 'code':'0xA13481'}
}

FaultsDict['FAULT_ESP_FltIndcn_CDD_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_FltIndcn_CDD_INVALID'] = {
	'FaultName' : 'FAULT_ESP_FltIndcn_CDD_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_CDD_Available',
	'Value' : 0x0,
	'FaultID' : FaultID['FAULT_ESP_FltIndcn_CDD_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10010, 'irr': 0b0},
	'DTC' : {'name':'DTC_CDD_NOT_AVAILABLE', 'code':'0xA11477'}
}

FaultsDict['FAULT_ESP_VEHICLESPEED_FAILURE'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_VEHICLESPEED_FAILURE'] = {
	'FaultName' : 'FAULT_ESP_VEHICLESPEED_FAILURE',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_187',
	'Signal' : 'ESP_VehicleSpeedValid',
	'Value' : 0x01,
	'FaultID' : FaultID['FAULT_ESP_VEHICLESPEED_FAILURE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_VehicleSpeed_INVALID', 'code':'0xA11681'}
}

FaultsDict['FAULT_ESP_VEHICLESPEED_FAILURE_2'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_VEHICLESPEED_FAILURE_2'] = {
	'FaultName' : 'FAULT_ESP_VEHICLESPEED_FAILURE_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_187',
	'Signal' : 'ESP_VehicleSpeed',
	'Value' : {'raw':0x1FFF},
	'FaultID' : FaultID['FAULT_ESP_VEHICLESPEED_FAILURE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_VehicleSpeed_INVALID', 'code':'0xA11681'}
}

FaultsDict['FAULT_ESP_VehStandstillIndcn_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_VehStandstillIndcn_INVALID'] = {
	'FaultName' : 'FAULT_ESP_VehStandstillIndcn_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_VehicleStandstill',
	'Value' : 0x03,
	'FaultID' : FaultID['FAULT_ESP_VehStandstillIndcn_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ESP_VehStandstillIndcn_INVALID', 'code':'0xA14381'}
}

FaultsDict['FAULT_ESP_WhlMovgDir_LF_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlMovgDir_LF_INVALID'] = {
	'FaultName' : 'FAULT_ESP_WhlMovgDir_LF_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_206',
	'Signal' : 'Wheel_Speed_FL_Direction',
	'Value' : 3,
	'FaultID' : FaultID['FAULT_ESP_WhlMovgDir_LF_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelDirection_INVALID', 'code':'0xA12D81'}
}

FaultsDict['FAULT_ESP_WhlMovgDir_RF_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlMovgDir_RF_INVALID'] = {
	'FaultName' : 'FAULT_ESP_WhlMovgDir_RF_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_206',
	'Signal' : 'Wheel_Speed_FR_Direction',
	'Value' : 3,
	'FaultID' : FaultID['FAULT_ESP_WhlMovgDir_RF_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelDirection_INVALID', 'code':'0xA12D81'}
}

FaultsDict['FAULT_ESP_WhlMovgDir_RL_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlMovgDir_RL_INVALID'] = {
	'FaultName' : 'FAULT_ESP_WhlMovgDir_RL_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : 'Wheel_Speed_RL_Direction',
	'Value' : 3,
	'FaultID' : FaultID['FAULT_ESP_WhlMovgDir_RL_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelDirection_INVALID', 'code':'0xA12D81'}
}

FaultsDict['FAULT_ESP_WhlMovgDir_RR_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlMovgDir_RR_INVALID'] = {
	'FaultName' : 'FAULT_ESP_WhlMovgDir_RR_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : 'Wheel_Speed_RR_Direction',
	'Value' :  0x3,
	'FaultID' : FaultID['FAULT_ESP_WhlMovgDir_RR_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelDirection_INVALID', 'code':'0xA12D81'}
}

FaultsDict['FAULT_ESP_WhlSpd_LF_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlSpd_LF_INVALID'] = {
	'FaultName' : 'FAULT_ESP_WhlSpd_LF_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_206',
	'Signal' : 'Wheel_Speed_FL_Valid_Data',
	'Value' : 0x1,
	'FaultID' : FaultID['FAULT_ESP_WhlSpd_LF_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelSpeed_INVALID', 'code':'0xA11581'}
}

FaultsDict['FAULT_ESP_WhlSpd_LF_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlSpd_LF_INVALID_2'] = {
	'FaultName' : 'FAULT_ESP_WhlSpd_LF_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_206',
	'Signal' : 'Wheel_Speed_FL_Data',
	'Value' : {'raw':0x1901}, #> 360 km/h
	'FaultID' : FaultID['FAULT_ESP_WhlSpd_LF_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelSpeed_INVALID', 'code':'0xA11581'}
}

FaultsDict['FAULT_ESP_WhlSpd_RF_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlSpd_RF_INVALID'] = {
	'FaultName' : 'FAULT_ESP_WhlSpd_RF_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_206',
	'Signal' : 'Wheel_Speed_FR_Valid_Data',
	'Value' : 0x1,
	'FaultID' : FaultID['FAULT_ESP_WhlSpd_RF_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelSpeed_INVALID', 'code':'0xA11581'}
}

FaultsDict['FAULT_ESP_WhlSpd_RF_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlSpd_RF_INVALID_2'] = {
	'FaultName' : 'FAULT_ESP_WhlSpd_RF_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : 'cloneFault',
	'MSG' : 'GW_206',
	'Signal' : 'Wheel_Speed_FR_Data',
	'Value' : {'raw':0x1901}, #> 360 km/h
	'FaultID' : FaultID['FAULT_ESP_WhlSpd_RF_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelSpeed_INVALID', 'code':'0xA11581'}
}

FaultsDict['FAULT_ESP_WhlSpd_RL_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlSpd_RL_INVALID'] = {
	'FaultName' : 'FAULT_ESP_WhlSpd_RL_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : 'Wheel_Speed_RL_Valid_Data',
	'Value' : 0x1,
	'FaultID' : FaultID['FAULT_ESP_WhlSpd_RL_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelSpeed_INVALID', 'code':'0xA11581'}
}

FaultsDict['FAULT_ESP_WhlSpd_RL_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlSpd_RL_INVALID_2'] = {
	'FaultName' : 'FAULT_ESP_WhlSpd_RL_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : 'Wheel_Speed_RL_Data',
	'Value' : {'raw':0x1901}, #> 360 km/h
	'FaultID' : FaultID['FAULT_ESP_WhlSpd_RL_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelSpeed_INVALID', 'code':'0xA11581'}
}

FaultsDict['FAULT_ESP_WhlSpd_RR_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlSpd_RR_INVALID'] = {
	'FaultName' : 'FAULT_ESP_WhlSpd_RR_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : 'Wheel_Speed_RR_Valid_Data',
	'Value' : 0x1,
	'FaultID' : FaultID['FAULT_ESP_WhlSpd_RR_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelSpeed_INVALID', 'code':'0xA11581'}
}

FaultsDict['FAULT_ESP_WhlSpd_RR_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_ESP_WhlSpd_RR_INVALID_2'] = {
	'FaultName' : 'FAULT_ESP_WhlSpd_RR_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_208',
	'Signal' : 'Wheel_Speed_RR_Data',
	'Value' : {'raw':0x1901}, #> 360 km/h
	'FaultID' : FaultID['FAULT_ESP_WhlSpd_RR_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_WheelSpeed_INVALID', 'code':'0xA11581'}
}

FaultsDict['FAULT_EngineSpeed_ERROR'] = dict(FaultsDict)
FaultsDict['FAULT_EngineSpeed_ERROR'] = {
	'FaultName' : 'FAULT_EngineSpeed_ERROR',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_196',
	'Signal' : 'EMS_EngineSpeedError',
	'Value' : 0x01,
	'FaultID' : FaultID['FAULT_EngineSpeed_ERROR'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_EngineSpeed_ERROR', 'code':'0xA10081'}
}

FaultsDict['FAULT_EngineSpeed_ERROR_2'] = dict(FaultsDict)
FaultsDict['FAULT_EngineSpeed_ERROR_2'] = {
	'FaultName' : 'FAULT_EngineSpeed_ERROR_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_196',
	'Signal' : 'EMS_EngineSpeed',
	'Value' : {'raw':0xFFFF},
	'FaultID' : FaultID['FAULT_EngineSpeed_ERROR'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_EngineSpeed_ERROR', 'code':'0xA10081'}
}

FaultsDict['FAULT_EngineStatus_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_EngineStatus_INVALID'] = {
	'FaultName' : 'FAULT_EngineStatus_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A6',
	'Signal' : 'EMS_EngineStatus',
	'Value' :  0x3,
	'FaultID' : FaultID['FAULT_EngineStatus_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_EngineStatus_INVALID', 'code':'0xA13381'}
}

FaultsDict['FAULT_EnvironmentalTemp_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_EnvironmentalTemp_INVALID'] = {
	'FaultName' : 'FAULT_EnvironmentalTemp_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_366',
	'Signal' : 'AC_EnvironmentalTempVD',
	'Value' : 0x01,
	'FaultID' : FaultID['FAULT_EnvironmentalTemp_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_EnvironmentalTemp_INVALID', 'code':'0xA13981'}
}

FaultsDict['FAULT_EnvironmentalTemp_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_EnvironmentalTemp_INVALID_2'] = {
	'FaultName' : 'FAULT_EnvironmentalTemp_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_366',
	'Signal' : 'AC_EnvironmentalTemp',
	'Value' : {'raw':0xFF},
	'FaultID' : FaultID['FAULT_EnvironmentalTemp_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_EnvironmentalTemp_INVALID', 'code':'0xA13981'}
}

FaultsDict['FAULT_FrictionalTorq_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_FrictionalTorq_INVALID'] = {
	'FaultName' : 'FAULT_FrictionalTorq_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_184',
	'Signal' : 'EMS_FrictionalTorq',
	'Value' : {'raw':0xFFFF},
	'FaultID' : FaultID['FAULT_FrictionalTorq_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_Torq_INVALID', 'code':'0xA12C81'}
}

FaultsDict['FAULT_IP_DIS_FAIL'] = dict(FaultsDict)
FaultsDict['FAULT_IP_DIS_FAIL'] = {
	'FaultName' : 'FAULT_IP_DIS_FAIL',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_2DE',
	'Signal' : 'IP_DISFail',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_IP_DIS_FAIL'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_IP_DIS_FAIL', 'code':'0xA16181'}
}

FaultsDict['FAULT_IndicatedDriverReqTorq_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_IndicatedDriverReqTorq_INVALID'] = {
	'FaultName' : 'FAULT_IndicatedDriverReqTorq_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_184',
	'Signal' : 'EMS_IndicatedDriverReqTorq',
	'Value' : {'raw':0xFFFF},
	'FaultID' : FaultID['FAULT_IndicatedDriverReqTorq_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_Torq_INVALID', 'code':'0xA12C81'}
}

FaultsDict['FAULT_IndicatedRealEngTorq_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_IndicatedRealEngTorq_INVALID'] = {
	'FaultName' : 'FAULT_IndicatedRealEngTorq_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_184',
	'Signal' : 'EMS_IndicatedRealEngTorq',
	'Value' : {'raw':0xFFFF},
	'FaultID' : FaultID['FAULT_IndicatedRealEngTorq_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_Torq_INVALID', 'code':'0xA12C81'}
}

FaultsDict['FAULT_MaxIndicatedTorq_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_MaxIndicatedTorq_INVALID'] = {
	'FaultName' : 'FAULT_MaxIndicatedTorq_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A6',
	'Signal' : 'EMS_MaxIndicatedTorq',
	'Value' : {'raw':0xFF},
	'FaultID' : FaultID['FAULT_MaxIndicatedTorq_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_Torq_INVALID', 'code':'0xA12C81'}
}

FaultsDict['FAULT_MinIndicatedTorq_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_MinIndicatedTorq_INVALID'] = {
	'FaultName' : 'FAULT_MinIndicatedTorq_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A6',
	'Signal' : 'EMS_MinIndicatedTorq',
	'Value' : {'raw':0xFF},
	'FaultID' : FaultID['FAULT_MinIndicatedTorq_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_Torq_INVALID', 'code':'0xA12C81'}
}

FaultsDict['FAULT_PRI_VFC_SensorState_VisionFault'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_SensorState_VisionFault'] = {
	'FaultName' : 'FAULT_PRI_VFC_SensorState_VisionFault',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_SensorState',
	'Signal' : 'VFC_SensorState_VisionFault',
	'Value' : [3, 4, 5, 6],
	'FaultID' : FaultID['FAULT_PRI_VFC_SensorState_VisionFault'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_SensorState_VisionFault', 'code':'0xA14681'}
}

FaultsDict['FAULT_QDCACC_FAIL'] = dict(FaultsDict)
FaultsDict['FAULT_QDCACC_FAIL'] = {
	'FaultName' : 'FAULT_QDCACC_FAIL',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_QDCACC',
	'Value' : [1, 2, 3],
	'FaultID' : FaultID['FAULT_QDCACC_FAIL'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10001, 'irr': 0b0},
	'DTC' : {'name':'DTC_QDCACC_FAIL', 'code':'0xA11708'}
}

FaultsDict['FAULT_QDashACC_FAIL'] = dict(FaultsDict)
FaultsDict['FAULT_QDashACC_FAIL'] = {
	'FaultName' : 'FAULT_QDashACC_FAIL',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_2DE',
	'Signal' : 'IP_QDashACCFail',
	'Value' : [1, 2, 3],
	'FaultID' : FaultID['FAULT_QDashACC_FAIL'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_QDashACC_FAIL', 'code':'0xA16081'}
}

FaultsDict['FAULT_QECACC_FAIL'] = dict(FaultsDict)
FaultsDict['FAULT_QECACC_FAIL'] = {
	'FaultName' : 'FAULT_QECACC_FAIL',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_26A',
	'Signal' : 'EMS_QECACC',
	'Value' : [1, 2, 3],
	'FaultID' : FaultID['FAULT_QECACC_FAIL'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_QECACC_FAIL', 'code':'0xA12408'}
}

FaultsDict['FAULT_RESPlus_ERROR'] = dict(FaultsDict)
FaultsDict['FAULT_RESPlus_ERROR'] = {
	'FaultName' : 'FAULT_RESPlus_ERROR',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_28C',
	'Signal' : 'GW_MFS_RESPlus_switch_signal',
	'Value' : [2, 3],
	'FaultID' : FaultID['FAULT_RESPlus_ERROR'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_RESPlus_ERROR', 'code':'0xA16981'}
}

FaultsDict['FAULT_SAS_Failure'] = dict(FaultsDict)
FaultsDict['FAULT_SAS_Failure'] = {
	'FaultName' : 'FAULT_SAS_Failure',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : 'IgnoreErrorPosition',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_SASFailure',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_SAS_Failure'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_SAS_FAIL', 'code':'0xA10881'}
}

FaultsDict['FAULT_SAS_SteerWhlAgSig_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_SAS_SteerWhlAgSig_INVALID'] = {
	'FaultName' : 'FAULT_SAS_SteerWhlAgSig_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_SteeringAngleValid',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_SAS_SteerWhlAgSig_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_SteeringAngle_INVALID', 'code':'0xA14481'}
}

FaultsDict['FAULT_SAS_SteerWhlAgSig_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_SAS_SteerWhlAgSig_INVALID_2'] = {
	'FaultName' : 'FAULT_SAS_SteerWhlAgSig_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_SteeringAngle',
	'Value' : {'raw':0x1E79}, #SAS_SteeringAngle < -780° or SAS_SteeringAngle > 780°
	'FaultID' : FaultID['FAULT_SAS_SteerWhlAgSig_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_SteeringAngle_INVALID', 'code':'0xA14481'}
}

FaultsDict['FAULT_SAS_SteerWhlAgSig_INVALID_3'] = dict(FaultsDict)
FaultsDict['FAULT_SAS_SteerWhlAgSig_INVALID_3'] = {
	'FaultName' : 'FAULT_SAS_SteerWhlAgSig_INVALID_3',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : 'cloneFault',
	'MSG' : 'GW_180',
	'Signal' : 'SAS_SASFailure',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_SAS_SteerWhlAgSig_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 5,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011100001, 'irr': 0b0},
	'DTC' : {'name':'DTC_SteeringAngle_INVALID', 'code':'0xA14481'}
}
FaultsDict['FAULT_ShiftinProgress_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_ShiftinProgress_INVALID'] = {
	'FaultName' : 'FAULT_ShiftinProgress_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_188',
	'Signal' : 'TCU_ShiftinProgressValid',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_ShiftinProgress_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ShiftinProgress_INVALID', 'code':'0xA12B81'}
}

FaultsDict['FAULT_TCSVDC_FAIL'] = dict(FaultsDict)
FaultsDict['FAULT_TCSVDC_FAIL'] = {
	'FaultName' : 'FAULT_TCSVDC_FAIL',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_187',
	'Signal' : 'ESP_TCSFailStatus',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_TCSVDC_FAIL'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_TCSVDC_FAIL', 'code':'0xA12081'}
}

FaultsDict['FAULT_TCU_ACTUALGEARPOSITION_FAILURE'] = dict(FaultsDict)
FaultsDict['FAULT_TCU_ACTUALGEARPOSITION_FAILURE'] = {
	'FaultName' : 'FAULT_TCU_ACTUALGEARPOSITION_FAILURE',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A8',
	'Signal' : 'TCU_ActualGearValid',
	'Value' : [1, 0xF],
	'FaultID' : FaultID['FAULT_TCU_ACTUALGEARPOSITION_FAILURE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_ActualGear_INVALID', 'code':'0xA12281'}
}

FaultsDict['FAULT_TCU_SHIFTPOSITION_FAILURE'] = dict(FaultsDict)
FaultsDict['FAULT_TCU_SHIFTPOSITION_FAILURE'] = {
	'FaultName' : 'FAULT_TCU_SHIFTPOSITION_FAILURE',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A8',
	'Signal' : 'TCU_ShiftPostionValid',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_TCU_SHIFTPOSITION_FAILURE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_GearShiftPosition_INVALID', 'code':'0xA12A77'}
}

FaultsDict['FAULT_TCU_SHIFTPOSITION_FAILURE_2'] = dict(FaultsDict)
FaultsDict['FAULT_TCU_SHIFTPOSITION_FAILURE_2'] = {
	'FaultName' : 'FAULT_TCU_SHIFTPOSITION_FAILURE_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A8',
	'Signal' : 'TCU_GearShiftPosition',
	'Value' : [8,9, 15],
	'FaultID' : FaultID['FAULT_TCU_SHIFTPOSITION_FAILURE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11001001, 'irr': 0b0},
	'DTC' : {'name':'DTC_GearShiftPosition_INVALID', 'code':'0xA12A77'}
}

FaultsDict['FAULT_TorqueConstant_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_TorqueConstant_INVALID'] = {
	'FaultName' : 'FAULT_TorqueConstant_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_1A6',
	'Signal' : 'EMS_TorqueConstant',
	'Value' : {'raw':0xFF},
	'FaultID' : FaultID['FAULT_TorqueConstant_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 14,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1001, 'irr': 0b0},
	'DTC' : {'name':'DTC_Torq_INVALID', 'code':'0xA12C81'}
}

FaultsDict['FAULT_YRS_LatAcce_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_YRS_LatAcce_INVALID'] = {
	'FaultName' : 'FAULT_YRS_LatAcce_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_278',
	'Signal' : 'ESP_LatAccel',
	'Value' : {'raw':0xFF},
	'FaultID' : FaultID['FAULT_YRS_LatAcce_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_LatAccel_INVALID', 'code':'0xA11381'}
}

FaultsDict['FAULT_YRS_LgtAcce_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_YRS_LgtAcce_INVALID'] = {
	'FaultName' : 'FAULT_YRS_LgtAcce_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_278',
	'Signal' : 'ESP_LongAccel',
	'Value' : {'raw':0x3FFF},
	'FaultID' : FaultID['FAULT_YRS_LgtAcce_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_LongAccel_INVALID', 'code':'0xA11281'}
}

FaultsDict['FAULT_YRS_YawRate_INVALID'] = dict(FaultsDict)
FaultsDict['FAULT_YRS_YawRate_INVALID'] = {
	'FaultName' : 'FAULT_YRS_YawRate_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_278',
	'Signal' : 'ESP_YawRate',
	'Value' : {'raw':0x3FFF},
	'FaultID' : FaultID['FAULT_YRS_YawRate_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_YawRate_INVALID', 'code':'0xA11081'}
}

FaultsDict['FAULT_YRS_YawRate_INVALID_2'] = dict(FaultsDict)
FaultsDict['FAULT_YRS_YawRate_INVALID_2'] = {
	'FaultName' : 'FAULT_YRS_YawRate_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_278',
	'Signal' : 'ESP_YawRateValid',
	'Value' : 1,
	'FaultID' : FaultID['FAULT_YRS_YawRate_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1100111110000000011010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_YawRate_INVALID', 'code':'0xA11081'}
}

FaultsDict['Fault_ESP_ABAavailable_INVALID'] = dict(FaultsDict)
FaultsDict['Fault_ESP_ABAavailable_INVALID'] = {
	'FaultName' : 'Fault_ESP_ABAavailable_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_ABAavailable',
	'Value' : 0,
	'FaultID' : FaultID['Fault_ESP_ABAavailable_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VAFs_DEGRADATION', 'code':'0xA11881'}
}

FaultsDict['Fault_ESP_AEBAvailable_INVALID'] = dict(FaultsDict)
FaultsDict['Fault_ESP_AEBAvailable_INVALID'] = {
	'FaultName' : 'Fault_ESP_AEBAvailable_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_AEBAvailable',
	'Value' : 0x0,
	'FaultID' : FaultID['Fault_ESP_AEBAvailable_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b1000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VAFs_DEGRADATION', 'code':'0xA11881'}
}

FaultsDict['Fault_ESP_AWBavailable_INVALID'] = dict(FaultsDict)
FaultsDict['Fault_ESP_AWBavailable_INVALID'] = {
	'FaultName' : 'Fault_ESP_AWBavailable_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_AWBavailable',
	'Value' : 0x0,
	'FaultID' : FaultID['Fault_ESP_AWBavailable_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b10000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VAFs_DEGRADATION', 'code':'0xA11881'}
}

FaultsDict['Fault_ESP_MasCylBrakePressure_INVALID'] = dict(FaultsDict)
FaultsDict['Fault_ESP_MasCylBrakePressure_INVALID'] = {
	'FaultName' : 'Fault_ESP_MasCylBrakePressure_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_258',
	'Signal' : 'ESP_MasCylBrakePressureValid',
	'Value' : 0x01,
	'FaultID' : FaultID['Fault_ESP_MasCylBrakePressure_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_MasCylBrakePressure_INVALID', 'code':'0xA11981'}
}

FaultsDict['Fault_ESP_MasCylBrakePressure_INVALID_2'] = dict(FaultsDict)
FaultsDict['Fault_ESP_MasCylBrakePressure_INVALID_2'] = {
	'FaultName' : 'Fault_ESP_MasCylBrakePressure_INVALID_2',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_258',
	'Signal' : 'ESP_MasCylBrakePressure',
	'Value' : {'raw':0xFFF},
	'FaultID' : FaultID['Fault_ESP_MasCylBrakePressure_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b11010001, 'irr': 0b0},
	'DTC' : {'name':'DTC_MasCylBrakePressure_INVALID', 'code':'0xA11981'}
}

FaultsDict['Fault_ESP_PrefillAvailable_INVALID'] = dict(FaultsDict)
FaultsDict['Fault_ESP_PrefillAvailable_INVALID'] = {
	'FaultName' : 'Fault_ESP_PrefillAvailable_INVALID',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'Signal',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'GW_277',
	'Signal' : 'ESP_PrefillAvailable',
	'Value' : 0x0,
	'FaultID' : FaultID['Fault_ESP_PrefillAvailable_INVALID'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 7,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'DTC_VAFs_DEGRADATION', 'code':'0xA11881'}
}

################## Platform ##################
FaultsDict['CANSM_E_BUSOFF_PCAN'] = dict(FaultsDict)
FaultsDict['CANSM_E_BUSOFF_PCAN'] = {
	'FaultName' : 'CANSM_E_BUSOFF_PCAN',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_1',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['CANSM_E_BUSOFF_PCAN'.upper()],
	'FaultType' : 'Unrecoverable',
	'EDT' : 250.0,
	'EHT' : 0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100111110000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_CAN_BUSOFF_PCAN', 'code':'0xD97300'}
}

FaultsDict['CANSM_E_BUSOFF_SFCAN'] = dict(FaultsDict)
FaultsDict['CANSM_E_BUSOFF_SFCAN'] = {
	'FaultName' : 'CANSM_E_BUSOFF_SFCAN',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_1',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['CANSM_E_BUSOFF_SFCAN'.upper()],
	'FaultType' : 'Unrecoverable',
	'EDT' : 250.0,
	'EHT' : 0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_CAN_BUSOFF_SFCAN', 'code':'0xD97388'}
}

FaultsDict['FAULT_ALIGNMENT_NEVER_DONE'] = dict(FaultsDict)
FaultsDict['FAULT_ALIGNMENT_NEVER_DONE'] = {
	'FaultName' : 'FAULT_ALIGNMENT_NEVER_DONE',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ALIGNMENT_NEVER_DONE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100001100000000011000110, 'irr': 0b0},
	'DTC' : {'name':'DTC_ALIGNMENT_NEVER_DONE', 'code':'0xA13178'}
}

FaultsDict['FAULT_ALIGNMENT_NOT_OK'] = dict(FaultsDict)
FaultsDict['FAULT_ALIGNMENT_NOT_OK'] = {
	'FaultName' : 'FAULT_ALIGNMENT_NOT_OK',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_ALIGNMENT_NOT_OK'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100001100000000011000110, 'irr': 0b0},
	'DTC' : {'name':'DTC_ALIGNMENT_NOT_OK', 'code':'0xA13278'}
}

FaultsDict['FAULT_BLINDNESS_ABSORPTION'] = dict(FaultsDict)
FaultsDict['FAULT_BLINDNESS_ABSORPTION'] = {
	'FaultName' : 'FAULT_BLINDNESS_ABSORPTION',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_BLINDNESS_ABSORPTION'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100001010000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_RADAR_BLIND', 'code':'0xA12604'}
}

FaultsDict['FAULT_BLINDNESS_DISTORTION'] = dict(FaultsDict)
FaultsDict['FAULT_BLINDNESS_DISTORTION'] = {
	'FaultName' : 'FAULT_BLINDNESS_DISTORTION',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_BLINDNESS_DISTORTION'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100001010000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_RADAR_BLIND', 'code':'0xA12604'}
}

FaultsDict['FAULT_HV_SERVICE_OOS'] = dict(FaultsDict)
FaultsDict['FAULT_HV_SERVICE_OOS'] = {
	'FaultName' : 'FAULT_HV_SERVICE_OOS',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_HV_SERVICE_OOS'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'NODTC', 'code':''}
}

FaultsDict['FAULT_HV_VELOCITY_TIRE_SIZE_ALIGNMENT_UNSTEADY'] = dict(FaultsDict)
FaultsDict['FAULT_HV_VELOCITY_TIRE_SIZE_ALIGNMENT_UNSTEADY'] = {
	'FaultName' : 'FAULT_HV_VELOCITY_TIRE_SIZE_ALIGNMENT_UNSTEADY',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_HV_VELOCITY_TIRE_SIZE_ALIGNMENT_UNSTEADY'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100101000000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_DACORE_OOS', 'code':'0xA1A586'}
}

FaultsDict['FAULT_HV_YAW_RATE_OFFSET_NOT_CONFIRMED'] = dict(FaultsDict)
FaultsDict['FAULT_HV_YAW_RATE_OFFSET_NOT_CONFIRMED'] = {
	'FaultName' : 'FAULT_HV_YAW_RATE_OFFSET_NOT_CONFIRMED',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_HV_YAW_RATE_OFFSET_NOT_CONFIRMED'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100101010000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_DACORE_OOS', 'code':'0xA1A586'}
}

FaultsDict['FAULT_MISALIGNMENT_HORIZONTAL_ABSOLUTE_EVENT'] = dict(FaultsDict)
FaultsDict['FAULT_MISALIGNMENT_HORIZONTAL_ABSOLUTE_EVENT'] = {
	'FaultName' : 'FAULT_MISALIGNMENT_HORIZONTAL_ABSOLUTE_EVENT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_MISALIGNMENT_HORIZONTAL_ABSOLUTE_EVENT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100000000000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_RADAR_MISALIGNED', 'code':'0xA12578'}
}

FaultsDict['FAULT_MISALIGNMENT_HORIZONTAL_RELATIVE_EVENT'] = dict(FaultsDict)
FaultsDict['FAULT_MISALIGNMENT_HORIZONTAL_RELATIVE_EVENT'] = {
	'FaultName' : 'FAULT_MISALIGNMENT_HORIZONTAL_RELATIVE_EVENT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_MISALIGNMENT_HORIZONTAL_RELATIVE_EVENT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100000000000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_RADAR_MISALIGNED', 'code':'0xA12578'}
}

FaultsDict['FAULT_MISALIGNMENT_VERTICAL_ABSOLUTE_EVENT'] = dict(FaultsDict)
FaultsDict['FAULT_MISALIGNMENT_VERTICAL_ABSOLUTE_EVENT'] = {
	'FaultName' : 'FAULT_MISALIGNMENT_VERTICAL_ABSOLUTE_EVENT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_MISALIGNMENT_VERTICAL_ABSOLUTE_EVENT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100000000000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_RADAR_MISALIGNED', 'code':'0xA12578'}
}

FaultsDict['FAULT_MISALIGNMENT_VERTICAL_RELATIVE_EVENT'] = dict(FaultsDict)
FaultsDict['FAULT_MISALIGNMENT_VERTICAL_RELATIVE_EVENT'] = {
	'FaultName' : 'FAULT_MISALIGNMENT_VERTICAL_RELATIVE_EVENT',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_MISALIGNMENT_VERTICAL_RELATIVE_EVENT'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100000000000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_RADAR_MISALIGNED', 'code':'0xA12578'}
}

FaultsDict['FAULT_PER_ENV_MODEL_SERVICE_OOS'] = dict(FaultsDict)
FaultsDict['FAULT_PER_ENV_MODEL_SERVICE_OOS'] = {
	'FaultName' : 'FAULT_PER_ENV_MODEL_SERVICE_OOS',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PER_ENV_MODEL_SERVICE_OOS'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100000000000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_DACORE_OOS', 'code':'0xA1A586'}
}

FaultsDict['FAULT_PER_ENV_MODEL_SERVICE_QM'] = dict(FaultsDict)
FaultsDict['FAULT_PER_ENV_MODEL_SERVICE_QM'] = {
	'FaultName' : 'FAULT_PER_ENV_MODEL_SERVICE_QM',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PER_ENV_MODEL_SERVICE_QM'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'NODTC', 'code':''}
}

FaultsDict['FAULT_PRODUCTION_MODE_ACTIVE'] = dict(FaultsDict)
FaultsDict['FAULT_PRODUCTION_MODE_ACTIVE'] = {
	'FaultName' : 'FAULT_PRODUCTION_MODE_ACTIVE',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRODUCTION_MODE_ACTIVE'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b1100101100000000011000110, 'irr': 0b0},
	'DTC' : {'name':'DTC_PRODUCTION_MODE_ACTIVE', 'code':'0xA12F06'}
}

FaultsDict['FAULT_RPM_EXECUTION_SERVICE_OOS'] = dict(FaultsDict)
FaultsDict['FAULT_RPM_EXECUTION_SERVICE_OOS'] = {
	'FaultName' : 'FAULT_RPM_EXECUTION_SERVICE_OOS',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_RPM_EXECUTION_SERVICE_OOS'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_DACORE_OOS', 'code':'0xA1A586'}
}

FaultsDict['FAULT_RPM_EXECUTION_SERVICE_QM'] = dict(FaultsDict)
FaultsDict['FAULT_RPM_EXECUTION_SERVICE_QM'] = {
	'FaultName' : 'FAULT_RPM_EXECUTION_SERVICE_QM',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_RPM_EXECUTION_SERVICE_QM'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'NODTC', 'code':''}
}

FaultsDict['FAULT_SENSOR_ABSORPTION'] = dict(FaultsDict)
FaultsDict['FAULT_SENSOR_ABSORPTION'] = {
	'FaultName' : 'FAULT_SENSOR_ABSORPTION',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_SENSOR_ABSORPTION'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'NODTC', 'code':''}
}

FaultsDict['FAULT_SENSOR_DISTORTION'] = dict(FaultsDict)
FaultsDict['FAULT_SENSOR_DISTORTION'] = {
	'FaultName' : 'FAULT_SENSOR_DISTORTION',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_5',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_SENSOR_DISTORTION'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'NODTC', 'code':''}
}

FaultsDict['FAULT_SIT_BC_SERVICE_OOS'] = dict(FaultsDict)
FaultsDict['FAULT_SIT_BC_SERVICE_OOS'] = {
	'FaultName' : 'FAULT_SIT_BC_SERVICE_OOS',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_SIT_BC_SERVICE_OOS'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b100000000000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_DACORE_OOS', 'code':'0xA1A586'}
}

FaultsDict['FAULT_SIT_BC_SERVICE_QM'] = dict(FaultsDict)
FaultsDict['FAULT_SIT_BC_SERVICE_QM'] = {
	'FaultName' : 'FAULT_SIT_BC_SERVICE_QM',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_SIT_BC_SERVICE_QM'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'NODTC', 'code':''}
}

FaultsDict['FAULT_SIT_BS_SERVICE_OOS'] = dict(FaultsDict)
FaultsDict['FAULT_SIT_BS_SERVICE_OOS'] = {
	'FaultName' : 'FAULT_SIT_BS_SERVICE_OOS',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_SIT_BS_SERVICE_OOS'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b100000000000000011000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_DACORE_OOS', 'code':'0xA1A586'}
}

FaultsDict['FAULT_SIT_BS_SERVICE_QM'] = dict(FaultsDict)
FaultsDict['FAULT_SIT_BS_SERVICE_QM'] = {
	'FaultName' : 'FAULT_SIT_BS_SERVICE_QM',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_SIT_BS_SERVICE_QM'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b0, 'irr': 0b0},
	'DTC' : {'name':'NODTC', 'code':''}
}

FaultsDict['FAULT_VBAT_HIGH'] = dict(FaultsDict)
FaultsDict['FAULT_VBAT_HIGH'] = {
	'FaultName' : 'FAULT_VBAT_HIGH',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_8',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VBAT_HIGH'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 500.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_VBAT_HIGH', 'code':'0xD70017'}
}

FaultsDict['FAULT_VBAT_LOW'] = dict(FaultsDict)
FaultsDict['FAULT_VBAT_LOW'] = {
	'FaultName' : 'FAULT_VBAT_LOW',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_8',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VBAT_LOW'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 500.0,
	'EHT' : 500.0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_VBAT_LOW', 'code':'0xD70016'}
}

FaultsDict['FAULT_VMC_CorridorLongitudinalComfort_StatusCheck'] = dict(FaultsDict)
FaultsDict['FAULT_VMC_CorridorLongitudinalComfort_StatusCheck'] = {
	'FaultName' : 'FAULT_VMC_CorridorLongitudinalComfort_StatusCheck',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VMC_CorridorLongitudinalComfort_StatusCheck'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : 3,
	'DEM_EHT' : 1,
	'SysReaction' : {'reaction': 0b101, 'irr': 0b0},
	'DTC' : {'name':'DTC_VMC_ERROR', 'code':'0xA12981'}
}
FaultsDict['FAULT_VMC_Variant_ERROR'] = dict(FaultsDict)
FaultsDict['FAULT_VMC_Variant_ERROR'] = {
	'FaultName' : 'FAULT_VMC_Variant_ERROR',
	'Variant' : ['NE15TGAB_21', 'NE15TGAC_22'],
	'Type' : 'PF_x',
	'EC' : 'ECG_4',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : '',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_VMC_Variant_ERROR'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : None,
	'EHT' : None,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11000101, 'irr': 0b0},
	'DTC' : {'name':'DTC_VMC_ERROR', 'code':'0xA12981'}
}

################## Platform Bosch ##################
################## Others ##################
FaultsDict['FAULT_PRI_VFC_LineInfo_BlockCounter_Error'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_LineInfo_BlockCounter_Error'] = {
	'FaultName' : 'FAULT_PRI_VFC_LineInfo_BlockCounter_Error',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'BLK',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_0x89',
	'Signal' : '',
	'Value' : None,
	'FaultID' : FaultID['FAULT_PRI_VFC_LineInfo_BlockCounter_Error'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 240,
	'EHT' : 0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_LineInfo_BlockCounter_Error', 'code':'0xD97168'}
}

FaultsDict['FAULT_PRI_VFC_ObjectInfo_BlockCounter_Error'] = dict(FaultsDict)
FaultsDict['FAULT_PRI_VFC_ObjectInfo_BlockCounter_Error'] = {
	'FaultName' : 'FAULT_PRI_VFC_ObjectInfo_BlockCounter_Error',
	'Variant' : ['NE15TGAC_22'],
	'Type' : 'BLK',
	'EC' : 'ECG_3',
	'Conditions' : '',
	'ExtendedOptions' : '',
	'MSG' : 'VFC_SensorState',
	'Signal' : 'VFC_SensorState_VisionFault',
	'Value' : 7,
	'FaultID' : FaultID['FAULT_PRI_VFC_ObjectInfo_BlockCounter_Error'.upper()],
	'FaultType' : 'Recoverable',
	'EDT' : 240,
	'EHT' : 0,
	'DEM_EDT' : None,
	'DEM_EHT' : None,
	'SysReaction' : {'reaction': 0b11000000000000000000000, 'irr': 0b0},
	'DTC' : {'name':'DTC_VFC_ObjectInfo_BlockCounter_Error', 'code':'0xD97068'}
}
