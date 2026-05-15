# Spade SDK

Spade SDK provides basic classes to implement Spade Files and Processes.
For more information about Spade, please visit [Spade](https://getspade.io)

It has no dependencies on other Python libraries, and allows development for Spade without
a need to install the full Spade app.

## Installation

```bash
pip install spadesdk
```

### Optional Dependencies

For file validation functionality, install with the `pandera` extra:

```bash
pip install spadesdk[pandera]
```

## Usage

All core classes are available directly from the top-level package:

```python
from spadesdk import Executor, Process, RunResult, File, FileProcessor, FileUpload, HistoryProvider, User
```

## Basic objects

### FileProcessor

`FileProcessor` processes the file uploaded by the user in the Spade app.

#### File Validation

The `FileProcessor` class includes a static `validate` method that can validate file
data against a schema using the Pandera library. This method validates DataFrame data
against a Frictionless schema defined in the `File` object.

**Requirements:**
- The ` spadesdk[pandera]` package must be installed (available as an optional dependency)
- A valid Frictionless schema must be defined in Spade

```
# Validate DataFrame against the schema
FileProcessor.validate(file, dataframe)
```

**Note:** If Pandera is not installed, calling the `validate` method will raise an `ImportError`. If `file.schema` is `None`, a `ValueError` is raised.

### Executor

`Executor` executes a Spade process, either by directly running Python code or by
calling an external service.

### HistoryProvider

`HistoryProvider` provides the history of a Spade from if the actual process is executed
by an external service. If the process is executed in Spade, a `HistoryProvider` is not
needed.

**Note:** The `get_runs()` method receives a `request` parameter that is expected to be
a Django HTTP request object. `HistoryProvider` implementations are therefore coupled to
Django.

## Releasing

Releases are published to PyPI automatically via GitHub Actions when a version tag is pushed:

```bash
git tag 0.5.0
git push origin 0.5.0
```

The workflow builds a wheel and sdist with `uv build`, then publishes using OIDC trusted publishing (no API token needed). Requires a `pypi` environment configured in the GitHub repository settings.
