# Using AI as a Learning Partner

**Read before:** Week 1 | **Time:** 10 minutes

AI tools like ChatGPT, Claude, and GitHub Copilot can be powerful learning aids—but like any tool, their value depends on how you use them. This guide helps you use AI effectively without undermining your own learning.

## The core principle

**AI should help you understand, not replace your understanding.**

There's a difference between:

- "AI, write me a script that does X" → You have a script but don't know how it works
- "AI, explain how to do X and walk me through the code" → You understand and can adapt it

The first approach gets you an answer. The second builds skills you'll use throughout your career.

---

## When AI helps learning

### Debugging error messages

Error messages can be cryptic. AI excels at translating them into plain language.

**Good prompt:**
```
I'm running this GeoPandas code and getting this error:
[paste your code]
[paste the full error message]

What does this error mean, and how can I fix it?
```

**Why this works:** You're asking for explanation, not just a fix. You'll understand the error next time you see it.

### Explaining unfamiliar code

When you encounter code you don't understand:

**Good prompt:**
```
Can you explain what this code does, line by line?
[paste code]

I'm new to Python and don't understand what .groupby() does.
```

**Why this works:** You're building understanding of specific concepts, not asking AI to write code for you.

### Installation and setup issues

Environment setup can be frustrating. AI can help diagnose configuration problems.

**Good prompt:**
```
I'm trying to install geopandas on Mac using conda and getting this error:
[paste error]

I already tried [what you tried]. What else should I check?
```

**Why this works:** You've shown what you attempted, so AI can help you learn from the specific problem.

### Understanding concepts

AI can be a patient tutor for conceptual questions.

**Good prompt:**
```
I'm learning about coordinate reference systems. Can you explain:
1. What a CRS actually represents
2. Why I need to reproject data
3. How to choose the right CRS for Australia

Use simple language - I'm a beginner.
```

---

## When AI hinders learning

### Writing code you don't understand

If AI writes your entire script and you can't explain what each line does, you haven't learned—you've outsourced.

**Warning signs:**

- You can't modify the code when requirements change
- You don't know why a particular function was chosen
- You couldn't write similar code without AI

**Better approach:** Ask AI to explain the approach first, then try writing the code yourself. Use AI to check your work or debug issues.

### Skipping the struggle

Some frustration is part of learning. When you work through a problem yourself, you build problem-solving skills and deeper understanding.

**The productive struggle zone:**

- Stuck for 5 minutes? Keep trying, check documentation
- Stuck for 15-20 minutes? Try a different approach, search online
- Stuck for 30+ minutes with no progress? AI can help unstick you

Don't skip straight to AI—give yourself a chance to learn from the challenge.

### Copy-pasting without reading

If you paste AI output directly into your code without reading and understanding it, you're building a house of cards that will collapse when something goes wrong.

**Better approach:** Read every line AI gives you. If you don't understand something, ask AI to explain that specific part.

---

## Good AI prompting practices

### Be specific about your context

**Weak:** "How do I make a map?"

**Strong:** "I'm using GeoPandas in Python to create a choropleth map of population density by suburb. I have a GeoDataFrame with a 'pop_density' column. How do I add a legend and title?"

### Share your code and errors

AI can't help with vague descriptions. Include:

- The actual code you're running
- The complete error message
- What you expected to happen
- What actually happened

### Ask for explanations, not just solutions

Add phrases like:

- "...and explain why this works"
- "...walk me through the logic"
- "...what would happen if I changed X?"

### Verify AI outputs

AI makes mistakes. Always:

- Read the code before running it
- Test with simple examples
- Check that the output makes sense
- Cross-reference with documentation for important functions

---

## AI and academic integrity

### What's usually acceptable

- Using AI to debug error messages
- Asking AI to explain concepts or code
- Getting help with installation and setup
- Using AI to brainstorm approaches (then implementing yourself)

### What's usually not acceptable

- Having AI write your assignments
- Submitting AI-generated work as your own
- Using AI during exams (unless explicitly allowed)

### The key question

Ask yourself: "If someone asked me to explain this code/analysis, could I do it confidently?"

If yes, you've learned something. If no, you've outsourced learning and will struggle later.

### When in doubt, cite

If you used AI to help with something, mention it:

> "I used ChatGPT to help debug an error with my CRS transformation"

This is honest and shows good practice.

---

## Effective learning workflows

### The "attempt first" workflow

1. Try the task yourself (15-20 minutes)
2. If stuck, clearly define what you don't understand
3. Ask AI for explanation/guidance
4. Try again with new understanding
5. If still stuck, ask AI for more specific help

### The "explain back" test

After AI helps you:

1. Close the AI chat
2. Try to explain the solution in your own words
3. Write the code again without looking at AI's version
4. If you can't, you need to understand it better

### The "modification" test

Take AI-generated code and:

1. Change a parameter and predict what will happen
2. Add a new feature
3. Adapt it for different data

If you can do this, you understand the code. If not, ask AI to explain the parts you can't modify.

---

## AI for GIS specifically

### Where AI helps in GIS

- Explaining CRS and projection concepts
- Debugging GeoPandas/QGIS errors
- Suggesting appropriate spatial analysis methods
- Explaining what parameters do in processing tools

### Where AI struggles in GIS

- Knowing your specific data (always describe it clearly)
- Making cartographic judgment calls (design is subjective)
- Understanding local geographic context
- Choosing appropriate boundaries or classifications (these are your decisions)

### Example GIS prompts

**For debugging:**
```
My spatial join returns no matches. Here's my code:
[code]
The left GeoDataFrame has CRS EPSG:4326, the right has EPSG:7844.
What might be causing the empty result?
```

**For learning:**
```
I'm trying to decide between Equal Interval and Quantile classification
for a choropleth map of income data that has some very high outliers.
What are the tradeoffs of each method?
```

**For setup:**
```
I'm getting "GDAL not found" when importing geopandas in my conda
environment on Windows. I installed with: conda install geopandas
What should I try?
```

---

## Summary

| Do | Don't |
|----|-------|
| Ask AI to explain concepts | Ask AI to do your work |
| Use AI to debug errors | Skip reading error messages yourself |
| Verify AI outputs | Trust AI blindly |
| Try yourself first | Go straight to AI |
| Ask "why" and "how" | Just copy-paste solutions |
| Cite AI assistance | Hide AI use |

**Remember:** The goal is to become a capable GIS analyst, not someone who depends on AI to do basic tasks. Use AI to accelerate your learning, not to avoid it.

---

*This course welcomes thoughtful AI use. If you're unsure whether something is appropriate, ask your instructor.*
