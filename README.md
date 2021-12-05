## My First Project.

# Library with community reviews

> **ERD:**

![image](https://user-images.githubusercontent.com/91483598/144767100-8234f1d1-147d-4f1f-9cd5-414f51cd82cf.png)

Above is a ERD to demonstrate the table relationships. 

I used two one to many relationships to link all data together from a common branch, in this case the author.

All tables have full CRUD functionality. 








> **CI/CD pipeline:**

![image](https://user-images.githubusercontent.com/91483598/144767352-4dbf403b-3d06-4ca0-b1a4-4643440826d0.png)

Above is the Jenkins webhook feature used to automate the creation of jobs.
It launched any time code was uploaded to the VCS, in this case Github.

![image](https://user-images.githubusercontent.com/91483598/144768137-1864fcf1-e019-44de-83c3-2183dcd4832a.png)
* "Checkout SCM" refers to pulling the code from Github.
* "Set Up!" refers to setting up  all the apt dependencies for the following stages to be able to execute.
* "Build" refers to building images set up in the docker-compose.yaml file. 
* "Push" refers to uploading the images to the dockerhub repository. 
* "Test" refers to running pytest and producing the coverage report. 
* "Deploy" refers to using swarm to deploy a full application stack. 
