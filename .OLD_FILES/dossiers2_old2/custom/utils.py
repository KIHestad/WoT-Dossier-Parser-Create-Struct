# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
# Embedded file name: scripts/common/dossiers2/custom/utils.py
from items import vehicles
import arena_achievements

def getVehicleNationID(vehTypeCompDescr):
    return vehicles.parseIntCompactDescr(vehTypeCompDescr)[1]


def isVehicleSPG(vehTypeCompDescr):
    itemTypeID, nationID, vehicleID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
    return 'SPG' in vehicles.g_list.getList(nationID)[vehicleID].tags


def getInBattleSeriesIndex(seriesName):
    return arena_achievements.INBATTLE_SERIES_INDICES[seriesName]