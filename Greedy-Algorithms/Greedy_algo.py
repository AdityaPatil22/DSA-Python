"""
What is a Greedy Algorithm?
A greedy algorithm makes the best possible decision at the current moment without worrying about future decisions.


When does Greedy Work?

Greedy does not always work.
A problem must satisfy two properties.

Property 1: Greedy Choice Property
Making the best local decision should eventually lead to the global optimum.
Example
Activity Selection
Always pick the activity that finishes earliest.
Turns out this always produces the maximum number of activities.

Property 2: Optimal Substructure
After making one decision, the remaining problem should be solvable optimally in the same way.
If these aren't true, Greedy usually fails.

How to Recognize a Greedy Problem?

Look for words like

Maximum
Minimum
Earliest
Largest
Smallest
Non-overlapping
Merge
Interval
Scheduling
Meeting
Jump
Reach
Gas
Cookies

If you can make a decision without needing to reconsider it later, greedy might work.

How to Think During Interviews

Always ask:

Question 1
Can I make the best choice now?

Question 2
Will I ever regret making this choice?
If yes, Greedy probably won't work.

Question 3
Can I prove this decision is always safe?
Interviewers love this reasoning.
"""

# General Greedy Temmplate
def greedy(arr):
    arr.sort()       # sometimes
    answer = ...
    for item in arr:
        if good_choice(item):
            take(item)
    return answer