# Mike_Challenge

Inside this repo you will find my cloudformation template which on deployment will setup the resources necessary to host a static web page. 
Once the deployment is complete, we can add the index.html file to the newly created S3 bucket with this command:
==========     aws s3 cp --acl "public-read" index.html s3://wearesecnet     ========
where wearesecnet is the stack name we pass into cloudformation before creating the stack which will in turn become the S3 bucket name. 

Below is a high level visual AR of the services being used:

![alt text](https://github.com/MikeBackman/Mike_Challenge/blob/main/Screenshot%202021-02-17%20at%201.36.20%20PM.png)


The user will enter through Route53 which utilizes CloudFront. CloudFront will serve the static content that will be uploaded to S3. 
