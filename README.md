# Film Timer

This project is a film timer for photography enthusiasts. It helps you keep track of the time required for developing different types of film.

## Features

- Easy-to-use interface
- Support for various film types

## Installation

1. Clone the repository: `git clone [https://github.com/soapcan/film-timer.git](https://github.com/soapchan/Film_Timer.git)`
2. Run the `run.bat` file to initialise the project.

## Usage

1. Open the terminal and navigate to the project directory.
2. Run the application: `run.bat`
3. Fill in the temperature and film-type queries and click `Confirm`

## Adding additional film types

To add additional film types, you can modify the `config.json` file in the project directory. Follow these steps:

1. Open the `config.json` file in a text editor.
2. Locate the `"film types"` section.
3. Add a new entry for the film type you want to add. The entry should follow the format:
    ```json
    {
        "film types": {
            "film_type_name": <rate_of_change>
            }
    }
    ```
    Replace `"film_type_name"` with the name of the film type and `<time_change per degree>` with the percentage of time that changes per degree.
4. Save the `config.json` file.

Now, when you run the application and select the film type you added, it will use the development rate specified in the `config.json` file.

Remember to follow the existing format and ensure that the film type name is unique.


## Contributing

Contributions are welcome! If you have any ideas or suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
