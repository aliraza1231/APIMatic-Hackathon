# Getting Started with Mixpanel Application
The following application fetches the events from the mixpanel using mixpanel SDK genrated through APIMatic and generates a graph of the activations.


## Building
You must have Python 3 >=3.7, <= 3.9 installed on your system to install and run this application.

Run the following command to install the dependencies
```
pip install -r requirements.txt
```

## Running the application
1. Update the mixpanel credentials used in main.py file
    ```python
    basic_auth_user_name='auth_user_name',
    basic_auth_password='auth_password',
    ```

2. Run main.py with python.exe and provide the arguments for week range to generate the data for
    ```
    python main.py [starting_week_number] [ending_week_number]

    e.g.

    # The follwoing will genearate a line graph for activations from Week 20 to Week 27
    python main.py 20 27
    ```
    The graph would be generated with the following name **Activations-{CurrentTime}.png**.

## Mixpanel SDK
The documentation for Mixpanel SDK generated through APIMatic CodeGen could be found [here](mixpanelexportapi/README.md).