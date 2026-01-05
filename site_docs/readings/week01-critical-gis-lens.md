# Seeing Assumptions in GIS

**Read before:** Week 1
**Time:** 10 minutes

---

## The invisible choices in every map

Every dataset you'll use in this course was created by someone, for a purpose, using categories that made sense to them. This isn't a flaw—it's simply how data works. But understanding it makes you a better analyst.

Here's a framing you can carry through all semester:

> **GIS doesn't just map the world—it reflects how the world has been understood, governed, and valued.**

---

## Data is produced, not found

When you download a dataset of "hospitals" or "crime incidents" or "land cover," you're not getting raw reality. You're getting:

- **Someone's decisions** about what counts as a hospital (Does urgent care count? Mobile clinics?)
- **Someone's boundaries** that define where data was collected and how it was aggregated
- **Someone's categories** that group complex phenomena into neat boxes

This is normal and necessary—we can't map without categories. But the categories we inherit carry assumptions from the people and institutions that created them.

---

## Three questions to carry through this course

For every dataset you encounter, practice asking:

### 1. Who created this data, and for what purpose?

- Census data is designed for governance and resource allocation. What does it prioritize? What doesn't it ask about?
- Crime data reflects policing patterns—where police patrol, what they prioritize, who reports. What does that mean for "high crime" labels?
- Environmental data often comes from agencies focused on development approvals. What might they not measure?

### 2. What categories are used, and what doesn't fit?

- Land use categories work well for zoning enforcement. Do they capture informal economies? Shared spaces? Temporary uses?
- Health facility lists include hospitals and clinics. What about traditional healers? Community health workers? Pharmacies?
- Employment categories distinguish "employed" from "unemployed." Where do gig workers fit? Unpaid carers? People with multiple part-time jobs?

### 3. What boundaries shape this data, and who drew them?

- Statistical boundaries (SA2, census tracts) are designed to be comparable over time. But they were drawn by institutions with priorities—often administrative efficiency, not community identity.
- Administrative boundaries (councils, districts) reflect political negotiations, historical accidents, and sometimes deliberate manipulation.
- "Natural" boundaries like watersheds or ecosystems are also choices—nature doesn't draw lines.

---

## Why this matters professionally

This isn't about being cynical or distrustful of all data. It's about being rigorous. The best GIS analysts understand:

- **Methodological limitations:** Knowing how data was collected helps you interpret results accurately and avoid overconfident conclusions.
- **Communication responsibility:** When you present a map, you inherit the assumptions baked into your data. Being explicit about them builds trust with your audience.
- **Problem-solving power:** Recognizing what data CAN'T show helps you seek complementary sources and design better analyses.

---

## An example: Mapping "access to green space"

Imagine you're asked to map which neighborhoods have "good access to green space." You download a parks shapefile and calculate distances. Simple, right?

But consider:

- **What counts as "green space"?** Official parks only? Vacant lots with trees? Private gardens visible from the street? Cemeteries?
- **What counts as "access"?** Walking distance? Driving distance? Are there gates, entry fees, or operating hours? Is it safe to walk there after dark?
- **Whose priorities shaped this data?** Parks departments track what they manage. What about informal green spaces that communities actually use but aren't officially designated?

A thoughtful analyst would:

1. Note these limitations explicitly
2. Consider supplementary data (satellite imagery for informal green space?)
3. Frame findings appropriately: "Access to registered public parks" rather than "access to green space"

The map isn't wrong—it just answers a specific question. The skill is recognizing *which* question it answers, and what other questions become harder to ask.

---

## What we're NOT saying

This isn't about:

- **Blaming anyone** for creating imperfect data—all data has limitations
- **Refusing to use data** because it's not perfect—we need data to make decisions
- **Claiming GIS is bad** or that maps are lies—GIS is powerful precisely because it shapes how we see and act

It IS about:

- **Seeing choices** that are often invisible
- **Asking better questions** about the data you use
- **Communicating honestly** about what your analysis can and cannot show

---

## Reflection questions

Before Week 1, think about:

1. Can you recall a map you've seen that left something important out? What was missing?
2. What categories in everyday life don't quite fit the boxes? (Think about forms you've filled out, surveys that didn't have your answer, classifications that felt wrong.)
3. What questions might be genuinely hard to answer with GIS data?

Bring one example to share in the Week 1 discussion.

---

**Key takeaway:** Every dataset answers some questions very well—and makes others almost impossible to ask. Your job as a GIS analyst is to understand both.
