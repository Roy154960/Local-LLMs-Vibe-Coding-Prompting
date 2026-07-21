# Local LLMs, Vibe Coding & Prompting

A summarizer project that calls a local model through OpenAI-compatible API.

## Project Files

**summarizer.py** Has `chat` function that sends a prompt to the model, and a few prebuilt prompts templates provided by `build_prompt`.

**notebook.ipynb** Is a notebook that studies the effects of temperature and top_p on the models output, and tests the models performance with zero_shots and few_shots tasks, and finally an json valid output.

**Example.txt** Is a example to use on the summarizer.

**Prompts.txt** Shows some prompts I used with opencode.

## Report

### Part 1: Serve a local model with Ollama

I chose `qwen2.5-coder:7b` as the model to use, because it is a lightweight model that my pc can run at a 64k+ context.
Can be run using the command: `ollama pull qwen2.5-coder:7b`

### Part 2: Connect opencode to your local model

Opencode can be run using: `ollama launch opencode --model qwen2.5-coder:7b`
The `--model qwen2.5-coder:7b` was added because running `ollama launch opencode` does not show `qwen2.5-coder:7b` as an option.

### Part 3: Vibe-code a small tool with opencode

I chose to build a summarizer as an app, it takes the text to summarize and three different formats to summarize it in: paragraph, bullets and key words.
It has two function:

* `chat`: function that sends a prompt to the model. The chat parameters are message a list, temperature a float with default value of 0.7, max_tokens an int with default value of 400, top_p a float with default value of 1.0. Mesage is the prompt being sent, temperature controls the creativity of the model, top_p controls the creativity of the model by sampling only from the smallest set of tokens whose probabilities sum to p, and max tokens controls the max size of the response.

* `build_prompt`: build prompt is a way to make inputing prompts easier for the user, the reason why `chat` does not build prompts internally is to have higher reusability.

I used fast API so that I can call the functions from my browser. To run go to the directory of the file and run the command: `python summarizer.py`

Then open the browser and go to: `http://127.0.0.1:8001/docs`

The project can summarize both text files or a paragraph writen in the input query directly in the browser.

Reflection is at the end of the README

### Part 4: Prompting & parameters mini-task

Is a notebook that studies the effects of temperature and top_p on the models output, and tests the models performance with zero_shots and few_shots tasks, and finally an json valid output. More details are available in the notebook as markdowns


### Reflection

The local ai model was helpful in creating this project, it provided code snippets and helped in debugging the code when I reached a roadblock. However the model was slow, so at times it was quicker to search for answers in the official documentation. Another problem is that the local model could misunderstand my request, and that problem was amplified by the fact that I was holding onto old prompts to include them in the assignment, and these old prompts made the model get confused at times. In future projects the model can be quicker and more accurate because I could erase old prompts when these issues rise. This project was simple so I did not have to correct a lot, and a lot of the code was present in the course material.

### Test Run

***Input***

What is Fixed (or static) Partitioning in the Operating System?  Fixed (or static) partitioning is one of the earliest and simplest memory management techniques used in operating systems. It involves dividing the main memory into a fixed number of partitions at system startup, with each partition being assigned to a process. These partitions remain unchanged throughout the system’s operation, providing each process with a designated memory space. This method was widely used in early operating systems and remains relevant in specific contexts like embedded systems and real-time applications. However, while fixed partitioning is simple to implement, it has significant limitations, including inefficiencies caused by internal fragmentation.      In fixed partitioning, the memory is divided into fixed-size chunks, with each chunk being reserved for a specific process. When a process requests memory, the operating system assigns it to the appropriate partition. Each partition is of the same size, and the memory allocation is done at system boot time.     Fixed partitioning has several advantages over other memory allocation techniques. First, it is simple and easy to implement. Second, it is predictable, meaning the operating system can ensure a minimum amount of memory for each process. Third, it can prevent processes from interfering with each other's memory space, improving the security and stability of the system.     However, fixed partitioning also has some disadvantages. It can lead to internal fragmentation, where memory in a partition remains unused. This can happen when the process's memory requirements are smaller than the partition size, leaving some memory unused. Additionally, fixed partitioning limits the number of processes that can run concurrently, as each process requires a dedicated partition.  Overall, fixed partitioning is a useful memory allocation technique in situations where the number of processes is fixed, and the memory requirements for each process are known in advance. It is commonly used in embedded systems, real-time systems, and systems with limited memory resources.  In operating systems, Memory Management is the function responsible for allocating and managing a computer's main memory. Memory Management function keeps track of the status of each memory location, either allocated or free to ensure effective and efficient use of Primary Memory.


***Paragraph Summary***

{
  "summary": "Fixed (or static) partitioning is an early memory management technique in operating systems that divides main memory into fixed partitions at startup, assigning each to a process, which remains unchanged throughout operation. Although simple to implement, it has limitations like internal fragmentation and restricts the number of concurrent processes due to fixed-size allocations. Despite these drawbacks, fixed partitioning remains relevant in specific contexts such as embedded systems and real-time applications by providing predictable memory allocation and improved system security and stability."
}


***Bullets***

{
  "summary": "- **Fixed (or static) Partitioning Definition**: Fixed partitioning involves dividing the main memory into fixed-size partitions during system startup.\n- **Memory Allocation**: Each partition is assigned to a specific process and remains unchanged throughout the system's operation.\n- **Advantages**:\n  - Simple and easy to implement.\n  - Predictable, ensuring minimum memory for each process.\n  - Prevents processes from interfering with each other’s memory space, enhancing security and stability.\n- **Disadvantages**:\n  - Can lead to internal fragmentation when a process's memory requirements are smaller than the partition size.\n  - Limits the number of processes that can run concurrently due to fixed-size partitions.\n- **Applicability**: Commonly used in embedded systems, real-time applications, and systems with limited memory resources.\n- **Role in Operating Systems**: Memory Management function tracks the status of each memory location (allocated or free) to ensure effective use of primary memory."
}

***Key Words***

{
  "summary": "Key words:\nFixed partitioning, memory management, operating system, partitions, process, system startup, internal fragmentation, simple implementation, predictable, security, stability, concurrent processes, limited memory resources, embedded systems, real-time systems."
}
