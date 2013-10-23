
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *


akVs5PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs5PFJets"),
    matched = cms.InputTag("ak5GenJets")
    )

akVs5PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs5PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs5PFcorr = patJetCorrFactors.clone(
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs5PFJets"),
    payload = "CAPak5OBJECT"
    )

akVs5PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs5PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs5PFcorr")),
                                               genJetMatch = cms.InputTag("akVs5PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs5PFparton"),
                                               jetIDMap = cms.InputTag("akVs5PFJetID"),
                                               )

akVs5PFAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs5PFpatJets"),
                                                             genjetTag = 'ak5GenJets',
                                                             rParam = 0.5,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs5PFpatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("TRACKS"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("hiGenParticles")
                                                             )


akVs5PFSequence_mc = cms.Sequence(akVs5PFmatch
                                                  *
                                                  akVs5PFparton
                                                  *
                                                  akVs5PFcorr
                                                  *
                                                  akVs5PFpatJets
                                                  *
                                                  akVs5PFAnalyzer
                                                  )

akVs5PFSequence_data = cms.Sequence(akVs5PFcorr
                                                    *
                                                    akVs5PFpatJets
                                                    *
                                                    akVs5PFAnalyzer
                                                    )


akVs5PFSequence = akVs5PFSequence_mc
