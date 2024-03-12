from cx_Freeze import setup, Executable

# Replace these values with your actual file names
files = ['bg.jpg', 'mic.jpg', 'Thiruvalluvar.jpg', 'Thirukural.csv', 'Thirukkural.py']

# Dependencies
build_exe_options = {
    'packages': ['pandas', 'elevenlabs', 'tkinter'],  # Add any required packages
    'include_files': files
}

setup(

       name="Thirukkural APp",

       version="1.0",

       description="simple thirukkural bot that uses nlp model",

       options={'build_exe': build_exe_options},

       executables=[Executable("Thirukkural.py")],
)   