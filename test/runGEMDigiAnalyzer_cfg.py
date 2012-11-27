import FWCore.ParameterSet.Config as cms

process = cms.Process("GEMANA")

process.load('FWCore.MessageService.MessageLogger_cfi')

process.load('Geometry.GEMGeometry.cmsExtendedGeometryPostLS1plusGEMXML_cfi')
process.load('Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi')
process.load('Geometry.CommonDetUnit.globalTrackingGeometry_cfi')
process.load('Geometry.MuonNumbering.muonNumberingInitialization_cfi')
process.load('Geometry.GEMGeometry.gemGeometry_cfi')
process.load('Geometry.TrackerGeometryBuilder.idealForDigiTrackerGeometryDB_cff')
process.load('Geometry.DTGeometryBuilder.idealForDigiDtGeometryDB_cff')
process.load('Geometry.CSCGeometryBuilder.idealForDigiCscGeometry_cff')


process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'POSTLS161_V12::All'


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("gem_digi_ana.root")
)


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:out_digi.root'
    )
)

process.ana = cms.EDAnalyzer("GEMDigiAnalyzer",
    verbosoty = cms.untracked.int32(1),
    inputTagRPC = cms.untracked.InputTag("simMuonRPCDigis"),
    inputTagGEM = cms.untracked.InputTag("simMuonGEMDigis")
)


process.p    = cms.Path(process.ana)

