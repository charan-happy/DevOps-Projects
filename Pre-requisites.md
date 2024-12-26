Tools :

1. Mobaxterm [Terminal]
2. AWS Account
3. Github Account
4. Git 

install docker on both sonarqube and nexus servers get installation instructions from docker official website

sudo chmod 666 /var/run/docker.sock

in sonarqube, run `docker run -d --name sonar -p 9000:9000 sonarqube:lts-community`

To access <server-ip>:9000, Default username and password are `admin:admin`

in nexus, run `docker run -d --name Nexus -p 8081:8081 sonatype/nexus3`

To access <server-ip>:8081, Default username is `admin` and password can be found inside the nexus container . `docker exec -it <container-id> /bin/bash` and password path we can find at the top right of the nexus ui after clicking on sign-in

jenkins sever
------------
jdk-17 or above

Get installation steps from official site of jenkins
```
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins -y
```
install docker also

To access jenkins --> <server-ip>:8080


plugins to be installed on jenkins server :

1. Eclipse Temurin installer
2. config file provider
3. pipeline maven integration
4. sonarqube scanner
5. docker 
6. docker pipeline
7. kubernetes, kubernetes cli, kubernetes credentials, kubernetes client api
8. Maven integration
9. prometheus metrics

configure tools in jenkins
-----------------------
go to manage jenkins --> Tools --> 

jdks --> jdk17 -->install automatically --> install from optium ---> select 17 from the dropdown

sonarqube scanner --> sonar-scanner --> 

maven --> maven3 --> 3.6.1

docker --> install automatically --> download from docker.com

Pipeline creation in jenkins
------------------------------
1. new job --> pipeline --> Give name to your job
2. configure --> discard old builds --> max value should be 2
3. Add our github token on credentials section of the jenkins
4. Write the jenkinsfile

sudo apt-get install wget apt-transport-https gnupg lsb-release

wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee -a /etc/apt/sources.list.d/trivy.list

sudo apt-get update

sudo apt-get install trivy -y

goto manage jenkins > system > sonarqube servers and 

generate sonar-token in the sonarqube server and kept it in manage jenkins > credentials > system > global credentials > secret text and give the value which we generated from sonarqube server

server name as sonar and url as sonarqube server url till port

Have to create webhook in the sonarqube server and name should be jenkins and url should be http://<jenkins-ip>:8080/sonarqube-webhook/

in master node of kubernetes we ahve to get sec.yml file 

and needs to keep its value in credentials of jenkins


cd ~/.kube

cat config   

    here we can able to see the server endpoint, clustername and namespace as webapps







