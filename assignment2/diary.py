import traceback

try:
    #Open diary.txt for appending
    with open('diary.txt', 'a') as file:
        #Prompt the user's initial input
        prompt_initial = input("What happened today? ")
        file.write(prompt_initial + "\n")
                
        #Prompt the user's input with a loop
        prompt_continue = input("What else? ")
        while prompt_continue != "done for now":
            file.write(prompt_continue + "\n")
            prompt_continue = input("What else? ")

        #Write "done for now"
        file.write("done for now\n")

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")