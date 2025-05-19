# School Website

A comprehensive school website built with Streamlit, featuring sections for Creche, Primary School, and Secondary School education.

## Features

- **Home Page**: School overview, highlights, and latest news
- **Creche Program**: Information about early childhood care and education
- **Primary School**: Curriculum and program details for ages 4-11
- **Secondary School**: Academic programs and extracurricular activities for ages 12-18
- **Admissions**: Online application form and process
- **Contact**: Contact form and location information

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Website

To run the school website, use the following command:
```bash
streamlit run app.py
```

The website will open in your default web browser at `http://localhost:8501`.

## Customization

The website can be customized by modifying `app.py`. Key areas for customization include:

- School information and contact details
- Program descriptions and curriculum
- School hours and schedules
- Admission requirements
- News and events
- School branding (logo, colors, etc.)

## Dependencies

- streamlit==1.32.0
- pandas==2.2.1
- numpy==1.26.4

## Future Enhancements

Potential features to add:
- Student portal
- Parent portal
- Online payment system
- Calendar integration
- Photo gallery
- Blog/News section
- Virtual tour
- Online learning resources 