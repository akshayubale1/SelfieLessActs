# SelfieLessActs

# Languages Used
1) Python
2) HTML
3) Javascript

# Introduction
SelfieLessActs is used to share information about anything that is good for the society that you observe.The entire application was built using Amazon Web Services.Examples of such acts could be

   ● Picking up a piece of garbage and dumping it in a garbage can
   ● Road getting laid in your area
   ● Someone helping a blind man cross the road.
   ● You helping your mother at home in the kitchen
   
The  SelfieLessActs application will allow users of the application to upload image of
the act with a small caption and categories. A user of the application will be
presented with a screen that
   ● Shows them lists of categories on which Acts have been shared. An act is a
     ombination of an image and a caption for that image.
   ● Allows them to select to a topic.
   ● On selection, they will be shown all Acts in a category sorted in reverse
     chronological order (latest image first).
   ● Upvote a particular Act.
   ● Upload an Act.
   ● Delete an Act

Cloud Orchestration is use of programming technology to manage the interconnection and interactions among workload on public  and private cloud infrastructure.
Implemented a custom container orchestrator engine that will: 
   1. Be able to start and stop Acts containers programmatically, and allocate ports for them on localhost.
   2. Load balance all incoming HTTP requests (to the Acts EC2 instance) equally between all running Acts containers in a           round-robin fashion.
   3. Monitor the health of each container through a health check API, and if a container is found to be unhealthy, stop the       container and start a new one to replace it.
   4. Increase the number of Acts containers if the network load increases above a certain threshold.
   
# Health Check
  1)If the server is functioning normally, i.e., able to server all requests and read/write to database, then respond with       code 200.
  2)If the server is disabled for some reason, such as due to not being able to read/write data, or if there’s no free memory     available to allocate new objects, then respond with code 500.
# Crash Server
  1)Once this API is called on an Acts container (and a 200 response is returned), henceforth every HTTP request to every         route, including the health check, must be responded with code 500.
  2)This API will be called by the testing script a certain point to permanently disable an Acts container and then check if     its health check (and other routes) return 500 subsequently.

# Load Balancing
  The second task is to implement the load balancing feature of the orchestrator engine.
  The orchestrator can be written as a simple web server in any language, which will run on the Acts instance itself. It must   listen on port 80 and forward HTTP requests to healthy Acts containers. The Acts containers themselves must be listening on   other ports (8000, 8001, 8002,..) on localhost. The orchestrator engine must track these active ports.The HTTP requests       must be distributed in a round-robin manner to every Acts container.
  
# Fault Tolerance
  For every 1 second interval, the orchestrator engine must poll the health check API of each running Acts container. If it     detects an unhealthy container, it must stop that container and start a new container (using the same Acts docker image).     The replacement container must listen on the same port that the unhealthy container was listening on.
  
# Auto Scaloing
  The orchestrator must keep a track of the number of incoming HTTP requests in the past two minutes. 
  At every 2 minute interval, depending on how many requests were received, the orchestrator must increase or decrease the     number of Acts containers

# Integration With Mobile App
  
 we have integrated our cloud backend with the mobile application.
  This app will make POST requests to acts. You will be able to select the category and user in the UI.
