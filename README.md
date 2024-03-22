
# bprofanity

![Static Badge](https://img.shields.io/badge/release-0.1-blue)

A Python package for detecting and filtering profanity from bangla text.

## How It Works

The "bprofanity" module specializes in detecting and handling Bangla profanity. By utilizing a Trie data structure, it efficiently identifies Bangla profanity slangs and offers functions for censorship, counting occurrences, and checking for profanity in text data. This module ensures accurate and targeted detection of Bangla profanity, enhancing content moderation for Bangla-language platforms.
## Installation

Install "bprofanity" with pip

```bash
pip install bprofanity
```
## Usage/Examples

```python
from bprofanity import ProfanityChecker
import os

profanity_checker = ProfanityChecker()
profanity_checker.load_words()

input_text = "Some text with a bad word like Bal"

profanity_checker.contains_profanity(input_text)
# True

profanity_checker.censor(input_text)
# Some text with a bad word like ***

profanity_checker.censor_count(input_text)
# 1
```

