import argparse
import json
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs='+', help="Path(s) to json file(s) with evaluation results. Either one CzechBench Bilingual result file, or separate results from CzechBench and CzechBench EN.")
parser.add_argument("-g", "--graph", action="store_true", help="Show graphical result comparison")
parser.add_argument("-o", "--output_graph_path", default=None, help="Output path for comparison graph. Requires --graph to be set to True.")

tasks = ["anli", "arc_challenge", "arc_easy", "belebele", "ctkfacts", "gsm8k", "mmlu", "subjectivity", "truthfulqa"]
task_display_names = {
    "anli": "ANLI",
    "arc_challenge": "ARC Challenge",
    "arc_easy": "ARC Easy",
    "belebele": "Belebele",
    "ctkfacts": "CTKFacts",
    "gsm8k": "GSM8K",
    "mmlu": "MMLU",
    "subjectivity": "Subjectivity",
    "truthfulqa": "TruthfulQA"
}

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)

    files = args.files
    if len(files) == 1:
        try:
            with open(files[0], "r") as f:
                data = json.load(f)

            results = data["results"]
            d = []
            for task in tasks:
                if task + "_cs" in results.keys() and task + "_en" in results.keys():
                    czech = results[task + "_cs"]
                    if "exact_match,none" in czech.keys():
                        cs_acc = czech["exact_match,none"]
                    elif "exact_match,flexible-extract" in czech.keys():
                        cs_acc = czech["exact_match,flexible-extract"]
                    elif "exact_match,strict-match" in czech.keys():
                        cs_acc = czech["exact_match,strict-match"]
                    else:
                        print(f"Could not find Czech accuracy results for {task}.")
                        break
                    english = results[task + "_en"]
                    if "exact_match,none" in english.keys():
                        en_acc = english["exact_match,none"]
                    elif "exact_match,flexible-extract" in english.keys():
                        en_acc = english["exact_match,flexible-extract"]
                    elif "exact_match,strict-match" in english.keys():
                        en_acc = english["exact_match,strict-match"]
                    else:
                        print(f"Could not English find accuracy results for {task}.")
                        break
                    d.append({"Task": task_display_names[task], "Czech": cs_acc, "English": en_acc, "Difference": abs(cs_acc - en_acc), "Relative Difference": abs(cs_acc - en_acc) / max(cs_acc, en_acc)})
            df = pd.DataFrame(d)
            print(df)

        except:
            raise Exception("Could not parse the input file.")
        
    elif len(files) == 2:
        try:
            with open(files[0], "r") as f:
                data = json.load(f)
            czech_results = data["results"]
            with open(files[1], "r") as f:
                data = json.load(f)
            english_results = data["results"]
            if "czechbench_english" in czech_results.keys():
                print("Result files automatically swapped.")
                czech_results, english_results = english_results, czech_results
            d = []
            for task in tasks:
                if task + "_cs" in czech_results.keys() and task + "_en" in english_results.keys():
                    czech = czech_results[task + "_cs"]
                    if "exact_match,none" in czech.keys():
                        cs_acc = czech["exact_match,none"]
                    elif "exact_match,flexible-extract" in czech.keys():
                        cs_acc = czech["exact_match,flexible-extract"]
                    elif "exact_match,strict-match" in czech.keys():
                        cs_acc = czech["exact_match,strict-match"]
                    else:
                        print(f"Could not find Czech accuracy results for {task}.")
                        break
                    english = english_results[task + "_en"]
                    if "exact_match,none" in english.keys():
                        en_acc = english["exact_match,none"]
                    elif "exact_match,flexible-extract" in english.keys():
                        en_acc = english["exact_match,flexible-extract"]
                    elif "exact_match,strict-match" in english.keys():
                        en_acc = english["exact_match,strict-match"]
                    else:
                        print(f"Could not English find accuracy results for {task}.")
                        break
                    d.append({"Task": task_display_names[task], "Czech": cs_acc, "English": en_acc, "Difference": abs(cs_acc - en_acc), "Relative Difference": abs(cs_acc - en_acc) / max(cs_acc, en_acc)})
            df = pd.DataFrame(d)
            print(df)

        except:
            raise Exception("Could not parse the input files.")
        
    else:
        raise Exception("Invalid number of input files. Please provide either one CzechBench Bilingual result file, or separate results from CzechBench and CzechBench EN.")
    
    print("Mean relative accuracy difference:", df["Relative Difference"].mean())

    if args.graph:
        ax = df.plot.barh(x='Task', y=['Czech', 'English'], xlabel="Task", ylabel="Accuracy", title="Czech vs. English Results Comparison", figsize=(10, 6)) 
        ax.invert_yaxis()
        for container in ax.containers:
            ax.bar_label(container, fontsize='medium', fmt="%.1f")
        if args.output_graph_path is not None:
            plt.savefig(args.output_graph_path)
        plt.show()