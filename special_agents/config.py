from dataclasses import dataclass
from special_agents.director import *
from special_agents.voc_manager import *
from special_agents.bpo_tools_manager import *
from special_agents.bpo_trainer import *
from special_agents.bpo_manager import *

@dataclass
class PAAgentsBundle:
    pa_director: object
    bpo_manager: object
    bpo_trainer: object
    bpo_tools_manager: object
    voc_manager: object


def build_pa_agents() -> PAAgentsBundle:
    bpo_tools_manager = build_bpo_tools_manager_agent()
    bpo_trainer_manager = build_bpo_trainer_agent()
    voc_manager = build_voc_manager_agent()
    bpo_manager = build_bpo_manager_agent()
    pa_director = build_director_agent(bpo_tools_manager, bpo_trainer_manager, voc_manager, bpo_manager)
    return PAAgentsBundle(
        pa_director=pa_director,
        bpo_manager=bpo_manager,
        bpo_trainer=bpo_trainer_manager,
        bpo_tools_manager=bpo_tools_manager,
        voc_manager=voc_manager
    )