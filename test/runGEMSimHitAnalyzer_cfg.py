import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Geometry.GEMGeometry.GeometryExtendedPostLS2plusGEM_cff')
process.load('Geometry.CommonDetUnit.globalTrackingGeometry_cfi')
process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')
process.load('Geometry.GEMGeometry.gemGeometry_cfi')

#process.load('Configuration.StandardSequences.GeometryDB_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'DESIGN60_V5::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("gem_simhit_ana.root")
)


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/out_sim_10k_2pv1.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_1_1_PnG.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_4_1_vyj.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_2_1_7eI.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_5_1_nqf.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_positiveEta/res/sim_3_1_Xxd.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_1_1_huA.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_4_1_rdG.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_2_1_idm.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_5_1_pwT.root',
        'file:/uscms_data/d2/willhf/CMSSW_6_0_0/src/50k_negativeEta/res/sim_3_1_nOE.root',
    )
)

process.gemSimHitAna = cms.EDAnalyzer('GEMSimHitAnalyzer')

process.p = cms.Path(process.gemSimHitAna)

