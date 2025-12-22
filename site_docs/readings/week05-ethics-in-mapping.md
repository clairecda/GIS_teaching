# Ethics in Spatial Analysis

**Read before:** Week 5 | **Time:** 20 minutes

---

## Why ethics matter in GIS

Maps are powerful. They influence decisions, shape perceptions, and can harm communities if used carelessly.

When you map crime, health, or demographics, you're not just displaying data — you're telling a story that affects real people and places.

---

## The power of maps

Maps can:
- **Reveal patterns** that help allocate resources fairly
- **Expose inequalities** that need attention
- **Reinforce stereotypes** if presented without context
- **Stigmatise communities** labelled as "high crime" or "disadvantaged"
- **Justify discrimination** in lending, insurance, or policing

**The same data can help or harm depending on how it's mapped and communicated.**

---

## Key ethical issues

### 1. Privacy and identifiability

**Problem:** Detailed maps can reveal where individuals live.

**Examples:**
- Mapping individual crime incidents could identify victims
- Health data at fine resolution could expose patient locations
- Poverty maps could stigmatise specific households

**Solutions:**
- Aggregate to larger areas (SA2 instead of points)
- Use counts rather than exact locations
- Apply jittering (random offset) to point data
- Check if the data publisher has guidelines

### 2. Bias in data

**Problem:** The data you map may not represent reality fairly.

**Examples:**
- Crime data reflects policing patterns, not just crime
- Complaints data shows who reports, not who's affected
- Survey data may underrepresent certain communities

**Questions to ask:**
- Who collected this data and why?
- Who is missing or underrepresented?
- What assumptions are built into the categories?

### 3. Context and framing

**Problem:** Maps without context can mislead.

**Examples:**
- "High crime" in absolute numbers vs per capita rates
- Comparing areas of vastly different population sizes
- Showing change without explaining what changed

**Solutions:**
- Use rates, not just counts (per 1,000 population)
- Provide temporal context (compared to when?)
- Acknowledge limitations in titles and captions
- Show comparison to averages or benchmarks

### 4. The ecological fallacy

**Problem:** Patterns at area level don't apply to individuals.

**Example:**
- A suburb has high average income
- Doesn't mean everyone there is wealthy
- Some residents may be struggling

**Reminder:** You're mapping areas, not people. Don't make individual-level claims from area-level data.

### 5. Unintended consequences

**Problem:** Your map may be used in ways you didn't intend.

**Examples:**
- Hotspot maps used to justify over-policing
- Disadvantage maps used to deny services or investment
- Health maps used to discriminate in insurance

**Questions to ask:**
- Who might use this map?
- How could it be misused?
- Should I add caveats or limit distribution?

---

## Crime mapping specifically

Crime maps are among the most ethically complex. Consider:

### What you're actually mapping

| Data type | What it measures | What it misses |
|-----------|------------------|----------------|
| Reported crime | What people report | Unreported crime |
| Arrests | Who police arrest | Crimes without arrests |
| Convictions | Court outcomes | Innocent people arrested |
| Calls for service | Demand for police | Areas with low trust in police |

**None of these = actual crime.** They measure system activity.

### Hotspot mapping risks

- Labels neighbourhoods as "dangerous" based on limited data
- Can justify increased policing, which finds more crime, which confirms the label
- Ignores reasons behind patterns (poverty, lack of services, historical factors)

### Responsible approaches

- Map rates, not just counts
- Include temporal context (crime this year vs last year)
- Acknowledge data limitations
- Consider who benefits and who is harmed
- Ask: would I publish this if I lived there?

---

## Health and disadvantage mapping

Similar issues apply:

- **SEIFA/SVI maps** can stigmatise areas as "disadvantaged"
- **Health outcome maps** might blame communities for structural problems
- **Service access maps** could be used to cut rather than add services

**Frame positively when possible:** "Areas for investment" vs "disadvantaged areas"

---

## Practical guidelines

### Before mapping

1. What is the purpose of this map?
2. Who will see it and use it?
3. Could it harm the communities shown?
4. Is the data appropriate for this purpose?

### During analysis

1. Aggregate to protect privacy
2. Use rates not just counts
3. Compare to meaningful benchmarks
4. Acknowledge data limitations

### When presenting

1. Title carefully — avoid stigmatising language
2. Add context in captions and legends
3. Note what the data doesn't show
4. Consider your audience

### Questions to ask

- If I lived in this area, would I want this map published?
- Am I reinforcing stereotypes or challenging them?
- Have I acknowledged uncertainty and limitations?
- Could someone misuse this map? How do I mitigate that?

---

## Key takeaways

✅ **Maps have power** — they influence decisions and perceptions

✅ **Data reflects systems** — crime data reflects policing, not just crime

✅ **Aggregation protects privacy** — don't map individuals

✅ **Context matters** — rates, comparisons, limitations

✅ **Consider consequences** — how might this map be used or misused?

✅ **Frame carefully** — words matter as much as colours

---

## Reflection questions

Before Week 5, think about:

1. Have you seen maps that stigmatised communities? What made them problematic?
2. How would you feel if your neighbourhood was mapped as a "hotspot"?
3. What's the difference between mapping crime and mapping policing?
