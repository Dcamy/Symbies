#!/usr/bin/env python
from familycrewai.crew import FamilycrewaiCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    FamilycrewaiCrew().crew().kickoff(inputs=inputs)