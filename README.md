# Process for Setting Up and Running Arya:

# Setting up Arya:

- downloaded source code onto machine [umma@csail.mit.edu]


### CPU Info
```
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              32
On-line CPU(s) list: 0-31
Thread(s) per core:  2
Core(s) per socket:  8
Socket(s):           2
NUMA node(s):        2
Vendor ID:           GenuineIntel
CPU family:          6
Model:               45
Model name:          Intel(R) Xeon(R) CPU E5-2690 0 @ 2.90GHz
Stepping:            7
CPU MHz:             3591.132
CPU max MHz:         3800.0000
CPU min MHz:         1200.0000
BogoMIPS:            5785.77
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            20480K
NUMA node0 CPU(s):   0-7,16-23
NUMA node1 CPU(s):   8-15,24-31
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx lahf_lm epb pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid xsaveopt dtherm ida arat pln pts md_clear flush_l1d
```

## Makefile modifications
https://stackoverflow.com/questions/10726537/how-to-install-tbb-from-source-on-linux-and-make-it-work
- install tbb or link to compiled by-hand-library arya/tbb-2017~U7
- change makefiles to include tbb manually:

in makefile:

```
HELPFLAGS = -I$(TBB_INCLUDE) -Wl,-rpath,$(TBB_LIBRARY_RELEASE) -L$(TBB_LIBRARY_RELEASE)
```

in .bashrc

```
export TBB_INSTALL_DIR=$HOME/arya/tbb-2017~U7
export TBB_INCLUDE=$TBB_INSTALL_DIR/include
export TBB_LIBRARY_RELEASE=$TBB_INSTALL_DIR/build/linux_intel64_gcc_cc7_libc2.27_release
export TBB_LIBRARY_DEBUG=$TBB_INSTALL_DIR/build/linux_intel64_gcc_cc7_libc2.27_debug
```
--------------------

# Arya Usage

### Graph Inputs:
- can use .cel files if each edge is symmetrically distributed
- otherwise can run directed_to_undirected.py on an edge-list to turn it into an undirected edgeless

- can strip the e <vid1> <vid2> from a .lg graph or .ctxt graph
- would you need to run .ctxt edgeless though directed_to_undirected.py?

### Pattern Inputs:
- can run the python program graph_decomp/graph_decomp.py
- first line = <# odd length cycles> <# stars>
- following lines are odd length cycles
- then the stars, with first vertices being the center
- then remaining edges

- ASAP runs on hard-coded patterns for 5house, triangle-triangle, 4clique

### Writing Patterns for Cliques: 
- a couple edges as 1-stars and then the rest as normal edges?
- or can do a couple odd length cycles and the remaining edges

# Successes

- friendster and mico report fast/accurate triangle counts, 5 cycle counts, and 3 star counts.

# Arya Problems
- seeing very high errors on graphs that are not just composed of odd length cycles/stars

results for arya on 4motif:
https://docs.google.com/spreadsheets/d/1NQPU5_-vb7mE5NGntfIg0ERQvKeQC39d-0r3Xnnk8GM/edit?usp=sharing

Paper cites N/A for 3star2star counts-- however, I am returning an exact count and finding arya's estimate to be significantly different.

## ASAP Problems
- mico 5house is quite different (ASAP: 26,511,846,609,059 vs edge-count: 1,655,449,692,098).

## 4Motif Sidenote -- Arya Reuse Sampler

In attempt to better reproduce 4motif from the paper, I then used the reuse sampler. However, I was uncertain how to interpret the results. I saw some 4motif specific code was commented out in `reuse_sampler_single_machine/GraphCounting.cc`, however I made no changes to encorperate the commented out code.

I attempted to run the reuse sampler as specified in the readme.

Input:
```
mpirun -n 4 ./../ad/graph_counting/src/reuse_sampler_single_machine/GraphCounting.out ../arya/graph_counting/graphs/mico/mico.undigraph ../ad/graph_counting/patterns/4_motif/3_star,../ad/graph_counting/patterns/4_motif/4_chain,../ad/graph_counting/patterns/4_motif/4_clique,../ad/graph_counting/patterns/4_motif/4_cycle,../ad/graph_counting/patterns/4_motif/4_motif_4,../ad/graph_counting/patterns/4_motif/4_motif_5 500000,500000,500000,500000,500000,500000 4,4,4,4,4,4 4
```

Output:
```
***** main: all threads finished 
raw results after merge threads (total_prob_inverse, total_sampled_times): 
4436479086366712 501000
pattern_nums sampling_times
8855247677.378666 501000
total_time_consumed(us) 227434

total_running_time = 227434

***** main: all threads finished 
raw results after merge threads (total_prob_inverse, total_sampled_times): 
4427335328192392 501000
pattern_nums sampling_times
8836996663.058666 501000
total_time_consumed(us) 237581

total_running_time = 237581

***** main: all threads finished 
raw results after merge threads (total_prob_inverse, total_sampled_times): 
4432313516600200 501000
pattern_nums sampling_times
8846933166.866667 501000
total_time_consumed(us) 239860

total_running_time = 239860

***** main: all threads finished 
raw results after merge threads (total_prob_inverse, total_sampled_times): 
4446664918561096 501000
pattern_nums sampling_times
8875578679.762667 501000
total_time_consumed(us) 292727

total_running_time = 292727
```

Why are there only four results for the patterns? What do they correspond to and why don't they line up?

