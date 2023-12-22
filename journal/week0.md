# Week 0 — Billing and Architecture

## Required Homework

###  1. Create an Admin User

i. Log into your AWS account as **Root User**  
ii. Search and select **IAM (Identiity and Access Management) service**  
iii. Click **Users** on the dashboard on the left side of the screen and select **Create User**  
iv. Enter the new user name and specify if you want such a user to have Console access by selecting **Provide user access to the AWS Management Console** and then **I want to create an IAM user**, create a password for the user and ensure that they change the password after 1st login session  
v. Set the User permissions by either adding the user to an existing group or creating a new group (best practice). Ensure that you attach the **AdministratorAccess** policy to the group you are creating  
vi. Review the new user's details and then click **Create User**.  
vii. Easily retrieve password by downloading the .csv file  

 
### 2. Use Cloudshell

i. Sign in as a user and click on the Cloudshell icon as indicated on the image below  

![cloudshell image](https://github.com/Nekembe-Boris/user-content/blob/main/cloud_bootcamp/cloudshell.png)

ii. If we want to get contact information of our AWS account, we can enter the following command  

``aws account get-contact-information --account-id <value>``  

The above command will display the address that was used when the AWS  account was created  
Get all the AWS  CLI commands on [here](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws)  

