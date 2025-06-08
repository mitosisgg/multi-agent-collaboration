# Multi-Agent Collaboration Demo

This project demonstrates how to orchestrate multiple AI agents as specialized tools in a business process optimization (BPO) context. Each agent focuses on a specific aspect of BPO operations, working together to provide comprehensive solutions.

## Project Structure

The project is organized into several specialized agents:

- **PA Director Agent**: Orchestrates the workflow and coordinates between different specialist agents
- **BPO Tools Manager Agent**: Manages call center operations and tool integrations
- **BPO Trainer Agent**: Handles training and onboarding of BPO agents
- **BPO Manager Agent**: Manages BPO operations and resource allocation
- **VOC Manager Agent**: Manages Voice of Customer data and insights

## Requirements

- Python 3.13+
- OpenAI API access
- Required packages listed in `requirements.txt`

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add environment variables to `.env` file:
```bash
OPENAI_API_KEY=your_api_key
```

4. Run the Jupyter notebook `multi-agent-collaboration.ipynb`.

## Usage

The main workflow is executed through the Jupyter notebook `multi-agent-collaboration.ipynb`. This notebook demonstrates how to:

1. Initialize all specialized agents
2. Run multi-agent workflows
3. View trace logs and outputs

## Features

- Multi-agent collaboration using OpenAI's agent framework
- Specialized agents for different business functions
- Tracing and logging capabilities
- Integration with various business tools (Zendesk, Talkdesk, etc.)
- Parallel processing capabilities

## Contributing

Feel free to contribute to this project by:
1. Adding new specialized agents
2. Enhancing existing agent capabilities
3. Improving the orchestration logic
4. Adding new integrations with business tools

## License

This project is for demonstration purposes only.
