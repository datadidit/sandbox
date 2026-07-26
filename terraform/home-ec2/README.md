# Home EC2

Simple Module to create an ec2 instance for you to login to from your home network and only you can access. This can be used for tunneling to various resources in your VPC from your local box.

## Commands

### Create the EC2

```bash
MacBookPro:home-ec2 mkwyche$ terraform apply
data.external.force_ipv4: Reading...
data.external.local_user: Reading...
data.http.my_public_ip: Reading...
data.external.local_user: Read complete after 0s [id=-]
data.external.force_ipv4: Read complete after 0s [id=-]
data.http.my_public_ip: Read complete after 0s [id=https://ifconfig.me/ip]
data.aws_key_pair.key_pair: Reading...
data.aws_ami.ami: Reading...
data.aws_key_pair.key_pair: Read complete after 0s [id=key-0aacf6008840baa11]
data.aws_ami.ami: Read complete after 0s [id=ami-01edba92f9036f76e]

Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
```

### SSH into the EC2

If your key has been added locally to ssh(`ssh-add -l`) you can now easily ssh in.

```bash
ssh ec2-user@ec2-13-220-44-159.compute-1.amazonaws.com
The authenticity of host 'ec2-13-220-44-159.compute-1.amazonaws.com (13.220.44.159)' can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ec2-13-220-44-159.compute-1.amazonaws.com' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
   ,     #_
   ~\_  ####_        Amazon Linux 2023
  ~~  \_#####\
  ~~     \###|
  ~~       \#/ ___   https://aws.amazon.com/linux/amazon-linux-2023
   ~~       V~' '->
    ~~~         /
      ~~._.   _/
         _/ _/
       _/m/'
[ec2-user@ip-172-31-13-45 ~]$
```

### Destroy the EC2

```bash
aws_vpc_security_group_ingress_rule.ssh_ingress_v4: Destroying... [id=sgr-0de0b6d7878d047ff]
aws_vpc_security_group_egress_rule.all_egress_v4: Destroying... [id=sgr-00fe6cc6be11c98e3]
aws_vpc_security_group_ingress_rule.ssh_ingress_v6[0]: Destroying... [id=sgr-014f4d42101b6e6c1]
aws_vpc_security_group_egress_rule.all_egress_v6: Destroying... [id=sgr-0f4ddbc6d5e168af3]
aws_instance.ec2_instance: Destroying... [id=i-03edc197398ff1491]
aws_vpc_security_group_egress_rule.all_egress_v6: Destruction complete after 1s
aws_vpc_security_group_ingress_rule.ssh_ingress_v6[0]: Destruction complete after 1s
aws_vpc_security_group_ingress_rule.ssh_ingress_v4: Destruction complete after 1s
aws_vpc_security_group_egress_rule.all_egress_v4: Destruction complete after 1s
aws_instance.ec2_instance: Still destroying... [id=i-03edc197398ff1491, 00m10s elapsed]
aws_instance.ec2_instance: Still destroying... [id=i-03edc197398ff1491, 00m20s elapsed]
aws_instance.ec2_instance: Still destroying... [id=i-03edc197398ff1491, 00m30s elapsed]
aws_instance.ec2_instance: Destruction complete after 30s
aws_security_group.ssh_restricted: Destroying... [id=sg-08ad998def9119e33]
aws_security_group.ssh_restricted: Destruction complete after 1s

Destroy complete! Resources: 6 destroyed.
```


## TODO

- Figure out SSH from ipv6 instead of needing to force ipv4
- Add a default user so you're not dependent on the default user in the AMI the issue I have with this is it makes passing down userdata a bit more complex but I'm sure it can be handled.
- Add dynamic filtering to just provide a OS name and it'll pull latest AMI for that OS.