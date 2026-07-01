# Load environment variables
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()  # Load environment variables from .env file
def main():
    print("Hello from langchain-course!")
    print("Loading environment variables from .env file...")
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("OPENAI_API_KEY is not set. Please set it in your .env file.")
    else:
        print("OPENAI_API_KEY loaded successfully.")

    information ="""
    Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is a businessman and former public official who is the CEO and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only ever trillionaire in terms of US dollars in 2026. As of June 2026, Forbes estimates his net worth to be US$951 billion.

Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded Zip2, a web software company. Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.

In 2002, Musk founded and became CEO and chief engineer of SpaceX, a space technology company; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, Musk co-founded OpenAI to advance artificial intelligence (AI) research, but later left; his growing discontent with the organization's direction and leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired Twitter, a social networking service; he implemented significant changes and rebranded it as X in 2023. His other businesses include Neuralink, a neurotechnology company that he co-founded in 2016, and the Boring Company, a tunneling company that he founded in 2017. In November 2025, Tesla approved a pay package worth $1 trillion for Musk, which he is to receive over 10 years if certain milestones are met, such as achieving a market capitalization of $8.5 trillion.

Musk is a supporter of global far-right politics, figures, and political parties. He was the largest donor in the 2024 U.S. presidential election, where he supported Donald Trump. After Trump was inaugurated in January 2025, Musk served as Senior Advisor to the President and as the de facto head of the Department of Government Efficiency (DOGE). Musk left the Trump administration in May 2025 and returned to managing his companies; shortly thereafter he had a public feud with Trump.

Musk's political activities, statements and views have made him a polarizing figure. He has been criticized for making unscientific and misleading statements, including spreading COVID-19 misinformation, promoting conspiracy theories, and affirming antisemitic, white nationalist, racist, and transphobic comments. His acquisition of Twitter was controversial because, following his pledge to decrease censorship, there was an increase in hate speech and misinformation on the service. His role in the second Trump administration attracted public backlash, particularly in response to DOGE and its cuts to the US Agency for International Development (USAID).

Early life and education
See also: Musk family
Elon Reeve Musk was born on June 28, 1971, in Pretoria, South Africa's administrative capital.[2][3] He is of British and Pennsylvania Dutch ancestry.[4][5] His mother, Maye (née Haldeman), is a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[6][7][8] Musk therefore holds both South African and Canadian citizenship from birth.[9] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, emerald dealer, and property developer, who partly owned a rental lodge at Timbavati Private Nature Reserve.[10][11][12][13]

His maternal grandfather, Joshua N. Haldeman, who died in a plane crash when Musk was a toddler, was an American-born Canadian chiropractor, aviator and political activist in the Technocracy movement[14][15] who moved to South Africa in 1950.[16] Haldeman's anti-government, anti-democratic and conspiracist views, which included the promotion of far-right antisemitic conspiracy theories,[17][18] "fanatical" support of apartheid,[18] and according to Errol, support of Nazism,[16] have been suggested as an influence on Musk.[19][20][21][22] During his childhood, Musk was told stories by his grandmother of Haldeman's travels and exploits, and he has suggested that all of Haldeman's descendants have his "desire for adventure, exploration – doing crazy things".[23]

Musk has a younger brother, Kimbal, a younger sister, Tosca, and four paternal half-siblings.[24][25][8][26] He was baptized as a child in the Anglican Church of Southern Africa.[27][28] The Musk family was wealthy during his youth.[13] Despite both Musk and Errol previously stating that Errol was a part owner of a Zambian emerald mine,[13] in 2023, Errol recounted that the deal he made was to receive "a portion of the emeralds produced at three small mines".[29][30] Errol was elected to the Pretoria City Council as a representative of the anti-apartheid Progressive Party and has said that his children shared their father's dislike of apartheid.[2]

After his parents divorced in 1979, Musk, aged around 9, chose to live with his father because he had an Encyclopædia Britannica set and a computer.[31][4][10] He later regretted his decision and became estranged from his father.[32] Musk has recounted trips to a wilderness school that he described as a "paramilitary Lord of the Flies" where "bullying was a virtue" and children were encouraged to fight over rations.[33] In one incident, after an altercation with a fellow pupil, Musk was thrown down concrete steps and beaten severely, leading to him being hospitalized for his injuries.[34] He described his father berating him after he was discharged from the hospital.[34] Errol denied berating Musk and claimed, "The [other] boy had just lost his father to suicide, and Musk had called him stupid. He had a tendency to call people stupid. How could I possibly blame that child?"[35]

Musk was an enthusiastic reader of books, and had attributed his success in part to having read The Lord of the Rings, the Foundation series, and The Hitchhiker's Guide to the Galaxy.[12][36] At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual.[37] At age twelve, in 1983, Musk sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500 (equivalent to $1,600 in 2025).[38][39]
    """
    
    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    #llm = ChatOpenAI(temperature=0, model="gpt-5")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)

    print("Finished processing. Please check the output above for the summary and interesting facts.")



if __name__ == "__main__":
    main()
