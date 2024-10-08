# rdu-autogen-sbx

Sandbox do poznawania frameworku autogen.
Skrytpy odpalane są w środowisku windows. 
Żeby nie zanieczyszczać hosta, proponuję uruchamiać je na maszynie wirtualnej z windowsem 11

Na początku upewnij się, że masz separowane środowiska, użyj conda
 - https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe 
 - dodaj conda do zmiennych środowiskowych, np.: 
   - C:\ProgramData\miniconda3\Scripts
   - C:\ProgramData\miniconda3
- masz uruchomiony silnik dockera


1. **Install Anaconda or Miniconda**:
   - If you haven't already, download and install [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. **Create a Conda Environment**:
   - Open a terminal in VSC (you can use `Ctrl + ` `).
   - Create a new Conda environment with the following command:
     ```bash
     conda create --name rdu-autogen-sbx python=3.12
     ```

3. **Activate the Conda Environment**:
   - In the terminal, activate your environment:
     ```bash
     conda activate rdu-autogen-sbx
     ```

4. **Select the Conda Environment in VSC**:
   - Open the Command Palette (`Ctrl + Shift + P`).
   - Type and select `Python: Select Interpreter`.
   - Choose your newly created Conda environment from the list.

5. **Configure Your Workspace**:
   - You can set your workspace to always use this environment by adding the following to your `.vscode/settings.json` file:
     ```json
     {
       "python.pythonPath": "C:\\Users\\YourUsername\\Anaconda3\\envs\\myenv\\python.exe"
     }
     ```
     Adjust the path to match your Conda installation and environment name, e.g.
     ```json
     {
       "python.pythonPath": "C:\\Users\\rdudzinski\\AppData\\Local\\miniconda3\\envs\\rdu-autogen-sbx\\python.exe"
     }
     ```

6. **Install Packages**:
  - With your environment activated, you can install any necessary packages using Conda:
     ```bash
     conda install package_name
     ```
  - install
    ```bash
    pip install pyautogen
    #
    # Install Azure CLI
    pip install azure-cli
    # RAG retrieve
    pip install "pyautogen[retrievechat]"
    pip install pyautogen azure-search-documents azure-identity
    pip install pyautogen
    pip install python-dotenv
    pip install pyautogen[graph]
    pip install azure-search-documents
    pip install azure-identity
    #
    #Install unstructured in ubuntu
    sudo apt-get update
    sudo apt-get install -y tesseract-ocr poppler-utils
    pip install unstructured[all-docs]

    ```

7. **Dodaj zmienne środowiskowe**:
  - przy założeniu, że używasz conda envs
    - listowanie zmiennych w aktywnym środowisku:
    ```powershell
    conda env config vars list
    ```
    - ustawianie zmiennych środowiskowych:
    ```powershell
    conda env config vars set my_var=value
    ```
    - po ustawieniu nowych zmiennych przeładować środowisko:
    ```powershell
    conda activate rdu-autogen-sbx
    ```
  - **ustaw poniższe zmienne**, wartości mają charakter ilustracyjny. Ustaw właściwe dla swojego środowiska
    ```
    conda env config vars set autogen_model=gpt-4-turbo090424
    conda env config vars set autogen_api_key=12..34
    conda env config vars set autogen_base_url=https://lazarus-swc.openai.azure.com/
    conda env config vars set autogen_api_type=azure
    conda env config vars set autogen_api_version=2024-02-15-preview
    ```
  - zmienne środowiskowe są przechowywane w pliku (możesz edytować je tam bezpośrednio, jeśli potrzebujesz)
    ```
    [...]\envs\rdu-autogen-sbx\conda-meta\state
    ```

# Autogen Studio
- Uruchomić menu start > Anaconda Prompt
- Otworzy się terminal, w którym wykonać następujące polecenia:
  - conda create -n autogenstudio python=3.11
  - conda activate autogenstudio
  - pip install autogenstudio
- Można zamknąć konsolę
- Uruchomienie (np. po przyjściu do pracy albo restarcie kompa)
- Uruchomić menu start > Anaconda Prompt
- W terminalu anacondy uruchomić:
  - conda activate autogenstudio
  - autogenstudio ui
  - uruchomić przeglądarkę i otworzyć adres: http://127.0.0.1:8081 


# Refs
- https://microsoft.github.io/autogen/
- https://microsoft.github.io/autogen/docs/autogen-studio