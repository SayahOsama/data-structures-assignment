
def recent_call_logs(calls,k):
    recent_calls = []
    while len(calls)>0 and k>0:
        recent_calls.append(calls.pop())
        k -= 1
    recent_calls.reverse()
    return recent_calls

calls = [1001,1002,1003,1004]
print("recent_call_logs: ",recent_call_logs(calls,5))