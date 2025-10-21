# Simple Boutique QA Test Suite

A targeted Selenium test framework that validates e-commerce workflows. Built to handle real shopping scenarios, not just login-logout.

## The Stack
- **Python 3.8+** - Because it's readable and gets the job done
- **Selenium 4** - Modern browser automation
- **Pytest** - Test runner that doesn't suck
- **Page Object Model** - So you don't hate yourself in 6 months

## Setup 
```bash
pip install -r requirements.txt
```

## Running Tests
```bash
# Run the full suite
pytest shopper_tests.py -v


```

## What It Tests
- **Premium shopper journey** - Complete purchase flow with multiple items
- **Guest browsing** - Cart interactions without commitment  
- **Error scenarios** - Handling problematic user flows
- **Data-driven testing** - Different customer profiles and products

## File Structure
```

├── shopper_tests.py    # Main test scenarios
├── page_objects/                # UI interactions live here
│   ├── boutique_pages.py # Page classes for the boutique
│   └── test_data_manager.py     # Customer profiles & test data
└── 
```



## Output 
- Console logs showing each test step
- HTML test reports
- Screenshots automatically captured on failures
- Clear pass/fail status for each scenario

