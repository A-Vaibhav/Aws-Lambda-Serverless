# Aws-Lambda-Serverless

### Serverless Setup :-
1. Install Dependencies (Node,AWS CLI).
   - Open Terminal and run the following commands :-
     - For Node :
       - sudo apt install nodejs
       - node -v 
       - sudo apt install npm
       - npm -v      
     - For AWS CLI :
       - curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
       - unzip awscliv2.zip
       - sudo ./aws/install
3. Install Serverless framework.
   - sudo npm install -g serverless
   - serverless --version
4. Creating a user in AWS Console and download credentials.
   - Aws > IAM > Users > Add User
   - Create user with programmatic access.
   - Download the key
6. Setup Serverless to use those credentials.
   - Run the following commands in the terminal :
     - serverless config
     - 
