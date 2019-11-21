# Strategy Editor SDK

This repository contains an SDK for writing Python strategies for the margin application
found at [margin.io]().

This package is available for Python 3.6 or higher through pip
```
pip install margin-strategy-sdk
```

You can import all classes and functions in your strategy by calling
```
from margin_strategy_sdk import *
```

**Note: The SDK does not provide any functionalities but merely mimics margin's strategy 
development interface. To actually run your strategy you need to start it from the margin 
application.**

The easiest way to start off your strategy implementation is by cloning the strategy
template found at https://github.com/MarginOpenSource/strategy-template.

Also check out the official strategies by margin at
https://github.com/MarginOpenSource/official-strategies and community created strategies
at https://github.com/MarginOpenSource/community-strategies.
