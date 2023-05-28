```
# you-win-you-do

you-win-you-do is a Python-based software that helps users cultivate healthy habits by engaging in debates with an AI-powered GPT (Generative Pre-trained Transformer) model. The purpose of this software is to encourage users to reflect on their behaviors and make more informed decisions.

## Features

- Utilizes OpenAI's GPT model for generating responses based on prompts
- Allows users to debate with the GPT model regarding their habits
- Provides an option to adopt the tone and personality of a favorite celebrity during the debate

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/skyline88888888/you-win-you-do.git
   ```

2. Install the required dependencies:

   ```shell
   pip install openai
   ```

3. Set up OpenAI API access:

   - Obtain an API key from OpenAI (refer to the OpenAI documentation for more details).
   - Replace `YOUR_API_KEY` in the code with your actual API key.

## Usage

1. Open the `main.py` file in your preferred Python IDE or editor.

2. Run the script:

   ```shell
   python main.py
   ```

3. Enter your viewpoint when prompted.

4. The GPT model will generate a response based on your input, engaging in a debate with you.

5. If desired, you can specify a celebrity tone by modifying the `celebrity_tone` variable in the code. For example:

   ```python
   celebrity_tone = "in the style of [Favorite Celebrity]"
   ```

   Replace `[Favorite Celebrity]` with the name of the celebrity whose tone you want the GPT model to adopt.

6. Repeat steps 3-5 for additional debates. Enter "退出" to exit the program.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch:

   ```shell
   git checkout -b feature/my-feature
   ```

3. Make your changes and commit them:

   ```shell
   git commit -am 'Add some feature'
   ```

4. Push the changes to your forked repository:

   ```shell
   git push origin feature/my-feature
   ```

5. Open a pull request, describing the changes you made.

Please ensure that your contributions adhere to the [Code of Conduct](CODE_OF_CONDUCT.md).
