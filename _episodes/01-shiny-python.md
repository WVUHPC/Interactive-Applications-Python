---
title: "Shiny for Python"
start: 600 
teaching: 60
exercises: 0
questions:
- "Create highly interactive visualizations, realtime dashboards, data explorers, model demos, all in pure Python"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

Shiny is a software package for build interactive web applications. Originally create for the R language, it has been now expanded to support Python Language. We will focus here on Shiny for Python. Most of the internals of Shiny are shared between the two implementations.

We start our exploration of shiny creating an virtual desktop on Thorny Flat using Open On-demand.
Goto to [Open On-Demand portal for Thorny Flat](https://ondemand-tf.hpc.wvu.edu). Enter your credentials.
From the dashboard select "Interactive Apps" and "Thorny Desktop"

<a href="{{ page.root }}/fig/shiny1.png">
   <img src="{{ page.root }}/fig/shiny1.png" alt="Open On-Demand" width="600" />
</a>

Select minimal requests such as "standby" for partition, 4 hours walltime, 4 CPU cores.
A new job will be created

<a href="{{ page.root }}/fig/shiny2.png">
   <img src="{{ page.root }}/fig/shiny2.png" alt="Open On-Demand" width="600" />
</a>

Click on "Launch Thorny Desktop" and open 2 windws, a terminal and a web browser.

<a href="{{ page.root }}/fig/shiny3.png">
   <img src="{{ page.root }}/fig/shiny3.png" alt="Open On-Demand" width="600" />
</a>

Load the module for Python on the terminal

    $> module load lang/python/cpython_3.11.3_gcc122

Now we are ready to create our first shiny app.

Create a folder for our shiny apps.
Lets call it SHINY and inside create a folder app1
  
    $> mkdir -p SHINY/app1
    $> cd SHINY/app1

Now we can create a simple example app with the command::

    $> shiny create .

Run the first app with:

    $> shiny run --reload

On the web browser go to https://localhost:8000 to visualize the app

<a href="{{ page.root }}/fig/shiny4.png">
   <img src="{{ page.root }}/fig/shiny4.png" alt="Open On-Demand" width="600" />
</a>

When we execute ``shiny create .`` a python file called ``app.py`` is created.
This file is a follows:

    from shiny import App, render, ui
    
    app_ui = ui.page_fluid(
      ui.h2("Hello Shiny!"),
      ui.input_slider("n", "N", 0, 100, 20),
      ui.output_text_verbatim("txt"),
    )

    def server(input, output, session):
      @output
      @render.text
      def txt():
          return f"n*2 is {input.n() * 2}"
     
    app = App(app_ui, server)

This file contains the main ingredients of a shiny app. 
Shiny applications consist of two parts: the user interface (or UI), and the server function. These are combined using a shiny.App object.

We can now copy this app and start adding modifications to it to construct our second app.
Cancel the exeuction of the first app executing ``^C``, move one folder up and copy the folder under a new name.

    $> cd ..
    $> cp -r app1 app2
    $> cd app2

Change the file ``app.py`` inside ``app2`` as follows:

    from shiny import App, render, ui
    
    app_ui = ui.page_fluid(
        ui.h2("Sum Shiny!"),
        ui.input_slider("a", "A", 0, 100, 20),
        ui.input_slider("b", "B", 0, 100, 20),
        ui.output_text_verbatim("txt"),
    )

    def server(input, output, session):
        @output
        @render.text
        def txt():
            return f"a+b is {input.a() + input.b()}"
    
    app = App(app_ui, server)

The UI part defines what visitors will see on their web page. 
The dynamic parts of our app happen inside the server function.

{% include links.md %}

