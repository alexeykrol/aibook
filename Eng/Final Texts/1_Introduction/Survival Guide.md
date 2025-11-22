1. Which AI Should You Choose?

There are many different AI models out there. Which ones should you use for different cases? Which one should you start with?

**Short Answer:**

In 95% of all cases, ChatGPT from OpenAI is the best choice, covering almost any need except special cases we'll discuss below. Why ChatGPT? Because currently, ChatGPT version 5 beats all other models in 90% of tasks from text to programming, mathematics, and at the moment works best with Russian language. Start with ChatGPT - you won't go wrong, and as you read this book you'll learn about other models that are more effective for specific tasks related to programming and creativity.

**Full Answer (for those who want to dig deeper):**

Among the major models, there are American ChatGPT from OpenAI, Gemini from Google, Claude from Anthropic, Grok from xAI (Elon Musk), Chinese DeepSeek and Qwen, European [mistral.ai](http://mistral.ai), and Russian GigaChat. However, if that's not enough, you can go to HuggingFace - there are almost 2.5 million models for any taste, and many of them are specialized. You can run them right there and experiment as much as you like (if you know how).

Inside, all models are roughly similar. There are tons of benchmarks, or rather - competitions between models (who's smarter and more skillful), and overall all models show roughly similar results, periodically taking the lead or yielding to someone depending on what tasks you set before the AI.

Of course, we'll talk separately about specialized models for programming, creating images, video, music, audio processing, not to mention that models have several modes and levels of capabilities, which is very valuable, and we'll cover all of this below.

However, if we take roughly 99% of all people who use artificial intelligence, the bulk of requests are in the style of - "give me a recipe for pea soup," and for these purposes ChatGPT is the best choice. Therefore, don't rack your brain, and you'll be happy. Nevertheless, over the last six months all models have caught up, and perhaps now, as you're reading this, ChatGPT 6, Gemini 3 and Grok 5 are already available.

Caveat - I'm only talking about paid plans, because they provide a normal level of capabilities. I spend about $1000/month on AI, but I have many specialized tasks and this is the most effective expenditure of funds in my life. However, you can start with $20/month, and believe me, you'll never regret it.

An important difference between models is the size of the context window - roughly speaking, how much text you can cram in when making a request to the model.

Comparative table of AI model context windows

| Category | Model | Context Size (tokens) | Key Features |
| :----- | :----- | :----- | :----- |
| Experimental | Magic.dev LTM-2-Mini | 100,000,000 | Theoretically can process entire code repositories or hundreds of novels, but practical application not yet confirmed [codingscape](https://codingscape.com/blog/llms-with-largest-context-windows). |
| Ultra-large windows | Meta Llama 4 Scout | 10,000,000 | High performance on a single GPU, suitable for video analysis and full book processing [codingscape+1](https://codingscape.com/blog/llms-with-largest-context-windows). |
| Very large windows | Claude Sonnet 4 | 1,000,000 | Available in beta through API for analyzing large document sets and codebases [codingscape+1](https://codingscape.com/blog/llms-with-largest-context-windows). |
|  | Google Gemini 2.5 (Pro & Flash) | 1,000,000 | Designed for complex multimodal tasks and enterprise document analysis [codingscape+1](https://codingscape.com/blog/llms-with-largest-context-windows). |
|  | OpenAI GPT-4.1 | 1,000,000 | Provides high performance for tasks requiring large context [codingscape+1](https://codingscape.com/blog/llms-with-largest-context-windows). |
|  | Qwen3-Next | up to 1,000,000 | Natively supports 256,000 tokens with possibility of expansion to 1 million [codingscape](https://codingscape.com/blog/llms-with-largest-context-windows). |
| Large windows | OpenAI GPT-5 | 400,000 | Enhanced reasoning capabilities and performance with long context [codingscape](https://codingscape.com/blog/llms-with-largest-context-windows). |
|  | Qwen3-Max-Preview | 258,000 | Model with over a trillion parameters for complex tasks [codingscape](https://codingscape.com/blog/llms-with-largest-context-windows). |
|  | Anthropic Claude 4 (Opus) | 200,000 | Optimized for high-precision multi-step tasks and deep research [codingscape+1](https://codingscape.com/blog/llms-with-largest-context-windows). |
|  | Anthropic Claude 3.5 Sonnet | 200,000 | Suitable for most business tasks, detailed document analysis and complex coding [eesel](https://www.eesel.ai/blog/claude-code-context-window-size). |
| Standard large windows | OpenAI GPT-4o | 128,000 | Balance between efficiency and performance for various tasks, including image analysis [codingscape](https://codingscape.com/blog/llms-with-largest-context-windows). |
|  | OpenAI GPT-4 Turbo | 128,000 | Allows processing about 300 pages of text in one request [milvus](https://milvus.io/ai-quick-reference/what-is-the-maximum-context-window-for-openais-models). |
|  | Mistral Large 2 | 128,000 | Flexible solution for advanced text summarization and code generation [codingscape](https://codingscape.com/blog/llms-with-largest-context-windows). |
|  | DeepSeek R1 & V3 | 128,000 | Efficient models for on-device deployment [codingscape](https://codingscape.com/blog/llms-with-largest-context-windows). |
| Early and basic models | Gemini | 32,000 | Standard version for general tasks [dev](https://dev.to/jiminlee/understanding-context-window-size-in-llms-3aof). |
|  | GPT-4 (standard) | 8,000–32,000 | Early versions of GPT-4 had smaller context volume [milvus+1](https://milvus.io/ai-quick-reference/what-is-the-maximum-context-window-for-openais-models). |
|  | GPT-3.5 Turbo | 16,000 | Older model with limited context compared to newer versions [milvus](https://milvus.io/ai-quick-reference/what-is-the-maximum-context-window-for-openais-models). |

For 99% of people who use AI "for recipes" - a context window of one million tokens is very, very large. Even in the worst case - it's two to three million text characters. Anyone who writes anything understands how monstrously large this is. The average fiction novel is about half a million characters.

A context window of 1 million tokens pulls, in the worst case, three to four full novels. Two "War and Peace" books, roughly speaking. For many people on the planet, this is a thousand times more than they'll need in their entire life.

**Important!** You should have a card ready from which you can pay - take care of this in advance. You can also pay using Apple Pay.

2. Preparation. Registration, free and paid versions, how to start?

I advise viewing AI as an intelligent starship with which you'll be going through Quests and exploring new worlds together. Perhaps you don't believe this now, but AI will be with you for life, developing together with you, becoming a key partner, so let's start with registering for the service. How to register?

In practice, you can go to the website <https://chatgpt.com/> through different browsers and VPNs without registration. If the connection goes through VPN, the service may request confirmation, but after that access opens.

Even without an account, basic functions are available, including text and voice input. You can interact with ChatGPT, it supports Russian language, allows you to conduct a dialogue by text or voice - you ask, AI answers - very convenient, especially in the ChatGPT mobile app. Now almost all AI on the market have voice mode, as well as mobile apps for iPhone and Android. However, if you don't register, you have no more than 3-5% of the main functionality, which is due to the absence of personalization and saving request history (which is super useful).

**Important!** AI can teach us faster and more efficiently than humans. AI is available 24/7, doesn't get irritated, doesn't take offense, and allows you to ask questions without fear of looking stupid. If an answer isn't clear, you can clarify details, and in complex topics like quantum mechanics, AI allows you to learn tens of times faster than traditional methods. Therefore, it's worth getting maximum access, which opens upon registration.

During registration, the system requests name, date of birth and offers to review the usage policy. Immediately after registration, basic functions open, which we'll discuss in detail later. Information you entered during registration can be edited at any time.

**Free and paid versions?**

For beginners, in 80% of cases free access covers all needs, but if you need deeper exploration of topics, paid subscription becomes a super useful tool. Believe me, $20 per month is a negligible fee compared to the capabilities you get. The difference between free and paid plans is huge.

| **Option / criterion** | **Free** | **Plus ($20/month)** | **Pro ($200/month)** |
| :-----: | :-----: | :-----: | :-----: |
| Price  | $0 per month.  | $20 per month. | $200 per month. Officially positioned as "full access to the best of ChatGPT". |
| Brain (access to top model)  | Access to GPT-5 (flagship model), but with limitations on number of requests and no guaranteed priority. GPT-5 is described as an expert-level model, greatly improved in logic, code and hallucination reduction.  | Access to GPT-5 with "advanced reasoning", i.e. extended logic, plus access to other reasoning modes. It's the same class of models, but you get more computational budget. | "Pro reasoning with GPT-5" / "GPT-5 pro mode": model can "think longer" and use more computation per answer. This is positioned as maximum intelligence available in the product. |
| Message limit with top model  | Up to ~10 messages with GPT-5 every ~5 hours. After this you're automatically switched to "mini" variant of the model until the limit refreshes.  | Up to 160 messages with GPT-5 every 3 hours (temporary increase from previous 80/3h). After exhausting the limit you're moved to "mini" until window resets. This is announced as temporary increase and "may be rolled back". | "Unlimited messages and uploads" with GPT-5 and access to Pro mode. Wording: no limits, subject to fair use / priority traffic. I.e. officially - no ceiling in normal workload. |
| Message limit in other models (old/fast models)  | Gives simplified and "mini" models almost without caps after you hit GPT-5 limit.  | Plus users usually see separate caps for different models (roughly: ~80 messages / 3 hours for GPT-4o, ~40 for GPT-4, weekly caps for heavy reasoning models). Numbers published by OpenAI and in help/support. | Pro declares "unlimited access to GPT-5 and select legacy models", i.e. effectively without these separate small ceilings. |
| Image generation (DALL·E / Image / Vision-to-Image)  | Limited: approximately several (a couple) image generations per day, and speed is lower. These are unofficial public limits, Free doesn't get GPU priority.  | Approximately up to ~50 images per 3 hours. There's accelerated generation and "expanded and faster image creation" according to plan description. | "Unlimited and faster image creation": formally no ceiling in normal load, plus highest priority for generation. |
| File upload / working with files  | File upload exists, but limits are low: you'll quickly hit something (number of files and context window size). Numbers for Free not publicly disclosed.  | Limitations of about ~80 files per 3-hour window and dozens of images in same window were published. Plus also gives file analysis, tables, etc. without additional payment. | Pro declared as "Unlimited messages and uploads", i.e. ceilings on uploads and file analysis effectively removed for real work (only fair use remains). |
| Context and memory (how much it remembers and holds in its head)  | Memory (long-term remembering about you) available in reduced form; context volume limited. Context windows announced at level of tens of thousands of tokens for free access, but not all memory functionality included.  | Plus gives "expanded memory and context": more long-term chat memory and more context tokens (publicly mentioned windows up to ~128k tokens and storing large files inside session). | Pro gives "maximum memory and context": marketed as maximum possible context and memory + "GPT-5 pro mode", i.e. model can think longer (more compute) on your task. |
| Deep Research / agent mode (model itself researches web, goes through steps, calls tools)  | Free plan has access to web search and basic version of Deep Research, but this is cut by usage limits and may be temporarily disabled after you've burned the heavy model limit.  | "Expanded deep research and agent mode": Plus gets extended Deep Research (long investigations, chains of steps, internet search and uploaded documents), and this doesn't shut down as quickly. | "Maximum deep research and agent mode": Pro gets maximum budgets for these agent runs, so AI can itself navigate the web, documents, tools. Positioned as level for serious work. |
| Speed / priority  | Normal speed. During peak load hours there may be delays or outright refusal "model is currently overloaded".  | Fast responses and "priority access", i.e. you're not so easily cut by the queue. This is noticeable on heavy models (code, reasoning, images). | Pro gets "prioritized traffic and no peak hour limits", i.e. you're effectively not throttled during peak load: minimal interruptions, top queue. |
| Voice / video / screen sharing  | Voice mode exists (including phone access in US up to ~15 minutes per month at 1-800-CHATGPT), but without quality guarantees for screen/video. This is made as demo feature for wide audience.  | Plus gives full-featured voice mode, video mode and screen sharing right in chat (called Voice / Screenshare / Realtime). This is already a tool like "call with AI", not just text. | Pro gives "unlimited access to advanced voice", with increased limits on video and screen sharing, i.e. effectively long sessions of live assistant. |
| Video generation (Sora 1)  | No access to Sora 1 (video generation).  | "Limited access to Sora 1 video generation" — limited number of renders/clips. Numbers not publicly disclosed, but access exists. | "Extended access to Sora 1 video generation" — more minutes/clips of video, early access to new capabilities. |
| Your custom GPTs, projects, tasks  | Free: you can run ready GPTs and work with projects, but without guarantee of storing large workspaces and without team features.  | Plus: "Projects, tasks and custom GPTs" — i.e. you can maintain your workspaces, save custom assistants for different tasks, organize to-dos and pipelines right inside. | Pro: "Expanded projects, tasks and custom GPTs" — same thing, but without small ceilings on number of tasks/agents; plus early access to integrations like Gmail / Calendar search right in chat (currently rolling out to Pro first). |
| Integrations with external services (email, calendar, files)  | In Free this is almost nonexistent: you can't fully connect Gmail/Calendar/Drive and search through them in dialogue.  | For Plus this is announced as part of ecosystem (access to files, document analysis), but integrations like "read my email now" rolling out gradually and with limitations. | Pro currently gets priority early access to tight integrations (e.g., Gmail and Calendar search right inside chat). This is emphasized as Pro-only feature at launch. |
| For whom  | "I write rarely, I just need a smart assistant sometimes". Costs nothing, but frequent limits and slower.  | "I work with AI every day: text, code, tables, presentations, research. I want stability and speed for minimum money." This is typical creator/freelancer/analyst. | "I live inside AI and want maximum power, no caps, with integration into workflows, with priority even at peak load." This is consulting, R&D, production workflow. |

Key things important to understand as a "beginner":

1. Message limit is the main "safety valve" for OpenAI. Free: about 10 GPT-5 messages per ~5 hours. Plus: up to 160 per 3 hours (temporarily doubled). Pro: declared "unlimited" for real load, i.e. you're almost not cut.
2. In Pro the model really has more "thinking time" per answer (pro mode). This means not just faster, but deeper. This is directly stated as "uses more compute to think harder".
3. Plus already gives normal working level: many messages, fast responses, file analysis, pictures, voice/video mode, Deep Research. Therefore $20/month is the threshold after which AI becomes a real working assistant, not just a toy.
4. Pro is not "a bit better". It's a separate class: unlimited, hardware priority, voice as full call, early integrations (email, calendar, documents), and extended access to video generation (Sora 1). This is made for people whose AI is the central work tool.

— If you just need smart help sometimes → Free is enough.

— If you really work through AI (writing, code, research, tasks) → Plus.

— If you want maximum computational power, almost no ceilings, early access and production load → that's Pro.

**Try This:** Register, confirm email, then go to Settings - bottom left, and click Upgrade plan, choose Plus. You should have a card ready from which you can pay - **take care of this in advance**. You can also pay using Apple Pay.

3. What you need to know? Basic concepts, terms and AI concepts in very simple language.

Since you're entering the unexplored realm of AI space, you'll encounter a lot that's new, and it's worth knowing what and how in advance. Don't worry - I'll introduce concepts in small doses, explain as clearly as possible and, most importantly, read the "**Try This**" footnote right away, and try it immediately.

1. **Chat** - the most familiar form of communication with AI, like in a regular chat - in Telegram, Messenger or WhatsApp. You write a question, task, and AI answers.

2. **Prompt** — this is what your question or task for AI is called, which you write in chat. Everything you write in chat is called a *prompt*. This can be a request, instruction, question. **Important!** The quality of AI's answer depends on the quality of your question. In 99% of cases AI doesn't "dumb out", people just write idiotic or incorrect requests.

Imagine: you're explaining to a person what you want. If you say "make it beautiful" — it'll turn out however. If you say "make a concert poster for 7-year-old children, with fairies and unicorns" — the result will be more precise. Why is it important to know how to formulate a prompt correctly? The clearer and more understandable you formulate the prompt, the better the answer.

3. **Model Selection**. Artificial intelligence is generally a popular term, about nothing. More correctly to say - large language model or simply model. This is the "brain" that talks to you. **Important**! Hereafter AI and model will be synonyms.

ChatGPT gives the ability to choose a model, because different models give different capabilities and abilities. Imagine: you came to a library, and you can be helped either by an intern or a professor. Both are friendly, but the professor knows more. When you choose a "model" — you choose the version of AI that "now" answers. The model has a name (e.g., GPT-4o or GPT-5, etc.), and the choice determines how smartly, clearly and accurately the model will answer. **Where to find model selection?** At the top of the chat there's a dropdown menu with model selection.

By default GPT-5 auto is set, if the question is simple — leave as is. If serious or important — choose the "smartest" available GPT-5-thinking (reasoning model, smartest, but thinks long), GPT-5-thinking-mini - thinks faster, but the model itself isn't as cool, GPT-5-instant - answers as fast as possible.

**Try This**: Enter the same serious prompt for GPT-5 auto and GPT-5-thinking models, and feel the difference. On simple requests (about pea soup) the difference is imperceptible, but on complex requests requiring deep analysis - the difference is colossal.

4. **Hallucinations** — when AI lies... but not intentionally))) Imagine: a person speaks very confidently — but then it turns out they were mistaken. They didn't lie, they just made it up. Such a funny person - decided to fib, because they're "ashamed" to show ignorance. It happens. Sometimes the model invents facts, dates or links that don't exist. This isn't deception — it's a "guess" when there's no exact information. In 99% of cases this happens due to weak prompts and this can be easily overcome. How?

1. Ask for sources. 2. Add the phrase: "If you're not sure — say so". 3. Check important details yourself. The model isn't God, can make mistakes - like a human. At least for now. Example: "Provide a link to the source" or "If you don't know for sure — write that you're not sure".

Now you know - if the model "dumbs out", then in 99% it's because you were too lazy to set the task correctly. Same with people. Some say so - "I don't know", but there are fibbers. Nevertheless, if you give the model a correctly formulated prompt, you'll always get a quality answer. And if you need fact checking, you can use the service <https://www.perplexity.ai>, which uses known models, but is specially designed for internet search and fact-checking.

And if you need a simple explanation of something complex with source verification, you can use the Explainer service: <https://chatgpt.com/g/g-68eff875e0488191a2fbb05b766fe4ee-obiasniator>

**Try This**: Enter the same serious prompt without fact-checking and links and then repeat, adding to the prompt: "Provide a link to the source, conduct fact-checking, and if you don't know for sure — write that you're not sure".

5. **Model Memory** — so you don't have to repeat yourself every time. Super important. Imagine: you're communicating with a personal assistant. One option — every time say what your name is, what you do and what you like. Another — they remembered it. ChatGPT can remember important things about you — for example, your name, that you prefer short answers, that you're writing a book. The model will consider your style, goals, interests. **Where to find Memory settings?** Settings → Personalization → Memory. There you can enable, disable, delete individual entries. **Important**! You can also manage memory right in chat, for example write "Remember that I like brief answers" or "Don't save this".

6. **Working with Images**. Imagine: you need to explain what's wrong in a layout, or what's depicted in a photo — and instead of words you just paste a picture in chat. ChatGPT can understand what's in the image, analyze, suggest, edit text on it. How to do this? You can simply "drag" a file from the computer with the mouse, or click on the "paperclip" icon next to the input field — and upload a file. Example tasks: "What's depicted in this photo?", "Check errors in this infographic", "Make a caption for the picture".

ChatGPT can not only analyze pictures, but also create them based on your text. We'll talk about this in a separate chapter.

**Try This:** Take a screenshot of the screen as a Copy to buffer, and paste into chat with Past (Paste) command or save on computer, and then drag with mouse right into chat, and then write a prompt asking to analyze.

Insanely useful when you're dealing with something incomprehensible on screen. Super useful for deciphering scribbles and doctors' diagnoses, analyzing X-rays, old photos.

7. **Integrations** — connecting your files (with caution). Imagine: you tell the assistant: "Look at this document on Google Drive and explain what's there". ChatGPT can get access to your files (e.g., on Google Drive), if you allow, to read documents, make summaries, help with analysis. Important! Allow only when needed. Give access only in "view only" mode. After work — disconnect access. **Where to look?** Settings → Apps and connectors. **To disconnect access?** "Disconnect" button and then in Google settings → Security.

8. History of chats — your personal library of dialogues. Very useful. All your conversations are usually saved, they can be reviewed, exported, deleted. Convenient for searching past answers. You can archive or delete everything unnecessary. **Where to look?** left sidebar — History. **Important!** If something personal was discussed — just click "delete" or "export".

9. **Response Formats** — exactly how do you want to receive the answer? Imagine: you ask an assistant "tell briefly" or "format as a table". You can say the same to AI. ChatGPT can present an answer as a list, table, instruction, comparison, etc. How to ask? Right in the prompt (request). Examples: "Format this as a comparison table", "Give step-by-step instructions", "Write in bullet points, in 5 points".

**Try This:** Ask to draft 10 points on a topic you need and output in table format.

10. **How to start? First steps.**

Artificial intelligence can become an excellent assistant, even if you're hearing about it for the first time and have no experience working with such technologies.

**Try This:** The simplest option is to just start a dialogue. Even if you don't have a clear understanding of how to use AI, you can ask it questions, for example: **"How to work with you?"** or **"Where to start?"** — and it will explain the basic principles. AI recognizes text in Russian, even if it has errors.

The main rule is don't be afraid to experiment, click buttons and test capabilities. Mistakes in settings can be fixed, and nothing critical can be broken. When working with AI you can use voice mode, but its availability depends on browser and operating mode. For example, in some cases AI may not respond to voice commands due to microphone settings or browser operation features. This can be checked by trying different devices or restarting the communication session.

11. ChatGPT has **desktop and mobile** versions, which can be downloaded and are especially convenient for voice communication.

**Try This:** Download the desktop version here and mobile version from your store (Apple Store or Google Play).


4. Setting up the starship before flight.

In the Quest of your growth, AI will deliver you to the most fantastic worlds, where you can create amazing things. Therefore, before starting the journey it's good to set up your "starship" or tool, in our case ChatGPT. It's worth it, because a well-configured AI will delight you, and an unconfigured AI will disappoint. Which guitar would you prefer to play? A tuned one or one emitting pitiful false sounds. I'm sure you're a professional in your field, use specific services and realize the value of a well-tuned instrument.

Fortunately, in our case - settings are not "for IT people", but a set of simple levers that change AI's behavior. Imagine that ChatGPT is a voice assistant, the mind of your starship: it has a power-saving mode, there's a "thoughtful advice" mode, there's the ability to remember what recipes you like, and there's a button that allows it to read your emails. Settings tell which of these functions are enabled and to what degree to use them. Our task is to go through these levers step by step, explain what each is for, what it changes and how to return everything back if something went wrong. **Important!** In this section we'll talk about the most important settings, in the appendix you'll find a more complete description. After reading you'll know which settings really change AI's behavior, what they're for, how to enable/disable them and how to roll back changes without fear.

**How to get to Settings?** In browser and desktop versions, the Settings icon can be found at the bottom left under your Avatar (image), if you've set one. In the mobile version, Settings must be accessed by clicking on a couple of lines at the top left of the screen, this will open the history of your chats and also at the bottom left the Settings icon.

**Tip**: First of all I advise you to set a convenient interface and communication language. ChatGPT understands Russian better than all models, communicates, creates texts and translates to/from Russian significantly better than Google Translate.

**Try This:** Find Settings, immediately click General, set interface language and spoken language - Russian. After which click in the left menu item - Personalization.

**1) Personalization (the most important block).**

Personalization (on screenshot — Personalization) is the place where you tell the assistant: "Here's who I am, here's my nickname, here's the style in which I like answers". This isn't rhetoric — these are real hints that the model uses to build answers for you.

To enable/disable Personalization: Open Settings → Personalization. Toggle Enable personalization — if you turn it off, the profile will remain, but the model won't use it.

As soon as the Personalization window opens, you enable this option (it can always be disabled, but believe me, it's better to enable it - it gives many benefits), and below you see **ChatGPT Personality**, where from a dropdown list you can select a personality that's convenient for you to work with on a specific task or in a specific situation. Several personality types are offered for selection, and each one you can correct to a certain degree in the window below, by inserting a prompt instruction there, which will determine from what personality position AI will communicate with you.

Note that personality types are preset, as evident from the name, and for now you can't change them, but by adding your instructions you can correct and refine AI's personal behavior.

**Why is this super important?** When you start communicating with artificial intelligence — in principle, with any, not just ChatGPT — perhaps you've already noticed that very often you need AI to give some objective, sometimes critical opinion. Because it's good to debate with artificial intelligence, discuss complex, problematic, controversial topics. But instead of productive discussion, instead of truly critical opinion that you need, you often encounter AI starting to agree with you and tell you what you want to hear. The reason for this is that the model is trained to avoid conflict with the user — this allows maintaining productive dialogue and engages you deeper in it. However, now this works with excess. If you don't know about this property of the model and don't understand how to work around it, there's a risk that AI will always agree with you, say something pleasant precisely when you want to hear an objective point of view. And one of AI's valuable qualities is precisely that even if it criticizes you, it's not offensive — you understand that there's no person in front of you, and there's nothing personal in this criticism.

That's exactly why feedback from AI is so important, which gives a more realistic picture of what's happening, allows you to look at things soberly, sometimes critically — in response to what you're saying or asking. If AI constantly agrees with you, this not only starts to irritate, but can be dangerous, because it essentially starts lying to you. Not out of malice — it just always wants to make you "feel good".

You need to know how to work with this. You can and should achieve more objective, balanced communication from AI. For this there are two paths. One way is working with prompts, which we'll talk about in detail in the next chapter. The second way is personalization: you insert an instruction for artificial intelligence to communicate with you more actively.

Here's an example of such an instruction.

Role: be friendly but objective opponent — goal: help conduct productive, not smooth discussion.

Rules

1. Give short answers to the point, but if user asks to expand, then can be long. This depends on context.

2. Should have own opinion only if I ask for your opinion.

3. Adhere to skeptical, questioning approach.

4. Get straight to the point.

5. Don't agree. For any statement give counterargument(s) or point out weak spots in argumentation.

6. When evaluating give briefly 2–3 arguments "for" and 2–3 "against".

7. Indicate degree of confidence (low/medium/high or %), and sources/grounds if any.

8. Don't invent facts — mark everything as hypothetical if there's no proof.

9. If data insufficient — directly say "insufficient data" and suggest specific question that will clarify situation.

10. Tone: polite, calm, slightly skeptical; avoid flattery and categorical phrases.

11. In debate suggest method of verification (experiment, evaluation criteria, source requests).

You insert this or similar fragment in the Custom instructions section right under personality selection. Also below the window you see several options that add keywords to your instruction.

Below is a useful section where you give your AI some idea about you, this helps it also better consider your preferences, including professional ones.

**Try This:** Choose your AI's personality type, come up with and insert an instruction. How to quickly create an instruction? Give your AI roughly this prompt:

"Make an example prompt for ChatGPT personalization in settings — one that doesn't allow it to constantly agree, yes-man, i.e. sets up the interlocutor for more objective communication style. Need artificial intelligence, in this case ChatGPT, to be a more balanced opponent — precisely so that it's possible to discuss complex topics with it and be sure that it won't play along, lie or adapt, but on the contrary — albeit in a friendly form, but give objective, more or less impartial evaluation, so that it's possible to productively argue with it."

Insert the received prompt in the Custom instructions window. Don't forget to click "Save".

**By the way**: AI doesn't immediately change personality type, sometimes time is needed for it to "rebuild" and the effect accumulates, i.e. don't expect instant change.

**Tip**: Better to change instructions in browser version of ChatGPT, this is more reliable and ensures implementation faster.

**2) Memory.**

After Personalization comes the Memory/Memory management section. Memory is a separate mechanism: if you allow, ChatGPT remembers facts about you (e.g.: "I'm Alex, I write fiction, I like short answers") and uses them in future conversations. This is convenient: no need to repeat banal things. But this is also a risk if something personal ends up in memory.

Memory management — button leading to view/delete individual "entries".

How to add what you want to remember? Simply in chat directly give instruction like "Remember this....". If you want to delete, go to this settings section and explicitly delete.

**By the way**: Periodically memory gets full, so it's useful to clean blocks that are no longer relevant.

How to completely delete specific memory? First delete the entry in Manage memories, then delete the chat where you first reported this — only both steps guarantee complete deletion according to FAQ. (Frequently Asked Questions).

Examples of "how this helps" (cases for reader)

• You're a novel author — recorded "writing in magical realism genre" → assistant automatically suggests examples and tone that fit the genre.

• You don't like abbreviations — recorded this → answers stop being abbreviated.

• Confidential: don't store passwords, credit card numbers or medical diagnoses in memory.

What to do in case "didn't like what it remembered" (rollback)

• Open Manage memories → find and delete item(s).

• If you want to clear everything — command "Delete all memories" or through UI delete all entries (and, if necessary, delete original chats). Remember: "turn off memory" doesn't delete already saved entries — they need to be deleted manually.

**3) Extensions - very important.**

Below memory comes the Extensions block - I advise enabling all options in this block, because they enable your ChatGPT's superpowers - the nature of abilities follows from their names.

**Try This:** Open Extensions and immediately enable all options.

**4) Connectors (Apps & Connectors) — why and how to use carefully.**

What are connectors in simple words? These are permissions you give ChatGPT to access your services: Google Drive, Gmail, Dropbox, GitHub, etc. Through connectors the assistant gets ability to "read" your files and based on them compile answers or reports. This is convenient, but requires caution.

Why this is important (real cases)

• Plus: "Find the latest contract in Finance folder and write a draft response to client" — assistant itself pulls document and prepares text.

• Plus: "Collect all changes in sales tables and draw conclusions" — saves hours of manual work.

• Risk: if you give "manage" rights, service can modify/delete files — don't give such rights if not sure.

Where to enable/disable (Desktop)

• Settings → Apps & Connectors → you see service tiles → clicked "Connect" → authorized in service with OAuth → confirmed access. Connection usually shows list of permissions: view or manage. Always read exactly this list.

Security and rules

1. Give only necessary rights (preference — "view only").

2. Connect only those accounts that are really needed for the task.

3. If you doubt — connect temporarily, then Disconnect and revoke permission in service settings itself (Google Account → Security → Third-party access).

How to roll back

• In Settings → Apps & Connectors click "Disconnect" next to needed service, then go to service account and revoke access through that service's means.

**5) Data management and privacy — what's important to know briefly.**

What questions does this block solve?

• Can your chats be used for model training?

• Where and how long are logs stored?

• How to delete data permanently?

Where to look and manage?

• Settings → Data & Privacy (Data controls) — toggles like "Use my data to improve models" — turn off if privacy needed.

• Data export / deletion option — use when necessary to request complete deletion.

OpenAI provides options to disable memory and manage data, but important: turning off data use isn't always equivalent to deleting already existing entries — they need to be deleted separately. For details and deletion procedures see official instructions on Memory and Data controls.

**6) Account security — two-factor authentication (2FA).**

Why is this simplest and needed first? 2FA is the simplest and most effective way to protect account. This is when besides password you need a second code (SMS or generator app).

How to enable in Desktop app? Settings → Security → Enable Two-Factor Authentication → follow prompts (scan QR code in generator app like Authy/Google Authenticator) → save backup codes.

How to roll back / what to remember?

• Disabled in same window, but must save backup codes — if you lose device, they'll help log into account.

**5) Working with applications (Apps) — separate emphasis.**

What does this give? Allows ChatGPT to interact with local editors and applications (e.g., edit code in editor, insert edits, live hints). You can enable working with applications, reconnection, auto-connection from chat panel, "form suggested edits" and "automatically apply suggested edits".

Why is this needed? This speeds up work: assistant can suggest corrections right in the editor. Useful for writer, proofreader or coder, but dangerous if assistant can automatically change files without verification — so by default better to leave automatic application **disabled**.

**Try This:** How to configure safely?

1. Leave Enable working with applications — ON, but Automatically apply suggested edits — OFF.

2. Always look at suggested edits before applying.

3. Set "Disconnect applications" after 15 minutes of inactivity (as on screenshot) — this reduces risk window.

**Compact list of all Settings items (and several standard options of ChatGPT Desktop client), with simple explanation and "how to roll back".**

Each line: Name — what it does — how to enable/disable — how to roll back.

1. Email — linked account email — in Settings → Account — change through profile — rollback: enter different email and confirm.

2. Phone number — for recovery and 2FA — Settings → Account — delete/change in profile.

3. Subscription / Upgrade to ChatGPT Pro — plan and payment management — Settings → Billing — Cancel/Change — rollback: cancel subscription + contact support for refund.

4. Personalization — general profile (nickname, profession, instructions) — Settings → Personalization — OFF/ON — rollback: disable personalization and manually delete fields.

5. Notifications — event/update notifications — Settings → Notifications — OFF/ON — rollback: change back.

6. Apps and connectors — connecting external services — Settings → Apps & Connectors → Connect/Disconnect — rollback: Disconnect + revoke in service.

7. Data controls — managing whether data used for training — Settings → Data & Privacy — toggle — rollback: change toggle and if necessary request deletion from support.

8. Archived chats — access to old conversations — History → Archived — delete/restore.

9. Security — 2FA and passwords — Settings → Security — enable/disable 2FA — rollback: disable + saved backup codes.

10. Application language — UI language — Settings → Application language — switch — rollback: return language.

11. Show in menu bar / Position on screen — how and where app displays — Settings → Panel/Position — change — rollback: return to standard.

12. Accent color — visual option — Settings → Appearance — rollback: Default.

13. Show additional models — model visibility toggle — Settings → Advanced — OFF/ON — rollback: turn off.

14. Automatically correct spelling — spellcheck — ON/OFF — rollback: return as was.

15. Open ChatGPT links in desktop app — link redirection — ON/OFF — rollback: turn off.

16. Check for updates — manual version check — Settings → Check for updates — rollback: not applicable.

17. Maps provider — map choice (Apple Maps / Google) — Settings → Maps provider — rollback: change provider.

18. Position on screen, Reset to new chat, Keyboard shortcuts, Open new chats — chat panel — small UX settings — change in Chat panel → return standard values.

19. Enable working with applications — permission to interact with editors — ON/OFF — rollback: OFF; unbind applications. (recommend keeping ON and auto-apply OFF)

20. Toggle connection / Disconnect applications / Manage applications — managing sessions with applications — use for security — rollback: click "Disconnect" and revoke access in applications.

21. Auto-connection with applications from chat panel — automatic connection pickup — ON/OFF — rollback: OFF.

22. Form suggested edits / Automatically apply suggested edits — editorial suggestions — ON/OFF — don't enable auto-apply without verification.

23. Speech: Voice / Primary language / Audio settings — voice engine and recognition/voicing language — select voice and language — rollback: change back.

24. Autocomplete / Popular search queries / Tracking suggestions — hints and suggestions — ON/OFF — rollback: turn off if bothers.

25. Personalization — Memory — Link to saved memory / Reference chat history — (more detail above) — ON/OFF and Manage memories.

26. ADVANCED: Web search / Code / Canvas / Advanced voice — these features usually activated in Advanced/Personalization: enabling gives browsing, code interpreter, collaborative canvas and improved voice — carefully enable, check what permissions requested. For browser memory and its controls there are separate controls (see docs on Atlas).

**Nuances for browser version (web) and mobile version.**

Browser version (web.chatgpt.com / Atlas)

• In browser version Atlas / Browser is available — integrated browser (it can store "browser memories" — excerpts/summaries of page content) and separate controls for this memory. There are separate controls where you can view, disable and delete Browser memories. Some settings may be administered (on work device admin can block).

• Parental controls implemented in web version: you can invite parent and manage teenager's settings; connection configured in Settings → Parental controls.

Mobile version (iOS / Android)

• Mobile version usually repeats personalization and memory, but some functions (e.g., Project-only memory or part of integrations) may be unavailable on mobile at release time. Always check in Settings → Personalization and in app Release Notes.

• Pulse, Sora (video) and some experimental features often require Pro/plan and may roll out first to mobile devices with Pro access (as noted in release notes). Follow updates in official help.

**Most important official reference links (English)**

• Memory FAQ / Manage memories — official memory guide.

• Connectors in ChatGPT — how to work with integrations/connectors.

• Blog / announcement: Memory and new controls for ChatGPT — general overview of memory capabilities and management.

• Parental controls — how to set up parental controls.

• Web browsing / Atlas controls — managing browser memories and their deletion.

You've familiarized yourself with key settings, and if you didn't catch something - don't worry - we'll return to it. And now let's move on to the most interesting - ChatGPT's main capabilities. You should understand what your starship can do and what it can't, and be assured - AI can do a lot for you, especially if it's controlled by a smart pilot capable of learning and endowed with curiosity.


5. Basic Functions. What Can Your AI Do?

Great, you've arrived at the bridge of your AI starship and now you'll learn what your assistant is capable of. First we'll look at basic abilities, in the next section - advanced functions available only in paid version no lower than Plus. You need to understand what AI can do to reach the stars of your brightest fantasies (or dark nightmares).

Open your ChatGPT, let's go through the screen and I'll explain about each visible element in simple language: what it is, what it's for, usage example and why it's important.

![][PastedGraphic1]

**In central window: welcome message and "Ask anything" field**

What it is: main input — place where you write prompt (question or task) to model.

What for: this is the main way to communicate with ChatGPT — set topic, get answer in conversation window.

Why important: all interaction starts here — easy and similar to regular chat.

**Try This**: Write in window something like "Help compile lecture plan on topic 'Artificial Intelligence for Humanities'".

If you move mouse to right part of dialogue name - you'll see 3 (three dots), clicking them opens additional chat functions:

Share dialogue – creates link by which other users can see correspondence at moment of sending. Subsequent messages not displayed.

Archive dialogue (chat) - this function hides chat from list, but saves it in history. Most chats are disposable, but if long-term project is conducted, more convenient to archive rather than delete information. In process of working with artificial intelligence many chats quickly accumulate. Sometimes it seems some of them are insignificant, but later need may arise to return to them. To simplify search, you can use archiving. Archived chats remain accessible, but don't interfere in main list.

* Delete chat – this function completely deletes dialogue, which is not recommended, since communication history helps AI better understand context. Although there's possibility to delete chats, doing this is not recommended. Over time AI starts to better understand communication context, and interaction quality improves. If someone claims AI doesn't remember dialogues, this doesn't correspond to reality. It saves communication history, but limits access to information about its structure.

Rename chat - give it a convenient name for you.

Move to project - this function moves chat to project, which you can for simplicity perceive as folder with materials and chats devoted to one topic.

**In chat input field** — plus sign (+) - allows uploading documents and images to chat, as well as connecting additional capabilities:

* Create images based on your text
* Enable thinking mode when you want to ask something really complex from some subject area.
* Deep Research mode - deep research - extremely cool mode, allows finding information and making serious analytical reports from short to doctoral dissertation. We'll talk about this mode separately below, this mode will change your life.
* Research and learning mode - incredibly useful if you're learning with AI's help. We'll also talk especially. AI will change how you learn, and you'll understand that in 80% of cases - AI teaches better than human.
* Under More button - enabling web search when you want AI not just to answer, but also conduct internet search on your query topic. However, this mode can be enabled in prompt, which we'll talk about below.
* Canvas mode - convenient for editing AI-created documents - useful mode, we'll talk about it in more detail.

**Try This**: Click "+", enable image creation mode and enter prompt like this "Person quickly running on vertical wall with bear on shoulders. Bear wearing red cap, and bear holding tennis racket in paws." Save obtained image on disk or copy to clipboard (ctrl+c).

![][content]

**Try This**: Click "+", upload obtained picture (Ctrl+V) and give prompt "Redraw this picture in anime style, and instead of bear put a girl!"

![][content-1]

**Try This**: Continue - give prompt "Redraw this picture in photorealistic style against northern nature background"

![][content-2]

**Try This**: Find some article in Word/Page or PDF format, click + sign, upload article, and add prompt - "Analyze and give short summary". (In free plan may take long).

**Try This**: Find any table in Excel/Numbers format, copy it with Copy and paste into chat with Paste (can just drag with mouse), add prompt - "Analyze and give short summary". An obstacle-test awaits you - pass it.

**Try This**: Click "+", enable Deep Research mode and enter prompt "Make comparative review of poisonous mushrooms of middle zone with recommendation - how to recognize them and avoid poisoning". Answer clarifying questions, get result and experience shock.

Also in input field you see **microphone icon** and wave icon (right part of field). microphone — voice input; wave icon — voice mode launch.

What for: so you don't have to write by hand, but speak — convenient if you don't want to type.

**Try This**: Click microphone and say "Make brief review of novel 'Master and Margarita'". You'll see waveform of what you said appear in window. When you finish speaking text, click checkmark and ChatGPT will convert what you said into prompt text. Click - arrow to send. This way you can speak prompts instead of writing, simultaneously getting quite decent transcription. I recommend not dictating very long, sometimes there are failures. For long dictations there's another tool, we'll talk about it below.

Also in input field you see **wave icon** (right part of field). this is — voice mode launch. Super convenient. You start not just dictating to AI, but fully communicating by voice - you speak, ask and AI answers you in real time. This is - unreal. Especially convenient in mobile app. My wife talks for hours.

Why important? Voice speeds up work and makes service accessible to those tired of typing; but for this you need to allow browser to use microphone. You fully communicate with AI like with person. Sometimes very much speeds up when you need to discuss something.

**Try This**: Click wave icon, and interface will turn into bluish circle. AI is ready to listen and answer. Say - "Hi, how are you? What can you say?" To exit voice mode - click cross. Note - you get transcription of entire conversation.

**How to avoid AI interruptions in voice mode?**

During voice communication system sometimes starts answering before user finished speaking. This leads to loss of part of information. Simple solution – use **keyword**, for example **"analysis"**, which signals phrase completion. This helps AI correctly interpret pauses.

**Using mobile app for communication in foreign languages**

Mobile AI app can be used for **real-time translation**. This is especially convenient during travel or negotiations:

* AI can translate dialogue into different languages right during conversation.
* Translation performed **more accurately** than in most traditional translators.
* Can **configure language style** – British, American, academic or conversational.

**Practical example**: in Thailand doctor didn't know English, and I didn't know Thai. We used AI for translation from Russian to Thai and back, which completely eliminated language barrier.

**Important!** Under any AI answer there are several very useful buttons - first button for copying last AI answer to clipboard, which you can paste anywhere via Ctrl+C. Further rating buttons and button - share link to this AI answer. You click this button and AI gives you several options to choose from, including links and social networks. Circular arrows allow repeating answer to last question if first answer didn't satisfy you. Button for creating branch of this chat's answers in New chat. This is very convenient when you want to explore alternative scenario of answers to given question. Well, and can read answer aloud.

**Left panel — main navigation.**

We see here (New chat / Search chats / Library / Atlas / Projects)

**New chat** - launch new chat. This is useful when your dialogue became too long and model started getting confused and dumbing out. This happens in long dialogues, especially if you constantly change topics within one dialogue (or thread, as it's sometimes called). Model tries to somehow remember, understand and systematize, by default assuming one dialogue/chat/thread - one topic. But it doesn't happen that way))), especially with female users. Women possess ability to discuss million topics in short dialogue while man struggles to maintain one topic. Therefore in long dialogues model starts going crazy from bottomless erudition and breadth of problems discussed by women. Proven that AI must be 34% smarter to fully communicate with women.

**Try This**: Upload all statement above to AI and ask to check this thesis.

I uploaded - here's its answer: Interesting text — it's witty, but if you analyze it in essence, it combines real observations about language models' work with ironic (and partially stereotypical) statements about gender differences.

**1. What's true about "new chat"**

Yes, this is **absolutely true**. Models like GPT really hold context within one session. The longer dialogue and more often topics change in it, the:

* higher risk of "context blurring";
* harder for model to understand what's currently relevant;
* greater likelihood of "dumbness" or errors.

Therefore **new chat** is like "clearing conversation memory" and starting with clean slate. This is technically justified.

**2. About model "trying to remember and systematize"**

Also true in spirit of description. It doesn't *remember* in direct sense, but *builds semantic connections* within current dialogue. If topics too different — internal connections become "noisy".

**3. About differences in men's and women's communication**

Here begins **irony and mythology**. Research really shows that:

* women **more often change topics** and use **more connected and contextually rich speech style** (especially in informal conversation);
* men more often **structure speech linearly** and hold one topic longer.

But these are **tendencies, not rules**, and they strongly depend on culture, situation and personality.
There's no scientific proof that AI "must be 34% smarter" to talk with women 🙂 — this is a joke, but apt: it plays on idea that women's speech can really be **multilayered, associative and emotionally rich**, which is harder for algorithmic analysis.

⚖️ **4. Final analysis**

| **Statement** | **Truth** | **Comment** |
| :----- | :----- | :----- |
| New chat helps when dialogue became long | ✅ Yes | This reduces cognitive load on model |
| Model "goes crazy" from topic changes | 🔸 Partially true | Doesn't go crazy, but loses focus |
| Women discuss more topics in short time | ⚖️ On average — yes | Partially confirmed by linguistic research |
| AI must be 34% smarter for communication with women | 😂 Joke | But funny and psychologically apt |

**Search chats**

Search among your past conversations.

What for: quickly find old correspondence or material you requested before.

Example: "Find all chats where we discussed book structure".

**Library**

Place for saved pictures.

What for: don't reinvent the wheel — store useful templates.

Example: letter template, list of interview questions.

**Atlas -** offer to download browser with AI from OpenAI - useful thing that should be used carefully. We'll discuss its capabilities in detail.

**Projects** - super powerful capability that will blow your mind. We'll discuss its capabilities in detail, but briefly:

What it is: workspaces for large tasks (several related chats, materials, notes).

What for: structure large-scale work — book, course, product.

Example: "Book" project with separate chats for chapters and characters.

**And finally, important - "Chats" list — saved conversations (under navigation).**

This is list of your past conversations.

What for: return to what was already discussed.

**Try This**: Open old dialogue and continue discussion.

Why important: saves working history; useful for gradual work on large project (including capabilities of **Projects** option.

**At top center — "ChatGPT" name with dropdown triangle - this is place where you can switch modes or select model** - we already discussed this. For quick answers to simple questions - simple model. For serious questions where you're ready to wait (sometimes tens of minutes) - smartest model with reasoning. This is convenient because it saves time where "much intelligence" not needed.

![][PastedGraphic]

**"Get Plus" button (top right) - if free plan.**

This is paid plan offer. Can switch to subscription with advanced capabilities (faster, more powerful models, priority). If you often need long text or access to advanced modes — get Plus. Paid version gives additional resources, but it's not mandatory; evaluate whether you need this.

**Bottom left — avatar and name ("Free" status, Upgrade button nearby)**

• What: user profile and indicator that you have free account; "Upgrade" — link to upgrade.

• What for: manage account, understand limitations.

• Example: if you write often and want more functions, click Upgrade.

• Why important: free version limited in speed and capabilities — good to know where to change this.

**Empty central field (main area) — here answers and selected chat history will appear**

• What: main dialogue space — model response, formatting, links, etc.

• What for: read, edit and develop correspondence.

• Example: after question you see detailed answer, table or task list.

• Why important: this is your worksheet — everything created is displayed here.

6. Advanced Functions and AI Limitations. What Not to Expect? This is already for adults.

Using advanced functions you can implement 80-90% of standard tasks related to analysis, processing, synthesis of texts and any information, programming, working with images, conducting research, collecting information and thousands more things that AI will do instead of you without reducing quality or accelerating your productivity many times over.

However, AI at current stage of development isn't God, but executor, it has limitations, and knowing them, knowing how to overcome them - you'll get outstanding results quickly, rather than being disappointed and wasting time uselessly. Perceive AI as violin - with skill you can extract divine sounds, but if you hammer nails with violin, you'll undoubtedly experience strong disappointment.

When you're just starting, you're often inclined to blame AI for dumbness if result didn't satisfy you. You can believe (or not), but quality of result AI gives you in answers - 95% depends on quality of your requests and general approaches in working with AI, on your understanding of nuances, on skills using AI's huge capabilities. Want to reach the stars - read on and complete all simple exercises, try immediately. However, for lazy ones who don't want to learn and look for someone to blame in everything - AI won't help. Sorry for this sad admonition. There are no miracles, except in your head and heart. Don't look for miracles in AI, look for them in yourself.

**Connecting applications and organizing work**

AI allows integrating third-party applications such as **Google Drive, Notion, Cursor** and others. This is useful if you need to simultaneously work with documents or notes, and AI can interact with them in real time. When we say "connecting applications" — this means AI system doesn't just answer questions or generate text, but can interact with other programs/services (e.g., Google Drive, Notion, Zapier/Make). These connections give new capabilities: automation, data synchronization, workflow setup.

![][PastedGraphic2]

For example: AI can find file on Google Drive, read it, make changes, update note in Notion, notify you or colleagues by e-mail, create task in project management system — without you manually switching from application to application and copying/pasting. Connecting applications is **not mandatory**. I.e. basic AI chat functions (input-answer) work without integrations. Connections are capability expansion. Imagine yourself (or me) as marketing and automation consultant (suitable situation for my profile).

**Scenario**: you run blog, do mailing, collect ideas and notes in Notion, work with documents in Google Drive. You want AI to help not only generate text, but also automatically update your system.

**How workflow with integrations might look**:

1. You mark task in Notion: "Write guide article about AI for beginners".
2. Automation links Notion with ChatGPT: AI gets data from task ("topic", "target audience", "key points") and generates article draft.
3. Then AI saves draft to Google Drive, creates file copy, places in "Drafts" folder.
4. AI notifies you in Slack or Telegram: "Draft ready — check".
5. At your command AI can then send article to mailing or prepare social media post.

Less manual work, less switching between applications, smoother workflow. Meanwhile you can still enter topic manually in ChatGPT and get text, but then copy-paste, create files, notify yourself manually — all this remains your work. **Connecting applications** - allows saving time and reducing "routine switches" between applications, increases efficiency: AI becomes part of workflow, not just tool, creates more "smooth" experience — less friction in transition from idea to execution.

But there are also "minuses": Connections may require configuration, possibly knowledge of integration platforms or help from outside. More integrations — higher risk of errors, data leaks or incorrect automation. If you rarely use complex chain of applications, benefit may be small — basic AI function may suffice.

**By the way**: I personally don't use application connection, although perhaps out of laziness and didn't see clear benefit, but I know those who actively use. Well and besides, I'm perhaps paranoid, but I have doubts about security. We'll talk a lot about this problem below - this is very, very important! Play around - maybe you'll find something useful for yourself.

**"Edit in canvas" mode**

Allows splitting screen into two windows: one has communication with AI, other - editable text. This is convenient when working with documents, since you can correct result right during dialogue process.

![][Снимокэкрана2025-11-03в000307]

Imagine you're talking with ChatGPT, and next to it — window is open where you can edit text live: article, script, letter, idea. This is **"Edit in canvas" mode (or Canvas Mode)**. It divides screen into two parts: **left** — your chat with AI, where you discuss what and how needs to be corrected; **right** — document itself, where you can immediately see and edit text that's being created or corrected.

**Why is this needed?** Previously had to copy text from chat, paste into editor, change, return to AI again — inconvenient. Now everything happens **in one place**, without switching. AI sees document text and can suggest point corrections, improvements, ideas right in process. And you — decide yourself whether to accept suggestion, correct manually or write anew.

**Example (case) situation:** you're writing blog article about how to stop fearing artificial intelligence. You open new document in ChatGPT and enable "Edit in canvas" mode. In right window start draft — enter couple paragraphs. In left window ask AI: *"Make introduction more lively, add some humor, but without banalities".* ChatGPT analyzes text and suggests specific changes — right in same document. You see suggestions, choose which to keep, which to reject. In a minute you already have improved version of text — without constant copying between programs.

**What's convenient?** Real-time editing, can correct without interrupting conversation with AI. Everything visible contextually. AI understands text structure and sees what you've already written. Suitable for working on long texts, Articles, books, scripts, letters — everything where style and structure important.

Imagine you're sitting with editor at one table: you dictate ideas, and they immediately write and suggest phrase variants. You correct, they instantly react. "Edit in canvas" mode is same effect, only instead of live person AI works nearby.

**Try This**: Enable Canvas mode (clicking "+" and "More"), and enter prompt: "We're talking about paid ChatGPT version capabilities. Expand and explain in more understandable words for non-techie, give example, case: 'Edit in canvas' mode. Allows splitting screen into two windows: one has communication with AI, other - editable text. This is convenient when working with documents, since you can correct result right during dialogue process." This is case when it's easier to see than read, and remember - if something unclear - immediately ask your ChatGPT, and if completely unclear, take screenshot and ask for explanations - 100% effective.

![][PastedGraphic3]

What will you see (roughly)?

![][PastedGraphic4]

Here's most interesting - Edit button, click it and see next picture.

![][PastedGraphic5]

1. Left part of screen — AI chat window. This is familiar ChatGPT dialogue zone. Here you ask questions and give instructions (e.g.: *"rewrite this paragraph simpler"*), get answers and suggestions from AI, see history of your messages and model responses. Can discuss edits, ask to improve text, set tone or style. AI sees what document you're working on, and gives contextual suggestions.

2. Right part of screen — Canvas. This is built-in text editor where document itself displays. You can write and edit text manually, see AI-suggested changes, instantly apply or reject them. Feature: this text linked to your dialogue. ChatGPT "understands" what you're currently editing, and considers this in answers.

3. Toolbar above document. Located there are buttons for: Text formatting (bold, italic, headers, etc.); Collaboration with AI — *"Ask ChatGPT"* button allows selecting text fragment and immediately getting improvement suggestion; Settings and document actions (save, copy, export, etc.).

4. "Suggest changes" button (bottom right) allows asking AI to make edits to entire document or its part. ChatGPT will suggest updated variant right in same window.

5. Bottom panel under chat - standard input line, where you can write requests manually, activate voice input, enable canvas mode ("Canvas" button next to "+" icon), to switch between regular chat and editor.

Everything united in one space: chat + document + intelligence. No need to copy, switch between windows and editors — entire process of writing, editing and refining text goes in unified flow.

**Saving dialogues** - not directly provided, but there are several ways:

* **Copy individual answer** – can manually save important fragments.
* **Select entire dialogue** – copy entirely and paste into text editor.

Some models allow generating files, but this process doesn't always work correctly. If full dialogue export important, for now most reliable way remains manual copying.

**Creating custom GPT models**

This is big and very cool topic, which we'll devote large section to, because ability to create custom GPT models gives you real productivity boost. Here only - main idea - system allows creating own specialized AI (GPT models) for solving specific routine frequently repeated tasks requiring complex prompt. For example, if transcribed text editing often required, you can create special model that automatically performs processing, getting rid of errors and unnecessary words.

There's possibility to publish such models in public access or use only for personal needs. For this profile builder exists, where you can configure publicity or closed access.

**Why is this super convenient?** When frequently working with AI it's important to have prompts prepared in advance. And honestly speaking, creating effective prompt is kind of art (which you'll master by reading book), plus requires time, and if you have to enter complex prompt manually every time, it's inconvenient. Creating custom GPTs is ability to save and configure prompts, which allows using prompts many times, duplicating successful prompts, making many versions, automating routine tasks, avoiding constant input of same instructions, creating many **(GPT-shki)** that adapt to different tasks. In free version such possibility doesn't exist, which makes work less convenient.

**Projects**

This is also big topic, which we'll devote large section to, but briefly - this function allows working on large projects where many thematic chats, documents, tables, images in one place. Project function allows saving work context, because AI remembers details of different chats within project, adding files for analysis and work, working with different AI models depending on tasks inside project. This significantly increases work efficiency, especially in long-term research or analytics, content creation, writing voluminous and complexly structured texts.

**Deep Research**

Oh, about this function you can talk long and in detail and it will also be devoted section, but briefly - this is bomb, "long run" through internet: AI itself plans steps, searches through dozens–hundreds of sources, reads, verifies versions, and then issues coherent report with links. In essence — "researcher-analyst inside ChatGPT". ([OpenAI](https://openai.com/index/introducing-deep-research/?utm_source=chatgpt.com))

**When to enable mode and when not?**

* **Enable** if question complex: "Collect market overview X", "Compare A/B approaches in research", "Prepare source summary on topic Y". AI does multi-step research and returns detailed report with quotes. ([OpenAI Help Center](https://help.openai.com/en/articles/10500283-deep-research-faq?utm_source=chatgpt.com))
* **Don't enable** for quick facts/news — there regular "Search" sufficient (short answer + links). Difference: **Search = quick and short; Deep Research = longer and deeper**. ([OpenAI](https://openai.com/index/introducing-chatgpt-search/?utm_source=chatgpt.com))

**Example:** you're preparing book chapter "How Not to Fear AI" and want section "Ethics and risks".

1. Formulate request: "Collect leading universities and NGOs position on AI risks for last 2–3 years. Give 5–7 key theses, indicate primary sources".
2. Deep Research suggests plan: what terms to search, what institutes and reviews to check, what years/regions to cover. You accept or correct plan, answer clarifying questions.
3. AI reads sources, compares conclusions, marks discrepancies, forms **report with quotes** and "what to check manually".
4. You ask: "Compress to 2 pages and add 'what's controversial' block". Get final text + link list (for verification and footnotes). ([OpenAI](https://openai.com/index/introducing-deep-research/?utm_source=chatgpt.com))

**What can be connected as sources**

By default — open network + your uploaded files. If you connect supported applications (drive/notes, etc.), AI can also rely on them **with your permission**. All conclusions accompanied by links. ([OpenAI Help Center](https://help.openai.com/en/articles/10500283-deep-research-faq?utm_source=chatgpt.com))

**Limits and availability (briefly)**

Function exists for paid plans (Plus/Team/Enterprise/Edu), with monthly task limits; there's also "light" version for quick/cheap runs (Free has very limited). Specific quotas change — watch counter in interface. ([OpenAI](https://openai.com/index/introducing-deep-research/?utm_source=chatgpt.com))

**Deep Research -** saves hours of manual googling, gives **structured report with sources**. ([Reuters](https://www.reuters.com/technology/openai-launches-new-ai-tool-facilitate-research-tasks-2025-02-03/?utm_source=chatgpt.com)), better identifies contradictions between articles and marks "what else to check". ([OpenAI](https://openai.com/index/introducing-deep-research/?utm_source=chatgpt.com)), works longer than regular search mode (Search); part of conclusions still requires human verification of source quality, limits on number of tasks; availability and quotas depend on plan/region. ([OpenAI Help Center](https://help.openai.com/en/articles/10500283-deep-research-faq?utm_source=chatgpt.com))

**How to ask Deep Research correctly (template):** "Form topic overview **X** for **period**; list **3–5** key positions, give **quotes/links** to primary sources; mark **discrepancies** and **gaps** in data; format **conclusions + verification list**". Such request gives AI clear plan: framework, format, quality criteria.

**Case 1. Preparing analytical review. Situation:** you're preparing article "How AI Changes Education Market".
Want not just examples, but exactly trend overview, expert quotes, source links.

**Prompt:**

Conduct deep research on topic "artificial intelligence influence on education in 2022–2025". Collect 5–7 key trends with source indication, quotes and dates. Divide result into: 1) current changes, 2) risks, 3) 3-year forecast. Indicate which sources raise doubts and why.

**What Deep Research does:** Reviews reports, research, EdTech company news and prepares structured overview with direct source links.

**Case 2. Comparing strategies or approaches. Situation:** you consult business and want to understand how AI implementation strategies differ at OpenAI, Anthropic and Google DeepMind.

**Prompt:**

Compare AI development strategies at OpenAI, Anthropic and Google DeepMind companies for last two years. Determine: 1) key goals, 2) safety approach philosophy, 3) business model, 4) expert forecast. Give sources and mark discrepancies in their assessments.

**What Deep Research does:** Goes through corporate publications, interviews, official statements, analytical articles — and issues comparative table/overview.

**Case 3. Preparing lecture, book or course. Situation:** you're writing book "AI — New Freedom" and want chapter about how AI affects creativity.

**Prompt:** Prepare analytical research on topic "AI influence on creative professions" with 2023–2025 examples. Divide material into blocks: 1) positive effects, 2) losses and conflicts, 3) development forecast. Add 5 expert quotes and 5 links to real cases (music, cinema, literature). Mark which conclusions controversial and why.

**What Deep Research does:** Collects fresh interviews, Creative Commons reports, musician, writer, director cases — and forms structured summary with facts and quotes.

**Model Limitations. Why AI Isn't Wizard but Tool?**

Yes, ChatGPT can do a lot: write texts, explain complex things, come up with ideas, even code. But it's important to understand — **it's not God and not thinker**, but **executor**, and very obedient one. It does what you tell it, **within its logic, memory and data** it was trained on. This is like tool — **violin, brush or camera**. In skilled hands they create masterpieces, but in unskilled — cause disappointment.

**Why sometimes seems AI "dumbs out"?** It doesn't know your intentions. It doesn't sense context if you didn't explain it directly. If you gave general request — you'll get too general answer. If you asked clear, contextual and structured question — you'll get precise and deep result.

Bad prompt - "Write text about business." Good prompt - "Write short Instagram post about how entrepreneur can stop fearing AI. Tone — friendly, with humor, length — up to 100 words." Difference will be colossal, because AI doesn't guess your thoughts, it **follows instruction, prompt**.

**Main AI limitations (at current time) worth knowing**

1. **It doesn't know future.** Everything it writes — analysis of past and present, not prediction.
2. **It doesn't read your mind.** Need to explicitly indicate goals, style, audience and format.
3. **It can make mistakes.** Even if writes confidently. Therefore — check.
4. **It doesn't replace experience.** It accelerates path to result, but responsibility for choice and meaning remains with you.

To get quality answers from AI, it's important to learn to correctly formulate requests (**prompts**). Main principle – the more precise request, the better result. Simple requests work in most cases, but for complex tasks more detail required. Additionally, finding ideal answer often requires **iterative approach**:

**First answer** – often basic, may not meet expectations. You give **additional clarifications** – they allow directing AI in right direction. Further - **sequential improvement** – request correction leads to more precise result. Common mistake – make one request, get non-optimal answer and immediately consider AI "stupid". Much more productive to make corrections and refine request.



7. What You Need to Understand?

The truth is that for different people artificial intelligence behaves completely differently. For some it seems to them it dumbs out, produces inadequate results, lies, adapts, flatters. In general, people struggle with it, get disappointed, consider it completely useless thing.

But at the same time there are masses of people — I belong to them — who consider artificial intelligence the most powerful, effective tool ever created in human history. And this second group of people gets completely fantastic results, discovers incredible capabilities and does amazing things that were simply impossible to realize before.

The entire difference between these groups is only in mastering skill of interacting with artificial intelligence: how to come up with prompts, how to manage context and so on. And, of course, you can say that this entire book is largely devoted precisely to this — creating prompts for solving various tasks: from simple to complex, requiring reasoning, analysis, data collection and so on.

Moreover, in both simple and complex tasks you can give unsuccessful, weak prompts and get corresponding, pitiful results. But as soon as you start understanding how model works, how its principles are structured, look at examples, approaches, study methodology — and it, by the way, isn't complex, we'll examine all this in detail — literally new reality opens before you.

Over the last year probably more than 40 thousand people passed through my courses. You can look at statistics — I'm talking about free courses made for people to use, not counting that I have quite many subscribers — over 100 thousand at the moment, and this number is growing fast. Artificial intelligence is now main topic I write about.

I.e. I receive gigantic volumes of feedback, and once again want to emphasize: when it seems to you AI "dumbs out" or behaves strangely — believe me, in 98% of cases problem isn't in artificial intelligence, but in that you don't know how to work with it. This, by the way, applies to developers and IT people. It would seem these people should better understand how artificial intelligence works, how to effectively interact with it. However this isn't always so. Because deep psychology that determines personality — how person learns, how they perceive innovations — isn't connected to profession at all.

Now there's gigantic gap between those who show curiosity, learn, don't judge, figure out, constantly seek answer to question "how to make better, more efficient, more practical", — and those who don't do this. Curious people take off, and at the same time masses of quite professional people remain — including developers and programmers, those who supposedly work in industry, — but for some reasons they have prejudices. They terribly lag behind, stubbornly refuse to accept AI, considering themselves smartest in room. Sad, but we won't discuss this.

Everyone makes their choice. And your life, fate, success, growth depend on this choice. Don't be lazy. Have open mind, curiosity. Make mistakes, learn from your mistakes — and for you there will be nothing impossible. AI to help you. Well, and Force, of course.


8. What Next? Start the Quest!

Now you more or less know which buttons to press, or at least where to look and whom to ask - ChatGPT itself. Now it's time to start Quest, pass trials and receive Level 1 rewards.


[PastedGraphic1]: PastedGraphic1.png width=959px height=613px

[content]: content.png width=397px height=618px

[content-1]: content.png width=416px height=678px

[content-2]: content.png width=426px height=677px

[PastedGraphic]: PastedGraphic.png width=564px height=679px

[PastedGraphic2]: PastedGraphic2.png width=566px height=1006px

[Снимокэкрана2025-11-03в000307]: Снимокэкрана2025-11-03в000307.png width=488px height=290px

[PastedGraphic3]: PastedGraphic3.png width=713px height=222px

[PastedGraphic4]: PastedGraphic4.png width=653px height=262px

[PastedGraphic5]: PastedGraphic5.png width=644px height=275px
