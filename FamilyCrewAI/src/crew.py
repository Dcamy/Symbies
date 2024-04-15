from crewai import Agent, Crew, Process, Task
from tasks.read_profile import read_profile_task  # Adjust the import path if necessary
from agents.alex import AlexAgent


alex = AlexAgent()
# Uncomment the following line to use an example of a custom tool
# from familycrewai.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# Instantiate your crew
my_crew = Crew(
    agents=[alex],  # List your agents here
    tasks=[read_profile_task],  # List your tasks here
    # ...other configurations for the crew...
)


class FamilycrewaiCrew:
    """Familycrewai crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
        )

    def reporting_analyst(self) -> Agent:
        return Agent(config=self.agents_config["reporting_analyst"], verbose=True)

    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"], agent=self.researcher())

    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            agent=self.reporting_analyst(),
            output_file="report.md",
        )

    my_crew = Crew(
        agents=[...],  # Your list of agent instances
        tasks=[
            read_profile_task,
            ...,
        ],  # Add your read_profile_task to the list of tasks
    )

    def crew(self) -> Crew:
        """Creates the Familycrewai crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


# Continue in crew.py
result = my_crew.kickoff()
print(result)  # Outputs the results of the tasks
