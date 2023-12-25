# Week 0 — Billing and Architecture

## Required Homework

### 1. Recreate Conceptual Diagram in Lucid Charts
![Lucid charts Cruddur Conceptual diagram](https://lucid.app/lucidchart/e2c17852-e646-47e9-9c2e-a505dcb38f2d/edit?viewport_loc=-280%2C-125%2C2237%2C1236%2C0_0&invitationId=inv_6bb0fe62-f6bb-434f-a6db-6b26e20b7c7c)  

[Conceptual diagram](https://github.com/Nekembe-Boris/user-content/blob/main/cloud_bootcamp/Conceptual_diagram.png)

### 2.  Recreate Logical Diagram in Lucid Charts
![Lucid charts Cruddur Logical diagram](https://lucid.app/lucidchart/2ae356f2-1b4c-4789-9360-b2eeffef69c8/edit?viewport_loc=-4376%2C-1824%2C6712%2C3708%2C0_0&invitationId=inv_a7c99550-d4fa-4b01-a757-42c6780c9e83)  
[Logical diagram](https://github.com/Nekembe-Boris/user-content/blob/main/cloud_bootcamp/Logical_diagram.png)


###  3. Create an Admin User

i. Log into your AWS account as **Root User**  
ii. Search and select **IAM (Identiity and Access Management) service**  
iii. On the dashboard on the left side of the screen,  click **Users** and select **Create User**  
iv. Enter the new user name and specify if you want such a user to have Console access by selecting **Provide user access to the AWS Management Console** and then **I want to create an IAM user**, create a password for the user and ensure that they change the password after 1st login session  
v. Set the User permissions by either adding the user to an existing group or creating a new group (best practice). Ensure that you attach the **AdministratorAccess** policy to the group you are creating  
vi. Review the new user's details and then click **Create User**.  
vii. Easily retrieve password and user details by downloading the .csv file


### 4. Use Cloudshell

i. Sign in as a user and click on the Cloudshell icon as indicated on the image below  

![cloudshell image](https://github.com/Nekembe-Boris/user-content/blob/main/cloud_bootcamp/cloudshell.png)

ii. For example, if we want to get contact information of our AWS account, we can enter the following command  

``aws account get-contact-information --account-id <value>``  

The above command will display the address that was used when the AWS  account was created  
Get all the AWS  CLI commands on [here](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws)  

### 5. Generate AWS Credentials

i. Sign in as a User  
ii. Search and select **IAM (Identiity and Access Management) service**  
iii. On the dashboard on the left side of the screen,  click **Users** and click again on the user you want to generate credentials for  
iv. Click on the **Security Credentials** tab  
v. Go to the **Access Keys** box and click **create access key"  
vi. Select the Use Case, Set the description tag and then create the new access key.  
vii. Easily save the created ACCESS KEY and ACCESS KEY ID by downloading the .csv file.  

### 6
