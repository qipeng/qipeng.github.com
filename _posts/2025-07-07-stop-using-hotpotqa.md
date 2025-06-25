---
layout: post
title: Why You Should Stop Using HotpotQA for AI Agents Evaluation in 2025
description: >

date: !!timestamp '2025-03-12 12:00:00'
tags:
    - Research
    - AI
head: >
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@qi2peng2">
    <meta name="twitter:creator" content="@qi2peng2">
    <meta name="twitter:title" content="Why You Should Stop Using HotpotQA for AI Agents Evaluation in 2025">
    <meta name="twitter:description" content="">
    <meta name="twitter:image" content="https://images.unsplash.com/photo-1695065011505-4f58da58290d?q=80&w=3872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
    <meta property="og:image" content="https://images.unsplash.com/photo-1695065011505-4f58da58290d?q=80&w=3872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
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
thumbnail: https://images.unsplash.com/photo-1695065011505-4f58da58290d?q=80&w=3872&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
---

<figure>
<center>
<img src="{{ '/blog/stop-using-hotpotqa/karsten-winegeart-01RYHGN-Zi0-unsplash.jpg' | relative_url }}" width="90%">
</center>
<figcaption>Photo by <a href="https://unsplash.com/@karsten116?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Karsten Winegeart</a> on <a href="https://unsplash.com/photos/a-traffic-light-with-a-red-heart-on-it-01RYHGN-Zi0?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>.
</figcaption>
</figure>

> That year, humanity launched their first functioning autonomous language agents into their collective cyberspace. Centuries later, historians of the Solar System will look back at this point in time and fully recognize the watershed moment that it was. What was formerly known as Year 2025 in the Common Era is now more colloquially known as Year 1 of the Agent Era.
>
> *-- An attempt at a Three Body-esque sci-fi narrative about AI agents*

Agents, agents everywhere. From countless startups to innumerable social media posts, AI agents are creeping up in your IDEs, your browsers, and perhaps places you are not even looking or consciously aware. Clearly the dominating narrative in artificial intelligence in 2025, "agents", transitive by the share of the public discourse AI is taking up, is firmly one of the most discussed topics in humanity's collective consciousness this year. Despite the fact that we do not even seem to have a shared definition for what AI agents are, we all seem to have developed a warm and buzzy feeling about them, and sincerely believe (or hope) that they are "the next big thing that changes everything as we know it".

If you are following frontier AI agents research closely, you might have come across a name called HotpotQA, that is somewhat often discussed in these research works. What is HotpotQA, and what does it have to do with the AI agents today?

### HotpotQA
Back in 2018, some awesome collaborators (from CMU and U de Montreal) and I published a paper called HotpotQA, which features a novel (at the time) idea of question answering through multi-step reasoning in the wild that helped fuel some of the early ideas in modern AI agents.

Consider the question *"What government position was held by the woman who portrayed Corliss Archer in the film Kiss and Tell?"* To answer this question, you'd first need to figure out who *"portrayed Corliss Archer in the film Kiss and Tell"*, before you can answer what government position she held (it's Shirley Temple, and her position was Chief of Protocol of the United States).

This was a time before [BERT](https://arxiv.org/abs/1810.04805) and any of the decoder-only breakthroughs in large language models (e.g., [GPT&#8209;2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), back when version numbers still made sense) we take for granted today, where most of the AI systems that can answer questions from a large collection of text (like Wikipedia) follows a **simple, scripted recipe**: retrieve a handful of passages from the corpus with the question, and shovel them into a neural network with the question to get the answer.

HotpotQA pioneered a class of AI task that requires the AI system to **autonomously** perform multiple steps of reasoning in an open-domain setting, where scripted approaches no longer worked well. Since, now, each question in HotpotQA requires at least two passages from separate Wikipedia pages to answer, often at least one of these won't surface if you searched with the question itself, and different questions use different natural language reasoning patterns that present challenges to a single script that works for all.

In its early days, researchers often challenged the motivation for HotpotQA by observing that the questions themselves are sometimes artificial, and that people can still break their complex questions down into subquestions manually so that existing AI systems can handle them. Our answer to these very valid considerations seems to have stood the test of time:

> We would still like to build AI systems that can solve more challenging problems through more autonomous reasoning and acting, rather than always relying on humans to cope with the limitations of the AI systems that are currently available.

HotpotQA, despite some of its limitations, was a step in the right direction to challenge the envelope of possible AI system capabilities, where we essentially oversampled a group of small but challenging problems to stress test how well our systems perform.

In my own follow up work a year later, [GoldEn Retriever](https://arxiv.org/pdf/1910.07000), we explored a prototype of such an AI system. Instead of following a scripted procedure, GoldEn Retriever proposes its own search queries based on the original question and whatever passages have been retrieved from the previous iteration (initially empty). This allows the system to autonomously focus on information related to *"Kiss and Tell"* in the first iteration of information gathering, then use the retrieved information about the movie, combined with the original question, to redirect its focus to *"Shirley Temple"* to solve the question by going beyond the information immediately available in the original question. This is a proof of concept for the ideas behind what would later become agentic retrieval and deep research, where the AI system is provided with strong agency in determining what information to gather at each step, gather information for multiple steps, and then formulate a coherent answer given all the context that is provided.

### Why you should stop using HotpotQA (alone) for agents research

Four score and seven months later, it is truly humbling to see the body of research work that this dataset has helped enable, where I constantly find new inspirations from the ingenuity of the community that works on AI agents, some of which find HotpotQA useful as a testbed.

However, when used alone, the evaluation that HotpotQA provides is no longer adequate for today's agentic systems.

First, the task **output format and evaluation metric** are a little outdated. Like many question answering datasets of its day, HotpotQA is an extractive question answering dataset following the pioneering work in SQuAD, which means that the answer came directly from a substring in the Wikipedia context that supports the answer. While this leads to relatively easy-to-implement and objective evaluation metric, it leads to a format that is no longer natural for today's generative AI systems, and is limited in its ability to evaluate semantically equivalent or other potentially feasible but unannotated answers. For instance, in our example, in the previous section, a system predicted answer *"The actress in question is Shirley Temple, who held the position of Chief of Protocol of the United States"*, while being perfectly sound to a human user, would not have received full credit in the exact match or F1 scores, because it provides extra information that the specific answer format did not allow.

Second, the **task is not realistic enough**, in the sense that it bakes in the assumption that *every single* question requires taking complex steps to arrive at the answer. In reality, this cannot be determined just by looking at the question itself, but also the knowledge sources that are available. In our example, it is plausible (though unlikely) that the Wikipedia page for Kiss and Tell mentions Shirley Temple's government capacity of Chief of Protocol of the United States, if this position temporally overlaps with the film's making, or has had an effect on the artistic decision-making in its production. In that case, only a single step of retrieval and reasoning would have been sufficient, and doing more risks introducing more noise for the model to cut through. In my 2021 follow-up work, we attempted to address this benchmarking problem by coming up with a unified single- and multi-hop question answering dataset based on the same knowledge corpus, [BeerQA](https://arxiv.org/pdf/2010.12527),[^1] alongside an autonomous system that performs retrieve-and-read for as many steps as needed for the question at hand, given the information retrieved so far. This more closely emulates the scenario where AI agents are being deployed: before exploring potential approaches to solve the given problem with the knowledge and tools provided, it is impossible to perfectly predict the complexity of the problem ahead of time.

Third, the **task is relatively contrived**, and reflects only a small slice of what humans would like to delegate to intelligent systems. Question answering is at the core of human needs to gather (and synthesize) knowledge, which undoubtedly improves upon the previous generation of technology that solves this problem, represented by powerful search engines. However, in many cases, knowledge gathering itself is not an end, but a means to an underlying one. One can gather knowledge to assist with more challenging decision-making, to educate oneself or others, to explore the boundary of adjacent knowledge, or even to serve as the basis of knowledge to help accomplish certain tasks, to name a few. As the capabilities of our AI models and systems improve, we should not stop at holding ourselves to solving only parts of these problems, but more aggressively explore their end-to-end solutions.

Finally, as is the case with any benchmark, **approaches overfit the benchmark over time**. Almost everyone that has worked on HotpotQA is probably familiar with some of the first 10 dev set examples by now, and powerful large language models have also likely seen the entire development set with the correct answers in its training.

### What to do instead

* stop using all multi-hop exclusive datasets, or at least test the same agent design on examples of varying complexity
* use more realistic benchmarks as a simple alternative
* maybe focus on other problems altogether?
    * do things instead of answering things
    * agent efficiency and robustness
    * pragmatics!
    * low-resource tasks
    * creative combinations of agentic capabilities (research agents, multiagent systems, multiagent societies)
    * evaluation, evaluation, evaluation

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Could the fast development and wide adoption of <a href="https://twitter.com/hashtag/gpt4?src=hash&amp;ref_src=twsrc%5Etfw">#gpt4</a> and friends actually lead to a Linguistic Renaissance?</p>&mdash; Peng Qi (@qi2peng2) <a href="https://twitter.com/qi2peng2/status/1635816369509007363?ref_src=twsrc%5Etfw">March 15, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

#### Footnotes

[^1]: Because you get different flavors of beer by adding different levels of hops, among other things. And beer is a great companion when having hotpot in the summer.