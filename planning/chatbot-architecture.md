# Chatbot Architecture for the Computational Geography Series

## Purpose

This document proposes an architecture and product direction for a conversational interface over the `Computational Geography` project.

The intent is not to add a generic chatbot to the site.

The intent is to design a research companion that can sit over:

- `Start Here`
- `Core Book`
- `Topic Libraries`
- `Laboratory`
- `Methods and Tools`
- future `Golden Paths`
- a future `Role / Function / Use-Case Library`

This should be understood as a planning document for a serious editorial and technical layer, not a novelty feature.

## Editorial Thesis

The project now has enough depth and internal structure that readers will increasingly need help with:

- where to start
- which concepts connect to which methods
- how discrete chapters assemble into a workflow
- which parts of the project matter for a given research question
- how to move from concept to application without already knowing the architecture

This makes the project a strong candidate for a conversational interface.

But the interface should not behave like a general-purpose assistant that happens to know about the book.

It should behave more like:

- a guided research companion
- a study and tutoring layer
- a workflow and path-building layer
- a structured retrieval system with conversational explanation

## Product Goal

The chatbot should help readers do four things well:

1. understand concepts from the series in plain language
2. find the right chapters, paths, and methods for a research question
3. assemble a practical workflow from question to output
4. compare approaches without losing sight of assumptions and limits

The chatbot should not primarily optimize for open-ended conversation.

It should optimize for:

- trustworthy guidance
- visible provenance
- strong reader orientation
- workflow usefulness

## Working Product Name

A useful internal working name would be:

- `Wayward Research Companion`

That name is broad enough to include:

- tutoring
- workflow guidance
- role-based navigation
- path assembly

without reducing the interface to a support bot.

## Why A Simple RAG Bot Is Not Enough

This project is not just a collection of documents.

It already contains an implicit editorial architecture:

- beginner-safe pathways
- specialist branches
- advanced investigations
- methods and tools
- emerging golden paths

A simple semantic search layer over chunked text would miss too much of that structure.

It might retrieve relevant paragraphs.

It would not consistently retrieve:

- the right chapter sequence
- the right workflow object
- the right reader pathway
- the right role-based entry point
- the right adjacent material

So the system should not be built as `vector search + LLM prompt` alone.

It should be built as a hybrid knowledge system.

## Recommended System Model

The strongest architecture is a hybrid of:

- `RAG` over the written corpus
- `structured retrieval` over editorial metadata
- `workflow retrieval` over golden paths and use-case objects
- `light orchestration` that can classify user intent and assemble the right context

This is the core design principle:

- use unstructured text for explanation
- use structured objects for navigation, relationships, and path guidance

## Architectural Layers

The system is best understood in five layers.

## 1. Content Layer

This is the raw source material.

Initial inputs:

- chapter `.qmd` files
- planning `.md` files
- golden path drafts
- section landing pages

Likely later inputs:

- glossary or concept definitions
- figure captions
- illustration notes
- role/use-case pages
- methods notes

The content layer should remain the source of truth for prose.

## 2. Knowledge Layer

This is the structured representation of the editorial system.

The project should model content as explicit objects rather than only as chunks.

Minimum entity types:

- `Volume`
- `Chapter`
- `GoldenPath`
- `Role`
- `UseCase`
- `Concept`
- `Method`
- `DataType`
- `Output`

Useful relationships:

- `Chapter belongs_to Volume`
- `Chapter teaches Concept`
- `Chapter uses Method`
- `GoldenPath uses Chapter`
- `GoldenPath serves Role`
- `GoldenPath addresses UseCase`
- `UseCase needs DataType`
- `Method produces Output`
- `Chapter adjacent_to Chapter`
- `GoldenPath adjacent_to GoldenPath`

This layer is what allows the chatbot to guide rather than merely summarize.

## 3. Retrieval Layer

The retrieval layer should be hybrid.

### Semantic Retrieval

Use embeddings for:

- conceptual similarity
- plain-language question matching
- finding relevant explanatory chunks

### Lexical Retrieval

Use keyword or BM25-style retrieval for:

- exact terms
- chapter titles
- named models
- acronym-heavy queries
- discipline-specific vocabulary

### Structured Retrieval

Use metadata lookups for:

- role entry
- use-case entry
- chapter families
- difficulty
- data types
- path families
- linked chapters

### Reranking

After retrieval, use reranking to build a compact, high-quality context pack containing:

- explanatory text
- relevant chapters
- relevant golden paths
- adjacent paths or chapters where helpful

## 4. Orchestration Layer

The chatbot should classify user intent before deciding how to retrieve and answer.

The system does not need a complex agent framework at first.

It does need query routing.

Useful intent classes:

- `Concept question`
- `Workflow question`
- `Role-based entry question`
- `Comparison question`
- `Study or tutoring question`
- `Navigation question`

Examples:

- `What is NDVI?` -> concept
- `How would I investigate urban flood risk?` -> workflow
- `I work in municipal planning. Where should I start?` -> role-based entry
- `Should I use change detection or time-series analysis here?` -> comparison
- `Teach me the difference between slope and aspect.` -> tutoring
- `What chapters belong to the core path?` -> navigation

The orchestration layer should then assemble the right response mode and the right supporting objects.

## 5. Experience Layer

This is the visible interface.

The key product decision is:

do not make the experience a blank chat box alone.

The interface should expose the project's architecture while still feeling conversational.

## Recommended UI Model

The most promising first interface is a three-panel layout.

### Left Rail: Navigation

This should expose the series architecture directly:

- `Start Here`
- `Core Book`
- `Topic Libraries`
- `Laboratory`
- `Methods and Tools`
- `Golden Paths`
- `Roles`

This keeps the chatbot grounded in the editorial structure rather than floating above it.

### Center Panel: Conversation

This is the main chat area.

The assistant should respond conversationally, but with clear structure.

Each answer should usually include:

- a direct answer
- supporting concepts or assumptions
- suggested next chapters or paths
- citations or visible provenance

### Right Panel: Live Context

This panel should show the objects currently in play.

Examples:

- chapter cards
- golden path cards
- concept cards
- cited excerpts
- suggested next steps

This makes the system feel inspectable and reduces the black-box problem common in chat interfaces.

## Recommended Entry Modes

The interface should support three main starting points.

### 1. Ask A Question

For readers who already know what they want to ask.

### 2. Browse By Role

For readers who think in professional or functional terms.

Examples:

- planner
- hazard analyst
- watershed manager
- remote sensing analyst
- emergency management officer

### 3. Browse By Research Goal

For readers who think in use cases or outcomes.

Examples:

- monitor change
- screen flood risk
- assess avalanche exposure
- identify bottlenecks
- map accessibility

This aligns especially well with the proposed golden-path framework.

## Conversation Modes

The assistant should likely expose several named modes, even if the mode switching is subtle.

### Explain

Used for concept questions and chapter explanation.

### Guide

Used for helping readers find the right part of the project.

### Assemble

Used for building a workflow from question to data to method to output.

### Compare

Used for method comparison, tradeoffs, and alternatives.

### Study

Used for tutoring, scaffolding, and beginner-friendly support.

The reason to think in modes is not aesthetic.

It is to keep answers matched to intent.

## Retrieval Strategy In Practice

The system should use different retrieval priorities depending on the query.

### For Concept Questions

Prioritize:

- chapter chunks
- concept objects
- beginner-safe explanatory material

Return:

- explanation
- one or two relevant chapters
- adjacent concepts

### For Workflow Questions

Prioritize:

- golden paths
- linked chapters
- methods and output objects

Return:

- a suggested path
- minimum data needs
- likely outputs
- next reading steps

### For Role Questions

Prioritize:

- role objects
- associated use cases
- recommended starter paths

Return:

- a role-oriented entry point
- a small set of likely workflows
- core chapters to start from

### For Comparison Questions

Prioritize:

- method objects
- chapter pairs
- path branches

Return:

- differences
- tradeoffs
- when each approach is a better fit

## Metadata Requirements

The chatbot will be much better if the project has lightweight metadata attached to major objects.

Minimum metadata for chapters:

- `chapter_id`
- `title`
- `volume`
- `part`
- `difficulty`
- `core_or_extension_or_laboratory`
- `concepts`
- `methods`
- `data_types`
- `outputs`
- `adjacent_chapters`

Minimum metadata for golden paths:

- `path_id`
- `title`
- `path_type`
- `path_family`
- `roles`
- `use_cases`
- `difficulty`
- `spatial_scale`
- `temporal_scale`
- `data_types`
- `outputs`
- `linked_chapters`
- `adjacent_paths`

Minimum metadata for roles:

- `role_id`
- `title`
- `common_use_cases`
- `recommended_paths`
- `recommended_starting_chapters`

## Knowledge Representation Options

There are at least three reasonable implementation choices.

### Option 1: Metadata In Frontmatter Or Sidecar Files

Store metadata close to the content in:

- YAML frontmatter
- JSON sidecar files
- generated manifest files

Benefits:

- simple
- transparent
- version-controlled with the content

This is likely the best first choice.

### Option 2: Postgres With Metadata Tables

Store structured objects in relational tables and use the repo content as input to ingestion.

Benefits:

- queryable
- stable
- works well with `pgvector`

This is a strong production option.

### Option 3: Graph Database

Store the relationships as a graph.

Benefits:

- expressive for relationship traversal

Costs:

- probably too much complexity for a first version

Recommendation:

start with content-side metadata plus Postgres.

Use graph-like relationships in schema design without committing to a separate graph database immediately.

## Suggested Technical Stack

The stack does not need to be exotic.

A pragmatic version could use:

- content ingestion from `.qmd` and `.md`
- metadata extraction from sidecar or frontmatter
- `Postgres` for structured content
- `pgvector` for embeddings
- an API layer in `Python` or `Node`
- a web frontend for chat plus context cards

This is enough for:

- hybrid retrieval
- object-based navigation
- response assembly
- citations and context display

If a dedicated vector database is preferred later, the system could move to:

- `Qdrant`
- `Weaviate`

But that is not required for a strong first implementation.

## Ingestion Pipeline

The ingestion pipeline should likely do five things:

1. parse source content
2. strip or normalize markup where needed
3. split text into retrievable chunks
4. extract or attach structured metadata
5. generate embeddings and store retrieval objects

The pipeline should preserve links back to:

- source file
- section heading
- content object
- volume and family

That provenance is important for trust and UI display.

## Response Design

Every strong answer should aim to include:

- a direct answer
- why the answer is relevant to the user's question
- visible references to chapters or paths
- suggested next steps

For workflow questions, the assistant should preferably return:

- the likely best starting path
- minimum data needed
- likely outputs
- optional deeper branches

For concept questions, it should preferably return:

- a plain-language explanation
- a mathematical or modelling interpretation when relevant
- where to read next in the series

## Example User Journeys

### Journey 1: Beginner Learner

Question:

`What is a watershed and why does it matter for flood modelling?`

Likely system behaviour:

- retrieve beginner-safe watershed explanation
- retrieve watershed delineation chapter
- retrieve adjacent flood chapters
- answer in `Explain` mode
- suggest a next reading sequence

### Journey 2: Planner

Question:

`I work in municipal planning and want to understand urban flood risk. Where should I start?`

Likely system behaviour:

- classify as role + workflow question
- retrieve urban flood golden path
- retrieve supporting core chapters
- answer in `Guide` mode
- show a path card and chapter cards

### Journey 3: Research Design

Question:

`I want to monitor drought stress in vegetation over time. What data and models should I use first?`

Likely system behaviour:

- retrieve vegetation stress path
- retrieve remote sensing and time-series chapters
- answer in `Assemble` mode
- provide minimum data needs and extensions

### Journey 4: Method Comparison

Question:

`When should I use change detection instead of a time-series approach?`

Likely system behaviour:

- retrieve both relevant chapters
- compare assumptions and use cases
- answer in `Compare` mode
- show adjacent path suggestions

## Trust And Safety Considerations

The main risk is not only hallucination.

The main risk is false confidence in workflow advice.

The interface should therefore:

- cite content objects visibly
- distinguish screening from calibrated modelling
- avoid claiming certainty when the underlying material is conditional
- show assumptions and limits clearly

For planning, hazard, and infrastructure questions, this matters especially.

The system should lean toward:

- `here is a dependable starting workflow`

rather than:

- `here is the definitive answer`

## Phased Roadmap

## Phase 1: Internal Prototype

Build a private prototype over:

- selected chapters
- planning docs
- golden-path pilots

Capabilities:

- chat
- hybrid retrieval
- chapter citations
- path suggestion cards

Goal:

prove that the system improves navigation and workflow discovery.

## Phase 2: Structured Companion

Add:

- chapter metadata
- golden-path metadata
- role/use-case objects
- better context panel

Goal:

turn the system from document chat into a guided series companion.

## Phase 3: Public Beta

Add:

- role browsing
- research-goal browsing
- saved path suggestions
- stronger onboarding and study mode

Goal:

make the companion usable as a real reader interface.

## Phase 4: Tool-Enhanced Research Guidance

Potential later additions:

- lightweight workflow builders
- custom path assembly
- simple concept quizzes
- optional calculation or notebook handoff
- user-uploaded problem statements

Goal:

expand from guidance into light research design support.

## Recommended First Build

If the project wants the strongest ratio of value to complexity, the first build should be:

- a hybrid retrieval chatbot
- over chapters, planning docs, and golden-path pilots
- with chapter cards and path cards in the UI
- and a small number of explicit query modes

This would already allow the system to do something much more valuable than a generic book chatbot:

- help users find a path through the project
- explain why that path fits their question
- show where to go next

## Relationship To Golden Paths

Golden paths are likely the most important structured object for this system after chapters themselves.

They are the bridge between:

- static content
- user intent
- practical workflow guidance

In that sense:

- chapters are the knowledge units
- golden paths are the orchestration units

This is one reason the golden-path framework is strategically valuable even before a chatbot exists.

It creates the intermediate structure that a conversational interface can use to guide rather than merely retrieve.

## Working Recommendation

The project should treat a chatbot not as an add-on feature, but as a possible new interface layer for the whole series.

The strongest conceptual model is:

- a `Wayward Research Companion`
- built on hybrid retrieval
- grounded in explicit editorial metadata
- centered on chapters, golden paths, roles, and use cases
- designed to explain, guide, compare, and assemble workflows

If built this way, the chatbot could become one of the clearest ways to make the project's depth more usable without flattening its architecture.
