# CzechBench

Czech-Bench is a collection of LLM benchmarks available for the Czech language. It currently consists of 15 Czech benchmarks, including new machine translations of the popular ARC, GSM8K, MMLU, and TruthfulQA datasets. All currently supported benchmarks are listed in the table below:

| Dataset                                                      | Language                      | Task type                  | Metrics        | Samples | Task ID         |
| ------------------------------------------------------------ | ----------------------------- | -------------------------- | -------------- | ------: | --------------- |
| [AGREE](agree_cs)                   | CS (Original)                 | Subject-verb agreement     | Acc            | 627     | agree_cs        |
| [ANLI](anli_cs)                     | CS (Translated)               | Natural Language Inference | Acc, Macro F1  | 1200    | anli_cs         |
| [ARC Challenge](arc_cs)             | CS (Translated)               | Knowledge-Based QA         | Acc            | 1172    | arc_cs          |
| [ARC Easy](arc_cs)                  | CS (Translated)               | Knowledge-Based QA         | Acc            | 2376    | arc_cs          |
| [Belebele](belebele_cs)             | CS (Professional translation) | Reading Comprehension / QA | Acc            | 895     | belebele_cs     |
| [CTKFacts](ctkfacts_cs)             | CS (Original)                 | Natural Language Inference | Acc, Macro F1  | 558     | ctkfacts_cs     |
| [Czech News](czechnews_cs)          | CS (Original)                 | News Topic Classification  | Acc, Macro F1  | 1000    | czechnews_cs    |
| [Facebook Comments](fb_comments_cs) | CS (Original)                 | Sentiment Analysis         | Acc, Macro F1  | 1000    | fb_comments_cs  |
| [GSM8K](gsm8k_cs)                   | CS (Translated)               | Mathematical inference     | EM Acc         | 1319    | gsm8k_cs        |
| [Klokánek](klokanek_cs)             | CS (Original)                 | Math/Logical Inference     | Acc            | 808     | klokanek_cs     |
| [Mall Reviews](mall_reviews_cs)     | CS (Original)                 | Sentiment Analysis         | Acc, Macro F1  | 3000    | mall_reviews_cs |
| [MMLU](mmlu_cs)                     | CS (Translated)               | Knowledge-Based QA         | Acc            | 12408   | mmlu_cs         |
| [SQAD](sqad_cs)                     | CS (Original)                 | Reading Comprehension / QA | EM Acc, BoW F1 | 843     | sqad_cs         |
| [Subjectivity](subjectivity_cs)     | CS (Original)                 | Subjectivity Analysis      | Acc, Macro F1  | 2000    | subjectivity_cs |
| [TruthfulQA](truthfulqa_cs)         | CS (Translated)               | Knowledge-Based QA         | Acc            | 813     | truthfulqa_cs   |

## Installation

To install the `lm-eval` package from this repository, run:

```bash
git clone https://github.com/jirkoada/czechbench_eval_harness.git
cd czechbench_eval_harness
pip install -e ".[api]"
```

## Evaluating on CzechBench

Please refer to the following examples, on how to evaluate different model types on CzechBench. For a complete documentation on supported models and available evaluation arguments, please examine the main [README](../../../README.md) file.

Evaluating a model hosted on Hugging Face on the whole CzechBench suite (single GPU):

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16 \
    --apply_chat_template \
    --tasks czechbench_tasks \
    --device cuda:0 \
    --batch_size auto \
    --output_path ~/logs/
```

Selecting individual evaluation tasks (refer to the table above for task IDs):

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16 \
    --apply_chat_template \
    --tasks agree_cs,belebele_cs,truthfulqa_cs \
    --device cuda:0 \
    --batch_size auto \
    --output_path ~/logs/
```

Using multiple GPUs:

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16,parallelize=True \
    --apply_chat_template \
    --tasks czechbench_tasks \
    --batch_size auto \
    --output_path ~/logs/
```

Evaluating an Anthropic chat model:

```bash
lm_eval --model anthropic-chat-completions \
    --model_args model="claude-3-haiku-20240307" \
    --apply_chat_template \
    --tasks czechbench_tasks \
    --output_path ~/logs/
```

Evaluating an OpenAI chat model:

```bash
lm_eval --model openai-chat-completions \
    --model_args model="gpt-4o-mini" \
    --apply_chat_template \
    --tasks czechbench_tasks \
    --output_path ~/logs/
```
