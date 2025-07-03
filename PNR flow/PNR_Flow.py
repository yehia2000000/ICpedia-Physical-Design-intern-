########################################################################################
################################# ICPedia intern #######################################
########################################################################################

import os

class Synthesis : 
    def __init__(self):
        #define Synthesis attribute 
        pass
    
    def run(self) : 
        with open ("Synthesis.tcl",'w') as syn :
            #Write Synthesis command 
            syn.write("")
            syn.close()
        
        #run the tcl file by the tool 
        os.system("")
    
    def report(self): 
        pass
        
class FloorPlanning : 
    def __init__(self):
        #define FloorPlanning attribute 
        pass
    
    def run(self) : 
        with open ("FloorPlanning.tcl",'w') as fop :
            #Write FloorPlanning command 
            fop.write("")
            fop.close()
        
        #run the tcl file by the tool 
        os.system("")    
    
    def report(self): 
        pass
        
class PowerPlanning  : 
    def __init__(self):
        #define PowerPlanning attribute 
        pass
    
    def run(self) : 
        with open ("PowerPlanning.tcl",'w') as pop :
            #Write PowerPlanning command 
            pop.write("")
            pop.close()
        
        #run the tcl file by the tool 
        os.system("")    
    
    def report(self): 
        pass
        
class Placement : 
    def __init__(self):
        #define Placement attribute 
        pass
    
    def run(self) : 
        with open ("Placement.tcl",'w') as plac :
            #Write Placement command 
            plac.write("")
            plac.close()
        
        #run the tcl file by the tool 
        os.system("")    
    
    def report(self): 
        pass

        
class ClockTreeSynthesis : 
    def __init__(self):
        #define ClockTreeSynthesis attribute 
        pass
    
    def run(self) : 
        with open ("ClockTreeSynthesis.tcl",'w') as cts :
            #Write ClockTreeSynthesis command 
            cts.write("")
            cts.close()
        
        #run the tcl file by the tool 
        os.system("")    
    
    def report(self): 
        pass
        
        
class Routing : 
    def __init__(self):
        #define Routing attribute 
        pass
    
    def run(self) : 
        with open ("Routing.tcl",'w') as rot :
            #Write Routing command 
            rot.write("")
            rot.close()
        
        #run the tcl file by the tool 
        os.system("")    
    
    def report(self): 
        pass
    
    

class Pnrflow : 
    def __init__(self,flow):
        self.flow = flow
        
    def run_flow (self): 
        for step in self.flow : 
            step.run()
            step.report()
            
# Testing the process of individual  process in pnr flow 
if __name__ == "__main__":
    pass
