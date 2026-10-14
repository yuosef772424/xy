# 10 · Market & Feasibility Research

> **Goal:** Before designing anything, know what already exists, what users want, what makes us different, and whether the project is worth building at all. · **Read when:** step 1 of [architecture planning](11-architecture.md); refresh it at major milestones. · **Pays off because:** it prevents building the wrong thing, missing features competitors prove users need, or ignoring a better existing solution. These are the costliest mistakes a project can make.

This is **deep research** (level 3 in [01](01-judgment.md)), and one of the best uses of the budget ([08](08-efficiency.md)). Run it through research agents that return structured summaries; the findings feed the Must/Should/Could list in [12](12-architecture-rules.md).

## Step 1 · Find as many similar products as possible

Find **as many relevant products as it takes to see the landscape** (often 10–25), covering:

- **Direct competitors:** same problem, same users.
- **Indirect competitors:** same problem, solved differently (including spreadsheets, manual work, or "doing nothing").
- **Open-source projects:** the code, architecture, and issue trackers are free lessons.
- **Adjacent products:** the same users with a neighboring problem; possible future competitors or partners.
- **Dead products:** startups that tried and shut down. Find out why.

Where to look: web search, app stores, Product Hunt, G2/Capterra, GitHub, Hacker News and Reddit discussions, "alternatives to X" lists, and industry reports.

## Step 2 · Analyze what they offer

For each product, record:

- core features, target users, pricing model and prices;
- strengths (what users praise in reviews);
- **weaknesses (what users complain about); these are our opportunities;**
- technology and architecture, where visible (especially for open source);
- traction signals: users, reviews, funding, update activity.

Summarize as a **feature matrix** (products × features) and a short profile for each of the top 5.

## Step 3 · Define our differentiation

Answer honestly:

1. What do users repeatedly complain about across competitors?
2. Which user segment is under-served?
3. What will we do **clearly better**, not just "also"? Better on what: price, simplicity, a specific feature, language, region, integration, or performance?
4. Why can't the big competitors easily copy it?
5. **The one-sentence positioning:** "For <users> who <need>, <product> is the <category> that <key benefit>, unlike <alternative>."

If there is no clear answer to 3, say so. That is a key finding, not a failure of the research.

## Step 4 · Check feasibility

| Dimension | Questions |
|---|---|
| **Demand** | Is there evidence people want this (search volume, community requests, competitor revenue, waitlists)? |
| **Market** | Rough size of the reachable market. Is it growing? |
| **Technical** | Can we build the MVP with the available skills, tools, and budget? What are the hardest technical risks? |
| **Cost & time** | Rough build and running cost; time to MVP. |
| **Business** | How does it make money or reach its goal? Is that realistic given competitor pricing? |
| **Legal / compliance** | Licensing, data protection, regulated domains, app store rules. |
| **Risks** | Top 3–5 risks, each with a likelihood, an impact, and a mitigation. |

## Step 5 · Give a verdict

End with one of these:

- **GO:** clear demand and clear differentiation; the risks are manageable.
- **GO WITH CHANGES:** viable if we change X (a narrower niche, a different feature focus, a different pricing model).
- **NO-GO:** the reasons, and what evidence would change the verdict.

Per [01 · Judgment](01-judgment.md): a NO-GO or GO-WITH-CHANGES verdict is a valuable result. Don't bend the research toward the answer the owner hopes for.

## Output

`RESEARCH.md`, using [the template](../templates/market-research.md), with sources linked for every important claim and a date on each finding (market data goes stale).

## Anti-patterns

- Finding 3 competitors and concluding "the market is open".
- Listing features without reading user reviews.
- A differentiation of "we'll do it better" with no specifics.
- Skipping feasibility because the owner is excited.
- Research that never ends: stop once the verdict is clear and stable.
