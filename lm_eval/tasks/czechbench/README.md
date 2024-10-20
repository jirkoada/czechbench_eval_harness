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

Evaluating a model hosted on Hugging Face on the whole CzechBench suite (with multi-GPU support):

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16,parallelize=True \
    --apply_chat_template \
    --tasks czechbench_tasks \
    --batch_size auto \
    --output_path ~/logs/
```

Selecting individual evaluation tasks (refer to the table above for task IDs):

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16,parallelize=True \
    --apply_chat_template \
    --tasks agree_cs,belebele_cs,truthfulqa_cs \
    --batch_size auto \
    --output_path ~/logs/
```

Using cache to recover interrupted evaluations:

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16,parallelize=True \
    --apply_chat_template \
    --tasks czechbench_tasks \
    --batch_size auto \
    --output_path ~/logs/ \
    --use_cache ~/eval_cache/gemma-2-9b-it
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

## Bilingual evaluation

Apart from comparing the performance of individual models, CzechBench also enables direct comparison of results achieved by a single LLM in equivalent Czech and English benchmarks. The provided [CzechBench EN](../czechbench_en/) collection contains equivalent English variants for 9 of the above-described evaluation tasks. These utilize the original English datasets as well as the CTKFacts and Subjectivity benchmarks, which were translated from the Czech language.

To evaluate a model on the English version of CzechBench, you can use the following example:

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16,parallelize=True \
    --apply_chat_template \
    --tasks czechbench_english \
    --batch_size auto \
    --output_path ~/logs/
```

You can also perform simultaneous evaluation on both versions of the supported tasks:

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16,parallelize=True \
    --apply_chat_template \
    --tasks czechbench_bilingual \
    --device cuda:0 \
    --output_path ~/logs/
```

### Result analysis

To closely examine the differences in performance, use the [bilingual_analysis](bilingual_analysis.py) script. It can provide both tabular and graphical comparison of individual results, as well as additional statistics.

The script accepts up to two positional arguments representing paths to the json files generated during evaluation. If only one path is provided, it is expected to to contain results of the [czechbench_bilingual](czechbench_bilingual.yaml) task collection. If two paths are provided, they must contain separate results of [czechbench_tasks](czechbench_tasks.yaml) and [czechbench_english](../czechbench_en/czechbench_english.yaml) evaluation runs. There are also two additional options for toggling the creation of a results comparison graph, and its optional saving to a provided output path.

Using the script may require additional installation of the Matplotlib package:

```bash
pip install matplotlib
```

Single file analysis example:

```bash
cd lm_eval/tasks/czechbench
python3 bilingual_analysis.py '~/logs/my_model/czechbench_bilingual.json' -g -o ~/figures/graph.png
```

Analysis of separate result files:

```bash
cd lm_eval/tasks/czechbench
python3 bilingual_analysis.py '~/logs/my_model/czechbench_tasks.json' '~/logs/my_model/czechbench_english.json' -g -o ~/figures/graph.png
```

