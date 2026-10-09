# PLP Python Week 3 Assignment: Conditions and Loops

## File Descriptions
- `grade_reporter.py`: Calculates letter grades for a list of scores, outputs pass/fail counts, and computes the average score rounded to 1 decimal place.
- `bug_hunt.py`: Contains a fixed while-loop program that calculates the sum of numbers from 1 to 5, including `# BUG:` explanatory comments for all three resolved errors.

## Bug Reflection
The hardest bug to find in Part B was the condition `count < 5` because it did not trigger any runtime or syntax error messages. The program ran cleanly, but the output was `10` instead of `15`. I knew something was wrong because manually adding $1 + 2 + 3 + 4 + 5$ equals $15$, indicating that the loop was terminating early before adding the final number.
