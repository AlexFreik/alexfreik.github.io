---
layout: post
title:  "Linux Assembly on macOS"
date:   2022-01-27
categories: programming
tags: docker 
excerpt_separator: <!--more-->
---

Computer Organisation / Architecture courses usually require write Assembly code for Linux.
And the problem that we will address here: **how to easily run Linux Assembly on macOS machines**.
<!--more-->

---
# Table of Content
1. [TL;DR](tldr)
2. [The *"Clumsy"* Way (VM)](#the-clumsy-way-vm)
    - [Pros](#pros)
    - [Pros](#cons)
3. [The *"Smart"* Way (Docker)](#the-smart-way-docker)
    - [Pros](#pros-1)
    - [Pros](#cons-1)
    - [Explanation of Code Snippets](#explanation-of-code-snippets)
    - [A Few Thing to Mention](#a-few-thing-to-mention)
4. [Renting a Linux Server](#renting-a-linux-server)
    - [Pros](#pros-2)
    - [Pros](#cons-2)

---


## TL;DR
There is a few ways how to do it, IMO the easiest and most pleasant way is to use `Docker`:
1. Watch this great 2h [Docker Tutorial for Beginners](https://youtu.be/fqMOX6JJhGo) from the FreeCodeCamp.
2. Install Docker Desktop for macOS and start docker.  
   You can check that everything is alright by executing `$ docker ps` command and not having errors.
3. Create a Docker image.
    - Create `Dockerfile` (doesn't matter where)
      ```Dockerfile
      # Dockerfile
      FROM ubuntu:latest

      RUN apt-get update
      RUN apt-get install -y gcc
      RUN apt-get install -y make
      ```
     - Build this image via `$ docker build -t linux-image .`
4. Create `docker-compose.yml` file in the folder with your Assembly code.
   ```yml
   # docker-compose.yml
   version: '3'
   services:
     linux:
       image: linux-image
       command: sleep 1000
       volumes:
         - .:/code
   ```
5. Run `$ docker-compose up`.  
   Now when you have your linux container running you can connect to it.
6. Connect to the container.
   In the other terminal window run `$ docker ps` and find the name `container_name` of the container.
   After run `$ docker exec -it container_name bash` to connect. 

You are ready to go! Your code will be in the `/code/` folder, you can edit it inside docker container and
changes will be seen in the host and vice versa, bcs it is "shared folder". 

After a container stopped (with CTRL-C for example) you can start it again repeating 5-6 steps again.

---
## The *"Clumsy"* Way (VM)
You can use VMs like `Virtual Box` or `Parallels` or `VM Ware`.
### Pros
 - It maybe a bit easier to start with, but the sacrifice in the experience doesn't worth it IMO =).

### Cons
 - Those apps are either:
   - Free and shitty (slow, ugly, and require quite a bit of time to set up everything), 
     like `Virtual Box`. 
   - Or paid and a bit less shitty, like `Parallels`. 
 - They really may take time, I gave up on setting "Shared Folder" to share code when using Virtual box.
And I spent almost a day trying to SSH into my `Parallels` VM... 

BTW if you still want to go with VM after this article I highly recommend using `SSH` instead of the
GUI that VM provides. 

If you don't know to connect via `SSH` basically means that you use your VM
as a local server and use your host terminal to connect to it. As a result you are able to execute 
commands on remote VM using your host terminal.

---
## The *"Smart"* Way (Docker)
Please don't be afraid it is not that hard at all, I promise. Please look at the code above in the [TL;DR 
section](#tldr).  
Does it look scary? Believe or not, this is the only code you would need.
So if you are interested please read further.

### Pros
 - You will learn a truly amazing technology that will be of a great help to you in the future as well.
 - I had the best experience using this way.
 - If you mess your container up you can easily restart it from its initial state...
 - You can easily make "Shared Folders" and connect to your container.

### Cons
 - You may spend quite a bit time in the beginning depending on you background.

### Explanation of Code Snippets
The FreeCodeCamp tutorial I linked above is explains everything in depth, but here I have small summary.

Essentially Docker Desktop for macOS is VM itself, so it allows us to run Linux container on macOS.

The `Dockerfile` is file that defines so-called "container image". It is a settings that you want to have
for your container. 
 - `FROM ubuntu:latest` says that we want our image to be based on another image, the latest ubuntu
 - `RUN <some command>` says docker to run this `<some command>` inside image when building. We are 
   installing `gcc` and `make` for using this command.

The `docker-compose.yml` is a file in which we define how exactly we want to run our container.
 - `image: linux-image` means that we want container to be created from image with name linux-image
 - `command: sleep 1000` is the command which will be executed in the container. Container will be 
   alive while the process executing this command is alive.
 - `volumes: .:/code` means that we map `.` folder in the host with the folder `/code/` in the container,
   so it will be a shared folder (so-called volume).

### A Few Thing to Mention:
 - As with everything in programming you **don't** need to know **everything** about tool to use it.
 - Docker is not a rocket science, but (especially if you are pretty new to programming) probably starting with
   reading dry documentation is not the brightest idea. There is really great tutorials out there.
 - Docker makes a lot of things *so freaking much easier*. For example, I'm writing this
   Jekyll website using Docker, because it is much faster than resolving *stupid* gem conflicts every
   few month and making mess of your system by installing a lot of different libraries and packages.


---
## Renting a Linux Server
Yes, you always can always rent a linux server and access it through `SSH`. 
### Pros
 - It is a bit easier than learning `Docker`.
 - It may be useful to have your own server. You can use it for hosting your website for example.

### Cons
 - It is more expensive than using Docker (will cost 10-20 EUR a month).
 - You can only access server when you have Internet.


<script src="//cdn1.lncld.net/static/js/3.0.4/av-min.js"></script>
<script src='//unpkg.com/valine/dist/Valine.min.js'></script>

<div id="vcomment"></div>
<script>
    new Valine({
        el: '#vcomment' ,
        appId: 'sHzkMbs7PwmC72n2LuIQCtqe-MdYXbMMI',
        appKey: 'YzmegDiF3KdpKYJH2XTEnHH7',
        requiredFields: ['nick'],
        lang: 'en'
    });
</script>



