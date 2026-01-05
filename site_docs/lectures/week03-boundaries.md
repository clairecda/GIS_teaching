# Week 3 Lecture · Boundary Systems & Data Joins

## This week
We unpack administrative and statistical boundary systems and learn how to join socio-economic indicators to spatial datasets responsibly.

## By the end of the week you will
- Describe the hierarchy and purpose of common boundaries (SA2, LGA, ADM levels).
- Understand how boundary updates affect longitudinal comparisons and how to mitigate issues.
- Perform attribute joins safely and document assumptions.
- Explain how boundary choices are political decisions, not neutral containers for data.

## Key vocabulary
ADM0/ADM1/ADM2 · SA2 · LGA · correspondence file · join key · area-weighted interpolation.

## Boundaries as power

Administrative boundaries aren't neutral containers for data—they're decisions about who belongs together, who governs whom, and how resources flow.

### Who draws the lines?

When you use SA2 boundaries or census tracts, you're inheriting decisions made by:

- **Statistical agencies** prioritizing data collection efficiency and comparability
- **Political bodies** responding to electoral pressures and governance needs
- **Historical processes** including colonial surveying, land grants, and municipal incorporations

These decisions have consequences:

- **Resource allocation:** Funding formulas tied to boundary-level statistics determine who gets what
- **Community identity:** Statistical boundaries often cut through neighborhoods people experience as unified
- **Political representation:** Boundary drawing can dilute or concentrate voting power (gerrymandering)

### MAUP is technical AND political

The Modifiable Areal Unit Problem isn't just a methodological curiosity—it's a tool of power.

Consider: If you want to show that "disadvantage is concentrated," you can use fine-grained units that highlight pockets. If you want to show "the region is doing fine," you can aggregate to larger areas where local problems disappear.

Same data. Different boundaries. Different policy conclusions.

This doesn't mean boundaries are bad—we need them to function. But it means:

1. Always ask "Who drew these boundaries, and for what purpose?"
2. Test your findings at multiple scales
3. Be transparent about boundary effects in your reporting

## What happens in class
- Review who maintains boundaries (ABS, census bureaus) and why updates occur.
- Demonstrate attribute joins between SA2 and SEIFA, highlighting data-type pitfalls.
- Discuss storytelling implications of choosing different geographies.
- Share troubleshooting techniques (correspondence files, data cleaning) before switching to lab time.

## Prepare beforehand
- Download SA2 + SEIFA datasets using the [data download guide](../onboarding/03-download-data.md).
- Review [Week 3 lecture slides](../slides/week03.html).
- Read [Understanding administrative boundaries](../readings/week03-admin-boundaries.md) and note questions for class.

## Connected lab
The [Week 3 lab](../weeks/week03.md) walks through join workflows, derived metrics, and error checking.

