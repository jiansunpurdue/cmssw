#ifndef JetMETCorrections_Type1MET_PFCandMETcorrInputProducer_h
#define JetMETCorrections_Type1MET_PFCandMETcorrInputProducer_h

/** \class PFCandMETcorrInputProducer
 *
 * Sum PFCandidates not within jets ("unclustered energy"),
 * needed as input for Type 2 MET corrections
 *
 * \authors Michael Schmitt, Richard Cavanaugh, The University of Florida
 *          Florent Lacroix, University of Illinois at Chicago
 *          Christian Veelken, LLR
 *
 * \version $Revision: 1.2 $
 *
 * $Id: PFCandMETcorrInputProducer.h,v 1.2 2011/10/14 10:14:35 veelken Exp $
 *
 */

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/METReco/interface/CorrMETData.h"

#include "CommonTools/Utils/interface/StringCutObjectSelector.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include <string>

class PFCandMETcorrInputProducer : public edm::EDProducer  
{
 public:

  explicit PFCandMETcorrInputProducer(const edm::ParameterSet&);
  ~PFCandMETcorrInputProducer();
    
 private:

  void produce(edm::Event&, const edm::EventSetup&);

  std::string moduleLabel_;

  edm::InputTag src_; // PFCandidate input collection

  struct binningEntryType
  {
    binningEntryType()
      : binLabel_(""),
        binSelection_(0)
    {}
    binningEntryType(const edm::ParameterSet& cfg)
    : binLabel_(cfg.getParameter<std::string>("binLabel")),
      binSelection_(new StringCutObjectSelector<reco::Candidate::LorentzVector>(cfg.getParameter<std::string>("binSelection")))
    {}
    ~binningEntryType() 
    {
      delete binSelection_;
    }
    std::string binLabel_;
    StringCutObjectSelector<reco::Candidate::LorentzVector>* binSelection_;
    CorrMETData binUnclEnergySum_;
  };
  std::vector<binningEntryType*> binning_;

  std::string residualCorrLabel_;
  double residualCorrEtaMax_;
  double residualCorrOffset_;
  double extraCorrFactor_;
};

#endif


 
