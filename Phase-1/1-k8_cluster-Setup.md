- Kubernetes Architecture Consists of both Masternode and worker/slave node. Let's create them first from EC2 instances

## Instances creation in AWS
To create an Ubuntu EC2 instance in AWS, follow these steps:

1. **Sign in to the AWS Management Console**:
   - Go to the AWS Management Console at https://aws.amazon.com/console/.
   - Sign in with your AWS account credentials.

2. **Navigate to EC2**:
   - Once logged in, navigate to the EC2 dashboard by typing "EC2" in the search bar at the top or by selecting "Services" and then "EC2" under the "Compute" section.

3. **Launch Instance**:
   - Click on the "Instances" link in the EC2 dashboard sidebar.
   - Click the "Launch Instance" button.

4. **Choose an Amazon Machine Image (AMI)**:
   - In the "Step 1: Choose an Amazon Machine Image (AMI)" section, select "Ubuntu" from the list of available AMIs.
   - Choose the Ubuntu version you want to use. For example, "Ubuntu Server 20.04 LTS".
   - Click "Select".

5. **Choose an Instance Type**:
   - In the "Step 2: Choose an Instance Type" section, select the instance type that fits your requirements. The default option (usually a t2.micro instance) is suitable for testing and small workloads.
   - Click "Next: Configure Instance Details".

6. **Configure Instance Details**:
   - Optionally, configure instance details such as network settings, subnets, IAM role, etc. You can leave these settings as default for now.
   - Click "Next: Add Storage".

7. **Add Storage**:
   - Specify the size of the root volume (default is usually fine for testing purposes).
   - Click "Next: Add Tags".

8. **Add Tags**:
   - Optionally, add tags to your instance for better organization and management.
   - Click "Next: Configure Security Group".

9. **Configure Security Group**:
   - In the "Step 6: Configure Security Group" section, configure the security group to allow SSH access (port 22) from your IP address.
   - You may also want to allow other ports based on your requirements (e.g., HTTP, HTTPS) as in this pic ![Project Architecture](https://github.com/user-attachments/assets/3385096c-bfd9-451b-b655-3c6a8276519a)
   - Click "Review and Launch".

10. **Review and Launch**:
    - Review the configuration of your instance.
    - Click "Launch".

11. **Select Key Pair**:
    - In the pop-up window, select an existing key pair or create a new one.
    - Check the acknowledgment box.
    - Click "Launch Instances".

12. **Access Your Instance**:
    - Use Mobaxterm

# Master Node

1. Update System Packages `sudo apt-get update`  
2. Install Docker 
```
sudo apt install docker.io -y
sudo chmod 666 /var/run/docker.sock 
```
3. Install Kubernetes Dependencies
```
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
sudo mkdir -p -m 755 /etc/apt/keyrings
```
4. Add kubernetes Repository and GPG Keys
```
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
```
5. update packages `sudo apt update`
6. Install Kubernetes Components `sudo apt install -y kubeadm=1.28.1-1.1 kubelet=1.28.1-1.1 kubectl=1.28.1-1.1`
7. Initialize Kubernetes Master node `sudo kubeadm init --pod-network-cidr=10.244.0.0/16`

- once you run this command you will get a command which will be like `kubeadm join .....` which you have to paste it in whichever the servers you wanted to make them as your worker nodes .

8. Configure Kubernetes Cluster
```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```
9. Deploy Networking Solution i.e; Calico
`kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml`
10. Deploying Ingress controller i.e; Nginx
`kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.49.0/deploy/static/provider/baremetal/deploy.yaml`



# Worker Node-1

1. Update System Packages `sudo apt-get update`  
2. Install Docker 
```
sudo apt install docker.io -y
sudo chmod 666 /var/run/docker.sock 
```
3. Install Kubernetes Dependencies
```
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
sudo mkdir -p -m 755 /etc/apt/keyrings
```
4. Add kubernetes Repository and GPG Keys
```
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
```
5. update packages `sudo apt update`
6. Install Kubernetes Components `sudo apt install -y kubeadm=1.28.1-1.1 kubelet=1.28.1-1.1 kubectl=1.28.1-1.1`

# Worker Node-2

1. Update System Packages `sudo apt-get update`  
2. Install Docker 
```
sudo apt install docker.io -y
sudo chmod 666 /var/run/docker.sock 
```
3. Install Kubernetes Dependencies
```
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
sudo mkdir -p -m 755 /etc/apt/keyrings
```
4. Add kubernetes Repository and GPG Keys
```
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
```
5. update packages `sudo apt update`
6. Install Kubernetes Components `sudo apt install -y kubeadm=1.28.1-1.1 kubelet=1.28.1-1.1 kubectl=1.28.1-1.1`


once the setup was done, to validate you can run `kubectl get nodes` in the master node. There you can able to see the Ips of the worker nodes

# vulnerability scan using kubeaudit tool

```
visit https://www.github.com/shopify/kubeaudit/releases and select based on your os architecture and then run 

wget https://www.github.com/shopify/kubeaudit/releases/.....<value>

tar -xvzf kubeaudit_<replace with name from the above command output>
sudo mv kubeaudit /usr/local/bin
kubeaudit all
```
