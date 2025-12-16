    main-folder-in-slug-case
        data
            raw
            cropped
            extracted
            labeled
        docs
            architecture.md
            hardware.md
            performance.md
            resources.md
            edge-cases.md
        models
        notebooks
        src
        tests
            make these as .py based on issues figured out in dev
        .gitignore
        README.md
        requirements.txt
        venv


__init__.py
- use this file to tell python that the directory is a package
- a package is a collection of modules that do things
- 'separation of concerns' means that one module should do one thing, and then main.py ties them together
- when you add __version__ = "0.0.1" and __author__ = "..."
Then you can
''' import src
''' print(src.__version__)

Within main.py, you then import your modules. i.e. from control_mappings import ControlHandler

Within each .py module, you define a class which is a 'thing' that does something. 


