# Homework 6



## Video Questions

1. **Where does Julia Cartwright work?**  National Instruments.

2. **What is PREEMT_RT? Hint: Google it.**  Real time preemptive Kernel for linux.

3. **What is mixed criticality?**  A way of running differnet types of tasks.  Allows you to run some non-time critical stuff while running real time requirements and latency bounded stuff.

4. **How can drivers misbehave?**  They can misbehave when using the shared driver stack methods. 

5. **What is Δ in Figure 1?**  Shows the time difference between the interrupt being called and the application executes.

6. **What is Cyclictest[2]?**  Takes a time stamp and it sleeps for a fixed duration and then takes another time stamp.

7. **What is plotted in Figure 2?**  A time plot showing the cpu handling lower and higher priority interrupts to showcase the problem of processing high priority events in real time..

8. **What is dispatch latency? Scheduling latency?**  It represents the amount of time it takes between the hardware actually firing and for the interrupt for the relevant thread to actually be woken and the interrupt dispatch to have occurred.  Scheduling latency is the thread scheduler being told this thread needs to run that latency so that the dispatch latency doesnt cause problems.

9. **What is mainline?**  Its a non-real time way of handling interrupts.

10. **What is keeping the External event in Figure 3 from starting?**  Its waiting for another interrupt that was previously triggered to finish executing.

11. **Why can the External event in Figure 4 start sooner?** They used "shims" of an event to wake up the thread which would happen even if something else is running at the same time. Then it can prioritize the most important events.

## PREEMPT_RT

Followed the instructions in exercise 36 to generate the histogram of the rt vs non rt kernel handling executions on the bone.  The plot is call out.png
