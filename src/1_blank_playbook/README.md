# How can i run this script?

we ignore the inventory file about called `hosts`. because inventory have the some sensitive value.but we can try writting like this format by yourself:
```
[dev]
127.0.0.1

[dev:vars]
ansible_connection=ssh 
ansible_user=kali

[all:vars]
ansible_connection=ssh 
ansible_user=ubuntu
```

running create and delete user by ansible command.

```
# test connection managed node. 
ansible all -m ping -i hosts

# run hello world on managed node.
ansible-playbook -i hosts playbook.yml
```
