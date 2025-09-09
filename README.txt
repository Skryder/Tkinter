


Hello. This is Past Dakota.

Future Dakota has probably forgotten everything again. So this README will detail exactly... wait how do i enable word wrapping

alt+z is how. there we go. also don't forget to docsista_env\Scripts\activate

You can run the API file with fastapi dev .\DOCSISTA_API.py 

build with  docker build -t docsista . 
run with    docker run -p 8000:8000 docsista

Currently, the API endpoint is hosted on http://127.0.0.1:8000/DOCSISTA_API/

the static index file for gui testing is on http://127.0.0.1:8000/static/index.html - Don't try to use the live server.

anyway, this doc will detail exactly what we've done so far. Please remember to update it as we go along.

First thing's first, we've got a few files here. 

CMTS_STATS_MODEL is our "model" class... or at least it will be... All this does right now is hold the CMTS output in a python dictionary.

The dictionary is built using our little Helpers file. This is mostly just a spot I put random bits of code to be used later. Right now it contains the ver-important dictify function which I made to break down the Huawei CMTS output into a python dictionary. 

The cool thing about dictionaries is that they can be easily converted to JSON and back which makes them very easy to serialize.

This brings us to our "main" file, which is not called main (Though we should probably make one of these soon) - that is, DOCSISTA_API. Yes you chose that name, you weirdo. 
This file has a few things going on. 
Primarily it houses a FASTAPI API with a number of callable functions. 
At the moment there is one POST function to post the CMTS output to the model, and two GET functions that return the model in different ways.

get-model just grabs the model as-is, which is a python dictionary. this is useful for diplaying it in the terminal and can be converted elsewhere.

get-readable uses a handy thing called Jinja2, which is the other thing this file does.

Jinja2 is a Framework for passing around any kind of text (in this case HTML), and appending variables into the text at runtime. It basically allows us to construct a template HTML file, fill it with information, and then send it as a string through an API data field to be appended to a web page as innnerHTML.

Jinja2 can do a lot of cool stuff like that, but we're just doing this for now.

You'll notice that the api calls all go through the /static directory. This is primarily because the .js file in there needs to be able to access the API endpoints. You still need to figure out how to make this a bit more workable and configurable and understand it better.

You'll see the index.html file in there is using Jinja brackets. You should figure out how to make the data appear a bit better there.

I've finally got it running on Docker now. See the build and run commands earlier in the readme.

