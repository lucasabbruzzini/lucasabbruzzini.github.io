from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cv_data = {
        'name': 'Lucas Abbruzzini',
        'title': 'Rust Developer To Be',
        'email': 'lucas.abbruzzini@proton.me',
        'phone': '+55 12 99620 0140',
        'location': 'Brazil',
        'place_of_living': 'Uberlândia – Brazil',
        'citizenship': 'Brazilian',
        'linkedin': '/in/lucasabbruzzini/',
        'github': 'github.com/lucasabbruzzini',
        'summary': 'I am a polymath with a background in finance, technology, and strategic consulting. My passion lies in crypto, data privacy, AI, and leveraging technology to solve complex problems across diverse fields.',
        'experience': [
            {
                'title': 'Tech Strategy Analyst',
                'company': 'Accenture',
                'period': 'May/23 - Present',
                'description': [
                    'Project & Program Management: Overseeing workstreams, managing timelines, resources, and aligning with objectives to ensure successful project delivery. Proactively addressing risks and resolving issues.',
                    'Python Development & Data Management: Building market data routines for risk management solutions, focusing on ETL processes, frontend integration, testing, and debugging for system reliability.',
                    'Data Analysis & Reporting: Conducting analysis, creating dashboards, and optimizing SQL queries to enhance reporting accuracy and decision-making.',
                    'Collaboration & Communication: Working with cross-functional teams to implement programs and connect technical and business leadership.',
                    'Strategic Problem Solving & Planning: Developing data-driven hypotheses, structuring problems, and planning roadmaps to support growth and innovation.',
                    'Business Case & IT Strategy: Assisting in creating actionable business cases and developing IT strategies, including opportunity assessments, systems, infrastructure, and architecture planning.'
                ]
            },
            {
                'title': 'Controls and Automation Engineer',
                'company': 'Dennis Group',
                'period': 'Jun/20 - Mar/21',
                'description': [
                    'PLC Design and Programming (Allen Bradley/Rockwell, Schneider Electric). SCADA and HMI Systems Development (Allen Bradley/Rockwell, Wonderware). Process Network Infrastructure Design (Ethernet, Device Net, Control Net, AS‑i, Modbus, etc).', 
                    'Specification and Procurement. Control Panel and Installation Design (AutoCAD). Hardware, Instrumentation, and Network Configuration.', 
                    'P&ID and Bid Documentation for Electrical and Automation. Electrical Construction Management and Supervision. System Commissioning and Start‑Up.'
                ]
            },
            {
                'title': 'Controls and Automation Intern',
                'company': 'Tech Solutions Inc.',
                'period': 'Jun/18 - Feb/20',
                'description': [
                    'Startup that performs quality control using computational vision.',
                    'Activities related to construction of embedded systems, quality control tests, installation of operating system, documentation and process optimization.',
                    'Conception of Industrial Communication and Automation projects.',
                    'Helped the start-up leave the incubator and start new co-workspace.',
                    'Pitched to investor and participated in meeting with clients.'
                ]
            }
        ],
        'education_and_skills': {
            'education': [
                {
                    'degree': 'Master of Science, MSc in Financial Engineering',
                    'institution': 'QuantWorld University',
                    'year': '2025'
                },
                {
                    'degree': 'Master of Science, Computer Science',
                    'institution': 'UFU - Universidade Federal de Uberlandia',
                    'year': '2022 - Interrupted'
                },
                {
                    'degree': 'Bachelor of Mechatronics Engineering',
                    'institution': 'UFU - Universidade Federal de Uberlandia',
                    'year': '2019'
                }
            ],
            'certifications': [
                {
                    'name': 'Google Cloud Digital Leader', 'icon': 'fab fa-google',
                },
                {
                    'name': 'AWS Practitioner', 'icon': 'fab fa-rust','icon': 'fab fa-aws',

                },
                {
                    'name': 'Microsoft Certified: Azure AI Fundamentals', 'icon': 'fab fa-microsoft',
                },
                {
                    'name': 'Microsoft Certified: Azure Data Fundamentals','icon': 'fab fa-microsoft',
                },
                {
                    'name': 'Microsoft Certified: Azure Fundamentals','icon': 'fab fa-microsoft',

                },
                {
                    'name': 'SAFe® 5 Agilist','icon': 'fa-solid fa-bars-progress',
                },
                                {
                    'name': 'Google Project Management Certificate','icon': 'fab fa-google',
                },
                                {
                    'name': 'LSE – MBA Essentials','icon': 'fa-solid fa-graduation-cap',
                },

            ],
            'coding_skills': [
                {'name': 'Rust', 'level': 20, 'icon': 'fab fa-rust'},
                {'name': 'Python', 'level': 70, 'icon': 'fab fa-python'},
                {'name': 'SQL', 'level': 60, 'icon': 'fas fa-database'},
                {'name': 'C', 'level': 30, 'icon': 'fab fa-c'},
              #  {'name': 'MATLAB', 'level': 50, 'icon': 'fa-solid fa-code'},
                {'name': 'JavaScript', 'level': 20, 'icon': 'fab fa-js-square'},
                {'name': 'HTML/CSS', 'level': 20, 'icon': 'fab fa-html5'},
            ],
            'other_skills': [
                {'name': 'MS Office', 'level': 20, 'icon': 'fas fa-file-word'},
                #{'name': 'MS Power BI', 'level': 30, 'icon': 'fas fa-chart-bar'},
#                {'name': 'AWS', 'level': 20, 'icon': 'fab fa-aws'},
#                {'name': 'Azure', 'level': 20, 'icon': 'fab fa-microsoft'},
#                {'name': 'GCP', 'level': 20, 'icon': 'fas fa-cloud'},
                {'name': 'Git', 'level': 20, 'icon': 'fab fa-git-alt'},
                {'name': 'Jira', 'level': 20, 'icon': 'fab fa-jira'},
                {'name': 'Trello', 'level': 20, 'icon': 'fab fa-trello'},
                {'name': 'Azure DevOps', 'level': 20, 'icon': 'fas fa-code-branch'}
            ],
        'languages': [
            {'name': 'English', 'level': 100, 'flag': 'us'},
            {'name': 'Portuguese', 'level': 100, 'flag': 'pt'},
            {'name': 'French', 'level': 50, 'flag': 'fr'},
            {'name': 'Spanish', 'level': 50, 'flag': 'es'},
            {'name': 'German', 'level': 20, 'flag': 'de'}
        ]
        }
    }

    portfolio_items = [
        {
            'title': 'Stoa',
            'description': 'Application focused on crypto risk and portfolio management, providing advanced tools for liquidity management, risk assessment, and portfolio optimization using blockchain technology.', 
            'link': 'https://github.com/stoa-rs/stoa.rs'
        },
        {
            'title': 'Mortgage Risk Analisys',
            'description': 't this project I attempted to analyze the credit worthiness of an individual when applying to finance a home. The main challenge was to find data as most of it is proprietary',
            'link': 'https://github.com/lucasabbruzzini/lucasabbruzzini.github.io/blob/main/Motgage.ipynb'
        },
        {
            'title': 'Macroeconomics Metrics Correlation',
            'description': 'this project I attempted to analyze the following metrics with macoeconomic indicator such as GDP and Fed Rate to look for corelations amongst them.',
            'link': 'https://github.com/lucasabbruzzini/lucasabbruzzini.github.io/blob/main/Macro_indicators_correlation.ipynb'
        }
    ]

    return render_template('index.html', cv_data=cv_data, portfolio_items=portfolio_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)