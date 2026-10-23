# EC2 w/ ALB

In this example is based on a lab in section 10 on Route 53. It stands up 3 EC2's fronted by an ALB and uses the Instance Metadata Service to get information on each EC2's Availablity Zone.

- TODO: Write Terraform for section 105 

## Notes

* Describing regions:

```bash
aws ec2 describe-availability-zones --region us-west-2
```

* Amazon Machine Instance Ids are region scoped.
* KeyPairs are also region scoped.
* So are security groups. The thing that I didn't notice was happening under the scenes in the console is that a security group was being created in each region
* This module is exactly what terragrunt is for but just doing w/ terraform is fine for my current scope.