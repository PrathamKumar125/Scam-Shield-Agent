import os
import spaces
import firecrawler
import rag
from huggingface_hub import login
import gradio as gr
from smolagents import HfApiModel, CodeAgent

# login(token = os.getenv('HF_API_KEY'))
hf_api_key = os.getenv('HF_API_KEY')

# Fetch tools
execute_firecrawl = firecrawler.FireCrawlTool()
retriever_tool = rag.retriever_tool 

agent = CodeAgent(
    tools=[execute_firecrawl, retriever_tool], 
    model=HfApiModel(token=hf_api_key),
    max_steps=10
)


def get_answer(url, text):
    """
    A function that takes any question as input and returns the answer using agent.run()
    
    Args:
        url (str): The URL to investigate
        text (str): Additional context about the situation
        
    Returns:
        str: Detailed analysis report
    """
    # Enhanced prompt with more specific instruction for detailed output
    full_prompt = f'''
    COMPREHENSIVE SCAM DETECTION ANALYSIS

    Objective: Provide a meticulously detailed, structured assessment of potential online risks.

    ANALYSIS FRAMEWORK:
    1. RISK LEVEL
   - Explicitly state an overall risk assessment (Low/Medium/High)

    2. URL ANALYSIS
       - Detailed breakdown of URL characteristics
       - Domain reputation assessment
       - Technical red flags
       - Registrar and hosting information insights

    3. CONTENT EVALUATION
       - Content quality assessment (use execute_firecrawl to retrieve contents sample)
       - Linguistic and communication pattern analysis
       - Consistency and professionalism evaluation

    4. SPECIFIC RED FLAGS
       - List at least 5 concrete indicators of potential scam
       - Use Scamwatch reference material (use retriever_tool)
       - Provide specific evidence for each red flag
       - Categorize red flags (e.g., Technical, Financial, Communication)

    5. RECOMMENDED ACTIONS
       - Specific, actionable steps for user protection
       - Use Scamwatch reference material (use retriever_tool)
       - Recommended verification methods
       - Suggested reporting channels
       - Personal safety guidelines

    6. ADDITIONAL INSIGHTS
       - Contextual background information
       - Potential motivations behind suspicious activity
       - Broader pattern recognition

    CONTEXT:
    - URL under investigation: {url}
    - User-provided situation description: {text}

    CRITICAL INSTRUCTIONS:
    - Maintain objective, evidence-based analysis
    - Talk in terms of risks rather then certainties.
    - Focus on user empowerment and protection
    - Use the retriever_tool tool to look up Scamwatch reference information scam types, reporting scams etc. Where possible prioritise this infomration.

    '''

    try:
        answer = agent.run(full_prompt)
        print("Final output:")
        print(answer)
        return answer
    except Exception as e:
        print(f"Error: {str(e)}")
        return f"An error occurred while processing your request: {str(e)}"

# Gradio Interface (rest of the code remains the same)
with gr.Blocks() as demo:
    theme=gr.themes.Monochrome()
   
    with gr.Row():
        with gr.Column(scale=1, min_width=300):
            gr.Markdown(
            """
            # ScamShield (agent edition)
            🛡️ A tool to help users identify scam red flags.
            """)
    
    with gr.Row():
        with gr.Column(scale=1, min_width=300):
            input_text = gr.Textbox(label="Description", info="Please describe your concerns regarding the situation", lines=3, value="Is this website a reliable source of investment information?")
            input_url = gr.Textbox(label="URLs", info="Please enter a suspicious URL", lines=3, value="https://fliojinews.xyz/9tKwgmC7")
            btn = gr.Button("Process submission")
        
        with gr.Column(scale=2, min_width=300):
            t3 = gr.Textbox(label="Advice", lines=10)
            
    btn.click(
        fn=get_answer, 
        inputs=[input_url, input_text], 
        outputs=[t3]
    )

# Launch
demo.launch()