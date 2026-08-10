# Historical Atlas

An interactive historical atlas exploring people, places, civilizations, cultures, texts, institutions, and events across time and geography.

The project combines historical data with an interactive map and timeline to make it possible to explore history spatially and chronologically — seeing what was happening in different parts of the world at different points in time.

## About the Project

Historical Atlas is an independent project created and maintained by Sridhar Ramachandran.

The goal is to explore history not simply as a sequence of dates, but as an interconnected story of:
 - People
 - Civilizations
 - Cultures
 - Empires and dynasties
 - Historical cities and places
 - Religious and philosophical traditions
 - Scientific developments
 - Historical texts
 - Universities and institutions
 - Major historical events
 - Natural disasters and pandemics
 - Trade and cultural networks

The interactive timeline allows users to move through history while the map shows events and entities associated with the selected period.

## What Can Be Explored?

The atlas currently contains data covering multiple regions and historical periods, including:
 - South Asia
 - East Asia
 - Southeast Asia
 - Central Asia
 - Europe
 - The Mediterranean
 - Middle East and ancient Near Eastern civilizations
 - Africa
 - North and South America
 - Australia and Oceania

Examples of subjects represented in the atlas include:

Indus Valley Civilization
Ancient Egypt
Sumer
Akkadian Empire
Ancient Greece
Ancient Rome
Maurya and Gupta Empires
Chinese and Japanese history
Maya and Olmec civilizations
Andean civilizations
Medieval and early-modern Europe
Major Indian philosophical and religious traditions
Scientific figures such as Aryabhata, Galileo, Newton, Mendel, and Darwin
Major historical texts
Universities and centers of learning
Major wars, disasters, pandemics, and other historical events

The dataset is continuously evolving.

## Timeline

Historical entities are represented using:

Start_Year
End_Year

Negative years represent BCE.

For example:

-500 = 500 BCE
1    = 1 CE
500  = 500 CE

Dates for ancient people, texts, traditions, and civilizations are sometimes approximate because historical scholarship does not always provide precise dates.

## Data Model

Each record follows the structure:

Name|Start_Year|End_Year|Latitude|Longitude|Info|Type|Category
Type

Type describes what the entity is.

Examples:

Person
Place
Polity
Civilization
Culture
Text
Event
Institution
Geography
Philosophy
Network
Period
Movement
Category

Category provides a more specific classification.

Examples:

Person → Scientist
Person → Philosopher
Person → Ruler
Person → Writer

Place → Historical City
Place → Monument
Place → Archaeological Site

Polity → Empire
Polity → Dynasty
Polity → Kingdom

Text → Epic
Text → Religious Text
Text → Medical Text

Event → Battle
Event → War
Event → Volcanic Eruption
Event → Earthquake
Event → Tsunami
Event → Pandemic

This separation allows the application to provide flexible filtering and exploration.

## Project Structure
historical-atlas/
│
├── ui.py
├── app.py
├── data_processor.py
├── requirements.txt
├── README.md
│
├── data/
│   └── historical_atlas.txt
│
└── ...
 - ui.py: Contains the Streamlit user interface, controls, filters, timeline, and map presentation.
 - app.py: Contains application-level functionality used by the UI.
 - data_processor.py: Handles loading, cleaning, processing, and preparing historical data for visualization.
 - data/ : Contains the historical atlas dataset.

## Running Locally
1. Clone the repository
git clone <YOUR_REPOSITORY_URL>
cd historical-atlas
2. Create a virtual environment
python -m venv .venv
3. Activate the environment
Windows
.venv\Scripts\activate
Linux / WSL
source .venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Run the application
streamlit run ui.py

The application will open in your browser.

## Online Version
A deployed version of the Historical Atlas is planned using Streamlit.
Live application: https://historical-atlas.streamlit.app/ 

## Data
The historical dataset is curated and organized specifically for this project.

Historical dates, locations, and descriptions may be approximate, particularly for ancient civilizations, historical figures, traditions, and texts where scholarly dating or geographic attribution is uncertain.

The atlas is intended primarily as an educational and exploratory visualization, not as a definitive historical reference.

Where historical uncertainty is significant, the dataset attempts to reflect that uncertainty in the description.

## Sources

Historical information is researched and cross-checked using appropriate historical, archaeological, academic, and reference sources.

Sources may include:
 - Academic publications
 - Archaeological references
 - Historical reference works
 - University and museum resources
 - Encyclopedic sources
 - Primary and translated historical texts

A future version of the project will provide more detailed source attribution for individual records.

## Design Philosophy

The project is based on a simple idea: History becomes easier to understand when time and geography are viewed together.
 - A traditional timeline answers: "When did this happen?"
 - A map answers: "Where did this happen?"

The Historical Atlas attempts to answer both questions simultaneously: "What was happening, where, and when?"

This makes it possible to explore relationships between civilizations, people, ideas, institutions, migration, trade, science, religion, and major historical events.

## Project Goals

Future development may include:
 - Expand global historical coverage
 - Improve source attribution
 - Add more historical events
 - Add historical migration and trade routes
 - Improve geographic representations
 - Add more ancient civilizations
 - Add historical regions and political boundaries
 - Improve timeline navigation
 - Add richer filtering
 - Add links between related historical entities
 - Add historical source references
 - Improve mobile presentation
 - Add downloadable datasets
 - Add an educational/research mode

## Technology
The project currently uses:
 - Python
 - Streamlit
 - Pandas
 - folium
 - Git
 - GitHub

Additional technologies and libraries may be added as the project evolves.

## Author
Sridhar Ramachandran
Historical Atlas is an independent personal project created and maintained by Sridhar Ramachandran.
© 2026 Sridhar Ramachandran · Historical Atlas

## License
Copyright © 2026 Sridhar Ramachandran.
Unless otherwise stated, the source code, original data organization, descriptions, visual design, and other original materials in this repository are the work of the author.
Historical facts and information themselves are not claimed as original intellectual property.
For permissions regarding reuse, redistribution, modification, or commercial use of the project's original materials, please contact the author.

## Disclaimer
Historical dates and interpretations can vary between sources, particularly for ancient and prehistoric subjects.

This atlas is intended for educational, exploratory, and visualization purposes. It should not be treated as a substitute for detailed academic or historical research.

## Contributing

This is currently a personal project.
Suggestions, corrections, and ideas for improving historical accuracy and functionality are welcome.

Please open an issue describing:
 - The record or feature concerned
 - The proposed correction or improvement
 - Supporting sources, where applicable

## Status
Active development

The Historical Atlas is an evolving project. New civilizations, people, places, texts, institutions, and historical events are continuously being added and reviewed.