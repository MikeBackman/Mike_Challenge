# Mike_Challenge

Inside this repo you will find my cloudformation template which on deployment will setup the resources necessary to host a static web page. 
Once the deployment is complete then we can add the index.html file to the newly created S3 bucket with this command:
==========     aws s3 cp --acl "public-read" index.html s3://wearesecnet     ========
where wearesecnet is the stack name we pass into cloudformation before creating the stack which will in turn become the S3 bucket name. 

Below is a high level visual AR of the services being used:


