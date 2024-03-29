#ifndef GEMDigitizer_GEMSynchronizer_h
#define GEMDigitizer_GEMSynchronizer_h

/** \class GEMSynchronizer
 *
 *  Class for the GEM strip response simulation based
 *  on a parametrized model
 *
 *  \author Vadim Khotilovich
 */

#include "CLHEP/Random/Random.h"

#include <FWCore/Framework/interface/Frameworkfwd.h>

class PSimHit;
class GEMSimSetUp;

namespace CLHEP
{
  class RandGaussQ;
}


class GEMSynchronizer
{
public:

  GEMSynchronizer(const edm::ParameterSet& config);

  ~GEMSynchronizer();

  int getSimHitBx(const PSimHit*);

  void setGEMSimSetUp(GEMSimSetUp *simsetup) { simSetUp_ = simsetup; }

  GEMSimSetUp* getGEMSimSetUp() { return simSetUp_; }

  void setRandomEngine(CLHEP::HepRandomEngine& eng);

private:

  double timeRes_;
  double timOff_;
  double dtimCs_;
  double resEle_;
  double sspeed_;
  double lbGate_;
  double lbGateNew_;

  bool cosmics_;

  CLHEP::RandGaussQ *gauss1_;
  CLHEP::RandGaussQ *gauss2_;

  GEMSimSetUp * simSetUp_;

};

#endif
