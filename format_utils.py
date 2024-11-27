def format_solution(input, expected, actual):
    is_answer_correct = expected == actual
    return f"{'+++' if is_answer_correct else '---'} Input: {input} - Expected: {expected} - Actual: {actual}"
