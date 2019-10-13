def check_log_history(events):
    if not events: return 0
    seen = set()
    stack = []
    for i, s in enumerate(events):
        state, id = s.split(' ')
        if state == 'ACQUIRE':
            if id in seen:
                return i + 1
            seen.add(id)
            stack.append(id)
        else:
            if stack and stack[-1] == id:
                seen.remove(stack.pop())
            else:
                return i + 1
    return 0 if not stack else len(events) + 1

