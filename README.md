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

## License
The source code is published under the MIT License:

MIT License

Copyright (c) 2019 Margin Open Source

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
