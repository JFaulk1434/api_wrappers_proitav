# api_wrappers_proitav

A collection of API wrappers to use in Python

## Setup

run `pip install .` to install this package locally. Must be ran from this directory.

## Importing

`from apiwrappers import IP5100` is an example of how to import into your package.

## Setup for Distribution via Github

Yes, distributing your Python package via GitHub is a very common and effective way to share your code, especially if you want to keep the package semi-private or make it available for easy installation without the formality of PyPI. Here's how you can do it:

### 1. Host Your Package on GitHub

First, ensure your package (with the proper structure and `setup.py` file) is uploaded to a GitHub repository. This includes all necessary source files, a README with installation and usage instructions, and any other relevant documentation.

### 2. Installable via `pip`

Users can install your package directly from GitHub using `pip`. To enable this, you need to ensure your `setup.py` is properly configured as mentioned in previous messages. Here's how someone would install your package directly from GitHub:

```bash
pip install git+https://github.com/yourusername/yourrepository.git
```

You can also specify a particular branch, tag, or commit if you want to install something other than the main branch:

```bash
pip install git+https://github.com/yourusername/yourrepository.git@yourbranch
```

### 3. Requirements for Easy Installation

- **Public Repository**: If the repository is public, anyone can install the package using the command above.
- **Private Repository**: If it's private, the user will need to have access to the repository. GitHub can handle authentication via SSH keys or a GitHub access token. Users installing from a private repository will need to configure their environment to authenticate correctly with GitHub.

### 4. Versioning

- **Tags for Releases**: Use Git tags to mark releases. This helps users to install specific versions of your package instead of pulling the latest commit from the main branch. You can install using tags like so:

```bash
pip install git+https://github.com/yourusername/yourrepository.git@v1.0.0
```

### 5. Dependency Management

- **Dependencies**: Ensure that your `setup.py` file accurately lists all dependencies. `pip` will attempt to resolve and install these dependencies automatically when installing your package.

### 6. Advantages of GitHub Distribution

- **Collaboration**: GitHub provides tools for managing issues, pull requests, and version control, which are invaluable for collaborative development.
- **Accessibility**: Easy for users to see the source code, issues, and how the project evolves over time.
- **Documentation and Examples**: Host your documentation directly alongside your code, perhaps in the repository wiki or in markdown files.

Using GitHub to distribute your package is particularly useful for collaborative projects, beta releases, or when you wish to maintain tighter control over who accesses the package. This approach simplifies many aspects of package distribution and user collaboration.
