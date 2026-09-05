# The 10^8 rule
[![The 10^8 rule](https://img.youtube.com/vi/vQvIpviNWdQ/0.jpg)](https://youtu.be/vQvIpviNWdQ)


When we try to solve a programming problem, we have to compare solutions. For example, here is duplicate interger problem.
nums = [1, 2, 2, 3] res = True because nums contain duplicates interger.
Bruteforce plan's time complexity is O(n^2).
Hashset plan's time complexity is O(n).
Which plan is better?
Of course A is efficient and smart.

But there are more conditions.
bruteforce's O(1), Hashset is the space complexity is O(n).
Which one is better?

In this case, we should confirm the range of n.
If maximum of n is really bigger, we have to think of more efficient approach.
Otherwise maximum of n is less, we can choose brute force approach.

Here's The 10^8 rule.

The ten to the power of eight rule is a rule of thumb based on typical CPU speeds and the overhead of high-level operations.
This rule can be used to check if an algorithm will pass within a standard 1-second time limit.

## Why is 10^8?
It’s a balance between CPU Clock Speed and Instruction Overhead.
Modern CPUs run at roughly 2–4 GHz (2 times 10^9 to 4 times 10^9 cycles per second).

One operation in your code(like an array access, and addition) is not one CPU cycle. It involves multiple low-level instructions, cache fetches, and branch checks.
So to ensure a solution passes across different judge environments, we use 10^8 as a conservative estimate.

Generally, 
- Go: 2 * 10^8 ~ 5 * 10^8
- C++ or Rust: 10^8 ~ 5 * 10^8
- Jave/C#: 10^7~10^8
- Python: 10^6 ~ 10^7 because Python is interpreted language. It running line by line so a lot of overhead. So slow.

## Why is 1 second time limit?
Most Online Judges seta Time Limit of 1,0 to 2.0 seconds per test case.
And it is the industry standard for measuring algorithmic efficiency.


Let's wrap up.
Keep in mind to be careful of constraints and time complexity.
If n is greater than 10^4, we shouldn't use O(n^2) approach, for example duplicates loops brute force.
On the other hand, if maximum of n is less than 10^4, you have some choices.