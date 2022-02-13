---
layout: post
title:  "Linux Assembly on macOS"
date:   2022-01-27
categories: programming
tags: docker
excerpt_separator: <!--more-->
---

Computer Organisation / Architecture courses usually require writing Assembly code for Linux.

What I'll address here is **how to easily run Linux Assembly on macOS machines**.
<!--more-->

---
### Table of Content
{:.no_toc}

* [TOC]
{:toc}
---


* A markdown unordered list which will be replaced with the ToC, excluding the "Contents header" from above
  {:toc}

## TL;DR
There are a few ways how to do it, IMO the easiest and most pleasant way is to use `Docker`:
1. Watch this great 2-h [Docker Tutorial for Beginners](https://youtu.be/fqMOX6JJhGo) from the FreeCodeCamp.
2. Install Docker Desktop for macOS and start `Docker`.  
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
   When you have your Linux container running, you can connect to it.
6. Connect to the container.
   In the other terminal window, run `$ docker ps` and find the name `container_name` of the container.
   After run `$ docker exec -it container_name bash` to connect.

You are ready to go! Your code will be in the `/code/` folder. You can edit it inside a docker container and
changes will be seen in the host and vice versa because it is a "shared folder".

After a container has stopped (with `CTRL-C`, for example), you can start it again by repeating 5-6 steps.

---
## The *"Clumsy"* Way (VM)
You can use VMs like `Virtual Box` or `Parallels` or `VM Ware`.
### Pros
- It may be a bit easier to start with, but the sacrifice in the experience doesn't worth it IMO =).

### Cons
- Those apps are either:
   - Free and shitty (slow, ugly, and require quite a bit of time to set up everything),
     like `Virtual Box`.
   - Or paid and a bit less shitty, like `Parallels`.
- They really may take the time. I gave up on setting "Shared Folder" to share code when using Virtual box.
  And I spent almost a day trying to SSH into my `Parallels` VM...

BTW if you still want to go with VM after this article I highly recommend using `SSH` instead of the
GUI that VM provides.

In case you don't know, to connect via `SSH` basically means that you are using your host terminal to connect to the VM, as to the server. As a result, you can execute
commands on a remote VM using your host terminal.

---
## The *"Smart"* Way (Docker)
Please don't be afraid it is not that hard at all, I promise. Please look at the code above in the [TL;DR
section](#tldr).  
Does it look scary? Believe it or not, this is the only code you would need.
So if you are interested, please read further.

### Pros
- You will learn a truly amazing technology that will be of great help to you in the future as well.
- I had the best experience using this way.
- If you mess your container up, you can easily restart it from its initial state.
- You can easily make "Shared Folders" and connect them to your container.

### Cons
- You may spend quite a bit of time, in the beginning, depending on your background.

### Explanation of Code Snippets
The FreeCodeCamp tutorial I linked above is explains everything in-depth, but here I have a small summary.

Essentially Docker Desktop for macOS is VM itself. Thus it allows us to run Linux containers on macOS.

The `Dockerfile` is a file that defines the so-called "container image". It contains the settings that you want to have
for your container.
- `FROM ubuntu:latest` says that we want our image to be based on another image, the latest ubuntu.
- `RUN <some command>` says docker to run this `<some command>` inside image when building. We are installing `gcc` and `make` for using this command.

The `docker-compose.yml` is a file where we define how exactly we want to run our container.
- `image: linux-image` means that we want the container to be created from the image with the name `linux-image`
- `command: sleep 1000` is the command which will be executed in the container. The container will be
  alive while the process executing this command is alive.
- `volumes: .:/code` means that we map `.` folder in the host with the folder `/code/` in the container. Therefore it will be a shared folder (so-called volume).

### A Few Thing to Mention:
- As with everything in programming, you **don't** need to know **everything** about tool to use it.
- Docker is not a rocket science, but (especially if you are pretty new to programming) probably starting with
  reading dry documentation is not the brightest idea. There are great tutorials out there.
- Docker makes a lot of things *so freaking much easier*. For example, I'm writing this
  `Jekyll` website uses `Docker` because it is much faster than resolving *stupid* gem conflicts every
  few months and making a mess of your system by installing a lot of different libraries and packages.


---
## Renting a Linux Server
Yes, you can always rent a Linux server and access it through `SSH`.
### Pros
- It is a bit easier than learning `Docker`.
- It may be useful to have your server. You can use it for hosting your website, for example.

### Cons
- It is more expensive than using `Docker` (will cost 10-20 EUR a month).
- You can only access the server when you have Internet.
