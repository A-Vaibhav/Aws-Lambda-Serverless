## 😄 Lets first Create a Simple Hello-World Program, to understand how serverless:
1. Create
2. Deploy
3. Run


#### 1. Create project folder with serverless:-</br>
   ``` 
   sls create --template aws-python3 --path Hello-World</br>
   ```
   - Change directory to Hello-World</br>
   ```
   cd Hello-World
   ```
   
#### 2. Open Project Folder in any Code Editor:-</br>
   - Open handler.py, and update the function</br>
   ```
   def hello(event,context):
           print("Hey there")
           return "Hello from Serverless"
   ```
   - Open the serverless.yml and go in provider section and add profile and region</br>
   ```
   provider:
      name: aws
      runtime: python3.8
      profile: serverless-vai
      region: ap-south-1
      lambdaHashingVersion: 20201221
   ```
#### 3. Deploy the lambda function to AWS 
   ```
   sls deploy --verbose
   ```
#### 4. Run the function 
   ```
   sls invoke -f hello -l
   ```
   </br>
   </br>
   
## 😄 Lets update the function and deploy only the function rather then entire stack

#### 1. Open handler.py, and update the function</br>
   ```
   def hello(event,context):
           print("First update")
           return "Hello from Serverless"
   ```
#### 3. Deploy the lambda function to AWS 
   ```
   sls deploy function -f hello
   ```
   
#### 4. Run the function 
   ```
   sls invoke -f hello -l
   ```
   
## 😄 Other Task that you can do with functions

#### 1. Fetching Function logs :
   ```
   sls logs -f hello
   ```
#### 2. Deleting Function :
   ```
   sls remove
   ```
