import FWCore.ParameterSet.Config as cms

process = cms.Process("GEMDIGI")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

#process.Timing = cms.Service("Timing")
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )


process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')

#process.load('Geometry.CMSCommonData.cmsExtendedGeometryModularXMLGEM_cfi')
#process.load('Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi')
process.load('Geometry.GEMGeometry.GeometryExtendedPostLS2plusGEM_cff')
process.load('Geometry.CommonDetUnit.globalTrackingGeometry_cfi')
process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')
process.load('Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometryDB_cff')
process.load('Geometry.DTGeometryBuilder.idealForDigiDtGeometryDB_cff')
process.load('Geometry.CSCGeometryBuilder.idealForDigiCscGeometry_cff')
process.load('Geometry.GEMGeometry.gemGeometry_cfi')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'POSTLS161_V12::All'
#process.GlobalTag.globaltag = 'DESIGN60_V5::All'


# GEM digitizer
process.load('SimMuon.GEMDigitizer.muonGEMDigis_cfi')

# customization of the process.pdigi sequence to add the GEM digitizer 
from SimMuon.GEMDigitizer.customizeGEMDigi import *
#process = customize_digi_addGEM(process)  # run all detectors digi
#process = customize_digi_addGEM_muon_only(process) # only muon+GEM digi
process = customize_digi_addGEM_gem_only(process)  # only GEM digi


inputFiles = [
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_1_1_PnG.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_4_1_vyj.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_2_1_7eI.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_5_1_nqf.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_3_1_Xxd.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_1_1_huA.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_4_1_rdG.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_2_1_idm.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_5_1_pwT.root',
    'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_3_1_nOE.root'
]

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        *inputFiles
    )
)


process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string( 
        'out_digi2.root'
    ),
    outputCommands = cms.untracked.vstring(
        'keep  *_*_*_*',
        # drop all CF stuff
        'drop *_mix_*_*',
        # drop tracker simhits
        'drop PSimHits_*_Tracker*_*',
        # drop calorimetry stuff
        'drop PCaloHits_*_*_*',
        # clean up simhits from other detectors
        'drop PSimHits_*_Totem*_*',
        'drop PSimHits_*_FP420*_*',
        'drop PSimHits_*_BSC*_*',
        # drop some not useful muon digis and links
        'drop *_*_MuonCSCStripDigi_*',
        'drop *_*_MuonCSCStripDigiSimLinks_*',
        #'drop *SimLink*_*_*_*',
        'drop *RandomEngineStates_*_*_*',
        'drop *_randomEngineStateProducer_*_*'
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('digi_step')
    )
)



#process.contentAna = cms.EDAnalyzer("EventContentAnalyzer")


process.digi_step    = cms.Path(process.pdigi)
process.endjob_step  = cms.Path(process.endOfProcess)
process.out_step     = cms.EndPath(process.output)


process.schedule = cms.Schedule(
    process.digi_step,
    process.endjob_step,
    process.out_step
)

