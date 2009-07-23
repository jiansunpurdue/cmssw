import FWCore.ParameterSet.Config as cms

# AlCaReco for muon based alignment using beam-halo muons in the CSC overlap regions
OutALCARECOMuAlBeamHaloOverlaps_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlBeamHaloOverlaps')
    ),
    outputCommands = cms.untracked.vstring(
        'keep *_ALCARECOMuAlBeamHaloOverlaps_*_*', 
        'keep *_muonCSCDigis_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*',
	'keep *_MEtoEDMConverter_*_*')
)

import copy
OutALCARECOMuAlBeamHaloOverlaps = copy.deepcopy(OutALCARECOMuAlBeamHaloOverlaps_noDrop)
OutALCARECOMuAlBeamHaloOverlaps.outputCommands.insert(0, "drop *")
