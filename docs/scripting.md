# Scripting

Uses for Python scripting in ParaView:

* Automate visualization workflows, especially for batch processing
* Create custom filters
* Create custom plots
* Save current state (File -> Save state -> Python state file type). This includes not just the visualization pipeline, but also the UI setup in terms of views

Easiest way to get started with Paraview scripting: use Trace functionality, edit resulting
script as you want

Different ways of executing scripts in ParaView:

* File -> Load State from a Python script
* `pvpython`: Python command-line (and run script file) tool for running ParaView visualization workflows 
* `pvbatch`: very similar to `pvpython`, but can only run scripts (no interactive prompt), and can execute in parallel when run under MPI
* ProgrammableFilter: a pipeline filter whose execution is defined by a Python script you can edit within the UI (XXX or from a script?)
* Python View: a view area that basically shows an that you create using a Python script
* Python Script Editor window: somewhat useful to edit and run scripts within the ParaView GUI. The editor itself isn't brilliant, though.