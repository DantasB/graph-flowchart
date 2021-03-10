Graph-Flowchart

Install
- Install Docker in your OS
- Install ArangoDb on your Docker using (docker pull arangodb/arangodb)
- Start your Docker Service as sudo systemctl start docker.service
- Start Arango Session as docker run -p 8529:8529 -e ARANGO_ROOT_PASSWORD=YOUR_PASSWORD_HERE arangodb/arangodb:3.7.9 (The login will be made on http://0.0.0.0:8529 page where the login is root and the root password is YOUR_PASSWORD)
- Then you can access it by your browser.