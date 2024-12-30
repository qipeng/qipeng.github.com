---
layout: post
title: What do industry researchers do, anyway? Part 2 -- What do they do when they are not publishing
description: >
    Many people seem to "disappear" from the academic publication scene once they graduate from their PhD and join industry research labs. What are they actually doing when they are not publishing? What do they have to show for their research work if they don't publish?
date: !!timestamp '2024-07-22 12:00:00'
tags:
    - Research
    - Industry
head: >
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@qi2peng2">
    <meta name="twitter:creator" content="@qi2peng2">
    <meta name="twitter:title" content="What do industry researchers do, anyway? Part 2 -- What do they do when they are not publishing">
    <meta name="twitter:description" content="Many people seem to "disappear" from the academic publication scene once they graduate from their PhD and join industry research labs. What are they actually doing when they are not publishing? What do they have to show for their research work if they don't publish?">
    <meta name="twitter:image" content="https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=3570&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
    <meta property="og:image" content="https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=3570&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
    <style>
    th { font-weight: bold; min-width: 120px; padding: 5px; border-bottom: 1px solid rgb(102,123,144);}
    td { padding: 5px; }
    table { border-top: 2px solid rgb(52,73,94); border-bottom: 2px solid rgb(52,73,94); margin: 20px 30px;}
    blockquote {
    border-left: 3px solid #aaa;
    margin: 1.5em 10px;
    padding: 0.5em 10px;
    quotes: "\201C""\201D""\2018""\2019";
    }
    blockquote:before {
    color: #aaa;
    content: "“";
    font-family: "Times New Roman", serif;
    font-size: 4em;
    line-height: 0.1em;
    margin-right: 0.25em;
    vertical-align: -0.4em;
    }
    blockquote p {
    display: block;
    margin: 0 3em;
    }
    blockquote footer {
    display: block;
    float: right;
    }
    </style>
---

<figure>
<center>
<img src="{{ '/blog/what-do-industry-researchers-do-part-2/patrick-tomasso-Oaqk7qqNh_c-unsplash.jpg' | relative_url }}" width="90%">
</center>
<figcaption>Photo by <a href="https://unsplash.com/@impatrickt?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Patrick Tomasso</a> on <a href="https://unsplash.com/photos/open-book-lot-Oaqk7qqNh_c?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>.</figcaption>
</figure>

One day in 2020, I was with my PhD advisor Chris Manning in one of our regular meetings. At this point, most of my PhD-ing work are wrapping up, so our conversations have gradually shifted towards me absorbing Chris' wisdom on meta-research topics and career outlook. I remember myself asking, "Why does it seem like industry research people 'disappear' after they graduate and many stop publishing?" Chris thought for a while and jokingly said, "Because they got fat and lazy -- or, *lean* and lazy, since many of them are more fit after working a few years." I understood that Chris was partly referring to the usually improved work-life balance of industry researchers compared to their former PhD selves, but surely, that cannot have explained *this* much of a difference, right?

Fast forward to about two years later, I was interviewing for jobs in early 2022. Until that point, I had been working at JD.com AI Research as a research scientist, where my team is almost solely focused on publishable research, and did not feel too different from a university lab. With a focus on applied research roles for this move, I find myself asking my interviewers, "What does your day-to-day work look like?" Much to my dismay, some interviewers told me that their day-to-day mostly involved optimizing models for size, accuracy, and latency in solving specific machine learning tasks, which was not exactly the innovative work for products that impact real people that I was more looking for. Is that really *it*? Is there nothing more to applied research work? Looking back, I don't really blame the interviewer for this answer when put on the spot like that, I probably wouldn't be able to give a more comprehensive picture had I not thought about this question.

Knowing what I know today, I hope to give my younger and less experienced self a better answer to these questions, and hope this benefits someone with similar questions at similar career stages today ([obligatory disclaimer on what I know](/blog/what-do-industry-researchers-do-part-0/#why-might-you-want-to-continuestop-reading)).

## Why don't industry researchers publish as much?

By and large, an average researcher publishes less when they move from academia to industry. Like every statistical story, there are notable exceptions to this average trend, but that's not what we are focusing on here. So what is it about industry research and its researchers that make them produce less published research works?

This is a perfect example where the [Anna Karenina principle](https://en.wikipedia.org/wiki/Anna_Karenina_principle) is at play. Simply put, **all published papers are alike, each unpublished paper is unpublishable in its own way**. More specifically, for (industry) researchers to publish papers, a number of factors need to be satisfied to a reasonable degree to allow for the paper-writing work to take place -- which is often harder to simultaneously satisfy in industry labs. A few key factors, in my mind, include: interest, incentive, team priorities, and time.

**Interest** is an important factor that is intrinsic to each researcher. I believe interest in research is of paramount importance, because most of the time research projects are not smooth sailing -- this is true even for some of my own work that went really smoothly from ideation to fruition. There will be research challenges that are much harder for the uninterested mind to comprehend and solve; for industry researchers, even if the research challenge itself is interesting and exciting, there are usually more hoops to jump through (e.g., dataset permissions/release review, various legal/business/budget/publicity approvals, to name a few) that will take the lead researchers some inner-drive to overcome.

One thing that is perhaps not anticipated or appreciated enough by folks in the thick of their PhDs, is that people's interest shift and change faster and more often than you might expect. People might fall out of love with the kinds of academic research they have been doing for years during their PhD, either by changing research topics or dropping out of doing research altogether. The industry is also a good source of myriads of applied research problems that are specific to its own scale, the kinds of customer scenarios it needs to deal with, and how it operates. These can often be equally challenging and attractive to researchers that are looking to solve interesting problems, and they sometimes even require more holistic solutions that is typically needed by a publishable research prototype. This can often lead to very fulfilling research careers that do not lead to publications (or at least as many of them).

**Incentive** is a longer-term extrinsic mechanism that influences how we work and how we work together. This is important because it determines how things are viewed and prioritized by you and your peers on a longer time horizon. Incentive is complex and influences different individuals differently, but the overall culture and atmosphere that results from it forms an implicit contract for a group of people to coordinate and achieve shared goals together. There are a lot of different incentives industry research jobs provide, and different people might be incentivized by (a combination of) different things at different times. These might include: higher pay, a more comfortable life, work-life balance, solving unique problems that are not available elsewhere (in some cases, the solution might not be entirely novel-from-scratch or might not generalize elsewhere), making progress on the corporate career ladder (getting higher numerals behind the "Level" word or getting more people to report to you), building cool products for internal or broader social recognition, working on great industry-scale research works, etc. Having a diverse set of incentives means that you would need to pick and choose which ones matter to you the most to spend your time and energy on. Oftentimes these do not directly contribute to publishing, and publishing is not a notable contributor to many of these goals. That's how you can easily have a few productive years as an industry researcher, but not necessarily many published papers to show for it.

Of course, incentives from your employer are not necessarily what you are optimizing for. Some people are largely oblivious to the career incentives in front of them, and choose instead to focus on what they are truly passionate about, which for some people is published research. There is absolutely nothing wrong with that, because more often than not, if your employer's incentives are pulling you away from what you enjoy the most at work, and if you do a great job at meeting the goals they incentivize, you will likely have even less time for your passion. Others publish to stay in touch with the research frontier, and to have something to talk about during their interviews should they decide to change jobs. A publication record could help a bit for your prospective employers to understand your skill set, and recent publications show that you are still familiar with the publishing game. But as long as you are not interviewing for a junior research role, publications are unlikely what takes up the most time in your interview discussions, in my experience.

**Team priorities** is how incentives and goals are manifested in more day-to-day decision making processes within your team. Among other things, priorities can determine how resources are allocated, which is a key enabler for many endeavors, including publishable research works. Here, "resources" is an often overly generalized term, which can include physical resources like funding, equipment, computational resources, etc., as well as personal bandwidth resources, including the bandwidth of in-house data experts, that of your collaborating researchers, and even that of your own. These can sometimes make huge differences in the journey of your work targeting publication. While I am not one to like over-generalizations most of the time, here it might be useful: resources largely determine the time it takes to produce something meaningful, and the quality of what is produced. In the world of scientific publications, being slow to achieve a high enough quality in research works sometimes means ideas will be scooped or no longer be relevant with new waves of technology.

Besides resources, another way that team priorities influence publications is in how it sets boundaries for acceptable behaviors from time to time. For instance, many industry researchers will be involved in somewhat secretive projects throughout their career, where not only is the timeline often tight, but also the need to protect trade secrets often a high priority. This sometimes means that even if resources are at your disposal, and that the results you are generating are exactly the kind that is relevant in the scientific literature at this moment, you might not be allowed to publish them at your liberty until a much later date, if at all.

**Time** is a valuable thing.[^1] Here, I am not just referring to how people choose to spend the nominal 40 working hours of the work week, but also the 144 hours of their typical week. While different people have wildly different working habits (some work 100-hour weeks, others 10-hour weeks), time is fair to everyone, in the sense that nobody gets more hours than others in any given day or week. Therefore, the main difference that accounts for the discrepancy in, for instance, working hours each week, is how we choose to allocate these hours differently.

The profile of a typical PhD student is usually someone in their 20s or 30s,childless, and overall in reasonable health conditions.[^2] Most of them, especially junior students, do not have more than 8 hours of meetings, scheduled discussions, or classes. All of these factor contribute to their energy, ability to concentrate, flexibility of their schedule, and their overall capacity to allocate uninterrupted hours to research-related (or personal health upkeep) activities. Life happens, and most of these factors will gradually (or abruptly) change as people near graduation from their PhD programs. They might start taking up more responsibility at work, start a family, experience the effect of early aging (boo!), decide to place more emphasis on work-life balance and long-term mental health, the list goes on and on. Aside from the natural and gradual course of life, another salient factor that usually contributes to this change is that people often plan their lives to accommodate major milestones in life, e.g., "I'll wait until I graduate to do such and such", or "once I graduate, I'll make sure to do so and so". All of these can take time and focus away from what is needed for publications, and more often than not, people actually embrace and welcome these changes when they are going through these processes.

### Is it bad if you don't publish as much when working as an industry researcher?

We have covered the various reasons that might lead to reduced publications from industry researchers, but what does it mean for the researchers involved, is it bad that they are not publishing as much?

**The short answer is, it depends a lot on your interests and situation, but generally, it is probably not as bad as you would think**. On the one hand, while many freshly minted PhDs feel a strong sense of FOMO (fear of missing out) when they join the industry for the first few years, they will also quickly learn that publications are just one of the many ways they can contribute to their employer or even the research community, and as a result they might choose to focus their time on fewer publications with more concentrated topics/flavors, or pause publishing altogether. On the other hand, if your are concerned about maintaining your competitiveness on the industry job market, stressing over publications is also often unnecessary especially for experienced hires, because your prospective employers are also going to be mindful about all the other ways you can contribute aside from publishing research papers, and focus on assessing those aspects. Sure, having some recent papers on your CV makes it easier for people to get a glimpse into your (current team's) recent interests and gives you something you can more easily talk about, which is a plus, but I think mindfully designed interview processes can help you demonstrate your capabilities even if these are not available.

Note that this statement might not hold as firmly if you are looking for opportunities that have a more pure research flavor (e.g., faculty positions at an R1 university). But even in those cases, the quantity of publications is likely far from the only key objective you should consider optimizing for.

## What are industry researchers doing when they are not publishing?

Even when controlled for the actual number of working hours, I suspect that an average PhD student would still be more productive on publications than an average industry researcher. Why? What are some places where industry researchers spend their time on?

As I [have discussed in a previous post](https://qipeng.me/blog/what-do-industry-researchers-do-part-0/#the-less-talked-about-similarities-between-academic-and-industry-research), a necessary consequence of working in the "real world" (both industry and academia) is that you work a lot more with other people, who are usually more experts in their own fields, but not your field. For more research-y jobs, these could be your peers, junior/senior colleagues, managers, administrators, etc. For more product-y jobs, you might also interact with product managers, engineers (more traditional software engineers as well as machine learning engineers in some cases), designers for user interfaces/experience, data annotators and people that help manage them, data scientists, research people that are more on the research or applied end of the spectrum than yourself, sales/marketing people, etc.

[ConvAI paper against tech solutionism](https://arxiv.org/pdf/2105.06457)

who do industry researchers work with?
Functions that a typical product or business might require:

- Product management
- Engineering (including MLE)
- Design / UX
- Marketing
- Finance
- Data annotation
- Data science
- Research / Applied Science

what are they working on?
- product-related work in general
    - internal prototyping, benchmarking
    - design
    - implement / work with others to implement
    - troubleshoot and solve issues
    - with live systems come great responsibility: scale, backwards compatibility, future compatibility, latency, cost,

#### Footnotes
[^1]: If you got the lyrical reference here, I am happy to share that [this song](https://en.wikipedia.org/wiki/In_the_End) was originally published in 2000, almost two and a half decades old now.
[^2]: This is by no means representative of all PhD students everywhere, but more derived from my personal experience with the majority of PhD students in the U.S. and China.