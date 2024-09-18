# CzechBench - English task variants

This collection contains English variants of 9 evaluation tasks included in the main [CzechBench](../czechbench/) suite. Task implementations are identical to the Czech variants in order to provide fair and direct result comparison. The results obtained here may thus differ from the official benchmarks implementations included in the LM Evaluation Harness framework.

| Dataset                                                      | Language                      | Task type                  | Metrics        | Samples | Task ID         |
| ------------------------------------------------------------ | ----------------------------- | -------------------------- | -------------- | ------: | --------------- |
| [ANLI](anli_en)                     | EN (Original)               | Natural Language Inference | Acc, Macro F1  | 1200    | anli_en         |
| [ARC Challenge](arc_en)             | EN (Original)               | Knowledge-Based QA         | Acc            | 1172    | arc_en          |
| [ARC Easy](arc_en)                  | EN (Original)               | Knowledge-Based QA         | Acc            | 2376    | arc_en          |
| [Belebele](belebele_en)             | EN (Original) | Reading Comprehension / QA | Acc            | 895     | belebele_en     |
| [CTKFacts](ctkfacts_en)             | EN (Translated)                 | Natural Language Inference | Acc, Macro F1  | 558     | ctkfacts_en     |
| [GSM8K](gsm8k_en)                   | EN (Original)               | Mathematical inference     | EM Acc         | 1319    | gsm8k_en        |
| [MMLU](mmlu_en)                     | EN (Original)               | Knowledge-Based QA         | Acc            | 12408   | mmlu_en         |
| [Subjectivity](subjectivity_en)     | EN (Translated)                 | Subjectivity Analysis      | Acc, Macro F1  | 2000    | subjectivity_en |
| [TruthfulQA](truthfulqa_en)         | EN (Original)               | Knowledge-Based QA         | Acc            | 813     | truthfulqa_en   |

## Installation

Please refer to the main [CzechBench README](../czechbench/) for installation instructions.

## Bilingual evaluation

To evaluate a model on the English version of CzechBench, you can use the following example:

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16 \
    --apply_chat_template \
    --tasks czechbench_english \
    --device cuda:0 \
    --batch_size auto \
    --output_path ~/logs/
```

You can also perform simultaneous evaluation on both versions of the supported tasks:

```bash
lm_eval --model hf \
    --model_args pretrained=google/gemma-2-9b-it,dtype=bfloat16 \
    --apply_chat_template \
    --tasks czechbench_bilingual \
    --device cuda:0 \
    --batch_size auto \
    --output_path ~/logs/
```

### Result analysis

To closely examine the differences in performance, use the [bilingual_analysis](../czechbench/bilingual_analysis.py) script. It can provide both tabular and graphical comparison of individual results, as well as additional statistics.

The script accepts up to two positional arguments representing paths to the json files generated during evaluation. If only one path is provided, it is expected to to contain results of the [czechbench_bilingual](../czechbench/czechbench_bilingual.yaml) task collection. If two paths are provided, they must contain separate results of [czechbench_tasks](../czechbench/czechbench_tasks.yaml) and [czechbench_english](czechbench_english.yaml) evaluation runs. There are also two additional options for toggling the creation of a results comparison graph, and its optional saving to a provided output path.

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
python3 bilingual_analysis.py '~/logs/my_model/czechbench_tasks.json' ~/logs/my_model/czechbench_english.json -g -o ~/figures/graph.png
```