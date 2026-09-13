# Project Euler First 100 Solutions.
I have used Project Euler to continue my learning of both math and programming after the completion of CS50P. 

Here you can find my solutions to the first 100 problems. I do not claim these solutions to be perfect- they likely aren't, I'm certain there are places where I got the correct answer but an edge case would have tripped up on the same algorithm. However, they are mine. 

In spirit of Project Euler, I will only publish solutions to the first 100 problems.

# Problem Solving Process
I follow the same process for most problems.
## 1. Choose the next Problem I want to solve.
At any given time I have a few problems "on deck" that I've seen and determined are probably the correct difficulty level. I choose whichever one looks the most obtainable. 

## 2. Brainstorm the Problem
I read the problem, perhaps before bed or before a car ride, or maybe over lunch. I'll usually either start with pen/paper or maybe create the file the problem will be solved in and comment out a section to start thinking about the following:
- What is this problem asking for? A single value, a list of values (that somehow are trivially modified to a single value for the answer submission), or something else.
- Have I done work in other problems that is useful here? If so, what problems?
- Have I written any functions that are in `functions.py` that could help with this problem?
- Can I write out a logic path in a few sentences of plain english that gets me started?
- Is there any research I need to do on this problem?
- Are there any standard libraries that may help with this problem, while not totally trivializing the concept? For example, I felt it important to write my own `is_prime(n)` function instead of utilizing an existing library. In some of my earlier problems I used `x**.5` instead of `math.sqrt(x)`. 
- Sleep on it. Most of the time I can get a bit further by letting the problem cook in my head overnight. 

## 3. Attempt the problem
Take whatever I have so far (logic paragraph, selected functions, research) and iterate. Write out a draft script and see how it goes. 
Frequently I'll find myself circling back to step 2 here. This is where I may end up receiving assistance (see below).
I attempt to document both assistance and logic as I go but my earlier problems are not documented exceedingly well. I have gotten better at that. 

## 4. Closeout the Problem
Assuming step 3 went well and I wasn't totally defeated I now have a solution. 
Final steps are adding additional documentation (yes, that should have already been done but it isn't always...) and ensuring I preserve any functions that may be useful later in `functions.py`. Lastly, I commit the file to the repo.

# Assistance and Documentation
I occasionally use AI in the form of the `/learn` skill of either ChatGPT or Claude to ask questions about logic if I am stumbling. In these cases I am careful to document where I ventured beyond my own skills. For syntax help I have relied on forums such as stack overflow and occasionally a quick google search. I prefer Google and the inline Gemini for quick syntax help because Gemini almost always scopes narrowly enough to keep me rolling but not so much as to solve the entire problem for me.

## Quote from "About - Project Euler" Page on 8 August 2026:

### "I learned so much solving problem XXX, so is it okay to publish my solution elsewhere?

It appears that you have answered your own question. There is nothing quite like that "Aha!" moment when you finally beat a problem which you have been working on for some time. It is often through the best of intentions in wishing to share our insights so that others can enjoy that moment too. Sadly, that will rarely be the case for your readers. Real learning is an active process and seeing how it is done is a long way from experiencing that epiphany of discovery. Please do not deny others what you have so richly valued yourself.

However, the rule about sharing solutions outside of Project Euler does not apply to the first one-hundred problems, as long as any discussion clearly aims to instruct methods, not just provide answers, and does not directly threaten to undermine the enjoyment of solving later problems. Problems 1 to 100 provide a wealth of helpful introductory teaching material and if you are able to respect our requirements, then we give permission for those problems and their solutions to be discussed elsewhere." Source: https://projecteuler.net/ 8 August 2026
