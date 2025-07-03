########################################################################################
################################# ICPedia intern #######################################
########################################################################################

import yaml 
import PNR_Flow

class DesignConfig:
    def __init__(self):
        pass


class ConfigLoader:
    def __init__(self, yaml_path):
        with open(yaml_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_design_config(self):
        config_par = self.config[""]
        #pass config_par through DesignConfig
        #return DesignConfig()

    def get_tool_config(self):
        return self.config[""]


class FlowController:
    def __init__(self, config_path):
        self.config_loader = ConfigLoader(config_path)
        self.design_config = self.config_loader.get_design_config()
        tool_cfg = self.config_loader.get_tool_config() 
        #pass the parameter by self.design_config from yaml file 
        PNR_Flow.Pnrflow.run_flow([PNR_Flow.Synthesis(),PNR_Flow.FloorPlanning(),PNR_Flow.PowerPlanning(),PNR_Flow.Placement(),PNR_Flow.ClockTreeSynthesis(),PNR_Flow.Routing()])

        
if __name__ == "__main__":
    flow = FlowController("config.yaml")
