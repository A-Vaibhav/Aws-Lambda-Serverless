# Aws-Lambda-Serverless

### Serverless Setup :-
1. Install Dependencies (Node,AWS CLI).
   - Open Terminal and run the following commands :-
     -  For Node :
          ```
          sudo apt install nodejs
          ```
          - Check the installed properly or not :
          ```
          node -v
          ```
          - Install npm package manager with :
          ```
          sudo apt install npm
          ```
          - Check the installed properly or not :    
          ```
          npm -v
          ```
     - For AWS CLI :
          ```
          curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
          ```
          ```
          unzip awscliv2.zip
          ```
          ```
          sudo ./aws/install
          ```
2. Install Serverless framework and check version.
   ```
   sudo npm install -g serverless
   ```
   ```
   serverless --version
   ```
3. Creating a user in AWS Console and download credentials.
   - Aws > IAM > Users > Add User
   - Create user with programmatic access.
   - Download the key
4. Setup Serverless to use those credentials.
   - Run the following commands in the terminal :
     - copy the key credentials (access id and key)
     ```
     serverless config credentials --provider aws --key copy_past_access_id --secret copy_paste_access_key --profile username_you_created_in_Aws_user
     ```
     - example : serverless config credentials --provider aws --key AKIA4RDW6YOEZRYKPC --secret O+q6okg/mpaEMvO7KkzpGZkS/D9pY5tNFRdDz --profile user123 
     - see the configured user with :</br> 
     ```
     sudo cat ~/.aws/credentials
     ```
