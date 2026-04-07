import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from tasks.easy import Easy
from tasks.medium import Medium
from tasks.hard import Hard
from evaluator.grader import grade_easy, grade_medium, grade_hard


def run_task(task_name: str, task_obj, grader):
    result = task_obj.run()
    score = grader(result)
    print(f"{task_name.title()} Task")
    print(f"  result: {result}")
    print(f"  score: {score:.3f}")
    return result, score


def main():
    print("Running baseline tasks for SupplyChainEnv")
    run_task('easy', Easy(), grade_easy)
    run_task('medium', Medium(), grade_medium)
    run_task('hard', Hard(), grade_hard)


if __name__ == '__main__':
    main()
