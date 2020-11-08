Available on GitHub at: https://github.com/Siyuan-Cao/QeeapChain.git

Preface

The purpose of this document is to outline a technical guide line for new developers or anyone who is going to join the team and start development. The project background will be briefly covered, followed by the setup process on a clean environment and the steps of how to deploy this project. A Getting Start section will be provided for future teams to quickly pick up the development from either frontend or backend. This document will also include the code standard and version control policy for a better understanding and also given as a recommendation.

Project Summary

Our project is the Indigenous Food Blockchain Project. This project mainly uses blockchain technology to achieve product traceability and product transparency. So that relevant stakeholders and consumers will not be deceived by illegal merchants. The traceability is to check the entire production process of the product, so that relevant stakeholders and consumers understand how the product is produced, and the knowledge of raw materials makes relevant stakeholders and Consumers can buy and use products with confidence, and on the other hand, they also protect the ownership of indigenous foods.

Setup client/developer machine

Visual Studio Code - Code Editor
Available at: https://code.visualstudio.com/

Python
Available at: https://www.python.org/downloads/
Test: Execute command ‘python --version’ to see the outcome of installation

JAVA
Available at: https://www.java.com/en/download/
Test: Execute command ‘java -version’ to see the outcome of installation

Flask - The framework used for web application
Available at: https://flask.palletsprojects.com/en/1.1.x/installation/#installation
Test: Execute command ‘pip freeze | grep Flask’ to see the current version
Git
Available at: https://git-scm.com/downloads
Test: Execute command ‘git --version’ to see the outcome of installation

cURL
Available at: https://curl.haxx.se/download.html
Test: Execute command ‘curl --version’ to see the outcome of installation

Docker and Docker Compose
Available at: https://www.docker.com/get-started
Test: Execute command ‘docker version’ to see the outcome of installation

Install Samples, Binaries, and Docker Images
Available at: https://github.com/hyperledger/fabric-samples
Installation instructions: https://hyperledger-fabric.readthedocs.io/en/release-2.2/install.html

Optional:
Oracle VM VirtualBox - For running Ubuntu on other OS
Available at: https://www.virtualbox.org/

Ubuntu
Available at: https://ubuntu.com/download/desktop

Postman - Great for API development and testing
Available at: https://www.postman.com/

Code/Comment Standard

Because our team members have different skills and different programming backgrounds, first of all, we first unify the web programming tools and use python flask to implement the front-end web pages. Our team has not developed any programming strategy, even if there is no strategy, we will definitely complete excellent projects as required. We will also strictly require the correctness of our code and the clarity of the code logic to facilitate future maintenance. For the code, we provide a functional explanation and an explanation of the main code. Our team tries to ensure the unity of code to avoid duplication rate. The next step is about comments. Our team has made detailed comments on the code, so that the subsequent development team can easily understand the logic and relationship of the code based on the comments of the system code. Facilitate the continued development of the program. If any problems occur in a timely manner, developers can quickly find the problem according to the code comments, and solve the problem quickly. Make the project delivered on schedule.

Version Control Policy

To manage our git flow and avoid any issues such as overwrite and merge into wrong branches, we followed a simple policy as below:

Master branch - Avoid push to the Master branch before the project is ready to be deployed.

Manage each Sprint as individual branches - Create a new branch when moving to a new Sprint. Keep another branch before all tests are executed and a passed, then merge to the main Sprint branch. Also, merge with the previous branch(if any) in the beginning of the new sprints.

Make your own branches during development - When team members are going to work on  PBIs, a new branch should be created from the Sprint branch.

Pull requests - Make pull requests after change to let other team members to review and be aware of it. Also make sure the code others are working on is up to date.

Merge pull requests - Requests should be reviewed and approved by at least half of the team(in our case - two team members), then to be merged.

Commenting - Each commit should have a meaningful and detailed comment to help other team members to understand what changes are made.

Comment format - Commenting should follow the same format that is: at the beginning of the comments, use for example [PBI5], [BUG FIX] or [TEST CASE] to indicate the content of the commit. This helps the team to keep track of product backlog items, test design and so on.

General policy - Pull frequently, push early and often to keep the git flow and your work space synchronized.

Deployment 

Prerequisites:
Visual Studio Code
Python
JAVA
Flask - The framework used for web application
Git
cURL
Docker and Docker Compose
Install Samples, Binaries, and Docker Images
Oracle VM VirtualBox
Ubuntu
Postman
Qeeap chain source code
For download and installation instructions please refer to the Setup section above.

There are three main steps to deployment of Qeeap chain:
Hyperledger Fabric deployment: 
Open Terminal, navigate to ‘../QeeapChain/Backend/foodchain’ directory. Run following command ‘./startFabric.sh java’. 

The above screenshot shows the blockchain network has been brought up successfully, a Smart Contract has also been installed.

API deployment:
Open Visual Studio Code, click File then choose Open Folder option.

Inside the popup window, navigate to the ‘QeeapChain’ folder and select ‘API’ folder then click ‘OK’. 
Inside the ‘EXPLORER’ side window, expand the ‘wallet’ folder

Before each deployment, delete all the ‘.id’ files within the folder.

Navigate to the ‘src/main/java/com/example/demo’ folder, right click on ‘EnrollAdmin.java’ and run. Then right click on ‘RegisterUser.java’ and run. The following screenshot indicates that the enroll and register has been successful.


And new ‘.id’ files can be found in the ‘wallet’ folder as below: 

Lastly, right click on the ‘QeeapAPI.java’ and run, we can see that

The API has been started on port ‘8080’.

Web application deployment:
Open Visual Studio Code, click File then choose Open Folder option.

Inside the popup window, navigate to the ‘QeeapChain’ folder and select ‘Frontend’ folder then click ‘OK’. 
Inside Visual Studio Code, Use short cut  to open a Terminal window. Type following command: ‘pip3 install virtualenv’ to install the Virtual environment package. A success message will be displayed afterward.

Next create a new virtual environment using ‘virtualenv env’, and a ‘env’ folder will be created.
Type ‘source env/bin/activate’ to activate the environment created. And the ‘(env)’ indicates you have successfully entered the virtual environment.

Then type ‘pip3 install flask pyqrcode pypng’ to install Flask as well as other extensions needed for Qeeap chain web application. A successful message will be displayed like below.

Lastly, run ‘python foodsystem.py’ to start the web application. And it’s can be seen that the web app is running and now can be accessed at ‘http://127.0.0.1:5000/’.

Now open browser and navigate to ‘http://127.0.0.1:5000/’, if the deployment was successful, the website will be dispalyed.



Getting Started 

<Illustrate and explain one function, how to start, coding on front end, back end, setting and deployment, screen shot on running example>

Prerequisites:
Visual Studio Code
Python
JAVA
Flask - The framework used for web application
Git
cURL
Docker and Docker Compose
Install Samples, Binaries, and Docker Images
Oracle VM VirtualBox
Ubuntu
Postman
Qeeap chain source code
For download and installation instructions please refer to the Setup section above and navigate to the Login portal.

User login example: 
Start the web application according to the deployment instructions described in the above section. 

The HTML layout used ‘login.html’ can be found inside the ‘Frontend/templates/’ folder.

Now, use username and password ‘e1’ and choose ‘User type’ as ‘Employee’, then click ‘LOGIN’. You will be redirected to the ‘EMPLOYEE PORTAL’.

Inside the ‘foodsystem.py’, the login details were validated by the ‘validEmployee’ function as below:


Hyperledger Fabric development:
For Chaincode development, open the ‘Backend/chaincode’ folder.  
The ‘Product.java’ defines the structure of the ‘Product’ type, and changes can be applied to this class when the structure needs to be modified. New types of assets can also be created in this directory, for example ‘Bond.java’.   

The ‘FoodBlockchain.java’ contains the functions of the Smart Contract that can be called by the API, such as ‘createProduct’ and ‘queryProduct’.

New Smart Contract functionalities should be added to this class when needed, for example ‘queryLastFiveProduct’.

Blockchain network development:
To config the blockchain network, navigate to the ‘/Backend/test-network’. The ‘network.sh’ contains the network setup process.

The ‘test-network/organizations’ folder contains files related to the organization's creation process. For adding new organizations, navigate to the ‘cryptogen’ folder and create a new ‘.yaml’ configuration file as needed, then update the organization's creation process in ‘network.sh’.

API development:
Open the ‘QuuapChain/API’ folder in VS Code. Open ‘ClientApp.java’

New API functionalities can be added here, and current functions can be modified as well. The ’Product.java’ defines the structure of the ‘Product’ type by this API, make sure this structure matches the ‘Product’ type in contained by the Chaincode to make sure the backend is functioning normally.
The ‘EnrollAdmin.java’ and ‘RegisterUser.java’ contain the necessary Certificate Authority validation processes. To enroll and register further users, please add to the configuration in the main function accordingly.

Web application development:
Open the ‘QeeapChain/Frontend’ folder in VS Code. For all style configurations and any media(pictures, gifs, videos) used in the web application, add to the ‘static’ folder. The ‘templates’ folder contains all the HTML layouts used, and further HTML files should be added inside this folder as well.

The ‘foodsystem.py’ contains all the frontend functionalities, new functions should be created here.
Lastly, the ‘foodsystemdatabase.py’ response for SQLite database setup, it can be used for modifying user login details and table creations.
