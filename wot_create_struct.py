##################################################
##  WoT create structures                       ##
##  Current version for WoT 9.20                ##
##                                              ##
##  Originally made by Phalynx at vBAddict      ##
##  Current version by BadButton at Wot Numbers ##
##################################################

import cPickle, struct, json, time, sys, os
from dossiers2.custom.records import *
from dossiers2.custom.battle_statistics_layouts import *
from dossiers2.custom.account_layout import *
from dossiers2.custom.vehicle_layout import COMPENSATION_BLOCK_LAYOUT, ACHIEVEMENTS15X15_BLOCK_LAYOUT

def main():
	createStructures()
	#sys.exit(1)

	
def getStructNumber():
    # Must be updated according to return value from the last method named "__updateFromVehicleDossierXX()" 
    # This method is found in file .\custom\updaters.py
    return 99 


def createStructures():
	# The list blocks[] must be updated according to the list blocksLayout[] from the last method named "__updateFromVehicleDossierXX()" 
    # The blocksLayout[] list is to be used as template for the list below, and is found in file .\custom\updaters.py
	
    # This list includes categories to be included in the struct, and the relevant layout-list for getting record from "record.py" in correct order
    # Sntax: List of ('categoryname', LIST_NAME_LAYOUT)
	blocks = [
		('a15x15', A15X15_BLOCK_LAYOUT),
        ('a15x15_2', A15X15_2_BLOCK_LAYOUT), 
        ('clan', CLAN_BLOCK_LAYOUT), 
        ('clan2', CLAN2_BLOCK_LAYOUT), 
        ('company', COMPANY_BLOCK_LAYOUT), 
        ('company2', COMPANY2_BLOCK_LAYOUT), 
        ('a7x7', A7X7_BLOCK_LAYOUT), 
        ('achievements', ACHIEVEMENTS15X15_BLOCK_LAYOUT), 
        ('total', TOTAL_BLOCK_LAYOUT), 
        ('max15x15', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT), 
        ('max7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT), 
        ('compensation',  COMPENSATION_BLOCK_LAYOUT), 
        ('achievements7x7', ACHIEVEMENTS7X7_BLOCK_LAYOUT), 
        ('historical', HISTORICAL_BLOCK_LAYOUT), 
        ('maxHistorical', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT), 
        ('uniqueAchievements', UNIQUE_ACHIEVEMENT_VALUES), 
        ('fortBattles', FORT_BLOCK_LAYOUT), 
        ('maxFortBattles', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT), 
        ('fortSorties', FORT_BLOCK_LAYOUT), 
        ('maxFortSorties', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT), 
        ('fortAchievements', FORT_ACHIEVEMENTS_BLOCK_LAYOUT), 
        ('singleAchievements', SINGLE_ACHIEVEMENTS_VALUES), 
        ('clanAchievements', CLAN_ACHIEVEMENTS_BLOCK_LAYOUT), 
        ('rated7x7', RATED_7X7_BLOCK_LAYOUT), 
        ('maxRated7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT), 
        ('globalMapCommon', GLOBAL_MAP_BLOCK_LAYOUT), 
        ('maxGlobalMapCommon', MAX_BLOCK_LAYOUT), 
        ('fallout', FALLOUT_BLOCK_LAYOUT), 
        ('maxFallout', MAX_FALLOUT_BLOCK_LAYOUT), 
        ('falloutAchievements', FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT), 
        ('ranked', RANKED_BLOCK_LAYOUT), 
        ('maxRanked', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT), 
        ('a30x30', A30X30_BLOCK_LAYOUT), 
        ('max30x30', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT), 
	]
	
	# get relevant records to process, in correct order according to layout
	structures = []
	r_version = getStructNumber()
    # loop through blocks
	for block in blocks:
        # get category
		r_offset = 0
		category = block[0]
        # loop through layout
		for record in block[1]:
            # get from records according to category and record name
			newrecord = getRecord(category, record)
			if newrecord != None:
				# get length of datatype
				r_length = struct.calcsize('<' + newrecord[3])
				# Debug output
				print newrecord[0], newrecord[1], r_offset, r_length
				# create structure now
				structure = {"category": newrecord[0], "name": newrecord[1], "offset": r_offset, "length": r_length, "version": r_version}
				structures.append(structure)
				# add to offset for next record
				r_offset += r_length

	# Write to file
	logFile = open("structures_" + str(r_version) + ".json ", "w")
	logFile.write(json.dumps(structures, sort_keys=True)) # all in one line
    #logFile.write(json.dumps(structures, sort_keys=True, indent=4)) # line breaks and indent
	logFile.close()


def getRecord(category, recordname):
    record = None
    for r in RECORDS:
        if r[0] == category and r[1] == recordname:
            record = r
            break
    if record == None:
        return None
    newrecord = dict()
    newrecord[0] = record[0] # category
    newrecord[1] = record[1] # variable name
    newrecord[2] = record[2] # datatype1 ?
    # if third parameter exists add it
    if len(record)>3:
        # skip some achievement records with strange datatypes
        if record[3]=='tankExpertStrg':
            return None
        if record[3]=='mechanicEngineerStrg':
            return None
        newrecord[3] = record[3] # datatype2 ?
    else:
        newrecord[3] = record[2] # use datatype1 if third element do not exits
    return newrecord


if __name__ == '__main__':
	main()
