docker compose up -d


# install nginx

`sudo apt update`

`sudo apt install nginx`

### check status
`sudo ufw app list`

# install docker
`sudo apt install apt-transport-https ca-certificates curl software-properties-common`

`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

`sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"`

`apt-cache policy docker-ce`

`sudo apt install docker-ce`
