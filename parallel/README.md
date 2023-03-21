## Parallel and Concurrent Programming

### Sequential Computing

A single processor executes a program in a sequential manner. The program is broken down into a sequence of discrete instructions that I execute one after another and I can only execute one instruction at any given moment. There is no overlap between them. The speed of a program is limited by the speed of the processor and how fast can execute a series of instructions.

### Parallel Computing

It increases the throughput of a program enabling us to:

* accomplish a single task faster
* accomplish more tasks in a given time

### Parallel Computing Architectures

* The most widely used system to classify multiple parallel computing architectures is Flynn's taxonomy.
* Flynn's taxonomy uses the number of instruction streams and data streams to do this classification.
    1. SISD: Single Instruction Single Data. The first generation of architecture.
    2. SIMD: Single Instruction Multiple Data. The second generation of architecture.
    3. MISD: Multiple Instruction Single Data. Not feasible.
    4. MIMD: Multiple Instruction Multiple Data. The most suitable for parallel computing.
        * SPMD
        * MPMD

### Parallel Programming Model

* Single Program, Multiple Data (SPMD). This is the most common. We will focus on this one.
* Multiple Program, Multiple Data (MPMD). We require a manager. We will focus on this one later.

### Shared vs Distributed Memory

Memory speed << Processor speed

* Shared memory: All processors access the same memory with global address space.
    * Uniform memory access (UMA): All the processor has equal access to all the memory.
        * Symmetric Multiprocessing System (SMP): We will focus on this one.
    * Non-uniform memory access (NUMA): Some processors have quicker access to some parts of memory than others.
* Distributed memory: Every single processor has its own local memory with its own address space so the concept of global address space does not exist. All of the processors are connected to the same network. Each processor operates independently. It is highly scalable but it requires more networking knowledge.

### Threads vs Process

Process

* Includes code, data, and state information
* Independent instance of a running program
* Separate address space

Threads

* Subset of a process
* Independent path of execution
* The operating system schedules threads for execution
* They are "lightweight" - it requires less overhead to create and terminate
* The operating system can switch between threads faster than processes

### Inter-Process Communication (IPC)

* Sockets and pipes
* Shared memory
* Remote procedure calls

### Concurrent Execution

* One or more processes are overlapping in time.
* Only one processing will be executed at any moment.
* Dealing with multiple things at once.
* Suitable for handling I/O dependant tasks.

### Parallel Hardware

* Multi-core processors.
* Graphics processing unit.
* Computer cluster.

### Parallel Execution

* One or more processes are executed at the same time using parallel hardware.
* Simultaneous execution.
* Doing multiple things at once.
* Suitable for computationally intensive tasks.

### CPython

* Default and most widely used Python interpreter.
* Written in C and Python.
* Uses GIL for thread-safe operation.
* GIL lives inside CPython, the most commonly used Python interpreter.

### I/O-Bound Applications

* GIL is not a bottleneck
* Use the Python threading module to implement multiple concurrent threads

### CPU-Bound Applications

* GIL can negatively impact performance
* Implement parallel algorithms as external library functions
* Use the Python multiprocessing package
* Communication between processes is more complicated than between threads
* Multiple processes use more system resources than creating multiple threads

### Thread Lifecycle

1. States: New, Runnable, Blocked, Terminated
2. Actions: Start, Waiting, Finish, Resume

* New
    * Start -> Runnable
* Runnable
    * Waiting -> Blocked
    * Finish -> Terminated
* Blocked
    * Resume -> Runnable
* Terminated