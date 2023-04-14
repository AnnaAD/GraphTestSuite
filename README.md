# Process for Setting Up and Running Arya:

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

### Writing Patterns for Cliques: 
- a couple edges as 1-stars and then the rest as normal edges?
- or can do a couple odd length cycles and the remaining edges

# Setting up Arya:
https://stackoverflow.com/questions/10726537/how-to-install-tbb-from-source-on-linux-and-make-it-work
- install tbb or link to compiled by-hand-library arya/tbb-2017~U7
- change makefiles to include tbb manually:

in makefile:

HELPFLAGS = -I$(TBB_INCLUDE) -Wl,-rpath,$(TBB_LIBRARY_RELEASE) -L$(TBB_LIBRARY_RELEASE)

somewhere:
\# tbb stuff
export TBB_INSTALL_DIR=$HOME/arya/tbb-2017~U7
export TBB_INCLUDE=$TBB_INSTALL_DIR/include
export TBB_LIBRARY_RELEASE=$TBB_INSTALL_DIR/build/linux_intel64_gcc_cc7_libc2.27_release
export TBB_LIBRARY_DEBUG=$TBB_INSTALL_DIR/build/linux_intel64_gcc_cc7_libc2.27_debug

--------------------

## Problems:
- seeing very high errors on graphs that are not just odd length cycles
- ASAP implementation -- very high errors
- some graphs fail to read

results for arya on 4motif:
https://docs.google.com/spreadsheets/d/1NQPU5_-vb7mE5NGntfIg0ERQvKeQC39d-0r3Xnnk8GM/edit?usp=sharing

-----------------------

- wrote 2 patterns for 6clique and for 9clique
- used the python graph decomposition tool and by hand
	- both not that successful/accurate
- friendster.cel file works well
- refined my dynamic coloring code
	- removes blank vertices
	- sorts for locality
	- overhead should allow fast adjustments to numbers of colors
- made automated test-running system where you can input json for the tests you want to run

--------------
- try reuse sampler for 4motif -- see if that replicates paper
- email about 4clique, etc. individual accuracies for 4motif patterns
- search if there is a way that they calculate average for 4motif in the paper
	- maybe email if don't find it

--------------------------
- correct count 3star-2star?
- verify mico and arya and their accuracy/count
- n choose 3 from neighbors, n choose 2, calculate instead of count
	- do for every edge
 	- symmetry? 

- how to detect/respond situation like patent_citation
	- sparse pattern count, exact count is small
	- larger graphs that have sparse, or small exact count.
	- dynamic adjustment of c

- ELP for estimation of c
- edge sparsification granularity when doing edge induced count

---------------------
- use bigger machines for larger patterns
- friendster.cel graph there
	- more cores/threads


------------------
mico - 
why is 3star-2star N/A error?



