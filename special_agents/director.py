from agents import Agent, ModelSettings, function_tool, Runner
from utils import load_prompt, DISCLAIMER
from dataclasses import dataclass
from pydantic import BaseModel
import json
import asyncio


class SpecialistRequestInput(BaseModel):
    section: str  # e.g., 'bpo_tools', 'bpo_trainer', 'bpo_manager', or 'voc'
    user_question: str
    guidance: str

# Core async functions for each specialist
async def specialist_analysis_func(agent, input: SpecialistRequestInput):
    result = await Runner.run(
        starting_agent=agent,
        input=json.dumps(input.model_dump()),
        max_turns=75,
    )
    return result.final_output

async def run_all_specialists_parallel(
    bpo_tools_manager, bpo_trainer_manager, bpo_manager, voc_manager,
    bpo_tools_input: SpecialistRequestInput,
    bpo_trainer_input: SpecialistRequestInput,
    bpo_manager_input: SpecialistRequestInput,
    voc_input: SpecialistRequestInput
):
    results = await asyncio.gather(
        specialist_analysis_func(bpo_tools_manager, bpo_tools_input),
        specialist_analysis_func(bpo_trainer_manager, bpo_trainer_input),
        specialist_analysis_func(bpo_manager, bpo_manager_input),
        specialist_analysis_func(voc_manager, voc_input)
    )
    return {
        "bpo_tools": results[0],
        "bpo_trainer": results[1],
        "bpo_manager": results[2],
        "voc": results[3]
    }

def build_director_agent(bpo_tools_manager, bpo_trainer_manager, bpo_manager, voc_manager):
    def make_agent_tool(agent, name, description):
        @function_tool(name_override=name, description_override=description)
        async def agent_tool(input: SpecialistRequestInput):
            return await specialist_analysis_func(agent, input)
        return agent_tool

    bpo_tools_manager_tool = make_agent_tool(bpo_tools_manager, "bpo_tools_analysis", "Generate the BPO Tools Analysis section.")
    bpo_trainer_manager_tool = make_agent_tool(bpo_trainer_manager, "bpo_trainer_manager_analysis", "Generate the BPO trainer manager Analysis section.")
    bpo_manager_tool = make_agent_tool(bpo_manager, "bpo_manager_analysis", "Generate the BPO manager Analysis section.")
    voc_manager_tool = make_agent_tool(voc_manager, "voc_manager_analysis", "Generate the VOC manager Analysis section.")

    @function_tool(name_override="run_all_specialists_parallel", description_override="Run all four specialists (BPO tools, BPO trainer manager, BPO manager, and VOC manager) in parallel and return their results as a dict.")
    async def run_all_specialists_tool(bpo_tools_input: SpecialistRequestInput, bpo_trainer_input: SpecialistRequestInput, bpo_manager_input: SpecialistRequestInput, voc_manager_input: SpecialistRequestInput):
        return await run_all_specialists_parallel(
            bpo_tools_manager, bpo_trainer_manager, bpo_manager, voc_manager, #agents
            bpo_tools_input, bpo_trainer_input, bpo_manager_input, voc_manager_input #inputs
        )

    return Agent(
        name="PA Director Agent",
        instructions=(
            load_prompt("pa_director_base.md") + DISCLAIMER
        ),
        model="gpt-4.1",
        
        tools=[bpo_tools_manager_tool, bpo_trainer_manager_tool, bpo_manager_tool, voc_manager_tool, run_all_specialists_tool],
        
        model_settings=ModelSettings(parallel_tool_calls=True, tool_choice="auto", temperature=0)
    ) 